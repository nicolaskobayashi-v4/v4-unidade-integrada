#!/usr/bin/env python3
"""render_kickoff.py — Apresentação de Kickoff (apoio à 1ª reunião).

Deck cliente-facing de APOIO à reunião de kickoff (30–45 min) — o começo do ciclo,
complementar à apresentacao-entrega.html (que é o fechamento). Vários slides são telas de
apoio: tópicos que lembram o cliente do que falar (Sobre a Empresa, Benchmarking), não dumps
de dados.

Slides: capa → quem conduz (investidor V4) → você além do contrato → sumário da reunião →
sobre a empresa (apoio) → benchmarking (apoio) → como funciona a entrega (semana a semana,
model-aware) → próximos passos.

Mesmo design system da apresentacao-entrega (paleta V4, IBM Plex Sans, navegação ← → F + touch).

Uso: render_kickoff.py <path_cliente>
Gera: <client_dir>/kickoff.html
"""

import sys
import os
import base64
import json
import html as _html
from datetime import datetime


# --- Helpers (autocontido) ---
def esc(s):
    return "" if s is None else _html.escape(str(s), quote=True)


def safe(v, default="—"):
    return default if v is None or v == "" or v == [] else v


def load_client(client_dir):
    path = os.path.join(client_dir, "client.json")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"client.json não encontrado em {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


LOGO = '<div class="slide__header"><span class="logo-v4" aria-label="V4"></span></div>'

MODELO_LABEL = {
    "e-commerce": "E-commerce",
    "inside-sales": "Inside Sales",
    "pdv": "PDV / Loja Física",
}

MESES_PT = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Nome amigável de cada entrega (espelha ENTREGA_NAMES de render_apresentacao_entrega.py —
# mantém consistência entre os dois decks). Cobre as 4 semanas dos 3 modelos.
SKILL_LABELS = {
    "ee-s1-persona-icp": "Persona & ICP",
    "ee-s2-posicionamento": "Posicionamento Estratégico",
    "ee-s3-manual-marca": "Manual de Marca",
    "ee-s2-pesquisa-mercado": "Pesquisa de Mercado",
    "ee-s1-swot": "Análise SWOT",
    "ee-s1-arquitetura-presenca": "Arquitetura de Presença",
    "ee-s2-diagnostico-midia": "Diagnóstico de Mídia Paga",
    "ee-s2-diagnostico-organico-ig": "Diagnóstico de Orgânico (IG)",
    "ee-s2-diagnostico-criativos": "Diagnóstico de Criativos",
    "ee-s3-gmb-otimizacao": "Otimização Google Meu Negócio",
    "ee-s3-pdv-gmn": "Presença Local (GMN)",
    "ee-s3-ecom-marketplace": "Estratégia de Marketplaces",
    "ee-s1-auditoria-comunicacao": "Auditoria de Comunicação",
    "ee-s2-diagnostico-cro": "Diagnóstico de CRO",
    "ee-s3-ecom-cro": "CRO de E-commerce",
    "ee-s3-ecom-funil": "Funil de E-commerce",
    "ee-s4-diagnostico-comercial": "Diagnóstico Comercial",
    "ee-s4-cliente-oculto": "Cliente Oculto",
    "ee-s3-is-metricas-funil": "Métricas do Funil",
    "ee-s3-is-pipeline": "Pipeline Comercial",
    "ee-s3-landing-page": "Landing Page",
    "ee-s3-copy-anuncios": "Copy de Anúncios",
    "ee-s3-criativos-anuncios": "Criativos de Anúncios",
    "ee-s5-scripts-sdr": "Scripts do SDR IA",
    "ee-s5-sdr-ia-config": "Configuração do SDR IA",
    "ee-s3-pdv-experiencia": "Experiência no PDV",
    "ee-s3-crm-setup": "Setup de CRM",
    "ee-s3-ecom-crm-regua": "Réguas de CRM (E-commerce)",
    "ee-s3-ecom-recuperacao-carrinho": "Recuperação de Carrinho",
    "ee-s3-pdv-base-ativa": "Ativação da Base",
    "ee-s3-pdv-regua-whatsapp": "Régua de WhatsApp",
    "ee-s1-diagnostico-maturidade": "Diagnóstico de Maturidade",
    "ee-s3-forecast-midia": "Forecast de Mídia",
}

# Fallback embutido do delivery-map (mantém o renderer autocontido no kit do design-system,
# que não tem acesso ao delivery-map.json do plugin). Espelha plugins/.../delivery-map.json.
DELIVERY_MAP_FALLBACK = {
    "comum": {
        "semana_1": [
            "ee-s1-persona-icp", "ee-s1-auditoria-comunicacao", "ee-s1-swot",
            "ee-s2-pesquisa-mercado", "ee-s1-arquitetura-presenca",
        ],
        "semana_2": [
            "ee-s2-diagnostico-midia", "ee-s2-diagnostico-organico-ig",
            "ee-s2-diagnostico-criativos", "ee-s1-diagnostico-maturidade", "ee-s2-posicionamento",
        ],
        "semana_4": [
            "ee-s3-manual-marca", "ee-s3-landing-page", "ee-s3-copy-anuncios",
            "ee-s3-criativos-anuncios", "ee-s3-crm-setup", "ee-s5-scripts-sdr",
            "ee-s5-sdr-ia-config", "ee-s3-forecast-midia",
        ],
    },
    "semana_3": {
        "e-commerce": [
            "ee-s3-ecom-cro", "ee-s3-ecom-funil", "ee-s3-ecom-marketplace",
            "ee-s3-ecom-crm-regua", "ee-s3-ecom-recuperacao-carrinho",
        ],
        "inside-sales": [
            "ee-s2-diagnostico-cro", "ee-s4-cliente-oculto", "ee-s4-diagnostico-comercial",
            "ee-s3-is-metricas-funil", "ee-s3-is-pipeline",
        ],
        "pdv": [
            "ee-s3-pdv-base-ativa", "ee-s3-pdv-gmn", "ee-s3-pdv-experiencia",
            "ee-s3-pdv-regua-whatsapp",
        ],
    },
}


def load_delivery_map():
    """Lê delivery-map.json do plugin (../delivery-map.json) ou cai no fallback embutido."""
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.path.join(here, "..", "delivery-map.json"),
                 os.path.join(here, "delivery-map.json")):
        if os.path.isfile(cand):
            try:
                with open(cand, encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
    return DELIVERY_MAP_FALLBACK


def resolve_weeks(modelo, dm):
    """As 4 semanas da estruturação (mesma lógica model-aware do render_portal.sh)."""
    comum = dm.get("comum", {}) or {}
    semana3 = (dm.get("semana_3", {}) or {}).get(modelo, [])
    modelo_titulo = MODELO_LABEL.get(modelo, modelo or "seu modelo de venda")
    return [
        {"n": 1, "title": "Descoberta do Negócio e Pesquisa de Mercado",
         "skills": list(comum.get("semana_1", []))},
        {"n": 2, "title": "Diagnóstico Digital e Posicionamento Estratégico",
         "skills": list(comum.get("semana_2", []))},
        {"n": 3, "title": "Estrutura da Operação de Venda — " + modelo_titulo,
         "skills": list(semana3)},
        {"n": 4, "title": "Identidade de Comunicação e Plano de Mídia",
         "skills": list(comum.get("semana_4", []))},
    ]


def _initials(name):
    parts = [p for p in str(name or "").split() if p]
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


# ---------------------------------------------------------------------------
# Slide builders
# ---------------------------------------------------------------------------

def build_capa(ctx):
    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">🚀 Reunião de Kickoff</span>
        <h1 class="title-mega">{esc(ctx['name'])}</h1>
        <p class="subtitle-text" style="margin-top:24px; font-size:clamp(1.1rem,1.5vw,1.5rem);">
          O início do projeto · Estruturação Estratégica · {esc(ctx['modelo_label'])}
        </p>
      </div>
      <div class="slide__footer">
        <span>{esc(ctx['date'])}</span>
        <span>V4 Company · Estruturação Estratégica</span>
      </div>
      <div class="deco-square deco-s1"></div>
      <div class="deco-square deco-s2"></div>
    </section>
    """


_USER_ICON = ('<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
              '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>'
              '<circle cx="12" cy="7" r="4"></circle></svg>')


def build_investidor(ctx):
    inv = ctx["investidor"]
    nome = safe(inv.get("nome"), "")
    cargo = safe(inv.get("cargo"), "")
    foto = inv.get("foto_url")
    if foto:
        photo_html = f'<img class="invest-photo" src="{esc(foto)}" alt="{esc(nome or "Investidor V4")}" referrerpolicy="no-referrer">'
    else:
        inner = esc(_initials(nome)) if nome else _USER_ICON
        photo_html = f'<div class="invest-photo invest-photo--empty">{inner}</div>'
    nome_html = esc(nome) if nome else "Seu Investidor V4"
    cargo_html = esc(cargo) if cargo else "Investidor V4 · à frente do seu projeto"
    return f"""
    <section class="slide slide--white slide--investidor">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">🤝 Quem vai conduzir o projeto</span>
        <h2 class="title-section">Seu ponto focal na V4</h2>
        <p class="lead">A pessoa que vai liderar a estratégia e a execução do seu projeto, lado a lado com você.</p>
        <div class="invest-id">
          <div class="invest-id__name">{nome_html}</div>
          <div class="invest-id__role">{cargo_html}</div>
        </div>
      </div>
      {photo_html}
      <div class="slide__footer"><span>{esc(ctx['name'])}</span><span>V4 Company · Estruturação Estratégica</span></div>
    </section>
    """


def build_cliente(ctx):
    contato = ctx["contato"]
    nome = safe(contato.get("contact_name"), "")
    cargo = safe(contato.get("contact_role"), "")
    chip = ""
    if nome and nome != "—":
        cargo_txt = f" · {esc(cargo)}" if cargo and cargo != "—" else ""
        chip = f'<div class="contract-chip"><span>No contrato</span>{esc(nome)}{cargo_txt}</div>'
    return f"""
    <section class="slide slide--diag">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">👋 Quebra-gelo</span>
        <h2 class="title-section">Quem é você, além do contrato?</h2>
        <p class="lead">Antes de mergulhar no negócio, conte um pouco sobre você — é com você que vamos construir isso.</p>
        {chip}
        <div class="topic-grid" style="margin-top:2.4vh;">
          <div class="topic"><div class="topic__title">👋 Você</div><ul>
            <li>Seu nome e como gosta de ser chamado(a)</li>
            <li>Seu papel no dia a dia da empresa</li></ul></div>
          <div class="topic"><div class="topic__title">🛤️ Sua jornada</div><ul>
            <li>Há quanto tempo está nessa missão</li>
            <li>Como você chegou até aqui</li></ul></div>
          <div class="topic"><div class="topic__title">🔥 O que te move</div><ul>
            <li>O que te motiva no negócio</li>
            <li>O que você espera dessa parceria</li></ul></div>
        </div>
      </div>
      <div class="slide__footer"><span>{esc(ctx['name'])}</span><span>V4 Company · Estruturação Estratégica</span></div>
    </section>
    """


_AGENDA = [
    ("👥 Apresentações", "V4 + você, para nos conhecermos", "~5 min"),
    ("🏢 Sobre a sua empresa", "história, desafios, canais, produto e persona", "~10 min"),
    ("🔍 Benchmarking", "seus principais concorrentes vs. a sua empresa", "~8 min"),
    ("🗓️ Como funciona a entrega", "a estruturação, semana a semana", "~10 min"),
    ("🚀 Próximos passos", "o que vem agora e a próxima reunião", "~5 min"),
]


def build_sumario(ctx):
    items = []
    for i, (titulo, desc, tempo) in enumerate(_AGENDA, start=1):
        items.append(
            f'<div class="agenda__item"><span class="agenda__num">{i}</span>'
            f'<span class="agenda__label">{esc(titulo)}<span class="agenda__desc"> — {esc(desc)}</span></span>'
            f'<span class="agenda__time">{esc(tempo)}</span></div>')
    return f"""
    <section class="slide slide--white">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">📋 Sumário · 30–45 min</span>
        <h2 class="title-section">O que vamos ver hoje</h2>
        <div class="agenda">{''.join(items)}</div>
      </div>
      <div class="slide__footer"><span>{esc(ctx['name'])}</span><span>V4 Company · Estruturação Estratégica</span></div>
    </section>
    """


def _topic(title, items):
    lis = "".join(f"<li>{esc(t)}</li>" for t in items)
    return f'<div class="topic"><div class="topic__title">{esc(title)}</div><ul>{lis}</ul></div>'


def build_empresa(ctx):
    topics = [
        ("📖 História da empresa", ["Como e por que começou", "Marcos e viradas no caminho"]),
        ("🧗 Desafios enfrentados", ["O que já travou o crescimento", "O que vocês tentaram para resolver"]),
        ("📣 Canais & estratégias", ["O que já usaram (mídia, indicação, orgânico…)", "O que funcionou e o que não"]),
        ("📦 Produto / serviço", ["O carro-chefe", "Ticket médio e margem", "O que diferencia a oferta"]),
        ("🎯 Persona / cliente", ["Quem compra de vocês", "Principais dores", "Por que escolhem vocês"]),
    ]
    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">🏢 Sobre a sua empresa · apoio</span>
        <h2 class="title-section">Conte a história do negócio</h2>
        <p class="lead">Quanto mais a gente entende, mais afiada fica a estratégia. Use os tópicos abaixo como guia — fique à vontade para se aprofundar.</p>
        <div class="topic-grid">{''.join(_topic(t, its) for t, its in topics)}</div>
      </div>
      <div class="slide__footer"><span>{esc(ctx['name'])}</span><span>V4 Company · Estruturação Estratégica</span></div>
    </section>
    """


def build_benchmarking(ctx):
    dims = ["Quem é e como se posiciona", "Preço, oferta e condições",
            "Presença digital (site, redes, anúncios)", "O que ele faz melhor que vocês",
            "Onde vocês ganham dele"]
    cols = "".join(
        f'<div class="topic"><div class="topic__title">🥊 Concorrente {n}</div>'
        f'<ul>{"".join(f"<li>{esc(d)}</li>" for d in dims)}</ul></div>'
        for n in (1, 2))
    return f"""
    <section class="slide slide--white">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">🔍 Benchmarking · apoio</span>
        <h2 class="title-section">Seus 2 principais concorrentes</h2>
        <p class="lead">Para cada um, compare com a sua empresa: onde ele leva vantagem e — principalmente — onde vocês ganham.</p>
        <div class="bench">{cols}</div>
      </div>
      <div class="slide__footer"><span>{esc(ctx['name'])}</span><span>V4 Company · Estruturação Estratégica</span></div>
    </section>
    """


WEEK_EMOJI = {1: "🔍", 2: "📊", 3: "⚙️", 4: "🎨"}


def build_entrega_semanas(ctx):
    cards = []
    for w in ctx["weeks"]:
        labels = [SKILL_LABELS.get(s, s) for s in w["skills"]]
        lis = "".join(f'<li class="week__item">{esc(lbl)}</li>' for lbl in labels) or \
            '<li class="week__item" style="opacity:.6">A definir</li>'
        emoji = WEEK_EMOJI.get(w["n"], "📌")
        cards.append(
            f'<div class="week"><div class="week__n">{emoji} Semana {w["n"]}</div>'
            f'<div class="week__title">{esc(w["title"])}</div>'
            f'<ul class="week__list">{lis}</ul></div>')
    return f"""
    <section class="slide">
      {LOGO}
      <div class="slide__content">
        <span class="eyebrow">🗓️ Como funciona a entrega</span>
        <h2 class="title-section" style="margin-bottom:1vh;">Sua estruturação, semana a semana</h2>
        <p class="lead" style="margin-bottom:1vh;">Quatro semanas, da descoberta ao plano de mídia. Cada semana entrega peças que se encaixam na próxima.</p>
        <div class="weeks">{''.join(cards)}</div>
      </div>
      <div class="slide__footer"><span>{esc(ctx['name'])}</span><span>V4 Company · Estruturação Estratégica</span></div>
    </section>
    """


def build_proximos_passos(ctx):
    steps = [
        "🔎 Começamos a Semana 1 — descoberta do negócio e pesquisa de mercado",
        "🔑 Você nos envia os acessos e materiais que vamos combinar",
        "📈 Devolvemos os primeiros diagnósticos e seguimos semana a semana",
    ]
    steps_html = "".join(
        f'<div class="step-line"><span class="chk">✓</span><span class="step-line__text">{esc(s)}</span></div>'
        for s in steps)
    return f"""
    <section class="slide slide--white">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">🚀 Próximos passos</span>
        <h2 class="title-section">O que acontece a partir de agora</h2>
        <div class="steps">{steps_html}</div>
        <div class="cta-box">
          <div class="cta-box__icon">📅</div>
          <div>
            <div class="cta-box__title">Vamos marcar a próxima reunião?</div>
            <div class="cta-box__sub">Alinhar agora o dia e o horário do nosso próximo encontro.</div>
          </div>
        </div>
      </div>
      <div class="slide__footer"><span>{esc(ctx['name'])}</span><span>V4 Company · Estruturação Estratégica</span></div>
    </section>
    """


def compose_slides(ctx):
    return "\n".join([
        build_capa(ctx),
        build_investidor(ctx),
        build_cliente(ctx),
        build_sumario(ctx),
        build_empresa(ctx),
        build_benchmarking(ctx),
        build_entrega_semanas(ctx),
        build_proximos_passos(ctx),
    ])


# ---------------------------------------------------------------------------
# Shell HTML (paleta V4 — vermelho + IBM Plex Sans). Marcadores via str.replace.
# ---------------------------------------------------------------------------

SHELL_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body {
    height: 100%; width: 100%; overflow: hidden;
    background: #0a0a0a; color: #fff;
    font-family: 'IBM Plex Sans', -apple-system, sans-serif;
  }
  .presentation { position: fixed; inset: 0; overflow: hidden; }
  .slides-track { display: flex; height: 100vh; width: 100vw;
    transition: transform 0.5s cubic-bezier(0.7, 0, 0.3, 1); }
  .slide {
    flex: 0 0 100vw; height: 100vh; position: relative;
    overflow-y: auto; overflow-x: hidden; padding: 5vh 6vw 9vh;
    display: flex; flex-direction: column;
    background: radial-gradient(ellipse at center, #ff3a1f 0%, #d61a0e 55%, #8a0d05 100%);
  }
  .slide--alt { background: linear-gradient(135deg, #ff5a2c 0%, #e6230e 60%, #8a0d05 100%); }
  .slide--diag { background: radial-gradient(circle at 30% 50%, #ff6a3c 0%, #d61a0e 50%, #5a0802 100%); }
  .slide--soft { background: linear-gradient(180deg, #b81409 0%, #f04823 100%); }
  .slide--white { background: #ffffff; }

  .slide__header { display: flex; align-items: center; gap: 16px; margin-bottom: 2.5vh; }
  .logo-v4 {
    display: inline-flex; width: 60px; height: 60px;
    background: #fff url("__LOGO_URI__") center/74% no-repeat;
    border-radius: 14px; box-shadow: 0 6px 22px rgba(0,0,0,0.18);
  }

  h1.title-mega {
    font-weight: 700; font-size: clamp(3.2rem, 7.5vw, 7rem);
    line-height: 0.95; letter-spacing: -0.03em;
    background: linear-gradient(180deg, #fff 0%, #fff 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
  }
  h2.title-section {
    font-weight: 700; font-size: clamp(2.2rem, 4.5vw, 4rem);
    line-height: 1.05; letter-spacing: -0.02em; color: #fff; margin-bottom: 2vh;
  }
  .eyebrow {
    display: inline-block; font-weight: 700; font-size: clamp(0.8rem, 0.95vw, 1rem);
    letter-spacing: 0.08em; text-transform: uppercase; color: #fff;
    padding: 8px 18px; border-radius: 100px;
    background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(8px); margin-bottom: 1.8vh; align-self: flex-start;
  }
  .subtitle-text {
    font-weight: 500; font-size: clamp(1rem, 1.3vw, 1.35rem); line-height: 1.5;
    color: rgba(255,255,255,0.92); max-width: 940px;
  }
  .lead {
    font-weight: 500; font-size: clamp(1rem, 1.3vw, 1.3rem); line-height: 1.5;
    color: rgba(255,255,255,0.9); max-width: 920px; margin-top: 1.4vh;
  }

  /* Investidor — foto preenchendo a metade direita da tela */
  .slide--investidor .slide__content { max-width: 52%; padding-right: 2vw; }
  .invest-id { margin-top: 3vh; }
  .invest-id__name { font-weight: 700; font-size: clamp(1.9rem, 3.1vw, 3rem); line-height: 1.04;
    letter-spacing: -0.02em; color: #2A0703; }
  .invest-id__role { font-weight: 600; font-size: clamp(1rem, 1.4vw, 1.4rem);
    color: #8a5a4f; margin-top: 10px; }
  .invest-photo { position: absolute; top: 0; right: 0; bottom: 0; width: 46%; height: 100%;
    object-fit: cover; object-position: center; }
  .invest-photo--empty { display: flex; align-items: center; justify-content: center;
    background: #f6f1ef; color: #C21A0A; font-weight: 800; font-size: clamp(4rem, 9vw, 8rem); }

  /* Chip "no contrato" */
  .contract-chip {
    align-self: flex-start; display: inline-flex; align-items: center; gap: 10px;
    margin-top: 1.8vh; padding: 10px 18px; border-radius: 100px;
    background: #fff; border: 1px solid rgba(0,0,0,0.06); box-shadow: 0 6px 18px rgba(0,0,0,0.14);
    font-weight: 700; font-size: clamp(0.92rem, 1.1vw, 1.1rem); color: #2A0703;
  }
  .contract-chip span { font-size: 0.66rem; letter-spacing: 0.1em; text-transform: uppercase;
    font-weight: 800; color: #C21A0A; }

  /* Agenda */
  .agenda { display: flex; flex-direction: column; gap: 10px; margin-top: 3vh; max-width: 940px; }
  .agenda__item { display: flex; align-items: center; gap: 18px;
    background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.16);
    border-radius: 14px; padding: 14px 20px; }
  .agenda__num { flex: none; width: 34px; height: 34px; border-radius: 50%; background: #fff;
    color: #C21A0A; font-weight: 800; display: inline-flex; align-items: center;
    justify-content: center; font-size: 0.95rem; }
  .agenda__label { font-weight: 700; font-size: clamp(1rem, 1.3vw, 1.25rem); color: #fff; }
  .agenda__desc { font-weight: 500; color: rgba(255,255,255,0.72); }
  .agenda__time { margin-left: auto; flex: none; font-size: 0.78rem; font-weight: 700;
    letter-spacing: 0.06em; text-transform: uppercase; color: rgba(255,255,255,0.65); }

  /* Tópicos de apoio (prompts) */
  .topic-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 16px; margin-top: 3vh; }
  .topic { background: #fff; border: 1px solid rgba(0,0,0,0.06);
    border-radius: 16px; padding: 20px 22px; box-shadow: 0 10px 28px rgba(0,0,0,0.16); }
  .topic__title { font-weight: 700; font-size: clamp(1.05rem, 1.4vw, 1.3rem); color: #2A0703;
    margin-bottom: 10px; }
  .topic ul { list-style: none; display: flex; flex-direction: column; gap: 7px; }
  .topic li { position: relative; padding-left: 18px; font-size: clamp(0.9rem, 1.05vw, 1.05rem);
    line-height: 1.4; color: #5a4742; }
  .topic li::before { content: "›"; position: absolute; left: 0; color: #FB2E0A; font-weight: 800; }

  /* Benchmarking */
  .bench { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 3vh; }

  /* Semanas de entrega */
  .weeks { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-top: 2.4vh;
    flex: 1; min-height: 0; }
  .week { background: #fff; border: 1px solid rgba(0,0,0,0.06);
    border-radius: 16px; padding: 18px 16px; display: flex; flex-direction: column; min-height: 0;
    box-shadow: 0 10px 28px rgba(0,0,0,0.16); }
  .week__n { font-weight: 800; font-size: 0.74rem; letter-spacing: 0.1em; text-transform: uppercase;
    color: #C21A0A; }
  .week__title { font-weight: 700; font-size: clamp(0.95rem, 1.05vw, 1.12rem); line-height: 1.22;
    color: #2A0703; margin: 6px 0 12px; }
  .week__list { list-style: none; display: flex; flex-direction: column; gap: 7px;
    overflow-y: auto; }
  .week__item { position: relative; padding-left: 16px; font-size: clamp(0.78rem, 0.9vw, 0.92rem);
    line-height: 1.3; color: #5a4742; }
  .week__item::before { content: ""; position: absolute; left: 0; top: 0.52em; width: 6px;
    height: 6px; border-radius: 50%; background: #FB2E0A; }

  /* Próximos passos */
  .steps { display: flex; flex-direction: column; gap: 12px; margin-top: 3vh; max-width: 820px; }
  .step-line { display: flex; gap: 16px; align-items: center;
    background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.18);
    border-radius: 14px; padding: 16px 20px; }
  .step-line .chk { flex: none; width: 30px; height: 30px; border-radius: 9px; background: #fff;
    color: #C21A0A; font-weight: 800; display: inline-flex; align-items: center;
    justify-content: center; }
  .step-line__text { font-weight: 600; font-size: clamp(1rem, 1.25vw, 1.2rem); color: #fff;
    line-height: 1.4; }
  .cta-box { align-self: flex-start; margin-top: 3.5vh; background: #fff; border-radius: 18px;
    padding: 24px 30px; display: flex; align-items: center; gap: 22px; flex-wrap: wrap;
    box-shadow: 0 14px 40px rgba(0,0,0,0.25); }
  .cta-box__icon { font-size: 2.4rem; line-height: 1; }
  .cta-box__title { font-weight: 800; font-size: clamp(1.3rem, 2vw, 1.9rem); color: #2A0703;
    letter-spacing: -0.01em; }
  .cta-box__sub { color: #6b4a42; font-size: clamp(0.92rem, 1.1vw, 1.05rem); margin-top: 4px; }

  /* ===== Slides de fundo branco (contraste — vermelho/escuro sobre branco) ===== */
  .slide--white .logo-v4 { border: 1px solid rgba(0,0,0,0.08); }
  .slide--white h2.title-section { color: #FB2E0A; }
  .slide--white .eyebrow { color: #C21A0A; background: rgba(251,46,10,0.08);
    border-color: rgba(251,46,10,0.2); backdrop-filter: none; }
  .slide--white .lead, .slide--white .subtitle-text { color: #5a4742; }
  .slide--white .slide__footer { color: rgba(0,0,0,0.4); }
  .slide--white .agenda__item { background: #f6f1ef; border-color: rgba(0,0,0,0.06); }
  .slide--white .agenda__num { background: #FB2E0A; color: #fff; }
  .slide--white .agenda__label { color: #2A0703; }
  .slide--white .agenda__desc { color: #8a5a4f; }
  .slide--white .agenda__time { color: #C21A0A; }
  .slide--white .topic { background: #f6f1ef; border-color: rgba(0,0,0,0.06); box-shadow: none; }
  .slide--white .topic__title { color: #2A0703; }
  .slide--white .topic li { color: #5a4742; }
  .slide--white .topic li::before { color: #FB2E0A; }
  .slide--white .step-line { background: #f6f1ef; border-color: rgba(0,0,0,0.06); }
  .slide--white .step-line .chk { background: #FB2E0A; color: #fff; }
  .slide--white .step-line__text { color: #2A0703; }
  .slide--white .cta-box { background: #FB2E0A; box-shadow: 0 14px 40px rgba(251,46,10,0.3); }
  .slide--white .cta-box__title { color: #fff; }
  .slide--white .cta-box__sub { color: rgba(255,255,255,0.9); }

  .slide__content { flex: 1; display: flex; flex-direction: column; min-height: 0; }
  .slide__footer {
    margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end;
    font-size: 0.78rem; color: rgba(255,255,255,0.5); font-weight: 500; padding-top: 1.5vh;
  }

  .controls {
    position: fixed; bottom: 0; left: 0; right: 0; display: flex; align-items: center; gap: 18px;
    padding: 14px 24px; background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.55) 60%); z-index: 10;
  }
  .control-btn {
    width: 38px; height: 38px; border-radius: 50%;
    background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.18);
    backdrop-filter: blur(8px); color: #fff; font-size: 1.1rem;
    display: inline-flex; align-items: center; justify-content: center;
    cursor: pointer; user-select: none; transition: background .2s;
  }
  .control-btn:hover { background: rgba(255,255,255,0.18); }
  .control-btn:disabled { opacity: 0.3; cursor: not-allowed; }
  .progress-bar { flex: 1; height: 4px; border-radius: 4px; background: rgba(255,255,255,0.16); overflow: hidden; }
  .progress-bar__fill {
    height: 100%; background: linear-gradient(90deg, #fff 0%, #fff 100%);
    transition: width 0.4s cubic-bezier(0.7, 0, 0.3, 1); border-radius: 4px;
  }
  .counter { font-weight: 600; font-size: 0.9rem; color: rgba(255,255,255,0.85); letter-spacing: 0.04em; min-width: 60px; text-align: center; }

  .deco-square {
    position: absolute; border-radius: 18px;
    background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
    border: 1px solid rgba(255,255,255,0.05); pointer-events: none;
  }
  .deco-s1 { width: 300px; height: 300px; top: -80px; right: -80px; transform: rotate(15deg); }
  .deco-s2 { width: 200px; height: 200px; bottom: -60px; left: 6%; transform: rotate(-12deg); opacity: 0.5; }

  .hint {
    position: fixed; top: 14px; right: 18px; font-size: 0.75rem;
    color: rgba(255,255,255,0.5); font-weight: 500; pointer-events: none; z-index: 5;
  }
  @media (max-width: 900px) {
    .bench { grid-template-columns: 1fr; }
    .weeks { grid-template-columns: 1fr 1fr; }
    .slide--investidor .slide__content { max-width: 100%; padding-right: 0; }
    .invest-photo { position: relative; width: 100%; height: 34vh; margin-top: 3vh; border-radius: 18px; }
  }
  @media (max-width: 640px) {
    .agenda__desc { display: none; }
  }
</style>
</head>
<body>

<div class="hint">← → setas para navegar · F para tela cheia</div>

<div class="presentation">
  <div class="slides-track" id="track">
__SLIDES__
  </div>

  <div class="controls">
    <button class="control-btn" id="prev" aria-label="Anterior">‹</button>
    <div class="progress-bar"><div class="progress-bar__fill" id="progress"></div></div>
    <span class="counter" id="counter">1 / __TOTAL__</span>
    <button class="control-btn" id="next" aria-label="Próximo">›</button>
    <button class="control-btn" id="fullscreen" aria-label="Tela cheia">⛶</button>
  </div>
</div>

<script>
  (function() {
    const track = document.getElementById('track');
    const slides = track.querySelectorAll('.slide');
    const total = slides.length;
    const counter = document.getElementById('counter');
    const progress = document.getElementById('progress');
    const prevBtn = document.getElementById('prev');
    const nextBtn = document.getElementById('next');
    const fsBtn = document.getElementById('fullscreen');
    let current = 0;

    function render() {
      track.style.transform = `translateX(-${current * 100}vw)`;
      counter.textContent = `${current + 1} / ${total}`;
      progress.style.width = `${((current + 1) / total) * 100}%`;
      prevBtn.disabled = current === 0;
      nextBtn.disabled = current === total - 1;
    }
    function next() { if (current < total - 1) { current++; render(); } }
    function prev() { if (current > 0) { current--; render(); } }
    function goto(i) { current = Math.max(0, Math.min(total - 1, i)); render(); }

    prevBtn.addEventListener('click', prev);
    nextBtn.addEventListener('click', next);
    fsBtn.addEventListener('click', () => {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
      else document.exitFullscreen();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); next(); }
      else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); prev(); }
      else if (e.key === 'Home') { e.preventDefault(); goto(0); }
      else if (e.key === 'End') { e.preventDefault(); goto(total - 1); }
      else if (e.key === 'f' || e.key === 'F') { fsBtn.click(); }
    });
    let touchStartX = 0;
    document.addEventListener('touchstart', (e) => { touchStartX = e.changedTouches[0].screenX; }, {passive: true});
    document.addEventListener('touchend', (e) => {
      const dx = e.changedTouches[0].screenX - touchStartX;
      if (Math.abs(dx) > 60) (dx < 0 ? next : prev)();
    }, {passive: true});

    render();
  })();
</script>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _logo_data_uri():
    asset = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "v4-favicon.jpg")
    if not os.path.isfile(asset):
        return ""
    try:
        with open(asset, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        return f"data:image/jpeg;base64,{b64}"
    except IOError:
        return ""


def render(client_dir):
    client = load_client(client_dir)
    meta = client.get("meta", {}) or {}
    briefing = client.get("briefing", {}) or {}
    name = meta.get("name", "Cliente")
    modelo = meta.get("modelo_venda", "")
    now = datetime.now()
    dm = load_delivery_map()
    ctx = {
        "name": name,
        "modelo_label": MODELO_LABEL.get(modelo, modelo or "—"),
        "date": f"{MESES_PT[now.month]} · {now.year}",
        "investidor": meta.get("investidor", {}) or {},
        "contato": (briefing.get("identification", {}) or {}),
        "weeks": resolve_weeks(modelo, dm),
    }

    slides_html = compose_slides(ctx)
    total = slides_html.count('<section class="slide')
    title = f"{name} · Reunião de Kickoff"

    html_out = (SHELL_HTML
                .replace("__TITLE__", esc(title))
                .replace("__LOGO_URI__", _logo_data_uri())
                .replace("__SLIDES__", slides_html)
                .replace("__TOTAL__", str(total)))

    out_path = os.path.join(client_dir, "kickoff.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    return out_path


def main():
    if len(sys.argv) < 2:
        print("Uso: render_kickoff.py <path_cliente>", file=sys.stderr)
        sys.exit(2)
    client_dir = sys.argv[1].rstrip("/")
    if not os.path.isdir(client_dir):
        print(f"Diretório não encontrado: {client_dir}", file=sys.stderr)
        sys.exit(2)
    out = render(client_dir)
    print(f"Apresentação de kickoff gerada: {out}")


if __name__ == "__main__":
    main()
