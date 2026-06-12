#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reconstrói o cliente Zenvet — envelopes RICOS (até 4 highlights + 3 findings) do consolidated.md."""
import json, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exemplo-clinica-zenvet")
OUT = os.path.join(BASE, "outputs")
os.makedirs(OUT, exist_ok=True)
NAME = "Clínica Veterinária Zenvet"

def hl(label, value, subtext="", tone="blue"):
    return {"label": label, "value": value, "subtext": subtext, "tone": tone}

def kf(category, text):
    return {"category": category, "text": text}

DATA = {
    "ee-s1-diagnostico-maturidade": {
        "summary_headline": "Maturidade digital 21/100 (crítico): rastreamento zerado, mídia, CRO e CRM no chão — esta é a base que precisa ser estruturada antes de qualquer escala.",
        "summary_highlights": [
            hl("Score geral", "21/100", "classificação crítica", "red"),
            hl("Piores pilares", "CRO 12 · CRM 14", "onde a operação mais perde hoje", "red"),
            hl("Mídia & conteúdo", "Mídia 18 · SEO 30", "criativos 32 — tudo abaixo do ideal", "yellow"),
            hl("Conversão atual", "16,6%", "lead → agendamento", "red"),
        ],
        "summary_key_findings": [
            kf("acao", "Prioridade 1: instalar Pixel/GA4 na LP e configurar eventos de conversão (clique WhatsApp, agendamento)."),
            kf("acao", "Corrigir tracking (Pixel + CAPI), migrar Meta para objetivo LEADS e preencher o budget contratado."),
            kf("acao", "Reconfigurar o Google Ads para intenção local e criar campanha 'especialista felinos Americana'."),
        ],
    },
    "ee-s1-persona-icp": {
        "summary_headline": "ICP: tutoras de gatos 25-55 (80% mulheres), classe média-alta, que querem uma veterinária que entenda de felinos de verdade — e têm medo de exame desnecessário.",
        "summary_highlights": [
            hl("Persona", "Mariana, 36", "professora · o gato é o filho da casa", "blue"),
            hl("Disposição a pagar", "\"Pago o que precisar\"", "limite é confiança + parcelamento", "green"),
            hl("Base atual", "70% gatos", "30% cães (segmento de expansão)", "blue"),
            hl("Renda", "R$ 5–12 mil/mês", "classe média a média-alta", "blue"),
        ],
        "summary_key_findings": [
            kf("vantagem", "O ICP valoriza acompanhamento próximo e teme exame desnecessário — diferencial direto da Nathalia."),
            kf("acao", "Maior vazamento na Consideração (3-7 dias): faltam sinais de especialização felina no GMB, bio do IG e reviews."),
            kf("posicao", "Converter crítico (emergência, sem teto de preço) em recorrência é a alavanca de LTV — não apenas reajustar rotina."),
        ],
    },
    "ee-s2-posicionamento": {
        "summary_headline": "Zenvet ocupa 'Especialista Felino · Humano · Transparente' — a combinação (felino + digital + humano + pós-consulta) que nenhum concorrente local replica.",
        "puv": "A clínica veterinária privada especialista em felinos de Americana — com medicina humana, acompanhamento pós-consulta e sem conta surpresa.",
        "summary_highlights": [
            hl("Território", "Felino · Humano · Transparente", "posição proprietária", "blue"),
            hl("Tagline aprovada", "\"Entende de felinos\"", "Seu gato merece uma veterinária que…", "green"),
            hl("Diferencial", "A combinação dos 4", "ninguém replica na microrregião", "green"),
            hl("Janela competitiva", "12–18 meses", "antes de o LM+ reagir", "yellow"),
        ],
        "summary_key_findings": [
            kf("vantagem", "O território 'premium felino + digital + humano' está vago — a concorrente orgânica tem o felino, mas não o digital."),
            kf("ameaca", "Janela de 12-18 meses antes de o LM+ reagir com capital ou de a concorrente orgânica escalar no digital."),
            kf("acao", "Ocupar a combinação em todos os canais em 4-8 semanas e formalizar ABFel + Cat Friendly Practice em 12-18 meses."),
        ],
    },
    "ee-s3-manual-marca": {
        "summary_headline": "Tom de marca: especialista acessível — técnica sem ser distante, próxima sem ser informal demais. Arquétipo Mentor.",
        "summary_highlights": [
            hl("Arquétipo", "Mentor", "firme no método, caloroso na relação", "blue"),
            hl("Tom de voz", "Profissional + calor humano", "técnica e acolhedora", "blue"),
            hl("Paleta", "Roxo + turquesa", "#4B1C7D · #00B8BD", "blue"),
        ],
        "summary_key_findings": [
            kf("acao", "Usar 'tutor', 'paciente', 'caso' — nunca 'dono', 'peludo', 'bichinho'. Foto da Nathalia com gato real, nunca banco de imagens."),
            kf("acao", "O tom precisa servir dois momentos: o racional (rotina/vacina) e o emocional (crise) — são a mesma Mariana em estados diferentes."),
        ],
    },
    "ee-s2-pesquisa-mercado": {
        "summary_headline": "Mercado endereçável de R$ 20 M na microrregião; a Zenvet captura R$ 653 mil (9,3% do SOM de R$ 7 M) — a meta da cliente é 1/5 do que o mercado permite.",
        "summary_highlights": [
            hl("SOM (teto)", "R$ 7,0 M", "Zenvet hoje captura 9,3%", "yellow"),
            hl("Upside vs. meta", "+R$ 5,68 M", "mercado que a cliente não enxerga", "green"),
            hl("Gap atual → SOM", "+972%", "+R$ 6,35 M sobre o faturamento atual", "green"),
            hl("Tendência felina", "+5,4% a/a", "~2x o ritmo dos cães", "green"),
        ],
        "summary_key_findings": [
            kf("vantagem", "Nenhum concorrente combina especialização felina + digital + humano + pós-consulta na região."),
            kf("ameaca", "Concorrente felina orgânica local + 4 clínicas Cat Friendly em Campinas (45-60 min) pressionam o nicho premium."),
            kf("posicao", "A meta da cliente (R$ 1,32 M) é só 18,9% do SOM — ela está pensando em menos de 1/5 do mercado disponível."),
        ],
    },
    "ee-s1-swot": {
        "summary_headline": "Zenvet tem método felino raro e base fiel, mas sangra no digital: zero tracking, Meta com link 404 e conversão lead→agendamento de só 16,6%.",
        "summary_highlights": [
            hl("Forças × Fraquezas", "4 × 4", "diferencial real, execução digital fraca", "yellow"),
            hl("Base ativa", "1.186 clientes", "show rate de ~100%", "green"),
            hl("Inativos", "486 pacientes", "sem régua de reativação", "yellow"),
            hl("Conversão", "16,6%", "lead → agendamento", "red"),
        ],
        "summary_key_findings": [
            kf("vantagem", "Atendimento domiciliar felino: alavanca de margem máxima, resolve a dor #1 (gato estressa no transporte) e ninguém comunica."),
            kf("ameaca", "A replicação do posicionamento felino é ameaça presente — não mais hipotética."),
            kf("acao", "Eliminar as hemorragias digitais (tracking zero, Meta 404, LP genérica) e construir ativos próprios (CRM, conteúdo, GMB)."),
        ],
    },
    "ee-s2-diagnostico-midia": {
        "summary_headline": "Zenvet subinveste 41% em mídia (R$ 1.875 real vs. R$ 3.200 contratado); reativar 2 Google + Pixel + migrar Meta para LEADS dobra os leads sem +1 real de teto.",
        "summary_highlights": [
            hl("CPL atual", "R$ 26", "topo do benchmark Pet/Vet (R$ 5–25)", "yellow"),
            hl("Subinvestimento", "−41%", "R$ 1.875 vs. R$ 3.200 contratado", "red"),
            hl("Google pausado", "5 de 6", "campanhas sem critério técnico", "red"),
            hl("Leads/mês", "72 → 145", "realocação + Pixel + reativar Google", "green"),
        ],
        "summary_key_findings": [
            kf("acao", "Pixel ausente é bloqueio P0: sem retargeting, sem lookalike, sem validar a conversão da LP — alavanca crítica antes de escalar."),
            kf("ameaca", "15 campanhas Meta fragmentadas em boost de posts antigos (objetivo MESSAGES/ENGAGEMENT) — inadequado para gerar leads."),
            kf("acao", "Subir a base de 1.186 clientes no Meta para criar Custom + Lookalike Audience do ICP Mariana."),
        ],
    },
    "ee-s2-diagnostico-organico-ig": {
        "summary_headline": "O feed da Zenvet já lidera o engajamento local (1,202% vs. 0,781% do LM+) — mas zero carrosséis educativos felinos em 90 dias, justo o posicionamento declarado.",
        "summary_highlights": [
            hl("Engajamento", "1,202%", "o maior dos 3 (LM+ 0,781%)", "green"),
            hl("Volume", "19 posts/90d", "vs. 4 do LM+ e 10 do Cantinho", "green"),
            hl("Carrosséis educativos", "0 em 90d", "lacuna vs. concorrência", "red"),
        ],
        "summary_key_findings": [
            kf("acao", "Lançar série mensal de 4 carrosséis felinos (Mariana-first): sinais de dor, transporte sem trauma, vacinas, quando levar."),
            kf("acao", "Sistematizar 'Dia com a Dra. Nathalia' (quinzenal) + 'Diário do Paciente' (o Fênix já funcionou) como fosso de humanização."),
            kf("acao", "Adicionar link wa.me clicável na bio e CTA em todo Reels de serviço — zero dos top posts tem CTA hoje."),
        ],
    },
    "ee-s1-auditoria-comunicacao": {
        "summary_headline": "Score médio 35/100 — três hemorragias: Meta com link 404 (R$ 800/mês), zero tracking e a mensagem felina ausente em todos os pontos de contato.",
        "summary_highlights": [
            hl("Score médio", "35/100", "5 quick wins sem custo esta semana", "red"),
            hl("Anúncios", "18/100", "Meta com link 404 destruindo R$ 800/mês", "red"),
            hl("Site", "28/100", "zero Pixel, GTM ou Analytics", "red"),
            hl("GMB", "46/100", "reviews falam de 'pet' genérico", "yellow"),
        ],
        "summary_key_findings": [
            kf("acao", "Corrigir a URL 404 do Meta e instalar Pixel + GTM no site — recupera R$ 800/mês imediatamente."),
            kf("acao", "Refinar a bio do IG: remover 'clínica geral de cães' (dilui), adicionar wa.me clicável e CTA explícito."),
            kf("acao", "Post no GMB com especialização felina + foto da Nathalia com gato + categoria atualizada."),
        ],
    },
    "ee-s2-diagnostico-cro": {
        "summary_headline": "A landing tem arquitetura básica mas tagueamento fantasma (GTM sem GA4/Pixel), zero LGPD e um H1 que contradiz o posicionamento felino aprovado.",
        "summary_highlights": [
            hl("Confiança da LP", "5/10", "sem autoridade médica visível", "red"),
            hl("PageSpeed mobile", "60/100", "TBT de 6,4 s", "yellow"),
            hl("SEO técnico", "100/100", "base boa para escalar", "green"),
            hl("LGPD", "0", "risco de multa ANPD", "red"),
        ],
        "summary_key_findings": [
            kf("acao", "Trocar o H1 para a especialização felina e adicionar seção 'Conheça a Dra. Nathalia' (CRMV, foto, experiência)."),
            kf("acao", "Instalar GA4 + Meta Pixel + Consent Mode v2 para medir conversão e respeitar a LGPD."),
            kf("acao", "Adicionar schema.org Veterinarian + Review + FAQ para gerar rich snippets no Google sem custo de mídia."),
        ],
    },
    "ee-s4-diagnostico-comercial": {
        "summary_headline": "72 leads/mês entram, mas 22 somem antes do contato e 76% dos contatados não agendam (24% vs. 35-50%) — perda de R$ 3,5–7 mil/mês.",
        "summary_highlights": [
            hl("Gargalo primário", "Contato → Agendamento", "24% vs. benchmark 35-50%", "red"),
            hl("Leads que somem", "22/mês", "antes mesmo do 1º contato (69%)", "red"),
            hl("Receita recuperável", "+R$ 3,5–7 mil/mês", "corrigindo os 2 gargalos", "green"),
            hl("Comparecimento", "~100%", "quem comparece, paga (+50pp)", "green"),
        ],
        "summary_key_findings": [
            kf("acao", "Implementar follow-up 24h/72h/7d no Kommo + script consultivo que abre com o diferencial antes do preço."),
            kf("vantagem", "A 1ª resposta (2-10 min) já é vantagem real — o problema não é velocidade, é a conversa estruturada depois."),
            kf("acao", "Treinar a qualificação 1-5★ com SLA por score (5★ em 5 min) para não perder o lead quente para o 24h."),
        ],
    },
    "ee-s4-cliente-oculto": {
        "summary_headline": "Atendimento nota 5,9/10: resposta em 2 min (excelente), mas 0 captura de nome, 0 perguntas clínicas e 0 follow-up em 24h — o lead some sem rastro.",
        "summary_highlights": [
            hl("Nota geral", "5,9/10", "classificação REGULAR", "red"),
            hl("Tempo de resposta", "9/10", "2 min — o ponto mais forte", "green"),
            hl("Identificação de necessidade", "3/10", "zero perguntas clínicas de aprofundamento", "red"),
            hl("Follow-up", "2/10", "nenhum retorno após o 'vou pensar'", "red"),
        ],
        "summary_key_findings": [
            kf("acao", "O SDR IA endereça os 6 pontos críticos (nome, urgência, follow-up): +R$ 5,5 mil/mês projetado."),
            kf("ameaca", "Não reconheceu sinal de urgência (FLUTD) num caso felino — falha de senso clínico-comercial."),
            kf("ameaca", "0 captura de nome da tutora ou da gata — sem identificação é impossível personalizar follow-up ou alimentar o CRM."),
        ],
    },
    "ee-s5-scripts-sdr": {
        "summary_headline": "Scripts do SDR IA cobrem boas-vindas, qualificação 1-5★ e follow-up 24h/72h/7d — abrindo com a especialização felina antes de o preço aparecer.",
        "summary_highlights": [
            hl("Cobertura", "24/7 · < 5 s", "resgata os 22 leads que somem", "green"),
            hl("Qualificação", "1–5★", "SLA por score, handoff só em 4★/5★", "blue"),
        ],
        "summary_key_findings": [
            kf("acao", "Handoff para a Louíse só em leads 4★/5★ — libera o humano para o fechamento consultivo."),
            kf("acao", "Follow-up automático 24h/72h/7d para todo lead que recebe preço e silencia (insistência → escassez → conteúdo)."),
        ],
    },
    "ee-s3-crm-setup": {
        "summary_headline": "CRM Kommo com réguas de boas-vindas, nutrição e reativação — para que nenhum dos 72 leads/mês e dos 486 inativos suma sem rastro.",
        "summary_highlights": [
            hl("Base inativa", "486 pacientes", "hoje sem régua de reativação", "yellow"),
            hl("Base ativa", "1.186 clientes", "reativação orgânica subexplorada", "green"),
            hl("Régua pós-consulta", "D+1 · D+7 · D+30", "sistematiza o WhatsApp da Nathalia", "green"),
        ],
        "summary_key_findings": [
            kf("acao", "Reativar a base dormindo (1.186 ativos + 486 inativos) gera receita de baixo custo nos próximos 90 dias."),
            kf("acao", "Programa de indicação no pico emocional pós-consulta (indicou uma amiga, ambas ganham 15% na próxima)."),
        ],
    },
    "ee-s3-forecast-midia": {
        "summary_headline": "Forecast: R$ 1 mil/mês incremental gera R$ 23 mil de retorno — ROI de 20,7x e payback de 16 dias (cenário realista, em regime ao fim da S12).",
        "summary_highlights": [
            hl("Investimento incremental", "R$ 1 mil/mês", "cenário realista", "blue"),
            hl("Retorno líquido", "+R$ 22 mil/mês", "ao fim da Semana 12", "green"),
            hl("ROI", "20,7x", "payback de 16 dias", "green"),
        ],
        "summary_key_findings": [
            kf("acao", "Pressupõe acessos liberados na S1 e curva de adoção do Kommo de ~30 dias antes do potencial pleno."),
        ],
    },
}

for skill, env in DATA.items():
    env = {"client_name": NAME, **env}
    with open(os.path.join(OUT, skill + ".json"), "w", encoding="utf-8") as f:
        json.dump(env, f, ensure_ascii=False, indent=2)

progress_skills = {s: {"status": "completed", "checkpoint": 0} for s in DATA}
client = {
    "meta": {"name": NAME, "slug": "clinica-veterinaria-zenvet", "workspace_id": None,
             "created_at": "2026-04-15", "modelo_venda": "inside-sales",
             "investidor": {"nome": "Ana Souza", "cargo": "Investidora V4 · à frente do projeto",
                            "foto_url": "https://i.pravatar.cc/400?img=47"}},
    "briefing": {"identification": {"name": NAME, "contact_name": "Dra. Nathalia Ramos",
                                    "contact_role": "Sócia-fundadora e veterinária responsável",
                                    "segment": "Saúde Animal & Pet Care", "location": "Americana, SP"}},
    "research": {"fetched_at": None},
    "connectors": {"fetched_at": None},
    "progress": {"current_week": 3, "skills": progress_skills},
    "history": [],
}
with open(os.path.join(BASE, "client.json"), "w", encoding="utf-8") as f:
    json.dump(client, f, ensure_ascii=False, indent=2)

tot_h = sum(len(e["summary_highlights"]) for e in DATA.values())
tot_f = sum(len(e["summary_key_findings"]) for e in DATA.values())
print(f"Criado: {len(DATA)} outputs · {tot_h} highlights · {tot_f} findings")
