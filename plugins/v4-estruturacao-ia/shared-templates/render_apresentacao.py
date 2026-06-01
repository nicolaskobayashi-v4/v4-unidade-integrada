#!/usr/bin/env python3
"""Gera apresentacao.html (slide deck V4) progressivamente a partir do client.json + outputs/*.json.

Uso:
    python3 render_apresentacao.py <path_cliente>

Comportamento progressivo:
- Capa + Pauta + Fechamento sempre presentes.
- Cada skill completada injeta o(s) seu(s) slide(s).
- Skill sem output ainda → slide pulado silenciosamente.

Resultado: deck cresce conforme a Estruturação avança (S1 → S2 → S3).
"""
import json
import os
import sys
import html as _html
from datetime import datetime


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def esc(s):
    if s is None:
        return ""
    return _html.escape(str(s), quote=False)


def safe(v, default="—"):
    if v is None or v == "" or v == []:
        return default
    return v


def fmt_brl(v, prefix="R$ "):
    if v is None:
        return "—"
    try:
        v = float(v)
    except Exception:
        return str(v)

    def _br(num, decimals=2):
        s = f"{num:,.{decimals}f}"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")

    if v >= 1_000_000_000:
        return f"{prefix}{_br(v/1_000_000_000, 2)} bi"
    if v >= 1_000_000:
        return f"{prefix}{_br(v/1_000_000, 2)} MM"
    if v >= 10_000:
        return f"{prefix}{_br(v/1_000, 0)} mil"
    if v >= 1_000:
        # 1.500 → R$ 1.500 (não "R$ 2 mil"). Mantém precisão para faixas até 10k.
        return f"{prefix}{_br(v, 0)}"
    return f"{prefix}{_br(v, 2)}"


def truncate(s, max_chars=180, suffix="…"):
    """Trunca string em palavra-boundary."""
    if not s:
        return ""
    s = str(s).strip()
    if len(s) <= max_chars:
        return s
    cut = s[:max_chars].rsplit(" ", 1)[0]
    return cut + suffix


def parse_money_from_text(s):
    """Extrai primeiro valor monetário de uma string ('R$ 1.270.000+ (...)' → 'R$ 1,27M').

    Retorna valor formatado ou a string original truncada se não achar número.
    """
    if not s:
        return ""
    import re
    m = re.search(r"R\$\s*([\d\.\,]+)", str(s))
    if not m:
        return truncate(s, 28)
    num_str = m.group(1).replace(".", "").replace(",", ".")
    try:
        v = float(num_str)
        return fmt_brl(v)
    except Exception:
        return m.group(0).strip()


def load_client(client_dir):
    path = os.path.join(client_dir, "client.json")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"client.json não encontrado em {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_outputs(client_dir):
    outputs = {}
    outdir = os.path.join(client_dir, "outputs")
    if not os.path.isdir(outdir):
        return outputs
    for fname in sorted(os.listdir(outdir)):
        if not fname.endswith(".json"):
            continue
        key = fname[:-5]
        try:
            with open(os.path.join(outdir, fname), encoding="utf-8") as f:
                outputs[key] = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return outputs


def class_for_score(score):
    if score is None:
        return "cls-low"
    try:
        s = float(score)
    except Exception:
        return "cls-low"
    if s < 20:
        return "cls-critical"
    if s < 35:
        return "cls-low"
    if s < 60:
        return "cls-medium"
    return "cls-good"


def fill_for_score(score):
    cls = class_for_score(score)
    return cls.replace("cls-", "fill-")


def label_for_classification(cls_):
    return {
        "critical": "gap crítico",
        "low": "baixo",
        "medium": "médio",
        "good": "bom",
        "high": "alto",
    }.get((cls_ or "").lower(), cls_ or "")


# ---------------------------------------------------------------------------
# Slide constants
# ---------------------------------------------------------------------------

LOGO = '<div class="slide__header"><span class="logo-v4"><img src="assets/logo-v4-vermelho.png" alt="V4"></span></div>'

# Ordem canônica de slides (a IDs ↔ função builder)
# Builder é chamado se a skill correspondente está completa (existe em outputs).
SLIDE_PLAN = [
    # id_lógico, builder_function_name, skill_id_requerida (None = sempre)
    ("cover", "build_cover", None),
    ("pauta", "build_pauta", None),
    ("onde_estamos", "build_onde_estamos", None),
    ("maturidade", "build_maturidade", "ee-s1-diagnostico-maturidade"),
    ("swot", "build_swot", "ee-s1-swot"),
    ("swot_cruzada", "build_swot_cruzada", "ee-s1-swot"),
    ("persona", "build_persona", "ee-s1-persona-icp"),
    ("auditoria_comm", "build_auditoria_comm", "ee-s1-auditoria-comunicacao"),
    ("pesquisa_mercado", "build_pesquisa_mercado", "ee-s2-pesquisa-mercado"),
    ("concorrentes", "build_concorrentes", "ee-s2-pesquisa-mercado"),
    ("posicionamento", "build_posicionamento", "ee-s2-posicionamento"),
    ("midia_atual", "build_midia_atual", "ee-s2-diagnostico-midia"),
    ("midia_cenarios", "build_midia_cenarios", "ee-s2-diagnostico-midia"),
    ("organico_comparativo", "build_organico_comparativo", "ee-s2-diagnostico-organico-ig"),
    ("organico_padroes", "build_organico_padroes", "ee-s2-diagnostico-organico-ig"),
    ("cro_tecnico", "build_cro_tecnico", "ee-s2-diagnostico-cro"),
    ("cro_muros", "build_cro_muros", "ee-s2-diagnostico-cro"),
    ("proximos_passos", "build_proximos_passos", None),
    ("fechamento", "build_fechamento", None),
]


# ---------------------------------------------------------------------------
# Slide builders
# ---------------------------------------------------------------------------

def build_cover(client, outputs):
    name = client.get("meta", {}).get("name", "Cliente")
    parts = name.split()
    if len(parts) > 1:
        title = f"{parts[0]}<br/>{' '.join(parts[1:])}"
    else:
        title = name
    now = datetime.now()
    month_pt = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ][now.month - 1]
    week = client.get("progress", {}).get("current_week", 1)
    subtitle = f"Diagnóstico Estratégico · Estruturação V4 · Semana {week}"
    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">Diagnóstico Estratégico</span>
        <h1 class="title-mega">{title}</h1>
        <p class="subtitle-text" style="margin-top:24px; font-size:clamp(1.1rem, 1.5vw, 1.5rem);">
          {esc(subtitle)}
        </p>
      </div>
      <div class="slide__footer">
        <span>{month_pt} · {now.year}</span>
        <span>V4 Company · Estruturação Estratégica</span>
      </div>
      <div class="deco-square deco-s1"></div>
      <div class="deco-square deco-s2"></div>
    </section>
    """


def build_pauta(client, outputs):
    items = []
    if "ee-s1-diagnostico-maturidade" in outputs:
        items.append("Maturidade digital — scores por pilar")
    if "ee-s1-persona-icp" in outputs:
        items.append("Persona — ICP e jornada")
    if "ee-s1-swot" in outputs:
        items.append("SWOT — forças, fraquezas, oportunidades, ameaças")
        items.append("SWOT cruzada — estratégias derivadas")
    if "ee-s1-auditoria-comunicacao" in outputs:
        items.append("Auditoria de comunicação — gaps por canal")
    if "ee-s2-pesquisa-mercado" in outputs:
        items.append("Pesquisa de mercado (TAM · SAM · SOM)")
        items.append("Concorrentes-chave")
    if "ee-s2-posicionamento" in outputs:
        items.append("Posicionamento aprovado")
    if "ee-s2-diagnostico-midia" in outputs:
        items.append("Diagnóstico de mídia paga")
    if "ee-s2-diagnostico-organico-ig" in outputs:
        items.append("Conteúdo orgânico — Instagram")
    if "ee-s2-diagnostico-cro" in outputs:
        items.append("Diagnóstico do site (CRO)")
    items.append("Próximos passos do projeto")

    if not items:
        return ""

    mid = (len(items) + 1) // 2
    col1 = "".join(f'<div class="pill">{i+1} · {esc(t)}</div>' for i, t in enumerate(items[:mid]))
    col2 = "".join(f'<div class="pill">{mid+i+1} · {esc(t)}</div>' for i, t in enumerate(items[mid:]))

    return f"""
    <section class="slide">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">Pauta de hoje</span>
        <h2 class="title-section">O que vamos cobrir</h2>
        <div class="row-2" style="margin-top:3vh;">
          <div class="stack">{col1}</div>
          <div class="stack">{col2}</div>
        </div>
      </div>
    </section>
    """


def build_onde_estamos(client, outputs):
    """Slide opcional com KPIs do briefing — exibe só se houver dados úteis."""
    ident = client.get("briefing", {}).get("identification", {})
    product = client.get("briefing", {}).get("product", {})
    research = client.get("research", {}) or {}
    ig = research.get("instagram", {}) or {}

    def _first_number(s):
        if not s:
            return None
        import re
        m = re.search(r"[\d\.\,]+", str(s))
        return m.group(0) if m else None

    kpis = []
    if ident.get("annual_revenue"):
        kpis.append({
            "label": "Faturamento anual",
            "value": esc(parse_money_from_text(ident["annual_revenue"])),
            "hint": esc(truncate(ident.get("monthly_revenue_avg"), 50, "")) if ident.get("monthly_revenue_avg") else "—",
        })
    if product.get("active_customers"):
        num = _first_number(product["active_customers"])
        kpis.append({
            "label": "Clientes ativos",
            "value": esc(num or product["active_customers"]),
            "hint": esc(truncate(product.get("ticket"), 50, "")) if product.get("ticket") else "—",
        })
    if ig.get("followers"):
        kpis.append({
            "label": "Instagram",
            "value": esc(ig["followers"]),
            "hint": ig.get("engagement_rate") and f"engagement {esc(ig['engagement_rate'])}" or "Orgânico",
        })
    if ident.get("years_in_market"):
        years_num = _first_number(ident["years_in_market"])
        kpis.append({
            "label": "Tempo de mercado",
            "value": f"{esc(years_num)} anos" if years_num else esc(ident["years_in_market"]),
            "hint": ident.get("location") and esc(ident["location"]) or "—",
        })

    if len(kpis) < 2:
        return ""

    cards = "".join(f"""
          <div class="glass">
            <div class="kpi__label">{k['label']}</div>
            <div class="kpi__value">{k['value']}</div>
            <div class="kpi__hint">{k['hint']}</div>
          </div>""" for k in kpis[:4])

    return f"""
    <section class="slide slide--diag">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Onde estamos hoje</span>
        <h2 class="title-section">{esc(client.get('meta', {}).get('name', 'Cliente'))} em números reais</h2>
        <div class="row-{len(kpis[:4])}" style="margin-top:3vh;">
          {cards}
        </div>
      </div>
    </section>
    """


def build_maturidade(client, outputs):
    d = outputs.get("ee-s1-diagnostico-maturidade")
    if not d:
        return ""
    overall = d.get("overall_score")
    overall_cls = class_for_score(overall)
    pillars = d.get("pillar_scores") or []
    bench = d.get("sector_benchmark", {}) or {}
    bench_avg = bench.get("sector_average")

    pillar_cards = []
    pillar_name_map = {
        "midia_paga": "Mídia Paga",
        "cro": "CRO",
        "crm": "CRM",
        "seo": "SEO",
        "criativos": "Criativos",
        "branding": "Branding",
        "orgânico": "Orgânico",
        "organico": "Orgânico",
        "site": "Site",
        "analytics": "Analytics",
    }
    for p in pillars[:6]:
        raw_name = (p.get("pillar") or "").lower()
        name = pillar_name_map.get(raw_name) or raw_name.replace("_", " ").title()
        score = p.get("score")
        cls = class_for_score(score)
        fill = fill_for_score(score)
        classification_label = label_for_classification(p.get("classification"))
        pillar_cards.append(f"""
          <div class="pillar-card">
            <div class="pillar-card__name">{esc(name)}</div>
            <div class="pillar-card__score {cls}">{esc(score)}</div>
            <div class="pillar-card__bar"><div class="pillar-card__bar-fill {fill}" style="width:{esc(score or 0)}%;"></div></div>
            <div class="pillar-card__class {cls}">{esc(classification_label)}</div>
          </div>""")

    row_cls = f"row-{min(5, max(2, len(pillar_cards)))}"

    bench_block = ""
    if bench_avg is not None:
        delta_text = ""
        try:
            diff = float(overall) - float(bench_avg)
            if diff > 0:
                delta_text = f'<span class="accent">{diff:+.0f} pts acima</span>'
            elif diff < 0:
                delta_text = f'<span class="accent">{abs(diff):.0f} pts abaixo</span>'
            else:
                delta_text = '<span class="accent">no patamar</span>'
        except Exception:
            pass
        bench_insight = truncate(bench.get("key_insight", ""), 220)
        bench_block = f"""
          <p class="subtitle-text" style="flex:1;">
            Comparado ao setor (média {esc(bench_avg)}), você está {delta_text}. {esc(bench_insight)}
          </p>"""

    headline = truncate(d.get("summary_headline", ""), 200)

    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Maturidade digital</span>
        <h2 class="title-section">Diagnóstico por pilar</h2>
        <div style="display:flex; align-items:center; gap:24px; margin-top:1vh;">
          <div class="glass" style="min-width: 220px; text-align:center; padding:22px;">
            <div class="kpi__label">Score geral</div>
            <div class="kpi__value {overall_cls}" style="font-size:3.4rem;">{esc(overall)}<span style="font-size:1.5rem; opacity:0.6">/100</span></div>
            <div class="kpi__hint {overall_cls}" style="font-weight:700; letter-spacing:0.08em; text-transform:uppercase;">{esc(label_for_classification(d.get('overall_classification')))}</div>
          </div>
          {bench_block}
        </div>
        <div class="{row_cls}" style="margin-top:3vh;">
          {''.join(pillar_cards)}
        </div>
        <div class="highlight-box" style="margin-top:3vh;">
          <div class="highlight-box__label">Leitura V4</div>
          <div class="highlight-box__text">{esc(headline)}</div>
        </div>
      </div>
    </section>
    """


def _swot_quad(label, items, modifier):
    lis = "".join(f"<li>{esc(truncate(t, 160))}</li>" for t in (items or [])[:5])
    return f"""
          <div class="swot-quad swot-quad--{modifier}">
            <div class="swot-quad__label">{esc(label)}</div>
            <ul>{lis}</ul>
          </div>"""


def _swot_items(raw):
    """Normaliza item de SWOT (string ou {text|description}) para string."""
    out = []
    for it in (raw or []):
        if isinstance(it, str):
            out.append(it)
        elif isinstance(it, dict):
            out.append(it.get("text") or it.get("description") or it.get("title") or "")
    return [x for x in out if x]


def build_swot(client, outputs):
    d = outputs.get("ee-s1-swot")
    if not d:
        return ""
    return f"""
    <section class="slide slide--diag">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Análise SWOT</span>
        <h2 class="title-section">Forças · Fraquezas · Oportunidades · Ameaças</h2>
        <div class="swot-grid" style="margin-top:2vh;">
          {_swot_quad('F · Forças', _swot_items(d.get('strengths')), 's')}
          {_swot_quad('W · Fraquezas', _swot_items(d.get('weaknesses')), 'w')}
          {_swot_quad('O · Oportunidades', _swot_items(d.get('opportunities')), 'o')}
          {_swot_quad('T · Ameaças', _swot_items(d.get('threats')), 't')}
        </div>
      </div>
    </section>
    """


def build_swot_cruzada(client, outputs):
    d = outputs.get("ee-s1-swot") or {}
    tows = d.get("tows_matrix") or {}
    if not tows or not isinstance(tows, dict):
        return ""
    so = _swot_items(tows.get("so_strategies"))
    wo = _swot_items(tows.get("wo_strategies"))
    st = _swot_items(tows.get("st_strategies"))
    wt = _swot_items(tows.get("wt_strategies"))
    if not any([so, wo, st, wt]):
        return ""
    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">SWOT cruzada — estratégias derivadas</span>
        <h2 class="title-section">Quatro frentes de ação</h2>
        <div class="swot-grid" style="margin-top:2vh;">
          {_swot_quad('SO · Ofensiva (F × O)', so, 's')}
          {_swot_quad('ST · Defensiva (F × T)', st, 'w')}
          {_swot_quad('WO · Reforço (W × O)', wo, 'o')}
          {_swot_quad('WT · Sobrevivência (W × T)', wt, 't')}
        </div>
      </div>
    </section>
    """


def build_persona(client, outputs):
    d = outputs.get("ee-s1-persona-icp")
    if not d:
        return ""
    persona = d.get("persona") or {}
    if not persona:
        return ""

    # Nome: pega só a primeira persona se houver " e " (dupla) — slide é da principal.
    raw_name = persona.get("name") or "Persona principal"
    name = raw_name.split(" e ")[0].split(" + ")[0].strip()

    # Story: trunca duro pro slide e tenta pegar só o trecho até o '|' (separador de personas)
    story = (persona.get("story") or "").split("|")[0].strip()
    story = truncate(story, 480)

    # Quote: persona.quote (campo direto) ou primeiro trecho até '|'
    quote_raw = persona.get("quote") or ""
    if isinstance(d.get("key_message"), dict):
        quote_raw = quote_raw or d["key_message"].get("primary", "")
    elif isinstance(d.get("key_message"), str):
        quote_raw = quote_raw or d["key_message"]
    quote = truncate((quote_raw or "").split("|")[0].strip(), 220)

    # Onde encontrar
    where = d.get("where_to_find") or {}
    where_summary = ""
    if isinstance(where, dict):
        chunks = []
        for k in ("digital", "online", "offline", "social", "physical", "channels"):
            v = where.get(k)
            if v:
                chunks.append(f"<strong>{esc(k.title())}:</strong> {esc(truncate(v, 140))}")
        where_summary = "<br/>".join(chunks[:3])
    elif isinstance(where, str):
        where_summary = esc(truncate(where, 280))

    return f"""
    <section class="slide">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Persona principal</span>
        <h2 class="title-section">{esc(name)}</h2>
        <div class="row-2" style="margin-top:2vh; flex:1; align-items:stretch;">
          <div class="glass">
            <h3 class="subtitle" style="margin-bottom:14px; color:#ffd0a8;">Quem é</h3>
            <p style="font-size:1.05rem; line-height:1.5; color:rgba(255,245,230,0.95);">{esc(story)}</p>
          </div>
          <div class="glass">
            <h3 class="subtitle" style="margin-bottom:14px; color:#ffd0a8;">Mensagem-chave</h3>
            <p style="font-weight:600; font-size:clamp(1.05rem, 1.35vw, 1.35rem); line-height:1.35; color:#fff; margin:8px 0 18px;">
              {esc(quote) if quote else '—'}
            </p>
            <h3 class="subtitle" style="margin-bottom:8px; color:#ffd0a8; font-size:1.05rem;">Onde encontrar</h3>
            <p style="color:rgba(255,245,230,0.92); font-size:1rem; line-height:1.45;">{where_summary or '—'}</p>
          </div>
        </div>
      </div>
    </section>
    """


def build_auditoria_comm(client, outputs):
    d = outputs.get("ee-s1-auditoria-comunicacao")
    if not d:
        return ""
    findings = d.get("summary_key_findings") or []
    quick_wins = d.get("quick_wins") or []
    qw_items = []
    for it in quick_wins[:5]:
        if isinstance(it, dict):
            qw_items.append(it.get("action") or it.get("title") or it.get("text") or "")
        else:
            qw_items.append(str(it))
    qw_html = "".join(f"<li>{esc(truncate(t, 160))}</li>" for t in qw_items if t)
    find_html = "".join(
        f"<li>{esc(truncate(f.get('text', ''), 200))}</li>" for f in findings[:5] if isinstance(f, dict)
    )

    headline = truncate(d.get("summary_headline", ""), 180)

    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Auditoria de comunicação</span>
        <h2 class="title-section">Gaps por canal</h2>
        <p class="subtitle-text" style="margin-bottom:1.5vh;">{esc(headline)}</p>
        <div class="row-2" style="margin-top:1.5vh; gap:18px;">
          <div class="glass">
            <h3 class="subtitle" style="color:#ffd0a8; margin-bottom:12px; font-size:1.1rem;">Achados principais</h3>
            <ul class="bullets">{find_html}</ul>
          </div>
          <div class="glass" style="border-left:3px solid #80ff9f;">
            <h3 class="subtitle" style="color:#80ff9f; margin-bottom:12px; font-size:1.1rem;">Quick wins</h3>
            <ul class="bullets bullets--check">{qw_html}</ul>
          </div>
        </div>
      </div>
    </section>
    """


def build_pesquisa_mercado(client, outputs):
    d = outputs.get("ee-s2-pesquisa-mercado")
    if not d:
        return ""
    tss = d.get("tam_sam_som") or {}
    tam = tss.get("tam", {}) if isinstance(tss.get("tam"), dict) else {}
    sam = tss.get("sam", {}) if isinstance(tss.get("sam"), dict) else {}
    som = tss.get("som", {}) if isinstance(tss.get("som"), dict) else {}

    def _money(node):
        if not isinstance(node, dict):
            return "—"
        v = node.get("value_brl") or node.get("value") or node.get("brl")
        if v is None:
            return node.get("display") or "—"
        return fmt_brl(v)

    def _short_desc(node):
        if not isinstance(node, dict):
            return ""
        s = node.get("description") or node.get("short_description") or ""
        # Remove flag estimativa [E] do início para slide
        s = s.replace("[E] ", "").replace("[E]", "").strip()
        return truncate(s, 110)

    headline = truncate(d.get("summary_headline", ""), 200)

    return f"""
    <section class="slide slide--diag">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Pesquisa de mercado</span>
        <h2 class="title-section">TAM · SAM · SOM</h2>
        <div class="row-3" style="margin-top:2.5vh;">
          <div class="glass" style="text-align:center;">
            <div class="kpi__label" style="font-size:1rem; letter-spacing:0.12em;">TAM</div>
            <div class="kpi__value" style="font-size:clamp(2.4rem, 3.6vw, 3.4rem);">{esc(_money(tam))}</div>
            <div class="kpi__hint" style="font-size:0.95rem;">{esc(_short_desc(tam))}</div>
          </div>
          <div class="glass" style="text-align:center; border: 2px solid rgba(255,208,168,0.4);">
            <div class="kpi__label" style="font-size:1rem; letter-spacing:0.12em;">SAM</div>
            <div class="kpi__value" style="font-size:clamp(2.4rem, 3.6vw, 3.4rem);">{esc(_money(sam))}</div>
            <div class="kpi__hint" style="font-size:0.95rem;">{esc(_short_desc(sam))}</div>
          </div>
          <div class="glass" style="text-align:center;">
            <div class="kpi__label" style="font-size:1rem; letter-spacing:0.12em;">SOM</div>
            <div class="kpi__value" style="font-size:clamp(2.4rem, 3.6vw, 3.4rem);">{esc(_money(som))}</div>
            <div class="kpi__hint" style="font-size:0.95rem;">{esc(_short_desc(som))}</div>
          </div>
        </div>
        <div class="highlight-box" style="margin-top:3vh;">
          <div class="highlight-box__label">Insight estratégico</div>
          <div class="highlight-box__text">{esc(headline)}</div>
        </div>
      </div>
    </section>
    """


def build_concorrentes(client, outputs):
    d = outputs.get("ee-s2-pesquisa-mercado")
    if not d:
        return ""
    competitors = d.get("competitors") or []
    if not competitors:
        return ""
    rows = []
    for c in competitors[:6]:
        if not isinstance(c, dict):
            continue
        score = c.get("digital_score")
        score_html = f"{esc(score)}<span style=\"opacity:0.5; font-weight:400\">/10</span>" if score is not None else "—"
        rows.append(f"""
            <tr>
              <td class="strong">{esc(c.get('name', '—'))}</td>
              <td class="accent-cell" style="white-space:nowrap;">{score_html}</td>
              <td>{esc(truncate(c.get('positioning', ''), 180))}</td>
            </tr>""")
    if not rows:
        return ""
    return f"""
    <section class="slide">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Concorrentes-chave</span>
        <h2 class="title-section">Quem disputa o mesmo território</h2>
        <table class="compare" style="margin-top:2.5vh;">
          <thead>
            <tr>
              <th>Concorrente</th><th style="width:120px;">Score digital</th><th>Posicionamento</th>
            </tr>
          </thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
      </div>
    </section>
    """


def build_posicionamento(client, outputs):
    d = outputs.get("ee-s2-posicionamento")
    if not d:
        return ""
    puv = d.get("puv")
    if isinstance(puv, dict):
        puv = puv.get("statement") or puv.get("text") or ""
    tagline = d.get("recommended_tagline")
    if isinstance(tagline, dict):
        tagline = tagline.get("text") or tagline.get("tagline") or ""
    territory = d.get("brand_territory") or {}
    if isinstance(territory, dict):
        adjectives = (
            territory.get("three_words")
            or territory.get("adjectives")
            or territory.get("attributes")
            or []
        )
    else:
        adjectives = []

    pills_block = ""
    if adjectives:
        pills = "".join(
            f'<span class="pill" style="font-size:clamp(1rem, 1.35vw, 1.35rem); padding:14px 32px; background:rgba(255,225,180,0.18); border-color:rgba(255,225,180,0.4);">{esc(a)}</span>'
            for a in adjectives[:5]
        )
        pills_block = f"""
        <div style="margin:3vh 0; text-align:center;">
          <div style="display:inline-flex; gap:14px; flex-wrap:wrap; justify-content:center;">{pills}</div>
        </div>"""

    return f"""
    <section class="slide slide--soft">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Posicionamento aprovado</span>
        <h2 class="title-section">Como vamos ser percebidos</h2>{pills_block}
        <div class="row-2" style="gap:18px;">
          <div class="glass">
            <div class="highlight-box__label">PUV — Proposta Única de Valor</div>
            <p style="font-weight:600; font-size:clamp(1rem, 1.2vw, 1.25rem); line-height:1.5; color:#fff; margin-top:10px;">
              {esc(truncate(puv or '', 320) or '—')}
            </p>
          </div>
          <div class="glass" style="display:flex; flex-direction:column; justify-content:center;">
            <div class="highlight-box__label">Tagline aprovada</div>
            <h3 style="font-weight:700; font-size:clamp(1.5rem, 2.6vw, 2.4rem); color:#fff; margin-top:10px; line-height:1.1;">
              {esc(tagline or '—')}
            </h3>
          </div>
        </div>
      </div>
    </section>
    """


def build_midia_atual(client, outputs):
    d = outputs.get("ee-s2-diagnostico-midia")
    if not d:
        return ""
    cm = d.get("current_metrics") or {}

    def _get(*keys):
        if not isinstance(cm, dict):
            return None
        for k in keys:
            v = cm.get(k)
            if v is not None:
                return v
        return None

    cpl = _get("cpl", "cpl_brl", "avg_cpl_brl")
    cpa = _get("cpa", "cpa_brl", "avg_cpa_brl")
    ctr = _get("ctr", "ctr_pct", "avg_ctr_pct")
    cpc = _get("cpc", "cpc_brl")
    leads = _get("total_leads", "leads", "conversions")
    invest = d.get("monthly_budget")
    if invest is None:
        invest = _get("monthly_investment_brl", "monthly_budget_brl", "investment_brl")

    headline = truncate(d.get("summary_headline", ""), 220)

    kpis_html = []
    if invest is not None:
        kpis_html.append(f"""
          <div class="glass">
            <div class="kpi__label">Investimento</div>
            <div class="kpi__value">{esc(fmt_brl(invest) if isinstance(invest, (int, float)) else invest)}<span style="font-size:1.1rem; opacity:0.6">/mês</span></div>
            <div class="kpi__hint">Volume atual de mídia paga</div>
          </div>""")
    # CPA tem prioridade sobre CPL; se ambos faltam mas há CPC, usa CPC
    cost_metric = None
    if cpa is not None:
        cost_metric = ("CPA médio", fmt_brl(cpa) if isinstance(cpa, (int, float)) else cpa, "Custo por aquisição")
    elif cpl is not None:
        cost_metric = ("CPL médio", fmt_brl(cpl) if isinstance(cpl, (int, float)) else cpl, "Custo por lead")
    if cost_metric:
        kpis_html.append(f"""
          <div class="glass">
            <div class="kpi__label">{esc(cost_metric[0])}</div>
            <div class="kpi__value">{esc(cost_metric[1])}</div>
            <div class="kpi__hint">{esc(cost_metric[2])}</div>
          </div>""")
    if ctr is not None:
        try:
            ctr_str = f"{float(ctr):.2f}".replace(".", ",")
        except Exception:
            ctr_str = str(ctr)
        kpis_html.append(f"""
          <div class="glass">
            <div class="kpi__label">CTR médio</div>
            <div class="kpi__value">{esc(ctr_str)}%</div>
            <div class="kpi__hint">Taxa de cliques</div>
          </div>""")
    if leads is not None:
        kpis_html.append(f"""
          <div class="glass">
            <div class="kpi__label">Leads (período)</div>
            <div class="kpi__value">{esc(leads)}</div>
            <div class="kpi__hint">{esc('CPC ' + fmt_brl(cpc) if isinstance(cpc, (int, float)) else 'Conversões medidas')}</div>
          </div>""")

    if not kpis_html:
        return ""

    row_cls = f"row-{min(4, max(2, len(kpis_html)))}"
    return f"""
    <section class="slide slide--diag">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Mídia paga · números atuais</span>
        <h2 class="title-section">Diagnóstico de mídia paga</h2>
        <p class="subtitle-text" style="margin-bottom:1.5vh;">{esc(headline)}</p>
        <div class="{row_cls}" style="margin-top:1.5vh;">
          {''.join(kpis_html)}
        </div>
      </div>
    </section>
    """


def build_midia_cenarios(client, outputs):
    d = outputs.get("ee-s2-diagnostico-midia")
    if not d:
        return ""
    scenarios = d.get("budget_reallocation_scenarios")
    if not isinstance(scenarios, dict):
        return ""

    cards = []
    for key, label in [
        ("scenario_a_conservative", "A · Conservador"),
        ("scenario_b_realistic", "B · Recomendado"),
        ("scenario_c_aggressive", "C · Agressivo"),
    ]:
        sc = scenarios.get(key)
        if not isinstance(sc, dict):
            continue
        total = sc.get("total_budget_monthly")
        leads = sc.get("expected_leads_monthly")
        delta = sc.get("delta_leads") or ""
        cpl = sc.get("expected_cpl")
        is_recommended = "realistic" in key
        border = "border: 2px solid rgba(255,208,168,0.4);" if is_recommended else ""
        color = "color:#ffd0a8;" if is_recommended else ""
        if leads:
            extras = []
            if delta:
                extras.append(esc(delta))
            if cpl is not None:
                extras.append(f"CPL {esc(fmt_brl(cpl) if isinstance(cpl, (int, float)) else cpl)}")
            extras_str = " · ".join(extras)
            hint_short = f"~{esc(leads)} leads/mês" + (f" · {extras_str}" if extras_str else "")
        else:
            hint_short = truncate(sc.get("risk_assessment", ""), 140)
        # Formato custom para budget: força "R$ X.XXX" em vez de "R$ X mil"
        if isinstance(total, (int, float)):
            total_fmt = f"R$ {int(total):,}".replace(",", ".")
        else:
            total_fmt = str(total or "—")
        cards.append(f"""
          <div class="glass" style="{border}">
            <div class="kpi__label" style="{color}">Cenário {esc(label)}</div>
            <div class="kpi__value" style="font-size:1.9rem; {color}">{esc(total_fmt)}<span style="font-size:1rem; opacity:0.6">/mês</span></div>
            <div class="kpi__hint" style="margin-top:8px;">{esc(hint_short)}</div>
          </div>""")

    if not cards:
        return ""

    return f"""
    <section class="slide">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Mídia paga · cenários de escala</span>
        <h2 class="title-section">Realocar e reestruturar a operação</h2>
        <div class="row-{len(cards)}" style="margin-top:3vh;">{''.join(cards)}</div>
        <div class="highlight-box" style="margin-top:3vh;">
          <div class="highlight-box__label">Recomendação V4</div>
          <div class="highlight-box__text">{esc(scenarios.get('description', ''))}</div>
        </div>
      </div>
    </section>
    """


def build_organico_comparativo(client, outputs):
    d = outputs.get("ee-s2-diagnostico-organico-ig")
    if not d:
        return ""
    me = d.get("client_account") or {}
    comps = d.get("competitor_accounts") or []
    if not me and not comps:
        return ""

    # Index by username
    cadence_by_user = {}
    for r in (d.get("cadence") or {}).get("by_account", []) or []:
        if isinstance(r, dict) and r.get("username"):
            cadence_by_user[r["username"]] = r
    eng_by_user = {}
    for r in (d.get("engagement_benchmark") or {}).get("by_account", []) or []:
        if isinstance(r, dict) and r.get("username"):
            eng_by_user[r["username"]] = r

    def _row(acc, is_me=False):
        u = acc.get("username", "")
        cad = cadence_by_user.get(u, {})
        eng = eng_by_user.get(u, {})
        followers = acc.get("followers_count")
        posts = cad.get("posts_per_week")
        engagement = eng.get("avg_engagement_proxy")
        fmt = eng.get("best_format_by_engagement") or "—"

        # Format engagement as percentage
        eng_str = "—"
        if engagement is not None:
            try:
                eng_str = f"{float(engagement):.2f}%"
            except Exception:
                eng_str = str(engagement)
        # Format posts/week
        posts_str = "—"
        if posts is not None:
            try:
                posts_str = f"{float(posts):.2f}".replace(".", ",")
            except Exception:
                posts_str = str(posts)
        # Followers with thousands separator
        fol_str = "—"
        if followers is not None:
            try:
                fol_str = f"{int(followers):,}".replace(",", ".")
            except Exception:
                fol_str = str(followers)

        if is_me:
            return f"""
            <tr style="background:rgba(255,225,180,0.1);">
              <td class="strong">@{esc(u)} (você)</td>
              <td>{esc(fol_str)}</td>
              <td>{esc(posts_str)}</td>
              <td class="accent-cell" style="font-size:1.15rem;">{esc(eng_str)}</td>
              <td>{esc(fmt)}</td>
            </tr>"""
        return f"""
            <tr>
              <td>@{esc(u)}</td>
              <td>{esc(fol_str)}</td>
              <td>{esc(posts_str)}</td>
              <td>{esc(eng_str)}</td>
              <td>{esc(fmt)}</td>
            </tr>"""

    rows = [_row(me, is_me=True)]
    for c in comps[:3]:
        if isinstance(c, dict):
            rows.append(_row(c))

    headline = truncate((d.get("key_insight") or {}).get("headline") or d.get("summary_headline", ""), 220)

    return f"""
    <section class="slide slide--diag">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Conteúdo orgânico · Instagram</span>
        <h2 class="title-section">Você vs concorrentes</h2>
        <table class="compare" style="margin-top:2.5vh;">
          <thead>
            <tr><th>Conta</th><th>Followers</th><th>Posts/sem</th><th>Engagement</th><th>Melhor formato</th></tr>
          </thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
        <div class="highlight-box" style="margin-top:3vh;">
          <div class="highlight-box__label">Leitura V4 — Key Insight</div>
          <div class="highlight-box__text">{esc(headline)}</div>
        </div>
      </div>
    </section>
    """


def build_organico_padroes(client, outputs):
    d = outputs.get("ee-s2-diagnostico-organico-ig")
    if not d:
        return ""
    missing = d.get("competitor_patterns_missing") or []
    if not missing:
        return ""
    cards = []
    for i, p in enumerate(missing[:5]):
        if not isinstance(p, dict):
            continue
        pattern_name = truncate(p.get("pattern", "—"), 60)
        body = p.get("why_works") or p.get("how_to_apply") or "—"
        cards.append(f"""
          <div class="glass" style="padding:18px;">
            <div class="kpi__label" style="font-size:0.85rem;">{i+1} · {esc(pattern_name)}</div>
            <p style="font-size:1rem; line-height:1.45; margin-top:10px; color:rgba(255,245,230,0.95);">
              {esc(truncate(body, 180))}
            </p>
          </div>""")
    if not cards:
        return ""
    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Conteúdo orgânico · gaps</span>
        <h2 class="title-section">Padrões dos concorrentes que você ainda não usa</h2>
        <div class="row-{min(5, len(cards))}" style="margin-top:3vh; gap:14px; flex:1;">{''.join(cards)}</div>
      </div>
    </section>
    """


def build_cro_tecnico(client, outputs):
    d = outputs.get("ee-s2-diagnostico-cro")
    if not d:
        return ""
    tech = d.get("technical_audit") or {}
    psi = tech.get("pagespeed") or tech.get("psi") or {}
    # Estrutura real: pagespeed.mobile_scores.{performance,accessibility,best_practices,seo}
    scores = {}
    if isinstance(psi, dict):
        ms = psi.get("mobile_scores") or psi.get("mobile") or psi
        if isinstance(ms, dict):
            scores = ms

    kpis = []
    for key, label in [
        ("performance", "PageSpeed"),
        ("accessibility", "Acessibilidade"),
        ("best_practices", "Best Practices"),
        ("seo", "SEO"),
    ]:
        v = scores.get(key)
        if v is not None:
            kpis.append((label, v))

    if not kpis:
        return ""

    kpi_html = "".join(f"""
          <div class="glass">
            <div class="kpi__label">{esc(label)}</div>
            <div class="kpi__value">{esc(score)}<span style="font-size:1.3rem; opacity:0.6">/100</span></div>
            <div class="kpi__hint">Mobile</div>
          </div>""" for label, score in kpis)

    headline = truncate(d.get("summary_headline", ""), 220)

    return f"""
    <section class="slide slide--diag">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Site e conversão · técnico</span>
        <h2 class="title-section">Diagnóstico técnico do site</h2>
        <p class="subtitle-text" style="margin-bottom:1.5vh;">{esc(headline)}</p>
        <div class="row-{min(4, len(kpis))}" style="margin-top:1.5vh;">{kpi_html}</div>
      </div>
    </section>
    """


def build_cro_muros(client, outputs):
    d = outputs.get("ee-s2-diagnostico-cro")
    if not d:
        return ""
    items = []

    # 1) Preferência: top_problems (se a skill os emitir explicitamente)
    top_problems = d.get("top_problems")
    if isinstance(top_problems, list):
        for p in top_problems[:3]:
            if isinstance(p, dict):
                items.append({
                    "title": p.get("title") or p.get("problem") or p.get("dimension") or "—",
                    "text": p.get("description") or p.get("text") or p.get("impact") or "",
                })

    # 2) Fallback: hipóteses P1 (high impact)
    if not items:
        hypotheses = d.get("test_hypotheses") or []
        p1 = [h for h in hypotheses if isinstance(h, dict) and h.get("priority") == "P1"]
        for h in p1[:3]:
            items.append({
                "title": h.get("element") or "—",
                "text": h.get("hypothesis") or h.get("expected_impact_description") or "",
            })

    # 3) Último recurso: critical_issues como strings
    if not items:
        ci = (d.get("technical_diagnosis") or {}).get("critical_issues")
        if isinstance(ci, list):
            for s in ci[:3]:
                if isinstance(s, str) and s.strip():
                    # tenta separar título em "— "
                    parts = s.split(" — ", 1)
                    items.append({
                        "title": truncate(parts[0], 60),
                        "text": parts[1] if len(parts) > 1 else "",
                    })

    if not items:
        return ""

    cards = "".join(f"""
          <div class="glass" style="border-left:3px solid #ff8080; padding:24px;">
            <h3 class="subtitle" style="color:#ff9c9c; margin-bottom:12px; font-size:1.2rem;">{esc(truncate(it['title'], 60))}</h3>
            <p style="font-size:1.05rem; line-height:1.5; color:rgba(255,245,230,0.95);">{esc(truncate(it['text'], 240))}</p>
          </div>""" for it in items)
    return f"""
    <section class="slide">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Site e conversão · principais gargalos</span>
        <h2 class="title-section">Os {len(items)} muros reais de conversão</h2>
        <div class="row-{len(items)}" style="margin-top:3vh; flex:1;">{cards}</div>
      </div>
    </section>
    """


def build_proximos_passos(client, outputs):
    """Slide gerado a partir do progresso atual + skills pendentes."""
    progress = client.get("progress", {}) or {}
    skills_state = progress.get("skills", {}) or {}
    current_week = progress.get("current_week", 1)

    # Skills pendentes da próxima semana
    next_week = current_week + 1
    next_week_skills_by_prefix = {
        2: "ee-s2",
        3: "ee-s3",
        4: "ee-s4",
        5: "ee-s5",
    }
    prefix = next_week_skills_by_prefix.get(next_week)
    if not prefix:
        return ""

    pending = []
    for sid, st in skills_state.items():
        if sid.startswith(prefix) and (st.get("status") in (None, "pending", "in_progress")):
            pending.append(sid)

    if not pending:
        return ""

    # Bucketize
    digital = []
    operacao = []
    identidade = []
    vendas = []
    for sid in pending:
        if "brandbook" in sid or "manual-marca" in sid or "identidade-visual" in sid:
            identidade.append(sid)
        elif "comercial" in sid or "cliente-oculto" in sid or "sdr" in sid or "crm" in sid:
            vendas.append(sid)
        elif "landing" in sid or "copy" in sid or "criativos" in sid or "forecast" in sid:
            digital.append(sid)
        else:
            operacao.append(sid)

    columns = []
    for name, lst in [
        ("Identidade", identidade),
        ("Digital", digital),
        ("Operação", operacao),
        ("Vendas", vendas),
    ]:
        if not lst:
            continue
        lis = "".join(f"<li>{esc(_pretty_skill_name(sid))}</li>" for sid in lst)
        columns.append(f"""
          <div class="glass">
            <h3 class="subtitle" style="color:#ffd0a8; margin-bottom:14px; font-size:1.2rem;">{name}</h3>
            <ul class="bullets bullets--check" style="font-size:1.02rem;">{lis}</ul>
          </div>""")

    if not columns:
        return ""

    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">Próximos passos do projeto</span>
        <h2 class="title-section">O que vamos executar na Semana {next_week}</h2>
        <div class="row-{min(3, len(columns))}" style="margin-top:3vh; gap:18px;">{''.join(columns)}</div>
      </div>
    </section>
    """


SKILL_PRETTY_NAMES = {
    "ee-s1-diagnostico-maturidade": "Diagnóstico de Maturidade",
    "ee-s1-swot": "SWOT",
    "ee-s1-persona-icp": "Persona / ICP",
    "ee-s1-auditoria-comunicacao": "Auditoria de Comunicação",
    "ee-s2-pesquisa-mercado": "Pesquisa de Mercado",
    "ee-s2-posicionamento": "Posicionamento",
    "ee-s2-diagnostico-midia": "Diagnóstico de Mídia Paga",
    "ee-s2-diagnostico-organico-ig": "Diagnóstico Orgânico (IG)",
    "ee-s2-diagnostico-cro": "Diagnóstico de CRO",
    "ee-s2-diagnostico-criativos": "Diagnóstico de Criativos",
    "ee-s3-brandbook": "Brandbook",
    "ee-s3-copy-anuncios": "Copy de Anúncios",
    "ee-s3-criativos-anuncios": "Criativos de Anúncios",
    "ee-s3-crm-setup": "Setup de CRM",
    "ee-s3-forecast-midia": "Forecast de Mídia",
    "ee-s3-gmb-otimizacao": "GMB · Otimização",
    "ee-s3-identidade-visual": "Identidade Visual",
    "ee-s3-landing-page": "Landing Page",
    "ee-s3-manual-marca": "Manual de Marca",
    "ee-s4-cliente-oculto": "Cliente Oculto",
    "ee-s4-diagnostico-comercial": "Diagnóstico Comercial",
    "ee-s5-scripts-sdr": "Scripts SDR",
    "ee-s5-sdr-ia-config": "SDR IA · Config",
}


def _pretty_skill_name(sid):
    """ee-s3-landing-page → Landing Page (com acentos)."""
    if sid in SKILL_PRETTY_NAMES:
        return SKILL_PRETTY_NAMES[sid]
    base = sid
    for prefix in ("ee-s1-", "ee-s2-", "ee-s3-", "ee-s4-", "ee-s5-"):
        if base.startswith(prefix):
            base = base[len(prefix):]
            break
    return base.replace("-", " ").title()


def build_fechamento(client, outputs):
    return """
    <section class="slide slide--soft">
      """ + LOGO + """
      <div class="slide__content" style="justify-content:center; text-align:center;">
        <h1 class="title-mega" style="margin:0 auto;">Obrigado.</h1>
        <p class="subtitle-text" style="margin:32px auto 0; font-size:clamp(1.1rem, 1.4vw, 1.4rem); max-width:700px;">
          Vamos juntos transformar contexto em escala.
        </p>
      </div>
      <div class="slide__footer">
        <span>V4 Company · Estruturação Estratégica</span>
        <span></span>
      </div>
    </section>
    """


# ---------------------------------------------------------------------------
# Composition
# ---------------------------------------------------------------------------

BUILDERS = {
    "build_cover": build_cover,
    "build_pauta": build_pauta,
    "build_onde_estamos": build_onde_estamos,
    "build_maturidade": build_maturidade,
    "build_swot": build_swot,
    "build_swot_cruzada": build_swot_cruzada,
    "build_persona": build_persona,
    "build_auditoria_comm": build_auditoria_comm,
    "build_pesquisa_mercado": build_pesquisa_mercado,
    "build_concorrentes": build_concorrentes,
    "build_posicionamento": build_posicionamento,
    "build_midia_atual": build_midia_atual,
    "build_midia_cenarios": build_midia_cenarios,
    "build_organico_comparativo": build_organico_comparativo,
    "build_organico_padroes": build_organico_padroes,
    "build_cro_tecnico": build_cro_tecnico,
    "build_cro_muros": build_cro_muros,
    "build_proximos_passos": build_proximos_passos,
    "build_fechamento": build_fechamento,
}


def compose_slides(client, outputs):
    slides_html = []
    for slide_id, builder_name, required_skill in SLIDE_PLAN:
        if required_skill and required_skill not in outputs:
            continue
        builder = BUILDERS.get(builder_name)
        if not builder:
            continue
        try:
            html_chunk = builder(client, outputs) or ""
        except Exception as e:
            sys.stderr.write(f"[apresentacao] builder {builder_name} falhou: {e}\n")
            continue
        if html_chunk.strip():
            slides_html.append(html_chunk)
    return "\n".join(slides_html)


# ---------------------------------------------------------------------------
# Shell HTML (estilo V4 — palette vermelha + IBM Plex Sans)
# ---------------------------------------------------------------------------

SHELL_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{
    height: 100%; width: 100%; overflow: hidden;
    background: #0a0a0a; color: #fff;
    font-family: 'IBM Plex Sans', -apple-system, sans-serif;
  }}

  .presentation {{ position: fixed; inset: 0; overflow: hidden; }}
  .slides-track {{
    display: flex; height: 100vh; width: 100vw;
    transition: transform 0.5s cubic-bezier(0.7, 0, 0.3, 1);
  }}
  .slide {{
    flex: 0 0 100vw; height: 100vh;
    position: relative; overflow-y: auto; overflow-x: hidden;
    padding: 4vh 5vw 8vh;
    display: flex; flex-direction: column;
    background: radial-gradient(ellipse at center, #ff3a1f 0%, #d61a0e 55%, #8a0d05 100%);
  }}
  .slide--alt {{ background: linear-gradient(135deg, #ff5a2c 0%, #e6230e 60%, #8a0d05 100%); }}
  .slide--diag {{ background: radial-gradient(circle at 30% 50%, #ff6a3c 0%, #d61a0e 50%, #5a0802 100%); }}
  .slide--soft {{ background: linear-gradient(180deg, #b81409 0%, #f04823 100%); }}

  .slide__header {{ display: flex; align-items: center; margin-bottom: 2.5vh; }}
  .logo-v4 {{
    display: inline-flex; align-items: center; justify-content: center;
    width: 64px; height: 64px; background: #fff;
    border-radius: 14px; box-shadow: 0 6px 22px rgba(0,0,0,0.18);
  }}
  .logo-v4 img {{ width: 72%; height: 72%; object-fit: contain; display: block; }}

  h1.title-mega {{
    font-weight: 700; font-size: clamp(3.5rem, 8vw, 7.5rem);
    line-height: 0.95; letter-spacing: -0.03em;
    background: linear-gradient(180deg, #ffe1c0 0%, #f5a665 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
  }}
  h2.title-section {{
    font-weight: 700; font-size: clamp(2.2rem, 4.5vw, 4rem);
    line-height: 1.05; letter-spacing: -0.02em; color: #fff; margin-bottom: 2vh;
  }}
  h3.subtitle {{ font-weight: 600; font-size: clamp(1.15rem, 1.7vw, 1.7rem); line-height: 1.2; color: #fff; }}
  .eyebrow {{
    display: inline-block; font-weight: 600; font-size: clamp(0.8rem, 0.95vw, 1rem);
    letter-spacing: 0.08em; text-transform: uppercase; color: #ffd0a8;
    padding: 8px 18px; border-radius: 100px;
    background: rgba(255,220,180,0.12); border: 1px solid rgba(255,220,180,0.2);
    backdrop-filter: blur(8px); margin-bottom: 1.6vh;
  }}
  .subtitle-text {{
    font-weight: 500; font-size: clamp(1rem, 1.3vw, 1.35rem); line-height: 1.45;
    color: rgba(255, 240, 220, 0.92); max-width: 900px;
  }}
  .accent {{ color: #ffd0a8; font-weight: 700; }}
  .strong {{ color: #fff; font-weight: 700; }}

  .pill {{
    display: inline-block; padding: 10px 22px; border-radius: 100px;
    background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.18);
    backdrop-filter: blur(12px); font-weight: 600; font-size: 0.95rem; color: #fff;
  }}
  .glass {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    backdrop-filter: blur(14px);
    border-radius: 18px; padding: 22px;
  }}

  .row-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }}
  .row-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
  .row-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }}
  .row-5 {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; }}
  .stack {{ display: flex; flex-direction: column; gap: 12px; }}

  .kpi__label {{
    font-weight: 600; font-size: 0.78rem;
    letter-spacing: 0.06em; text-transform: uppercase;
    color: rgba(255,220,180,0.85); margin-bottom: 6px;
  }}
  .kpi__value {{
    font-weight: 700; font-size: clamp(1.9rem, 2.8vw, 2.6rem);
    line-height: 1; color: #fff; letter-spacing: -0.02em; margin-bottom: 6px;
  }}
  .kpi__hint {{ font-size: 0.9rem; color: rgba(255,255,255,0.75); line-height: 1.35; }}

  ul.bullets {{ list-style: none; padding: 0; }}
  ul.bullets li {{
    font-weight: 500; font-size: clamp(1rem, 1.18vw, 1.18rem);
    line-height: 1.45; color: rgba(255,245,230,0.96);
    padding: 9px 0 9px 28px; position: relative;
  }}
  ul.bullets li::before {{
    content: ''; position: absolute; left: 0; top: 20px;
    width: 16px; height: 2px; background: #ffd0a8; border-radius: 2px;
  }}
  ul.bullets--check li::before {{
    content: '✓'; width: auto; height: auto; background: none;
    left: 2px; top: 8px; color: #ffd0a8; font-weight: 700; font-size: 1.15rem;
  }}

  .highlight-box {{
    background: linear-gradient(135deg, rgba(255,225,180,0.16), rgba(255,225,180,0.06));
    border-left: 4px solid #ffd0a8; padding: 18px 22px; border-radius: 10px;
  }}
  .highlight-box__label {{
    font-size: 0.78rem; letter-spacing: 0.1em; text-transform: uppercase;
    color: #ffd0a8; font-weight: 700; margin-bottom: 6px;
  }}
  .highlight-box__text {{
    font-weight: 600; font-size: clamp(1rem, 1.2vw, 1.25rem);
    line-height: 1.45; color: #fff;
  }}

  .compare {{ width: 100%; border-collapse: collapse; }}
  .compare th, .compare td {{
    padding: 13px 14px; text-align: left;
    font-size: clamp(0.9rem, 1.05vw, 1.05rem);
    color: rgba(255,245,230,0.94);
  }}
  .compare th {{
    font-weight: 700; font-size: 0.78rem;
    letter-spacing: 0.08em; text-transform: uppercase;
    color: #ffd0a8; border-bottom: 1px solid rgba(255,255,255,0.18);
  }}
  .compare td {{ border-bottom: 1px solid rgba(255,255,255,0.06); }}
  .compare tr:last-child td {{ border-bottom: none; }}
  .compare .accent-cell {{ color: #ffd0a8; font-weight: 700; }}

  .swot-grid {{
    display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr;
    gap: 16px; flex: 1; min-height: 0;
  }}
  .swot-quad {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    backdrop-filter: blur(14px); border-radius: 14px;
    padding: 20px 22px; overflow: hidden;
    display: flex; flex-direction: column;
  }}
  .swot-quad__label {{
    font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase;
    color: #ffd0a8; font-weight: 700; margin-bottom: 12px;
  }}
  .swot-quad ul {{ list-style: none; padding: 0; }}
  .swot-quad ul li {{
    font-size: clamp(0.95rem, 1.05vw, 1.05rem);
    line-height: 1.4; padding: 6px 0 6px 18px;
    position: relative; color: rgba(255,245,230,0.95);
  }}
  .swot-quad ul li::before {{
    content: '•'; position: absolute; left: 4px; top: 5px;
    color: #ffd0a8; font-weight: 700;
  }}
  .swot-quad--s {{ border-left: 3px solid #80ff9f; }}
  .swot-quad--w {{ border-left: 3px solid #ffb780; }}
  .swot-quad--o {{ border-left: 3px solid #80c8ff; }}
  .swot-quad--t {{ border-left: 3px solid #ff8080; }}

  .pillar-card {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    backdrop-filter: blur(14px); border-radius: 14px;
    padding: 18px; text-align: center;
  }}
  .pillar-card__score {{
    font-weight: 700; font-size: clamp(2.2rem, 3vw, 2.8rem);
    line-height: 1; letter-spacing: -0.02em; margin-bottom: 4px;
  }}
  .pillar-card__bar {{
    height: 8px; background: rgba(255,255,255,0.16);
    border-radius: 6px; overflow: hidden; margin: 10px 0 10px;
  }}
  .pillar-card__bar-fill {{ height: 100%; border-radius: 6px; }}
  .pillar-card__name {{
    font-weight: 600; font-size: 0.95rem;
    letter-spacing: 0.04em; text-transform: uppercase;
    color: rgba(255,220,180,0.9); margin-bottom: 4px;
  }}
  .pillar-card__class {{
    font-size: 0.78rem; text-transform: uppercase;
    letter-spacing: 0.08em; font-weight: 700;
  }}
  .cls-critical {{ color: #ff8c8c; }}
  .cls-low {{ color: #ffb780; }}
  .cls-medium {{ color: #ffe18c; }}
  .cls-good {{ color: #80ff9f; }}
  .fill-critical {{ background: linear-gradient(90deg, #ff3a3a, #ff7a7a); }}
  .fill-low {{ background: linear-gradient(90deg, #ff7a3a, #ffb780); }}
  .fill-medium {{ background: linear-gradient(90deg, #ffb780, #ffe18c); }}
  .fill-good {{ background: linear-gradient(90deg, #80ff9f, #b8ffc8); }}

  .slide__content {{ flex: 1; display: flex; flex-direction: column; min-height: 0; }}
  .slide__footer {{
    margin-top: auto; display: flex; justify-content: space-between;
    align-items: flex-end; font-size: 0.78rem;
    color: rgba(255,220,180,0.5); font-weight: 500; padding-top: 1.5vh;
  }}

  .controls {{
    position: fixed; bottom: 0; left: 0; right: 0;
    display: flex; align-items: center; gap: 18px;
    padding: 14px 24px;
    background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.55) 60%);
    z-index: 10;
  }}
  .control-btn {{
    width: 38px; height: 38px; border-radius: 50%;
    background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.18);
    backdrop-filter: blur(8px); color: #fff; font-size: 1.1rem;
    display: inline-flex; align-items: center; justify-content: center;
    cursor: pointer; user-select: none; transition: background .2s;
  }}
  .control-btn:hover {{ background: rgba(255,255,255,0.18); }}
  .control-btn:disabled {{ opacity: 0.3; cursor: not-allowed; }}
  .progress-bar {{
    flex: 1; height: 4px; border-radius: 4px;
    background: rgba(255,255,255,0.16); overflow: hidden;
  }}
  .progress-bar__fill {{
    height: 100%; background: linear-gradient(90deg, #ffd0a8 0%, #f5a665 100%);
    transition: width 0.4s cubic-bezier(0.7, 0, 0.3, 1); border-radius: 4px;
  }}
  .counter {{
    font-weight: 600; font-size: 0.9rem;
    color: rgba(255,255,255,0.85); letter-spacing: 0.04em;
    min-width: 60px; text-align: center;
  }}

  .deco-square {{
    position: absolute; border-radius: 18px;
    background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
    border: 1px solid rgba(255,255,255,0.05); pointer-events: none;
  }}
  .deco-s1 {{ width: 300px; height: 300px; top: -80px; right: -80px; transform: rotate(15deg); }}
  .deco-s2 {{ width: 200px; height: 200px; bottom: -60px; left: 6%; transform: rotate(-12deg); opacity: 0.5; }}

  .hint {{
    position: fixed; top: 14px; right: 18px;
    font-size: 0.75rem; color: rgba(255,220,180,0.5);
    font-weight: 500; pointer-events: none; z-index: 5;
  }}
</style>
</head>
<body>

<div class="hint">← → setas para navegar · F para tela cheia</div>

<div class="presentation">
  <div class="slides-track" id="track">
{slides}
  </div>

  <div class="controls">
    <button class="control-btn" id="prev" aria-label="Anterior">‹</button>
    <div class="progress-bar"><div class="progress-bar__fill" id="progress"></div></div>
    <span class="counter" id="counter">1 / {total_slides}</span>
    <button class="control-btn" id="next" aria-label="Próximo">›</button>
    <button class="control-btn" id="fullscreen" aria-label="Tela cheia">⛶</button>
  </div>
</div>

<script>
  (function() {{
    const track = document.getElementById('track');
    const slides = track.querySelectorAll('.slide');
    const total = slides.length;
    const counter = document.getElementById('counter');
    const progress = document.getElementById('progress');
    const prevBtn = document.getElementById('prev');
    const nextBtn = document.getElementById('next');
    const fsBtn = document.getElementById('fullscreen');
    let current = 0;

    function render() {{
      track.style.transform = `translateX(-${{current * 100}}vw)`;
      counter.textContent = `${{current + 1}} / ${{total}}`;
      progress.style.width = `${{((current + 1) / total) * 100}}%`;
      prevBtn.disabled = current === 0;
      nextBtn.disabled = current === total - 1;
    }}

    function next() {{ if (current < total - 1) {{ current++; render(); }} }}
    function prev() {{ if (current > 0) {{ current--; render(); }} }}
    function goto(i) {{ current = Math.max(0, Math.min(total - 1, i)); render(); }}

    prevBtn.addEventListener('click', prev);
    nextBtn.addEventListener('click', next);
    fsBtn.addEventListener('click', () => {{
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
      else document.exitFullscreen();
    }});

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{ e.preventDefault(); next(); }}
      else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{ e.preventDefault(); prev(); }}
      else if (e.key === 'Home') {{ e.preventDefault(); goto(0); }}
      else if (e.key === 'End') {{ e.preventDefault(); goto(total - 1); }}
      else if (e.key === 'f' || e.key === 'F') {{ fsBtn.click(); }}
    }});

    let touchStartX = 0;
    document.addEventListener('touchstart', (e) => {{ touchStartX = e.changedTouches[0].screenX; }}, {{passive: true}});
    document.addEventListener('touchend', (e) => {{
      const dx = e.changedTouches[0].screenX - touchStartX;
      if (Math.abs(dx) > 60) (dx < 0 ? next : prev)();
    }}, {{passive: true}});

    render();
  }})();
</script>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def render(client_dir):
    client = load_client(client_dir)
    outputs = load_outputs(client_dir)

    # Gate: apresentacao só aparece a partir da primeira skill S1 completa.
    # Antes disso, o cliente recém-onboardado não precisa de deck.
    has_s1_output = any(k.startswith("ee-s1-") for k in outputs.keys())
    out_path = os.path.join(client_dir, "apresentacao.html")
    if not has_s1_output:
        return None

    slides_html = compose_slides(client, outputs)
    name = client.get("meta", {}).get("name", "Cliente")
    title = f"{name} · Diagnóstico Estratégico"
    total_slides = slides_html.count('<section class="slide')
    html_out = SHELL_HTML.format(title=esc(title), slides=slides_html, total_slides=total_slides)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    return out_path


def main():
    if len(sys.argv) < 2:
        print("Uso: render_apresentacao.py <path_cliente>", file=sys.stderr)
        sys.exit(2)
    client_dir = sys.argv[1].rstrip("/")
    if not os.path.isdir(client_dir):
        print(f"Diretório não encontrado: {client_dir}", file=sys.stderr)
        sys.exit(2)
    out = render(client_dir)
    if out is None:
        print("Apresentação não gerada — nenhuma skill S1 completa ainda.")
    else:
        print(f"Apresentação gerada: {out}")


if __name__ == "__main__":
    main()
