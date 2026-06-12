#!/usr/bin/env python3
"""render_apresentacao_entrega.py — Apresentação da Entrega (narrativa educativa).

Diferente de render_apresentacao.py (readout de diagnóstico, slide por skill), esta é a
apresentação CLIENTE-FACING: educativa, cirúrgica e organizada pela jornada de execução
de marketing — Atrair → Converter → Reter.

Filosofia (decisões travadas com o operador):
  - Roteiro pela jornada de execução (Atrair / Converter / Reter).
  - Slide cirúrgico: 1 ideia = statement de impacto + 1 dado + ponte "→ Na execução".
  - Conteúdo determinístico: a moldura educativa (por quê / como usar) é templatizada por
    estudo; o dado e o statement vêm do envelope comum dos outputs (summary_headline,
    summary_highlights, summary_key_findings).
  - Model-aware e progressivo: só renderiza estudos cujo output existe; uma fase só ganha
    divisória se houver ao menos um estudo dela.

Uso: render_apresentacao_entrega.py <path_cliente>
Gera: <client_dir>/apresentacao-entrega.html
"""

import sys
import os
import base64
from datetime import datetime

# Reaproveita helpers do renderizador irmão (mesmo diretório; guard __main__ evita rodar o main dele).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_apresentacao import esc, safe, truncate, load_client, load_outputs  # noqa: E402

# Logo é inserido via CSS (background do .logo-v4), data-URI único — autocontido.
LOGO = '<div class="slide__header"><span class="logo-v4" aria-label="V4"></span></div>'

_DOC_ICON = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>'
             '<polyline points="14 2 14 8 20 8"></polyline></svg>')


def slide_header(entrega=None, count_label=""):
    """Header do slide com logo + (opcional) tag 'Entrega · Nome' e contador 'i/n'."""
    if not entrega:
        return LOGO
    cnt = f'<span class="entrega-count">{esc(count_label)}</span>' if count_label else ""
    return ('<div class="slide__header"><span class="logo-v4" aria-label="V4"></span>'
            f'<span class="entrega-tag">{_DOC_ICON}Entrega · <b>{esc(entrega)}</b>{cnt}</span></div>')

MODELO_LABEL = {
    "e-commerce": "E-commerce",
    "inside-sales": "Inside Sales",
    "pdv": "PDV / Loja Física",
}

MESES_PT = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

TONE_COLORS = {"red": "#ff8c8c", "yellow": "#ffe18c", "green": "#80ff9f", "blue": "#80c8ff"}
CATEGORY_TONE = {"ameaca": "red", "vantagem": "green", "acao": "yellow", "posicao": "blue"}


def tone_color(t):
    return TONE_COLORS.get((t or "").lower(), "#fff")


# ---------------------------------------------------------------------------
# Fases da jornada de execução
# ---------------------------------------------------------------------------

PHASES = {
    "atrair": {
        "num": "01",
        "label": "Atrair",
        "titulo": "Atrair as pessoas certas",
        "sub": "Trazer quem tem o perfil — e parar de gastar verba com quem nunca vai comprar.",
    },
    "converter": {
        "num": "02",
        "label": "Converter",
        "titulo": "Converter atenção em cliente",
        "sub": "Transformar o interesse em venda, fechando os vazamentos no caminho.",
    },
    "reter": {
        "num": "03",
        "label": "Reter",
        "titulo": "Reter e fazer crescer",
        "sub": "Fazer o cliente voltar, indicar e valer mais ao longo do tempo.",
    },
}
PHASE_ORDER = ["atrair", "converter", "reter"]

# Nome amigável do ENTREGÁVEL por skill (exibido na tag "Entrega · ..." de cada slide).
ENTREGA_NAMES = {
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

# Essência (2-4 palavras, para o contraste "de → para") e pergunta de negócio por entrega.
ENTREGA_DETAIL = {
    "ee-s1-persona-icp": {"essencia": "quem atrair", "pergunta": "Para quem, exatamente, vamos vender?"},
    "ee-s2-posicionamento": {"essencia": "como ser percebido", "pergunta": "Que lugar queremos ocupar na cabeça do cliente?"},
    "ee-s3-manual-marca": {"essencia": "como falar", "pergunta": "Como a marca soa e se mostra — sempre igual?"},
    "ee-s2-pesquisa-mercado": {"essencia": "onde está o espaço", "pergunta": "Onde há espaço de mercado que ninguém ocupa?"},
    "ee-s1-swot": {"essencia": "onde temos vantagem", "pergunta": "Onde temos vantagem real para atacar?"},
    "ee-s1-arquitetura-presenca": {"essencia": "as portas de entrada", "pergunta": "Por onde o cliente realmente chega até nós?"},
    "ee-s2-diagnostico-midia": {"essencia": "pra onde vai a verba", "pergunta": "Cada real de mídia está trazendo retorno?"},
    "ee-s2-diagnostico-organico-ig": {"essencia": "atrair com conteúdo", "pergunta": "O conteúdo orgânico atrai a gente certa?"},
    "ee-s2-diagnostico-criativos": {"essencia": "o que para o scroll", "pergunta": "Nossos criativos ganham a atenção?"},
    "ee-s3-gmb-otimizacao": {"essencia": "ser achado localmente", "pergunta": "Quem busca perto encontra e escolhe a gente?"},
    "ee-s3-pdv-gmn": {"essencia": "ser achado localmente", "pergunta": "Quem busca perto encontra e escolhe a gente?"},
    "ee-s3-ecom-marketplace": {"essencia": "onde vender além do site", "pergunta": "Quais marketplaces valem a margem?"},
    "ee-s1-auditoria-comunicacao": {"essencia": "os vazamentos", "pergunta": "Onde o cliente desiste no caminho?"},
    "ee-s2-diagnostico-cro": {"essencia": "a página converte?", "pergunta": "A página transforma visita em ação?"},
    "ee-s3-ecom-cro": {"essencia": "PDP e checkout", "pergunta": "Onde a venda online se perde?"},
    "ee-s3-ecom-funil": {"essencia": "onde o funil vaza", "pergunta": "Onde perdemos receita do clique ao pago?"},
    "ee-s4-diagnostico-comercial": {"essencia": "onde perdemos a venda", "pergunta": "Onde o lead some no funil comercial?"},
    "ee-s4-cliente-oculto": {"essencia": "como atendemos", "pergunta": "Como é o nosso atendimento, de verdade?"},
    "ee-s3-is-metricas-funil": {"essencia": "o que é lead bom", "pergunta": "O que conta como lead qualificado?"},
    "ee-s3-is-pipeline": {"essencia": "o caminho até fechar", "pergunta": "Como o lead avança até virar venda?"},
    "ee-s3-landing-page": {"essencia": "a página que converte", "pergunta": "Para onde mandamos o tráfego?"},
    "ee-s3-copy-anuncios": {"essencia": "as palavras que vendem", "pergunta": "O que dizer para gerar o clique?"},
    "ee-s3-criativos-anuncios": {"essencia": "o que mostrar", "pergunta": "O que para o scroll e gera desejo?"},
    "ee-s5-scripts-sdr": {"essencia": "resposta na hora", "pergunta": "Como respondemos o lead no momento certo?"},
    "ee-s5-sdr-ia-config": {"essencia": "atendimento 24/7", "pergunta": "Quem atende sempre, sem perder follow-up?"},
    "ee-s3-pdv-experiencia": {"essencia": "a experiência na loja", "pergunta": "O que o cliente sente no ponto de venda?"},
    "ee-s3-crm-setup": {"essencia": "não perder lead", "pergunta": "Como garantir que nenhum lead some?"},
    "ee-s3-ecom-crm-regua": {"essencia": "fazer voltar", "pergunta": "Como trazer o cliente de volta a comprar?"},
    "ee-s3-ecom-recuperacao-carrinho": {"essencia": "recuperar carrinho", "pergunta": "Como recuperar quem quase comprou?"},
    "ee-s3-pdv-base-ativa": {"essencia": "a mina na base", "pergunta": "Como vender mais para quem já é cliente?"},
    "ee-s3-pdv-regua-whatsapp": {"essencia": "trazer de volta à loja", "pergunta": "Como reativar e reduzir o no-show?"},
    "ee-s3-forecast-midia": {"essencia": "o plano de mídia", "pergunta": "Quanto investir e o que esperar nos próximos 6 meses?"},
}


# ---------------------------------------------------------------------------
# Registro de estudos — moldura educativa templatizada (por quê / como usar).
# Cobre as skills comuns + as semanas 3 dos 3 modelos. Só renderiza o que tem output.
# Ordem da lista = ordem dos slides dentro de cada fase.
# Cada entrada vira UM slide de conteúdo no template de 2 zonas (build_content).
# ---------------------------------------------------------------------------

STUDY_REGISTRY = [
    # ---------------- ATRAIR ----------------
    {"skill": "ee-s1-persona-icp", "phase": "atrair", "title": "Para quem vamos falar",
     "por_que": "Antes de investir um real, definimos exatamente quem traz resultado — e quem só consome verba.",
     "execucao": "Vira a segmentação da mídia e o ângulo de toda copy. Nada de público amplo no escuro."},
    {"skill": "ee-s2-posicionamento", "phase": "atrair", "title": "Como vamos ser percebidos",
     "por_que": "Sem um território claro, todo anúncio acaba competindo por preço. Aqui cravamos o ângulo único.",
     "execucao": "É o fio condutor de cada campanha, criativo e página — todos contam a mesma história."},
    {"skill": "ee-s3-manual-marca", "phase": "atrair", "title": "Como vamos falar",
     "por_que": "Uma voz consistente faz o cliente reconhecer a marca em qualquer ponto de contato.",
     "execucao": "Guia copy, criativos e o SDR IA — a marca soa igual em todo lugar."},
    {"skill": "ee-s2-pesquisa-mercado", "phase": "atrair", "title": "Onde está o espaço",
     "por_que": "Medimos o tamanho do mercado e a concorrência para achar o espaço que ninguém ocupa.",
     "execucao": "Define os territórios de mensagem e as primeiras campanhas de teste."},
    {"skill": "ee-s1-swot", "phase": "atrair", "title": "Nosso terreno de jogo",
     "por_que": "Cruzamos forças e fraquezas para atacar onde temos vantagem real, não onde dói.",
     "execucao": "As forças viram argumento de venda; as fraquezas viram backlog de correção."},
    {"skill": "ee-s1-arquitetura-presenca", "phase": "atrair", "title": "As portas de entrada",
     "por_que": "Mapeamos por onde o cliente realmente chega — pra não investir em canal que não converte.",
     "execucao": "Concentra esforço e verba nos canais de entrada que de fato trazem gente certa."},
    {"skill": "ee-s2-diagnostico-midia", "phase": "atrair", "title": "Pra onde a verba vai hoje",
     "por_que": "Olhamos o que a mídia entrega hoje para saber onde realocar cada real com mais retorno.",
     "execucao": "Vira o plano de realocação de budget e a base do forecast de mídia."},
    {"skill": "ee-s2-diagnostico-organico-ig", "phase": "atrair", "title": "Atrair com conteúdo",
     "por_que": "O orgânico atrai sem pagar por clique — se o conteúdo certo estiver no ar.",
     "execucao": "Define a linha editorial e os formatos que puxam audiência qualificada."},
    {"skill": "ee-s2-diagnostico-criativos", "phase": "atrair", "title": "O que para o scroll",
     "por_que": "O criativo decide a atenção nos 3 primeiros segundos — ou o anúncio morre ali.",
     "execucao": "Vira o briefing de produção dos próximos criativos de melhor performance."},
    {"skill": "ee-s3-gmb-otimizacao", "phase": "atrair", "title": "Ser achado localmente",
     "por_que": "Quem busca perto quer resolver agora — o perfil local precisa converter essa intenção.",
     "execucao": "Otimização de perfil, posts e avaliações pra capturar a busca local."},
    {"skill": "ee-s3-pdv-gmn", "phase": "atrair", "title": "Ser achado localmente",
     "por_que": "Quem busca perto quer resolver agora — o perfil local precisa converter essa intenção.",
     "execucao": "Plano de perfil, fotos, avaliações e tracking de ligações e rotas."},
    {"skill": "ee-s3-ecom-marketplace", "phase": "atrair", "title": "Onde vender além do site",
     "por_que": "Marketplaces trazem demanda pronta — mas comem margem. Decidimos onde realmente vale.",
     "execucao": "Define o mix de canais e a alocação por margem líquida."},

    # ---------------- CONVERTER ----------------
    {"skill": "ee-s1-auditoria-comunicacao", "phase": "converter", "title": "Os vazamentos no caminho",
     "por_que": "Mapeamos cada ponto de contato pra achar exatamente onde o cliente desiste.",
     "execucao": "Cada gap vira um quick-win de correção priorizado por impacto."},
    {"skill": "ee-s2-diagnostico-cro", "phase": "converter", "title": "A página converte?",
     "por_que": "Tráfego sem conversão é dinheiro no ralo — auditamos a jornada da página a fundo.",
     "execucao": "Vira hipóteses de teste A/B priorizadas e um wireframe de melhorias."},
    {"skill": "ee-s3-ecom-cro", "phase": "converter", "title": "PDP, carrinho e checkout",
     "por_que": "É na página de produto e no checkout que a venda online se ganha ou se perde.",
     "execucao": "Hipóteses A/B priorizadas por ICE, prontas pra rodar."},
    {"skill": "ee-s3-ecom-funil", "phase": "converter", "title": "Onde o funil vaza",
     "por_que": "Mapeamos do clique ao pago pra cravar o gargalo que mais custa receita.",
     "execucao": "Foca a otimização no gargalo de maior receita recuperável."},
    {"skill": "ee-s4-diagnostico-comercial", "phase": "converter", "title": "Onde perdemos no comercial",
     "por_que": "O lead chega — a pergunta é onde ele some dentro do funil de vendas.",
     "execucao": "Define critério de qualificação e SLA por etapa do pipeline."},
    {"skill": "ee-s4-cliente-oculto", "phase": "converter", "title": "Como atendemos de verdade",
     "por_que": "Simulamos um cliente real pra sentir o atendimento na pele, sem maquiagem.",
     "execucao": "As falhas viram script e régua de resposta do time / SDR."},
    {"skill": "ee-s3-is-metricas-funil", "phase": "converter", "title": "O que conta como lead bom",
     "por_que": "Sem definição de funil, cada um mede uma coisa. Padronizamos o que é Lead, MQL, SQL.",
     "execucao": "Vira scoring por estrela e SLA — base do CRM e do SDR IA."},
    {"skill": "ee-s3-is-pipeline", "phase": "converter", "title": "O caminho até o fechamento",
     "por_que": "Um pipeline claro evita lead esquecido e proposta sem follow-up.",
     "execucao": "Vira as etapas, réguas e o script consultivo do time comercial."},
    {"skill": "ee-s3-landing-page", "phase": "converter", "title": "A página que converte",
     "por_que": "A landing page é onde a promessa do anúncio precisa virar ação.",
     "execucao": "Página no ar, copy seção por seção, pronta pra receber as campanhas."},
    {"skill": "ee-s3-copy-anuncios", "phase": "converter", "title": "As palavras que convertem",
     "por_que": "A copy certa transforma atenção em clique e clique em lead qualificado.",
     "execucao": "Banco de 30+ variações por funil e plataforma, pronto pra subir."},
    {"skill": "ee-s3-criativos-anuncios", "phase": "converter", "title": "Os criativos que vendem",
     "por_que": "Sem criativo forte, a melhor copy não chega a ser lida.",
     "execucao": "Pack de variações com hooks distintos, pronto pra produção."},
    {"skill": "ee-s5-scripts-sdr", "phase": "converter", "title": "Resposta na hora certa",
     "por_que": "Lead quente esfria em minutos — a resposta precisa ser imediata e qualificada.",
     "execucao": "Scripts de boas-vindas, qualificação e follow-up do SDR IA."},
    {"skill": "ee-s5-sdr-ia-config", "phase": "converter", "title": "O vendedor que nunca dorme",
     "por_que": "Um SDR IA responde em segundos, 24/7, e nunca esquece um follow-up.",
     "execucao": "Agente no ar no Patagon, integrado ao CRM e alertando o vendedor."},
    {"skill": "ee-s3-pdv-experiencia", "phase": "converter", "title": "A experiência na loja",
     "por_que": "No PDV a experiência é o anúncio — avaliamos o que o cliente realmente sente.",
     "execucao": "Gaps viram plano de melhoria de atendimento e ambiente."},

    # ---------------- RETER ----------------
    {"skill": "ee-s3-crm-setup", "phase": "reter", "title": "Não perder mais nenhum lead",
     "por_que": "Sem follow-up estruturado, a maioria dos leads simplesmente some sem dar sinal.",
     "execucao": "CRM com réguas de boas-vindas, nutrição e reativação rodando."},
    {"skill": "ee-s3-ecom-crm-regua", "phase": "reter", "title": "Fazer o cliente voltar",
     "por_que": "Custa muito menos vender de novo pra quem já comprou do que conquistar um novo.",
     "execucao": "Réguas de pós-compra, recompra e reativação segmentadas por RFM."},
    {"skill": "ee-s3-ecom-recuperacao-carrinho", "phase": "reter", "title": "Recuperar quem quase comprou",
     "por_que": "Carrinho abandonado é venda a um passo de distância — não pode ser ignorada.",
     "execucao": "Fluxo multi-canal de recuperação por objeção, no ar (T+1h/24h/72h)."},
    {"skill": "ee-s3-pdv-base-ativa", "phase": "reter", "title": "A mina de ouro na base",
     "por_que": "A base ativa já confia em você — é a venda mais barata e rápida que existe.",
     "execucao": "Curva de recompra vira campanhas de reativação segmentadas."},
    {"skill": "ee-s3-pdv-regua-whatsapp", "phase": "reter", "title": "Trazer de volta à loja",
     "por_que": "Uma régua no WhatsApp reduz no-show e reativa quem sumiu.",
     "execucao": "Réguas pré/durante/pós-visita e reativação no ar."},
    {"skill": "ee-s3-forecast-midia", "phase": "reter", "title": "Quanto investir e o que esperar",
     "por_que": "Com a operação já estruturada, modelamos o investimento e o retorno dos próximos 6 meses — para a decisão ser baseada em número, não em achismo.",
     "execucao": "Vira o plano de mídia mês a mês: distribuição por plataforma e funil, campanhas e metas."},
]

# Lookup auxiliar para tratamentos especiais (abertura / fechamento).
MATURIDADE_SKILL = "ee-s1-diagnostico-maturidade"


# ---------------------------------------------------------------------------
# Extração do envelope comum dos outputs
# ---------------------------------------------------------------------------

def get_headline(out, fallback=""):
    h = out.get("summary_headline") or out.get("summary") or fallback
    return truncate(str(h).strip(), 175)


def dado_card(highlight):
    if not highlight:
        return ""
    sub = safe(highlight.get("subtext"), "")
    sub_html = f'<span class="dado__sub">{esc(sub)}</span>' if sub and sub != "—" else ""
    return f"""<div class="dado">
          <span class="dado__label">{esc(safe(highlight.get('label')))}</span>
          <span class="dado__value">{esc(safe(highlight.get('value')))}</span>
          {sub_html}
        </div>"""


# ---------------------------------------------------------------------------
# Builders de slide
# ---------------------------------------------------------------------------

def build_cover(ctx):
    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">Apresentação da Entrega</span>
        <h1 class="title-mega">{esc(ctx['name'])}</h1>
        <p class="subtitle-text" style="margin-top:24px; font-size:clamp(1.1rem,1.5vw,1.5rem);">
          Da estratégia à execução · Plano de Marketing · {esc(ctx['modelo_label'])}
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


def build_logica(ctx):
    return f"""
    <section class="slide">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">Como ler esta apresentação</span>
        <h2 class="title-section">Da estratégia à execução</h2>
        <p class="subtitle-text">
          Cada estudo aqui não é teoria — é a base de uma <b class="accent">execução contínua</b> de marketing.
          Vamos percorrer a jornada do seu cliente em três movimentos, e em cada um você vê
          <b class="accent">o porquê do estudo</b> e <b class="accent">como ele vira ação</b>.
        </p>
        <div class="row-3 journey-cards" style="margin-top:3.5vh;">
          <div class="glass"><div class="step-num">01</div><div class="step-name">Atrair</div>
            <p>Trazer as pessoas certas — quem realmente tem perfil pra comprar.</p></div>
          <div class="glass"><div class="step-num">02</div><div class="step-name">Converter</div>
            <p>Transformar a atenção em cliente, sem vazamentos no caminho.</p></div>
          <div class="glass"><div class="step-num">03</div><div class="step-name">Reter</div>
            <p>Fazer voltar, indicar e crescer o valor de cada cliente.</p></div>
        </div>
      </div>
    </section>
    """


def build_ponto_partida(ctx, out):
    return render_content_slide(
        " slide--diag", slide_header("Diagnóstico de Maturidade"),
        "Ponto de partida",
        "antes de agir, medimos a maturidade digital para saber a distância real até a meta.",
        get_headline(out, "Onde a operação está hoje"),
        "Define a ordem do turnaround: o que atacar primeiro para destravar resultado mais rápido.",
        out.get("summary_highlights") or [], out.get("summary_key_findings") or [],
        f"{ctx['name']} · Diagnóstico de Maturidade", "Ponto de partida")


def build_divider(phase_key):
    p = PHASES[phase_key]
    chips = []
    for k in PHASE_ORDER:
        active = " journey-chip--active" if k == phase_key else ""
        chips.append(f'<span class="journey-chip{active}">{PHASES[k]["num"]} · {PHASES[k]["label"]}</span>')
    return f"""
    <section class="slide slide--transition slide--divider">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="phase-num">{p['num']}</span>
        <span class="eyebrow">Movimento {p['num']}</span>
        <h1 class="title-mega">{esc(p['titulo'])}</h1>
        <p class="subtitle-text" style="margin-top:18px; font-size:clamp(1.1rem,1.4vw,1.45rem);">{esc(p['sub'])}</p>
        <div class="journey-track">{''.join(chips)}</div>
      </div>
    </section>
    """


FIND_TAG = {"posicao": "Posição", "vantagem": "Vantagem", "ameaca": "Atenção", "acao": "Ação"}


def _stat(h):
    sub = safe(h.get("subtext"), "")
    sub_html = f'<div class="stat__sub">{esc(sub)}</div>' if sub and sub != "—" else ""
    return (f'<div class="stat"><div class="stat__label">{esc(safe(h.get("label")))}</div>'
            f'<div class="stat__value">{esc(safe(h.get("value")))}</div>{sub_html}</div>')


def _leitura(f):
    tag = FIND_TAG.get((f.get("category") or "").lower(), "Leitura")
    return (f'<div class="leitura"><span class="leitura__tag">{esc(tag)}</span>'
            f'<span class="leitura__text">{esc(f.get("text", ""))}</span></div>')


def render_content_slide(variant, header_html, eyebrow, why, statement, exec_text,
                         highlights, findings, footer_left, footer_right, puv=None):
    """Slide de conteúdo em 2 zonas: narrativa à esquerda, painel de evidência à direita."""
    hero = highlights[0] if highlights else None
    secondary = highlights[1:4] if highlights else []
    stats_html = ('<div class="stat-row">' + "".join(_stat(h) for h in secondary) + "</div>") if secondary else ""
    leituras_html = ""
    if findings:
        leituras_html = ('<div class="leituras"><div class="leituras__title">Leituras</div>'
                         + "".join(_leitura(f) for f in findings[:3]) + "</div>")
    evidence_html = (dado_card(hero) if hero else "") + stats_html + leituras_html
    puv_html = f'<div class="puv-quote"><span>Proposta de valor</span>{esc(puv)}</div>' if puv else ""
    why_html = f'<p class="why-line"><b>Por que olhamos isto:</b> {esc(why)}</p>' if why else ""
    return f"""
    <section class="slide{variant}">
      {header_html}
      <div class="slide__content">
        <div class="angle-grid">
          <div class="angle-left">
            <span class="eyebrow">{esc(eyebrow)}</span>
            {why_html}
            <h2 class="title-statement">{esc(statement)}</h2>
            {puv_html}
            <div class="exec-bridge"><span class="arrow">→</span><div><span class="exec-label">Na execução</span>{esc(exec_text)}</div></div>
          </div>
          <div class="evidence">{evidence_html}</div>
        </div>
      </div>
      <div class="slide__footer"><span>{esc(footer_left)}</span><span>{esc(footer_right)}</span></div>
    </section>
    """


def build_content(ctx, entry, out):
    phase_key = entry["phase"]
    variant = {"converter": " slide--diag", "reter": " slide--alt"}.get(phase_key, "")
    entrega = ENTREGA_NAMES.get(entry["skill"], entry["title"])
    return render_content_slide(
        variant, slide_header(entrega),
        f"{PHASES[phase_key]['label']} · {entry['title']}",
        entry["por_que"], get_headline(out, entrega), entry["execucao"],
        out.get("summary_highlights") or [], out.get("summary_key_findings") or [],
        f"{ctx['name']} · {entrega}", PHASES[phase_key]["label"], puv=out.get("puv"))


def build_plano(ctx, outputs):
    return f"""
    <section class="slide slide--soft">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="eyebrow">O que vem agora</span>
        <h2 class="title-section">Estratégia é o mapa.<br/>Execução é a viagem.</h2>
        <p class="subtitle-text">
          Tudo que você viu vira um <b class="accent">ciclo contínuo</b> de marketing — medido e otimizado semana a semana:
        </p>
        <div class="row-3" style="margin-top:3vh;">
          <div class="glass"><div class="step-num">01</div><div class="step-name">Atrair</div>
            <p>Campanhas e conteúdo mirando o ICP, com o ângulo do posicionamento.</p></div>
          <div class="glass"><div class="step-num">02</div><div class="step-name">Converter</div>
            <p>Página, copy e atendimento afinados pra transformar lead em cliente.</p></div>
          <div class="glass"><div class="step-num">03</div><div class="step-name">Reter</div>
            <p>CRM e réguas pra fazer voltar, indicar e crescer o LTV.</p></div>
        </div>
      </div>
    </section>
    """


def build_fechamento(ctx):
    return f"""
    <section class="slide slide--alt">
      {LOGO}
      <div class="slide__content" style="justify-content:center; text-align:center;">
        <h1 class="title-mega" style="margin:0 auto;">Bora executar.</h1>
        <p class="subtitle-text" style="margin:32px auto 0; font-size:clamp(1.1rem,1.4vw,1.4rem); max-width:720px;">
          O estudo está feito. Agora é transformar cada decisão em resultado — juntos, semana após semana.
        </p>
      </div>
      <div class="slide__footer"><span>{esc(ctx['name'])}</span><span>V4 Company · Estruturação Estratégica</span></div>
    </section>
    """


# ---------------------------------------------------------------------------
# Composição
# ---------------------------------------------------------------------------

def build_entrega_transition(ctx, entry, prev_essencia, seq, total_seq):
    """Slide de contraste/transição que marca a mudança de entrega (fundo escuro)."""
    skill = entry["skill"]
    phase_key = entry["phase"]
    nome = ENTREGA_NAMES.get(skill, entry["title"])
    det = ENTREGA_DETAIL.get(skill, {})
    essencia = det.get("essencia", entry["title"])
    pergunta = det.get("pergunta", "")
    if prev_essencia:
        contrast = f"""<div class="contrast-row">
          <div class="contrast-cell"><span class="contrast-lbl">De onde viemos</span><b>{esc(prev_essencia)}</b></div>
          <span class="contrast-arrow">→</span>
          <div class="contrast-cell contrast-cell--to"><span class="contrast-lbl">Agora vamos a</span><b>{esc(essencia)}</b></div>
        </div>"""
    else:
        contrast = f"""<div class="contrast-row">
          <div class="contrast-cell contrast-cell--to"><span class="contrast-lbl">Começamos por</span><b>{esc(essencia)}</b></div>
        </div>"""
    perg = (f'<p class="transition-q">A pergunta que esta entrega responde:<br/><b>{esc(pergunta)}</b></p>'
            if pergunta else "")
    return f"""
    <section class="slide slide--white">
      {LOGO}
      <div class="slide__content" style="justify-content:center;">
        <span class="entrega-kicker">Entrega {seq} de {total_seq} · {esc(PHASES[phase_key]['label'])}</span>
        <h1 class="title-mega" style="font-size:clamp(2.6rem,5.5vw,4.8rem);">{esc(nome)}</h1>
        {contrast}
        {perg}
      </div>
    </section>
    """


def compose_slides(ctx, outputs):
    slides = [build_cover(ctx), build_logica(ctx)]

    if MATURIDADE_SKILL in outputs:
        slides.append(build_ponto_partida(ctx, outputs[MATURIDADE_SKILL]))

    # Lista ordenada de entregas com output (por fase), dedup por skill — base da numeração.
    ordered = []
    for phase_key in PHASE_ORDER:
        seen = set()
        for e in STUDY_REGISTRY:
            if e["phase"] == phase_key and e["skill"] in outputs and e["skill"] not in seen:
                seen.add(e["skill"])
                ordered.append(e)
    total_seq = len(ordered)

    prev_essencia = None
    current_phase = None
    for seq, entry in enumerate(ordered, start=1):
        if entry["phase"] != current_phase:
            current_phase = entry["phase"]
            slides.append(build_divider(current_phase))
        slides.append(build_entrega_transition(ctx, entry, prev_essencia, seq, total_seq))
        slides.append(build_content(ctx, entry, outputs[entry["skill"]]))
        prev_essencia = ENTREGA_DETAIL.get(entry["skill"], {}).get("essencia", entry["title"])

    slides.append(build_plano(ctx, outputs))
    slides.append(build_fechamento(ctx))
    return "\n".join(slides)


# ---------------------------------------------------------------------------
# Shell HTML (palette V4 — vermelho + IBM Plex Sans). Marcadores via str.replace.
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

  .slide__header { display: flex; align-items: center; gap: 16px; margin-bottom: 2.5vh; }
  .entrega-tag {
    display: inline-flex; align-items: center; gap: 8px; margin-left: auto;
    padding: 9px 18px; border-radius: 100px; font-weight: 700;
    font-size: clamp(0.74rem, 0.95vw, 0.95rem); letter-spacing: 0.05em; text-transform: uppercase;
    color: #C21A0A; background: #fff;
    border: 1px solid rgba(0,0,0,0.06); box-shadow: 0 4px 16px rgba(0,0,0,0.22);
  }
  .entrega-tag svg { opacity: 0.9; flex: none; }
  .entrega-tag b { font-weight: 800; }
  .entrega-tag .entrega-count { color: #9a3c14; font-weight: 800; margin-left: 2px; }

  /* Slides de transição entre entregas (contraste forte — fundo escuro) */
  .slide--transition { background: linear-gradient(135deg, #240705 0%, #4a0d05 55%, #2a0703 100%); }
  .entrega-kicker {
    display: inline-block; font-weight: 700; font-size: clamp(0.8rem, 1vw, 1rem);
    letter-spacing: 0.12em; text-transform: uppercase; color: #fff; margin-bottom: 1.4vh;
  }
  .contrast-row { display: flex; align-items: stretch; gap: 18px; margin-top: 3.5vh; flex-wrap: wrap; }
  .contrast-cell {
    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.14);
    border-radius: 16px; padding: 18px 24px; min-width: 230px;
  }
  .contrast-cell b {
    display: block; font-size: clamp(1.3rem, 2.2vw, 2.1rem); font-weight: 700;
    color: #fff; line-height: 1.12; margin-top: 8px;
  }
  .contrast-cell--to { background: rgba(255,255,255,0.14); border-color: rgba(255,255,255,0.45); }
  .contrast-cell--to b { color: #fff; }
  .contrast-lbl {
    font-size: 0.72rem; letter-spacing: 0.1em; text-transform: uppercase;
    color: rgba(255,255,255,0.7); font-weight: 700;
  }
  .contrast-arrow { display: flex; align-items: center; font-size: 2.2rem; color: #fff; font-weight: 800; }
  .transition-q {
    margin-top: 3.5vh; font-size: clamp(1.05rem, 1.4vw, 1.4rem); line-height: 1.45;
    color: rgba(255,255,255,0.85); max-width: 900px;
  }
  .transition-q b { color: #fff; font-weight: 700; }

  /* Slides BRANCOS das estruturas de entrega (vermelho sobre branco — contraste máximo) */
  .slide--white { background: #ffffff; }
  .slide--white .logo-v4 { border: 1px solid rgba(0,0,0,0.08); }
  .slide--white .entrega-kicker { color: #C21A0A; }
  .slide--white h1.title-mega { background: none; -webkit-text-fill-color: #FB2E0A; color: #FB2E0A; }
  .slide--white .contrast-cell { background: #f6f1ef; border-color: rgba(0,0,0,0.08); }
  .slide--white .contrast-cell b { color: #2A0703; }
  .slide--white .contrast-lbl { color: #9a3c14; }
  .slide--white .contrast-cell--to { background: #FB2E0A; border-color: #FB2E0A; }
  .slide--white .contrast-cell--to b { color: #fff; }
  .slide--white .contrast-cell--to .contrast-lbl { color: rgba(255,255,255,0.88); }
  .slide--white .contrast-arrow { color: #FB2E0A; }
  .slide--white .transition-q { color: #5a4742; }
  .slide--white .transition-q b { color: #C21A0A; }
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
  h2.title-statement {
    font-weight: 700; font-size: clamp(2rem, 4.2vw, 3.6rem);
    line-height: 1.07; letter-spacing: -0.02em; color: #fff;
    margin-bottom: 3vh; max-width: 1000px;
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
  .accent { color: #fff; font-weight: 700; }

  .why-line {
    font-size: clamp(0.95rem, 1.1vw, 1.18rem); line-height: 1.45;
    color: rgba(255,255,255,0.82); max-width: 860px; margin-bottom: 2.6vh;
  }
  .why-line b { color: #fff; font-weight: 700; }

  .dado {
    align-self: flex-start; display: inline-flex; flex-direction: column; gap: 7px;
    padding: 22px 28px; border-radius: 18px; min-width: 240px;
    background: #fff; border: 1px solid rgba(0,0,0,0.05);
    border-left: 6px solid #FB2E0A; box-shadow: 0 12px 34px rgba(0,0,0,0.22);
  }
  .dado__label {
    font-size: 0.76rem; letter-spacing: 0.08em; text-transform: uppercase;
    color: #C21A0A; font-weight: 800;
  }
  .dado__value {
    font-weight: 800; font-size: clamp(2.2rem, 4vw, 3.2rem);
    line-height: 1; color: #2A0703; letter-spacing: -0.02em;
  }
  .dado__sub { font-size: 0.95rem; color: #6b4a42; }

  /* Layout de conteúdo em 2 zonas: narrativa (esquerda) + evidência (direita) */
  .angle-grid { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 44px; flex: 1; min-height: 0; align-items: stretch; }
  .angle-left { display: flex; flex-direction: column; min-height: 0; }
  .angle-left h2.title-statement { font-size: clamp(1.7rem, 3.2vw, 3rem); max-width: none; margin-bottom: 2.4vh; }
  .angle-left .exec-bridge { margin-top: auto; }
  .evidence { display: flex; flex-direction: column; gap: 16px; min-height: 0; justify-content: center; }
  .stat-row { display: flex; gap: 12px; flex-wrap: wrap; }
  .stat { flex: 1 1 40%; min-width: 150px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 14px; padding: 13px 16px; backdrop-filter: blur(8px); }
  .stat__label { font-size: 0.68rem; letter-spacing: 0.06em; text-transform: uppercase; color: rgba(255,255,255,0.8); font-weight: 700; margin-bottom: 5px; }
  .stat__value { font-weight: 800; font-size: clamp(1.15rem, 1.7vw, 1.6rem); color: #fff; line-height: 1.08; letter-spacing: -0.01em; }
  .stat__sub { font-size: 0.78rem; color: rgba(255,255,255,0.72); margin-top: 4px; line-height: 1.3; }
  .leituras { margin-top: 6px; }
  .leituras__title { font-size: 0.72rem; letter-spacing: 0.1em; text-transform: uppercase; color: #fff; font-weight: 800; margin-bottom: 8px; opacity: 0.85; }
  .leitura { display: flex; gap: 10px; align-items: flex-start; padding: 9px 0; border-top: 1px solid rgba(255,255,255,0.15); }
  .leitura:first-of-type { border-top: none; padding-top: 2px; }
  .leitura__tag { flex: none; font-size: 0.6rem; letter-spacing: 0.05em; text-transform: uppercase; font-weight: 800; color: #C21A0A; background: #fff; border-radius: 6px; padding: 3px 7px; }
  .leitura__text { font-size: clamp(0.84rem, 1vw, 1rem); line-height: 1.36; color: rgba(255,255,255,0.95); }
  .puv-quote { border-left: 3px solid #fff; padding: 6px 0 6px 14px; margin-bottom: 2.2vh; font-size: clamp(1rem, 1.25vw, 1.3rem); font-style: italic; color: #fff; max-width: 640px; line-height: 1.4; }
  .puv-quote span { display: block; font-size: 0.66rem; font-style: normal; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.7); font-weight: 800; margin-bottom: 5px; }
  @media (max-width: 900px) { .angle-grid { grid-template-columns: 1fr; gap: 20px; } }

  .exec-bridge {
    margin-top: auto; display: flex; gap: 14px; align-items: flex-start;
    background: linear-gradient(135deg, rgba(255,255,255,0.18), rgba(255,255,255,0.05));
    border-left: 4px solid #fff; border-radius: 12px; padding: 18px 22px;
    max-width: 980px;
  }
  .exec-bridge .arrow { color: #fff; font-weight: 800; font-size: 1.4rem; line-height: 1.2; }
  .exec-bridge .exec-label {
    display: block; color: #fff; text-transform: uppercase;
    letter-spacing: 0.08em; font-size: 0.7rem; font-weight: 800; margin-bottom: 4px;
  }
  .exec-bridge > div { font-weight: 600; font-size: clamp(1rem, 1.3vw, 1.3rem); line-height: 1.4; color: #fff; }

  .glass {
    background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.16);
    backdrop-filter: blur(14px); border-radius: 18px; padding: 22px;
  }
  .row-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
  .journey-cards .glass p, .row-3 .glass p {
    font-size: clamp(0.92rem, 1.05vw, 1.1rem); line-height: 1.45;
    color: rgba(255,255,255,0.9); margin-top: 8px;
  }
  .step-num {
    font-weight: 700; font-size: 1rem; color: #fff; letter-spacing: 0.06em;
  }
  .step-name {
    font-weight: 700; font-size: clamp(1.3rem, 1.8vw, 1.7rem); color: #fff;
    margin-top: 2px; letter-spacing: -0.01em;
  }

  .highlight-box {
    background: linear-gradient(135deg, rgba(255,255,255,0.16), rgba(255,255,255,0.06));
    border-left: 4px solid #fff; padding: 18px 22px; border-radius: 10px;
  }
  .highlight-box__label {
    font-size: 0.76rem; letter-spacing: 0.1em; text-transform: uppercase;
    color: #fff; font-weight: 700; margin-bottom: 6px;
  }
  .highlight-box__text { font-weight: 600; font-size: clamp(1rem, 1.2vw, 1.25rem); line-height: 1.45; color: #fff; }

  .phase-num {
    font-weight: 700; font-size: clamp(4rem, 9vw, 8rem); line-height: 0.9;
    color: rgba(255,255,255,0.16); letter-spacing: -0.04em; margin-bottom: 1vh;
  }
  .journey-track { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 3.5vh; }
  .journey-chip {
    padding: 9px 18px; border-radius: 100px; font-weight: 600; font-size: 0.85rem;
    color: rgba(255,255,255,0.7); background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.14);
  }
  .journey-chip--active {
    color: #8a0d05; background: #fff; border-color: #fff; font-weight: 700;
  }

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
  @media (max-width: 640px) { .row-3 { grid-template-columns: 1fr; } }
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
    """Lê o favicon V4 do shared-templates/assets e devolve data-URI base64 (ou vazio)."""
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
    outputs = load_outputs(client_dir)

    # Gate: a apresentação só existe a partir da 1ª skill completa.
    if not outputs:
        return None

    meta = client.get("meta", {}) or {}
    name = meta.get("name", "Cliente")
    modelo = meta.get("modelo_venda", "")
    now = datetime.now()
    ctx = {
        "name": name,
        "modelo_label": MODELO_LABEL.get(modelo, modelo or "—"),
        "date": f"{MESES_PT[now.month]} · {now.year}",
    }

    slides_html = compose_slides(ctx, outputs)
    total = slides_html.count('<section class="slide')
    title = f"{name} · Apresentação da Entrega"

    html_out = (SHELL_HTML
                .replace("__TITLE__", esc(title))
                .replace("__LOGO_URI__", _logo_data_uri())
                .replace("__SLIDES__", slides_html)
                .replace("__TOTAL__", str(total)))

    out_path = os.path.join(client_dir, "apresentacao-entrega.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    return out_path


def main():
    if len(sys.argv) < 2:
        print("Uso: render_apresentacao_entrega.py <path_cliente>", file=sys.stderr)
        sys.exit(2)
    client_dir = sys.argv[1].rstrip("/")
    if not os.path.isdir(client_dir):
        print(f"Diretório não encontrado: {client_dir}", file=sys.stderr)
        sys.exit(2)
    out = render(client_dir)
    if out is None:
        print("Apresentação da entrega não gerada — nenhum output ainda.")
    else:
        print(f"Apresentação da entrega gerada: {out}")


if __name__ == "__main__":
    main()
