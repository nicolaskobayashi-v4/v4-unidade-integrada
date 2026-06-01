#!/usr/bin/env python3
"""
meta_ads_fetch.py — Scraper headless da Meta Ads Library.

Uso:
    python3 meta_ads_fetch.py <client_dir> \\
        --pages <slug1>:<page_id_or_search>,<slug2>:<page_id_or_search>,... \\
        [--max-ads 30] \\
        [--country BR] \\
        [--headless true]

Exemplo:
    python3 meta_ads_fetch.py clientes/<slug-do-cliente> \\
        --pages cliente:<page_id>,concorrente-1:<Nome%20Concorrente>,concorrente-2:<page_id>

Se o valor depois de `:` for numerico, e tratado como page_id.
Caso contrario, busca por nome.

Output:
    <client_dir>/assets/creatives/meta/<slug>/<ad_id>/
        image.jpg
        video.mp4 (se houver — opcional)
        metadata.json
    <client_dir>/assets/creatives/meta/<slug>/_manifest.json
    <client_dir>/cache/meta_ads_fetch-<ts>.json   (raw)
"""

from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    from playwright.async_api import async_playwright, TimeoutError as PWTimeout
except ImportError:
    print("ERRO: playwright nao instalado. Rode:", file=sys.stderr)
    print("  pip3 install -r plugins/v4-estruturacao-ia/scripts/requirements-meta.txt", file=sys.stderr)
    print("  python3 -m playwright install chromium", file=sys.stderr)
    sys.exit(2)

try:
    import requests
except ImportError:
    print("ERRO: requests nao instalado (requirements-meta.txt).", file=sys.stderr)
    sys.exit(2)


ADS_LIBRARY_BASE = "https://www.facebook.com/ads/library/"


def build_url(target: str, country: str = "BR") -> str:
    """Constroi URL do Ads Library. Se target e numerico, usa view_all_page_id.

    Aceita target plain-text OU ja percent-encoded (nao duplica encoding).
    """
    from urllib.parse import quote, unquote
    target = target.strip()
    if target.isdigit():
        params = (
            f"active_status=all&ad_type=all&country={country}"
            f"&view_all_page_id={target}&search_type=page"
        )
    else:
        # Decodifica primeiro (caso ja venha encoded) e re-encoda 1x
        decoded = unquote(target)
        params = (
            f"active_status=all&ad_type=all&country={country}"
            f"&q={quote(decoded)}&search_type=keyword_unordered"
        )
    return ADS_LIBRARY_BASE + "?" + params


async def accept_cookies(page) -> None:
    """Tenta aceitar cookies/gate se aparecer."""
    for selector in [
        'button[data-cookiebanner="accept_button"]',
        'button[title*="ccept"]',
        'button:has-text("Allow all")',
        'button:has-text("Permitir")',
        'button:has-text("Accept")',
        'button:has-text("Aceitar")',
    ]:
        try:
            btn = page.locator(selector).first
            if await btn.is_visible(timeout=800):
                await btn.click()
                await page.wait_for_timeout(600)
                return
        except Exception:
            continue


async def auto_scroll(page, max_ads: int, max_scrolls: int = 20) -> None:
    """Rola a pagina para forcar lazy-load de mais cards.
    Usa contagem via imagens visiveis como proxy (DOM cards varia)."""
    prev_count = 0
    stable_rounds = 0
    for i in range(max_scrolls):
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(1500)
        count = await page.evaluate(
            "document.querySelectorAll('img[src*=\"fbcdn.net\"]').length"
        )
        if count >= max_ads * 3:  # ~3 imgs por ad (avatar + midia + logos)
            return
        if count == prev_count:
            stable_rounds += 1
            if stable_rounds >= 3:
                return
        else:
            stable_rounds = 0
        prev_count = count


def extract_ads_from_html(html: str, max_ads: int | None = None) -> list[dict]:
    """Extrai ads dos payloads JSON embedados no HTML da Ads Library.

    A Meta expoe os dados no objeto `ad_library_main.search_results_connection.edges[]`.
    Cada edge.node.collated_results[] contem { ad_archive_id, snapshot, start_date, ... }.
    """
    import re as _re
    import json as _json

    ads: list[dict] = []
    seen_ids: set[str] = set()

    # Match cada collated_result individualmente — mais tolerante a mudancas de estrutura
    # Procura "ad_archive_id":"NNNN" e, a partir dali, lê o objeto JSON correspondente
    # usando contagem de chaves.
    pattern = _re.compile(r'"ad_archive_id":"(\d+)"')
    for m in pattern.finditer(html):
        ad_id = m.group(1)
        if ad_id in seen_ids:
            continue
        # Voltar ate a { de abertura do objeto collated_result
        start = m.start()
        depth = 0
        open_idx = -1
        # Caminha para tras ate encontrar a { que inicia o objeto onde estamos
        i = start
        while i > 0:
            c = html[i]
            if c == '}':
                depth += 1
            elif c == '{':
                if depth == 0:
                    open_idx = i
                    break
                depth -= 1
            i -= 1
        if open_idx < 0:
            continue
        # Agora caminha para frente do open_idx ate fechar o objeto
        depth = 0
        in_str = False
        esc = False
        j = open_idx
        close_idx = -1
        while j < len(html):
            c = html[j]
            if in_str:
                if esc:
                    esc = False
                elif c == '\\':
                    esc = True
                elif c == '"':
                    in_str = False
            else:
                if c == '"':
                    in_str = True
                elif c == '{':
                    depth += 1
                elif c == '}':
                    depth -= 1
                    if depth == 0:
                        close_idx = j
                        break
            j += 1
        if close_idx < 0:
            continue
        raw = html[open_idx:close_idx+1]
        try:
            obj = _json.loads(raw)
        except Exception:
            continue
        if obj.get("ad_archive_id") != ad_id:
            # Nao era o collated_result em si (provavelmente um wrapper) — pula
            continue
        seen_ids.add(ad_id)

        snap = obj.get("snapshot") or {}
        # Midia
        images_raw = snap.get("images") or []
        videos_raw = snap.get("videos") or []
        cards_raw = snap.get("cards") or []

        image_urls: list[str] = []
        poster_urls: list[str] = []
        video_urls: list[str] = []

        for img in images_raw:
            if not isinstance(img, dict):
                continue
            for k in ("original_image_url", "resized_image_url"):
                v = img.get(k)
                if v and v.startswith("http"):
                    image_urls.append(v)
        for vid in videos_raw:
            if not isinstance(vid, dict):
                continue
            for k in ("video_hd_url", "video_sd_url"):
                v = vid.get(k)
                if v and v.startswith("http"):
                    video_urls.append(v)
            p = vid.get("video_preview_image_url")
            if p and p.startswith("http"):
                poster_urls.append(p)
        for card in cards_raw:
            if not isinstance(card, dict):
                continue
            for k in ("original_image_url", "resized_image_url"):
                v = card.get(k)
                if v and v.startswith("http"):
                    image_urls.append(v)
            for k in ("video_hd_url", "video_sd_url"):
                v = card.get(k)
                if v and v.startswith("http"):
                    video_urls.append(v)
            p = card.get("video_preview_image_url")
            if p and p.startswith("http"):
                poster_urls.append(p)

        body = snap.get("body") or {}
        copy_text = body.get("text") if isinstance(body, dict) else None

        start_date_raw = None
        sd = obj.get("start_date")
        if isinstance(sd, (int, float)) and sd > 0:
            try:
                start_date_raw = dt.datetime.fromtimestamp(int(sd), tz=dt.timezone.utc).strftime("%Y-%m-%d")
            except Exception:
                start_date_raw = None

        platforms_raw = obj.get("publisher_platform") or []
        platforms = [str(p).lower() for p in platforms_raw if p]

        ads.append({
            "ads_library_id": ad_id,
            "ads_library_url": f"https://www.facebook.com/ads/library/?id={ad_id}",
            "start_date_raw": start_date_raw,
            "platforms": platforms,
            "image_urls": list(dict.fromkeys(image_urls)),
            "video_urls": list(dict.fromkeys(video_urls)),
            "poster_urls": list(dict.fromkeys(poster_urls)),
            "cta_type": snap.get("cta_text") or snap.get("cta_type"),
            "copy_excerpt": (copy_text[:400] if copy_text else None),
            "display_format": snap.get("display_format"),
            "link_url": snap.get("link_url"),
            "page_name": snap.get("page_name") or obj.get("page_name"),
            "page_id": snap.get("page_id") or obj.get("page_id"),
        })
        if max_ads is not None and len(ads) >= max_ads:
            break

    return ads


EXTRACT_JS = r"""
() => {
  // Coleta cards — Meta DOM muda seguido, tentamos varios anchors.
  const ads = [];
  const seen = new Set();

  // Estrategia 1: qualquer link que contenha id= no padrao ads_library
  const idLinks = Array.from(document.querySelectorAll('a[href*="ads/library/?id="]'));
  const idFromHref = (href) => {
    try {
      const u = new URL(href, location.origin);
      return u.searchParams.get('id');
    } catch(e) { return null; }
  };

  for (const link of idLinks) {
    const id = idFromHref(link.href);
    if (!id || seen.has(id)) continue;
    seen.add(id);

    // Sobe ate o "card" (article ou container com varios filhos)
    let card = link.closest('div[role="article"]');
    if (!card) {
      card = link;
      for (let k=0; k<8 && card.parentElement; k++) {
        card = card.parentElement;
        if (card.querySelectorAll('img, video').length > 0) break;
      }
    }
    if (!card) card = link;

    // Texto visivel do card
    const text = (card.innerText || '').trim();

    // Data de inicio (Running since X / Veiculando desde X)
    let startDate = null;
    const dateMatch = text.match(/(Started running on|Running since|Veiculando desde|Veiculado desde|Iniciou em)\s*([^\n\r•]+)/i);
    if (dateMatch) startDate = dateMatch[2].trim();

    // Plataformas — Meta mostra aria-labels de icones
    const platforms = [];
    card.querySelectorAll('[aria-label]').forEach(el => {
      const a = (el.getAttribute('aria-label') || '').toLowerCase();
      ['facebook','instagram','messenger','audience network','threads'].forEach(p => {
        if (a.includes(p) && !platforms.includes(p.replace(' ',''))) platforms.push(p.replace(' ',''));
      });
    });

    // Midias: coleta TODAS imagens e videos do card
    const images = Array.from(card.querySelectorAll('img'))
      .map(img => img.src)
      .filter(s => s && s.startsWith('http') && !s.includes('static.xx.fbcdn.net/rsrc.php'));
    const videos = Array.from(card.querySelectorAll('video'))
      .map(v => v.src || v.currentSrc || (v.querySelector('source') ? v.querySelector('source').src : null))
      .filter(s => s && s.startsWith('http'));
    const posters = Array.from(card.querySelectorAll('video'))
      .map(v => v.poster)
      .filter(s => s && s.startsWith('http'));

    // CTA (procura botoes com texto curto)
    let cta = null;
    const ctaCandidates = Array.from(card.querySelectorAll('div[role="button"], a[role="button"], div[aria-label]'))
      .map(el => (el.innerText || '').trim())
      .filter(t => t && t.length < 30 && t.length > 2);
    const ctaWords = ['Learn more','Saiba mais','Send message','Enviar mensagem','Shop now','Comprar','Book now','Sign up','Get offer','Contact us','Call now','Ligar agora','Baixe agora'];
    for (const c of ctaCandidates) {
      if (ctaWords.some(w => c.toLowerCase().includes(w.toLowerCase()))) { cta = c; break; }
    }

    // Copy: pega o maior bloco de texto do card que nao e header/footer
    let copy = null;
    const blocks = Array.from(card.querySelectorAll('div[dir="auto"], span[dir="auto"]'))
      .map(el => (el.innerText || '').trim())
      .filter(t => t.length > 30);
    if (blocks.length) copy = blocks.reduce((a,b) => a.length > b.length ? a : b);

    ads.push({
      ads_library_id: id,
      ads_library_url: `https://www.facebook.com/ads/library/?id=${id}`,
      start_date_raw: startDate,
      platforms,
      image_urls: [...new Set(images)],
      video_urls: [...new Set(videos)],
      poster_urls: [...new Set(posters)],
      cta_type: cta,
      copy_excerpt: copy ? copy.substring(0, 400) : null,
    });
  }

  return {
    ads,
    total_found: ads.length,
    page_url: location.href,
  };
}
"""


def is_ad_media_url(url: str) -> bool:
    """Filtra URLs que parecem midia de anuncio (nao avatars/rsrc)."""
    if not url:
        return False
    if "static.xx.fbcdn.net/rsrc.php" in url:
        return False
    # Profile pictures normalmente <100px
    if "/s100x100/" in url or "/s60x60/" in url:
        return False
    return True


def download_media(url: str, dest: Path, timeout: int = 20) -> bool:
    """Baixa midia. Retorna True se sucesso."""
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        r = requests.get(url, timeout=timeout, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        })
        if r.status_code != 200 or len(r.content) < 1000:
            return False
        dest.write_bytes(r.content)
        return True
    except Exception as e:
        print(f"  [download failed] {url[:80]}... : {e}", file=sys.stderr)
        return False


def pick_best_image(image_urls: list[str], poster_urls: list[str]) -> str | None:
    """Escolhe a melhor imagem/poster (maior e que parece ser midia do ad)."""
    candidates = [u for u in image_urls if is_ad_media_url(u)]
    if poster_urls:
        candidates = poster_urls + candidates
    if not candidates:
        return None
    # Prefere URLs com 'jpg' ou tokens de tamanho (t51 do IG, fna do FB)
    scored = sorted(
        candidates,
        key=lambda u: (
            1 if ".jpg" in u or ".jpeg" in u else 0,
            1 if "fna.fbcdn.net" in u or "cdninstagram" in u else 0,
            len(u),
        ),
        reverse=True,
    )
    return scored[0]


async def fetch_page(playwright, target: str, country: str, max_ads: int, headless: bool) -> dict[str, Any]:
    """Fetcha uma pagina de concorrente/cliente."""
    browser = await playwright.chromium.launch(headless=headless, args=[
        "--no-sandbox",
        "--disable-blink-features=AutomationControlled",
    ])
    context = await browser.new_context(
        viewport={"width": 1440, "height": 900},
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        locale="pt-BR",
    )
    page = await context.new_page()

    url = build_url(target, country=country)
    print(f"[fetch] {target} -> {url[:120]}")

    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(3500)
        await accept_cookies(page)
        await page.wait_for_timeout(1500)
        # Espera a rede ficar "quieta" para garantir que os payloads JSON carregaram
        try:
            await page.wait_for_load_state("networkidle", timeout=12000)
        except PWTimeout:
            pass
        await auto_scroll(page, max_ads=max_ads)
        html = await page.content()
        ads = extract_ads_from_html(html, max_ads=max_ads)
        result = {
            "ads": ads,
            "total_found": len(ads),
            "page_url": url,
        }
        if os.environ.get("META_DEBUG"):
            debug_dir = Path(os.environ.get("META_DEBUG_DIR", "/tmp"))
            debug_dir.mkdir(parents=True, exist_ok=True)
            slug = re.sub(r"[^a-z0-9]+", "-", target.lower())[:40] or "page"
            try:
                (debug_dir / f"meta-debug-{slug}.html").write_text(html)
                print(f"  [debug] html -> {debug_dir}/meta-debug-{slug}.html")
            except Exception as _e:
                print(f"  [debug failed] {_e}")
        print(f"  [ok] {result['total_found']} ads encontrados")
    except Exception as e:
        print(f"  [error] {target}: {e}", file=sys.stderr)
        result = {"ads": [], "total_found": 0, "page_url": url, "error": str(e)}
    finally:
        await context.close()
        await browser.close()

    return result


async def main_async(args) -> int:
    client_dir = Path(args.client_dir).resolve()
    if not client_dir.exists():
        print(f"ERRO: client_dir nao existe: {client_dir}", file=sys.stderr)
        return 1

    assets_root = client_dir / "assets" / "creatives" / "meta"
    assets_root.mkdir(parents=True, exist_ok=True)
    cache_dir = client_dir / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Parse --pages slug1:target1,slug2:target2
    pages: list[tuple[str, str]] = []
    for spec in args.pages.split(","):
        spec = spec.strip()
        if not spec or ":" not in spec:
            continue
        slug, target = spec.split(":", 1)
        pages.append((slug.strip(), target.strip()))

    if not pages:
        print("ERRO: --pages vazio ou invalido", file=sys.stderr)
        return 1

    now_iso = dt.datetime.now(dt.timezone.utc).isoformat()
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    raw_output = {
        "fetched_at": now_iso,
        "country": args.country,
        "max_ads_per_page": args.max_ads,
        "pages": {},
    }

    async with async_playwright() as pw:
        for slug, target in pages:
            page_dir = assets_root / slug
            page_dir.mkdir(parents=True, exist_ok=True)
            result = await fetch_page(
                pw, target, args.country, args.max_ads, headless=args.headless
            )
            ads = (result.get("ads") or [])[: args.max_ads]

            # Downloads
            manifest_items = []
            for ad in ads:
                ad_id = ad["ads_library_id"]
                ad_dir = page_dir / ad_id
                ad_dir.mkdir(parents=True, exist_ok=True)

                image_url = pick_best_image(ad.get("image_urls", []), ad.get("poster_urls", []))
                image_saved = None
                if image_url:
                    dest = ad_dir / "image.jpg"
                    if download_media(image_url, dest):
                        image_saved = str(dest.relative_to(client_dir))

                # Video: nao baixamos (grande demais pra commitar) — guardamos URL direto
                video_url = None
                if ad.get("video_urls"):
                    video_url = ad["video_urls"][0]

                meta = {
                    "ads_library_id": ad_id,
                    "ads_library_url": ad["ads_library_url"],
                    "page_name": ad.get("page_name"),
                    "page_id": ad.get("page_id"),
                    "start_date_raw": ad.get("start_date_raw"),
                    "platforms": ad.get("platforms", []),
                    "display_format": ad.get("display_format"),
                    "cta_type": ad.get("cta_type"),
                    "link_url": ad.get("link_url"),
                    "copy_excerpt": ad.get("copy_excerpt"),
                    "image_url": image_saved,
                    "thumbnail_url": image_saved,
                    "video_url": video_url,
                    "source_image_url": image_url,
                    "fetched_at": now_iso,
                }
                (ad_dir / "metadata.json").write_text(
                    json.dumps(meta, ensure_ascii=False, indent=2)
                )
                manifest_items.append(meta)

            # Manifest por pagina
            manifest = {
                "slug": slug,
                "target": target,
                "fetched_at": now_iso,
                "total_ads": len(manifest_items),
                "ads": manifest_items,
                "source_url": result.get("page_url"),
            }
            (page_dir / "_manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2)
            )
            raw_output["pages"][slug] = manifest
            print(f"  [saved] {slug}: {len(manifest_items)} ads -> {page_dir.relative_to(client_dir)}")

    raw_path = cache_dir / f"meta_ads_fetch-{ts}.json"
    raw_path.write_text(json.dumps(raw_output, ensure_ascii=False, indent=2))

    # Manifest agregado (latest)
    summary = {
        "fetched_at": now_iso,
        "pages": {
            slug: {
                "total_ads": data["total_ads"],
                "target": data["target"],
            }
            for slug, data in raw_output["pages"].items()
        },
    }
    (assets_root / "_latest.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2)
    )

    print(f"\nOK. Raw: {raw_path}")
    print(f"    Assets: {assets_root}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("client_dir", help="Diretorio do cliente (ex: clientes/<slug-do-cliente>)")
    parser.add_argument("--pages", required=True, help="slug1:page_id_or_name,slug2:...")
    parser.add_argument("--max-ads", type=int, default=30, dest="max_ads")
    parser.add_argument("--country", default="BR")
    parser.add_argument("--headless", default="true", help="true/false")
    args = parser.parse_args()
    args.headless = args.headless.lower() != "false"
    return asyncio.run(main_async(args))


if __name__ == "__main__":
    sys.exit(main())
