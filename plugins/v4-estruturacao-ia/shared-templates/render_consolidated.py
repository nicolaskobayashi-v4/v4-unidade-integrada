#!/usr/bin/env python3
"""Gera consolidated.md a partir do client.json + outputs/*.json.

Uso:
    python3 render_consolidated.py <path_cliente>

Ex:
    python3 render_consolidated.py clientes/<slug-do-cliente>
"""
import json
import os
import re
import sys
from datetime import datetime

PORTAL_TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portal.html")


SECTIONS = [
    ("1. Identidade do Cliente", "identity"),
    ("2. Produto, Oferta & Unidade Econômica", "product"),
    ("3. ICP & Persona", "icp"),
    ("4. Mercado & Concorrência", "market"),
    ("5. Maturidade Digital & SWOT", "maturity_swot"),
    ("6. Posicionamento Estratégico", "positioning"),
    ("7. Comunicação & Auditoria de Canais", "comms"),
    ("8. Orgânico Instagram", "organic"),
    ("9. Mídia Paga", "paid"),
    ("10. CRO & Landing Page", "cro"),
    ("11. Marca & Identidade Visual", "brand"),
    ("12. Diagnóstico Comercial & Funil", "diagnostico_comercial"),
    ("13. Cliente Oculto — Avaliação do Atendimento", "cliente_oculto"),
    ("14. Roadmap de Evolução", "roadmap"),
]


def safe(v, default="—"):
    if v is None or v == "" or v == []:
        return default
    return v


def bullets(items, fmt=lambda x: x):
    if not items:
        return "—"
    return "\n".join(f"- {fmt(i)}" for i in items)


def fmt_brl(v):
    """Formata valor em BRL no padrão pt-BR (vírgula decimal, ponto milhar).
    Para valores abreviados (M, bi), usa 2 casas decimais com vírgula.
    """
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
        return f"R$ {_br(v/1_000_000_000, 2)} bi"
    if v >= 1_000_000:
        return f"R$ {_br(v/1_000_000, 2)} M"
    if v >= 1_000:
        return f"R$ {_br(v/1_000, 0)} mil"
    return f"R$ {_br(v, 2)}"


def load_outputs(base):
    outputs = {}
    outdir = os.path.join(base, "outputs")
    if not os.path.isdir(outdir):
        return outputs
    for f in sorted(os.listdir(outdir)):
        if f.endswith(".json"):
            key = f.replace(".json", "")
            with open(os.path.join(outdir, f), encoding="utf-8") as fp:
                outputs[key] = json.load(fp)
    return outputs


def section_identity(client, outputs):
    b = client.get("briefing", {})
    ident = b.get("identification", {})
    team = ident.get("v4_team", {}) or {}
    md = []
    md.append(f"**Cliente:** {safe(ident.get('name'))}")
    md.append(f"**Segmento:** {safe(ident.get('segment'))}")
    md.append(f"**Localização:** {safe(ident.get('location'))}")
    if ident.get("address"):
        md.append(f"**Endereço:** {ident['address']}")
    md.append(f"**Cidades atendidas:** {', '.join(ident.get('coverage_cities') or []) or '—'}")
    md.append("")
    md.append("### Contato")
    md.append(f"- **Responsável:** {safe(ident.get('contact_name'))} — {safe(ident.get('contact_role'))}")
    if ident.get("contact_financial"):
        md.append(f"- **Financeiro:** {ident['contact_financial']}")
    md.append(f"- **WhatsApp:** {safe(ident.get('whatsapp'))}")
    md.append(f"- **Instagram:** {safe(ident.get('instagram'))}")
    md.append(f"- **Site:** {safe(ident.get('website'))}")
    md.append("")
    md.append("### Contrato")
    md.append(f"- **Valor:** {safe(ident.get('contract_value'))}")
    md.append(f"- **Início:** {safe(ident.get('contract_start'))}")
    md.append(f"- **Faturamento anual:** {safe(ident.get('annual_revenue'))}")
    md.append(f"- **Faturamento mês atual:** {safe(ident.get('monthly_revenue_last'))} · **Meta:** {safe(ident.get('monthly_revenue_goal'))}")
    md.append("")
    md.append("### Equipe V4")
    md.append(f"- **Closer:** {safe(team.get('closer'))}")
    md.append(f"- **Executor:** {safe(team.get('executor'))}")
    md.append(f"- **Diagnóstico:** {safe(team.get('diagnostico'))}")
    return "\n".join(md)


def section_product(client, outputs):
    b = client.get("briefing", {})
    p = b.get("product", {})
    md = []
    md.append(f"**Produto principal:** {safe(p.get('main_product'))}")
    md.append("")
    md.append(f"- **Ticket médio:** {safe(p.get('ticket'))}")
    md.append(f"- **Modelo:** {safe(p.get('billing_model'))}")
    md.append(f"- **Ciclo de venda:** {safe(p.get('sales_cycle'))}")
    md.append(f"- **Base de clientes ativos:** {safe(p.get('active_customers'))}")
    md.append(f"- **Mix atual:** {safe(p.get('mix_atual'))}")
    md.append(f"- **Mais rentável:** {safe(p.get('most_profitable'))}")
    md.append(f"- **Potencial de crescimento:** {safe(p.get('growth_potential'))}")
    md.append("")
    if p.get("services"):
        md.append("### Serviços oferecidos")
        md.append(bullets(p["services"]))
    # Unit economics do diagnóstico de mídia se existir
    media = outputs.get("ee-s2-diagnostico-midia", {})
    cm = media.get("current_metrics") or {}
    if cm:
        md.append("")
        md.append("### Unidade econômica atual (últimos 90d) *[refinado em Semana 2]*")
        if cm.get("leads_per_month"):
            md.append(f"- **Leads/mês:** {cm['leads_per_month']}")
        if cm.get("cpl_estimated"):
            md.append(f"- **CPL estimado:** R$ {cm['cpl_estimated']}")
        if cm.get("conversion_rate"):
            md.append(f"- **Taxa de conversão (lead→agendamento):** {cm['conversion_rate']}")
        if cm.get("cac"):
            md.append(f"- **CAC atual:** R$ {cm['cac']}")
    return "\n".join(md)


def section_icp(client, outputs):
    o = outputs.get("ee-s1-persona-icp", {})
    if not o:
        return "*ICP ainda não definido.*"
    icp = o.get("icp", {}) or {}
    persona = o.get("persona", {}) or {}
    secondary = o.get("icp_secondary", {}) or {}
    anti = o.get("anti_persona", {}) or {}
    km = o.get("key_message", {}) or {}
    md = []
    md.append(f"> **Resumo:** {o.get('summary', '—')}")
    md.append("")
    md.append("### ICP principal")
    md.append(f"**Segmento:** {safe(icp.get('segment_label'))}")
    dem = icp.get("demographics", {}) or {}
    if dem:
        md.append(f"- **Faixa etária:** {safe(dem.get('age_range'))}")
        if dem.get('gender'):
            md.append(f"- **Gênero:** {safe(dem.get('gender'))}")
        md.append(f"- **Renda:** {safe(dem.get('income_or_revenue'))}")
        md.append(f"- **Localização:** {safe(dem.get('location'))}")
        md.append(f"- **Relação com o pet:** {safe(dem.get('pet_relationship'))}")
    md.append("")
    md.append("### Persona — Mariana")
    md.append(f"**{safe(persona.get('name'))}, {safe(persona.get('age'))}** — {safe(persona.get('occupation'))} em {safe(persona.get('location'))}")
    if persona.get("story"):
        md.append("")
        md.append(persona["story"])
    md.append("")
    if km.get("chosen_message"):
        md.append("### Mensagem-chave aprovada")
        md.append(f"> **\"{km['chosen_message']}\"**")
        if km.get("usage_context"):
            md.append(f"*Uso:* {km['usage_context']}")
        if km.get("rationale"):
            md.append(f"*Justificativa:* {km['rationale']}")
    md.append("")
    if secondary:
        md.append("### ICP secundário")
        md.append(f"**{safe(secondary.get('segment_label'))}**")
        sdem = secondary.get("demographics", {}) or {}
        if sdem:
            md.append(f"- {safe(sdem.get('age_range'))} · {safe(sdem.get('income_or_revenue'))} · {safe(sdem.get('location'))}")
        pains = secondary.get("pains") or []
        if pains:
            first = pains[0] if isinstance(pains[0], str) else (pains[0].get("pain") or pains[0].get("description"))
            md.append(f"*Dor principal:* {first}")
    md.append("")
    if anti:
        md.append("### Anti-persona")
        md.append(f"{safe(anti.get('description'))}")
        profiles = anti.get("profiles") or []
        for p in profiles[:3]:
            if isinstance(p, dict):
                md.append(f"- **{safe(p.get('label'))}** — {safe(p.get('who'))}")
    bj = o.get("buyer_journey")
    if bj and bj.get("stages"):
        md.append("")
        md.append("### Jornada de compra")
        if bj.get("description"):
            md.append(f"*{bj['description']}*")
            md.append("")
        for s in bj["stages"]:
            md.append(f"**{safe(s.get('stage') or s.get('name'))}**")
            if s.get("trigger"):
                md.append(f"- *Gatilho:* {safe(s['trigger'])}")
            if s.get("mental_state"):
                md.append(f"- *Estado mental:* {safe(s['mental_state'])}")
            if s.get("primary_channel"):
                md.append(f"- *Canal principal:* {safe(s['primary_channel'])}")
            if s.get("dominant_question"):
                md.append(f"- *Pergunta dominante:* {safe(s['dominant_question'])}")
            if s.get("client_intervention"):
                md.append(f"- *Intervenção do cliente:* {safe(s['client_intervention'])}")
            if s.get("friction_today"):
                md.append(f"- *Fricção atual:* {safe(s['friction_today'])}")
            if s.get("duration_estimate"):
                md.append(f"- *Duração estimada:* {safe(s['duration_estimate'])}")
            md.append("")
        if bj.get("critical_leakage_point"):
            md.append(f"> **Vazamento crítico do funil:** {bj['critical_leakage_point']}")
    wtp = o.get("willingness_to_pay")
    if wtp and wtp.get("services"):
        md.append("")
        md.append("### Disposição a pagar — precificação estratégica")
        if wtp.get("context"):
            md.append(f"*{wtp['context']}*")
            md.append("")
        for s in wtp["services"]:
            category_tag = f" *[{safe(s.get('category'))}]*" if s.get('category') else ""
            md.append(f"**{safe(s.get('service'))}**{category_tag}")
            if s.get("current_ticket_range"):
                md.append(f"- Ticket atual: {safe(s.get('current_ticket_range'))}")
            if s.get("perceived_fair_range"):
                md.append(f"- Faixa percebida justa: {safe(s.get('perceived_fair_range'))}")
            if s.get("premium_ceiling"):
                md.append(f"- Teto premium: {safe(s.get('premium_ceiling'))}")
            if s.get("elasticity"):
                md.append(f"- Elasticidade: {safe(s.get('elasticity'))}")
            if s.get("pricing_lever"):
                md.append(f"- Alavanca de preço: {safe(s.get('pricing_lever'))}")
            md.append("")
        if wtp.get("strategic_implication"):
            md.append(f"> **Implicação estratégica:** {wtp['strategic_implication']}")
    return "\n".join(md)


def section_market(client, outputs):
    o = outputs.get("ee-s2-pesquisa-mercado", {})
    if not o:
        return "*Pesquisa de mercado ainda não realizada.*"
    md = []
    md.append(f"> **Headline:** {o.get('summary_headline', o.get('summary', '—'))}")
    md.append("")
    md.append("### Tamanho de mercado")
    ts = o.get("tam_sam_som", {}) or {}
    for lvl in ("tam", "sam", "som"):
        v = ts.get(lvl, {}) or {}
        if v:
            val = v.get("value_brl") or v.get("value")
            val_str = fmt_brl(val) if isinstance(val, (int, float)) else safe(val)
            md.append(f"- **{lvl.upper()}:** {val_str} — {safe(v.get('description'))}")
            if v.get("source"):
                md.append(f"  *Fonte:* {v['source']}")
    ms = o.get("market_share")
    if ms and isinstance(ms, dict):
        md.append("")
        cur = ms.get("current_share_of_sam_pct")
        tgt = ms.get("target_share_of_sam_pct")
        if cur is not None:
            md.append(f"**Market share atual:** {cur}% do SAM · **SOM:** {tgt}% do SAM")
        # Jornada Atual → (Meta cliente) → SOM com gaps escalonados (espelha chart do portal)
        som_val = ts.get("som", {}).get("value_brl") if ts else None
        current_val = ms.get("current_revenue_brl")
        client_goal = ms.get("client_annual_revenue_goal_brl")
        if current_val and som_val:
            has_goal = client_goal and current_val < client_goal < som_val
            md.append("")
            md.append("**Jornada de captura — posição atual vs meta da cliente vs SOM:**")
            if has_goal:
                gap_to_goal = client_goal - current_val
                gap_goal_to_som = som_val - client_goal
                gap_to_goal_pct = (gap_to_goal / current_val * 100) if current_val else 0
                gap_goal_to_som_pct = (gap_goal_to_som / client_goal * 100) if client_goal else 0
                gap_total = som_val - current_val
                gap_total_pct = (gap_total / current_val * 100) if current_val else 0
                cur_pct_of_som = (current_val / som_val * 100) if som_val else 0
                goal_pct_of_som = (client_goal / som_val * 100) if som_val else 0
                md.append(f"- **Atual:** {fmt_brl(current_val)} ({cur_pct_of_som:.1f}% do SOM)")
                md.append(f"- **Meta da cliente:** {fmt_brl(client_goal)} ({goal_pct_of_som:.1f}% do SOM)")
                md.append(f"- **SOM:** {fmt_brl(som_val)} (teto de mercado)")
                md.append("")
                md.append(f"- **Gap atual → meta da cliente:** +{fmt_brl(gap_to_goal)} (+{gap_to_goal_pct:.0f}% sobre atual)")
                md.append(f"- **Gap meta da cliente → SOM:** +{fmt_brl(gap_goal_to_som)} (+{gap_goal_to_som_pct:.0f}% sobre a meta — upside de mercado não enxergado pela cliente)")
                md.append(f"- **Gap total atual → SOM:** +{fmt_brl(gap_total)} (+{gap_total_pct:.0f}% sobre atual)")
                md.append("")
                md.append(f"> **Leitura:** a meta comercial da cliente ({fmt_brl(client_goal)}) é conservadora frente ao que o mercado permite — o SOM aponta {fmt_brl(gap_goal_to_som)} de upside adicional, capturável com consolidação do posicionamento + expansão operacional do nicho premium.")
            else:
                gap_total = som_val - current_val
                gap_total_pct = (gap_total / current_val * 100) if current_val else 0
                cur_pct_of_som = (current_val / som_val * 100) if som_val else 0
                md.append(f"- **Atual:** {fmt_brl(current_val)} ({cur_pct_of_som:.1f}% do SOM)")
                md.append(f"- **SOM:** {fmt_brl(som_val)} (teto de mercado)")
                md.append(f"- **Gap atual → SOM:** +{fmt_brl(gap_total)} (+{gap_total_pct:.0f}% sobre atual)")
        if client_goal:
            goal_source = ms.get("client_annual_revenue_goal_source")
            source_note = f" — fonte: {goal_source}" if goal_source else ""
            md.append("")
            md.append(f"**Meta comercial anual da cliente:** {fmt_brl(client_goal)}{source_note} — métrica operacional separada do SOM.")
            goal_vs_som = ms.get("client_goal_vs_som_note")
            if goal_vs_som:
                md.append(f"*{goal_vs_som}*")
        enderecavel_val = ms.get("enderecavel_value_brl")
        enderecavel_note = ms.get("enderecavel_note")
        if enderecavel_val or enderecavel_note:
            md.append("")
            md.append("**Por que o SOM não é o SAM inteiro? — camada do mercado endereçável**")
            if enderecavel_val:
                sam_val_for_ratio = ts.get("sam", {}).get("value_brl") if ts else None
                pct_of_sam = (enderecavel_val / sam_val_for_ratio * 100) if sam_val_for_ratio else None
                som_over_end = (som_val / enderecavel_val * 100) if som_val and enderecavel_val else None
                extra_bits = []
                if pct_of_sam:
                    extra_bits.append(f"{pct_of_sam:.0f}% do SAM")
                if som_over_end:
                    extra_bits.append(f"SOM = {som_over_end:.0f}% do endereçável")
                extra = f" ({' · '.join(extra_bits)})" if extra_bits else ""
                md.append(f"- **Mercado endereçável:** {fmt_brl(enderecavel_val)}{extra} — fatia do SAM relevante à oferta (decisão estratégica de não competir em commodity/ocasional)")
            comp = ms.get("enderecavel_composition")
            if comp:
                md.append(f"- **Composição:** {comp}")
            if enderecavel_note:
                md.append(f"- *{enderecavel_note}*")
        if ms.get("commentary"):
            md.append(f"*{ms['commentary']}*")
    md.append("")
    md.append("### Concorrentes mapeados")
    comps = o.get("competitors", []) or []
    for c in comps[:6]:
        md.append(f"**{safe(c.get('name'))}**")
        md.append(f"- Posicionamento: {safe(c.get('positioning'))}")
        md.append(f"- Pontos fortes: {', '.join(c.get('strengths') or []) or '—'}")
        md.append(f"- Pontos fracos: {', '.join(c.get('weaknesses') or []) or '—'}")
        md.append("")
    md.append("### Tendências e ameaças")
    for t in (o.get("trends") or [])[:3]:
        md.append(f"- **Tendência:** {safe(t.get('trend') or t.get('title'))} — {safe(t.get('evidence') or t.get('description'))}")
    for t in (o.get("threats") or [])[:3]:
        md.append(f"- **Ameaça:** {safe(t.get('threat') or t.get('title'))} — {safe(t.get('potential_impact') or t.get('impact') or t.get('description'))}")
    md.append("")
    op = o.get("unexploited_opportunity")
    if op:
        md.append("### Oportunidade não explorada")
        if isinstance(op, dict):
            md.append(f"{safe(op.get('description'))}")
        else:
            md.append(str(op))
    diffs = o.get("real_differentials")
    if diffs:
        md.append("")
        md.append("### Diferenciais reais")
        if isinstance(diffs, dict):
            has = diffs.get("has_today") or []
        elif isinstance(diffs, list):
            has = diffs
        else:
            has = []
        for d in has:
            if isinstance(d, dict):
                lbl = d.get("differential") or d.get("title") or d.get("item")
                jus = d.get("icp_relevance") or d.get("rationale") or d.get("description") or d.get("action_needed") or ""
                status = d.get("status")
            else:
                lbl, jus, status = d, "", None
            status_tag = f" *[{status}]*" if status else ""
            md.append(f"- **{safe(lbl)}**{status_tag} — {safe(jus)}")
    return "\n".join(md)


def section_maturity_swot(client, outputs):
    m = outputs.get("ee-s1-diagnostico-maturidade", {})
    s = outputs.get("ee-s1-swot", {})
    md = []
    if m:
        md.append("### Maturidade Digital")
        md.append(f"- **Score geral:** {safe(m.get('overall_score'))}/100 ({safe(m.get('overall_classification'))})")
        bench = m.get("sector_benchmark", {}) or {}
        if bench:
            md.append(f"- **Benchmark setorial:** {safe(bench.get('average_score'))}/100 ({safe(bench.get('sector'))})")
        md.append("")
        md.append("**Scores por pilar:**")
        for p in (m.get("pillar_scores") or []):
            md.append(f"- {safe(p.get('pillar'))}: **{safe(p.get('score'))}/100** ({safe(p.get('classification'))})")
        md.append("")
        if m.get("priorities"):
            md.append("**Prioridades (top 3):**")
            for p in m["priorities"][:3]:
                md.append(f"{p.get('rank', '•')}. {safe(p.get('action'))} — *Esforço: {safe(p.get('effort'))} / Pilar: {safe(p.get('pillar'))}*")
    md.append("")
    if s:
        md.append("### SWOT")
        md.append(f"> {s.get('summary', '—')}")
        md.append("")
        for label, key in [("Forças", "strengths"), ("Fraquezas", "weaknesses"),
                           ("Oportunidades", "opportunities"), ("Ameaças", "threats")]:
            items = s.get(key, []) or []
            md.append(f"**{label}:**")
            for i in items[:4]:
                if isinstance(i, dict):
                    md.append(f"- {safe(i.get('item') or i.get('title') or i.get('description'))}")
                else:
                    md.append(f"- {i}")
            md.append("")
        fin = s.get("financial_summary_90d") or {}
        if fin:
            md.append("### Projeção financeira 90d")
            if fin.get("description"):
                md.append(f"*{fin['description']}*")
                md.append("")
            simple_fields = [
                ("total_monthly_investment_incremental", "Investimento mensal incremental", "brl"),
                ("total_monthly_return_incremental", "Retorno mensal incremental", "brl"),
                ("net_monthly_return", "Retorno líquido mensal", "brl"),
                ("roi_multiplier", "ROI (multiplicador)", "x"),
                ("payback_days_blended", "Payback", "dias"),
            ]
            for key, label, unit in simple_fields:
                v = fin.get(key)
                if v is None:
                    continue
                if unit == "brl":
                    md.append(f"- **{label}:** {fmt_brl(v)}")
                elif unit == "x":
                    md.append(f"- **{label}:** {v}x")
                elif unit == "dias":
                    md.append(f"- **{label}:** {v} dias")
                else:
                    md.append(f"- **{label}:** {v}")
            caveats = fin.get("caveats") or []
            if caveats:
                md.append("")
                md.append("*Ressalvas:*")
                for c in caveats:
                    md.append(f"  - {c}")
    return "\n".join(md)


def section_positioning(client, outputs):
    o = outputs.get("ee-s2-posicionamento", {})
    if not o:
        return "*Posicionamento ainda não definido.*"
    md = []
    md.append(f"> **Headline:** {o.get('summary_headline', o.get('summary', '—'))}")
    md.append("")
    territory = o.get("brand_territory") or {}
    if isinstance(territory, dict) and territory:
        md.append("### Território de marca")
        three = territory.get("three_words") or []
        if three:
            md.append(f"**{' · '.join(three)}**")
        elif territory.get("name"):
            md.append(f"**{territory['name']}**")
        if territory.get("description"):
            md.append(territory["description"])
    md.append("")
    puv = o.get("puv")
    if puv:
        md.append("### PUV — Proposta Única de Valor")
        if isinstance(puv, dict):
            md.append(f"> **{safe(puv.get('statement') or puv.get('text'))}**")
            if puv.get("rationale"):
                md.append(f"*{puv['rationale']}*")
        else:
            md.append(f"> **{puv}**")
    md.append("")
    tag = o.get("recommended_tagline")
    if tag:
        if isinstance(tag, dict):
            tagstr = tag.get("text") or tag.get("tagline")
        else:
            tagstr = tag
        md.append("### Tagline recomendada")
        md.append(f"> *\"{safe(tagstr)}\"*")
    md.append("")
    canvas = o.get("canvas_4p") or {}
    if isinstance(canvas, dict) and canvas:
        md.append("### Canvas 4P")
        for p in ("product", "price", "place", "promotion"):
            v = canvas.get(p)
            if v:
                label = {"product": "Produto", "price": "Preço", "place": "Praça", "promotion": "Promoção"}[p]
                if isinstance(v, dict):
                    if p == "product":
                        desc = v.get("delivers") or v.get("description") or ""
                    elif p == "price":
                        desc = v.get("justification") or v.get("description") or ""
                        if v.get("positioning"):
                            desc = f"Posicionamento **{v['positioning']}**. {desc}"
                    elif p == "place":
                        main = v.get("main_channel") or ""
                        just = v.get("main_channel_justification") or ""
                        desc = f"{main}. {just}"
                    elif p == "promotion":
                        tone = v.get("tone") or ""
                        top = v.get("top_funnel_message") or ""
                        desc = tone
                        if top:
                            desc = f"{tone}\n  - *Topo de funil:* {top}"
                    else:
                        desc = v.get("description") or ""
                    md.append(f"- **{label}:** {safe(desc)}")
                else:
                    md.append(f"- **{label}:** {v}")
    insight = o.get("key_insight")
    if insight:
        md.append("")
        md.append("### Insight estratégico")
        if isinstance(insight, dict):
            if insight.get("headline"):
                md.append(f"**{insight['headline']}**")
            if insight.get("context"):
                md.append("")
                md.append(insight["context"])
            reasons = insight.get("numbered_reasons") or []
            if reasons:
                md.append("")
                for i, r in enumerate(reasons, 1):
                    md.append(f"{i}. {r}")
        else:
            md.append(str(insight))
    op_dir = o.get("operator_direction")
    if op_dir and isinstance(op_dir, dict):
        md.append("")
        md.append("### Direção estratégica")
        if op_dir.get("strongest_differential"):
            md.append(f"- **Diferencial mais forte:** {op_dir['strongest_differential']}")
        if op_dir.get("desired_position"):
            md.append(f"- **Posição desejada:** {op_dir['desired_position']}")
        if op_dir.get("desired_tone"):
            md.append(f"- **Tom desejado:** {op_dir['desired_tone']}")
        restr = op_dir.get("positioning_restrictions") or []
        if restr:
            md.append("- **Restrições:**")
            for r in restr:
                md.append(f"  - {r}")
    return "\n".join(md)


def section_comms(client, outputs):
    o = outputs.get("ee-s1-auditoria-comunicacao", {})
    if not o:
        return "*Auditoria de comunicação ainda não realizada.*"
    md = []
    md.append(f"> **Resumo:** {o.get('summary', '—')}")
    md.append("")
    md.append(f"**Score médio:** {safe(o.get('overall_score'))}/100 ({safe(o.get('overall_classification'))})")
    md.append("")
    md.append("### Scores por canal")
    for c in (o.get("channel_scores") or []):
        md.append(f"- {safe(c.get('channel'))}: **{safe(c.get('score'))}/100** — {safe(c.get('summary') or c.get('classification'))}")
    md.append("")
    tp = o.get("top_problems") or []
    if tp:
        md.append("### Problemas críticos")
        for p in tp[:5]:
            if isinstance(p, dict):
                md.append(f"- **{safe(p.get('title') or p.get('problem'))}** — {safe(p.get('description') or p.get('impact'))}")
            else:
                md.append(f"- {p}")
    md.append("")
    qw = o.get("quick_wins") or []
    if qw:
        md.append("### Quick Wins")
        for q in qw[:5]:
            if isinstance(q, dict):
                md.append(f"- {safe(q.get('action') or q.get('title'))} *(Impacto: {safe(q.get('impact'))})*")
            else:
                md.append(f"- {q}")
    return "\n".join(md)


def section_organic(client, outputs):
    o = outputs.get("ee-s2-diagnostico-organico-ig", {})
    if not o:
        return "*Diagnóstico de Instagram ainda não realizado.*"
    md = []
    md.append(f"> **Resumo:** {o.get('summary', '—')}")
    md.append("")
    bench = o.get("engagement_benchmark", {}) or {}
    if bench:
        md.append("### Engagement vs concorrência")
        accounts = bench.get("by_account") or []
        for a in accounts:
            if isinstance(a, dict):
                md.append(f"- **@{safe(a.get('username'))}** — engagement proxy: {safe(a.get('avg_engagement_proxy'))}% · formato forte: {safe(a.get('best_format_by_engagement'))}")
        if bench.get("insight"):
            md.append("")
            md.append(f"*{bench['insight']}*")
    md.append("")
    wp = o.get("client_winning_patterns") or []
    if wp:
        md.append("### O que já funciona")
        for p in wp[:4]:
            if isinstance(p, dict):
                md.append(f"- {safe(p.get('pattern') or p.get('description'))}")
            else:
                md.append(f"- {p}")
    md.append("")
    gaps = o.get("competitor_patterns_missing") or []
    if gaps:
        md.append("### Lacunas vs concorrência")
        for g in gaps[:4]:
            if isinstance(g, dict):
                md.append(f"- {safe(g.get('pattern') or g.get('description'))}")
            else:
                md.append(f"- {g}")
    md.append("")
    na = o.get("next_actions") or []
    if na:
        md.append("### Próximas ações")
        for a in na[:5]:
            if isinstance(a, dict):
                md.append(f"- {safe(a.get('action') or a.get('title'))}")
            else:
                md.append(f"- {a}")
    return "\n".join(md)


def section_paid(client, outputs):
    o = outputs.get("ee-s2-diagnostico-midia", {})
    if not o:
        return "*Diagnóstico de mídia ainda não realizado.*"
    md = []
    md.append(f"> **Headline:** {o.get('summary_headline', o.get('summary', '—'))}")
    md.append("")
    md.append(f"- **Período analisado:** {safe(o.get('data_period'))}")
    md.append(f"- **Budget contratado:** {safe(o.get('monthly_budget'))}/mês")
    md.append(f"- **Google Ads:** {safe(o.get('monthly_budget_google'))}/mês")
    md.append(f"- **Meta Ads:** {safe(o.get('monthly_budget_meta'))}/mês")
    md.append("")
    cm = o.get("current_metrics") or {}
    if cm:
        md.append("### Métricas atuais (90d)")
        label_map = {
            "cpl": "CPL", "ctr": "CTR", "cpc": "CPC", "cpa": "CPA", "cpm": "CPM",
            "conversion_rate": "Taxa de conversão",
            "total_investment": "Investimento total",
            "total_leads": "Total de leads",
            "total_clicks": "Total de clicks",
            "impressions": "Impressões",
            "frequency": "Frequência",
        }
        for k, v in cm.items():
            if isinstance(v, (str, int, float)):
                label = label_map.get(k, k.replace("_", " ").capitalize())
                md.append(f"- **{label}:** {v}")
    md.append("")
    highlights = o.get("summary_highlights") or []
    if highlights:
        md.append("### Principais achados")
        for h in highlights[:6]:
            if isinstance(h, dict):
                label = h.get("label") or h.get("title") or ""
                value = h.get("value") or ""
                subtext = h.get("subtext") or h.get("description") or ""
                md.append(f"- **{label}:** {value} — {subtext}")
            else:
                md.append(f"- {h}")
    md.append("")
    diag = o.get("diagnosis_by_dimension") or {}
    if diag:
        md.append("### Diagnóstico por dimensão")
        for dim, content in diag.items():
            dim_label = dim.replace("_", " ").capitalize()
            if isinstance(content, dict):
                # Pega primeiro campo textual relevante
                text_keys = ["segmentation", "summary", "description", "analysis", "diagnostic", "issue"]
                text = ""
                for k in text_keys:
                    if content.get(k):
                        text = content[k]
                        break
                if not text:
                    # pega primeiro valor string
                    for k, v in content.items():
                        if isinstance(v, str) and v.strip():
                            text = v
                            break
                md.append(f"- **{dim_label}:** {text or '—'}")
            elif isinstance(content, str):
                md.append(f"- **{dim_label}:** {content or '—'}")
    return "\n".join(md)


def section_cro(client, outputs):
    o = outputs.get("ee-s2-diagnostico-cro", {})
    if not o:
        return "*Diagnóstico de CRO ainda não realizado.*"
    md = []
    md.append(f"> **Resumo:** {o.get('summary', '—')}")
    md.append("")
    md.append(f"- **URL analisada:** {safe(o.get('url'))}")
    conv = o.get("current_conversion_rate")
    bounce = o.get("current_bounce_rate")
    time_p = o.get("avg_time_on_page")
    md.append(f"- **Taxa de conversão atual:** {safe(conv)+'%' if conv is not None else 'Não disponível — GA4 não instalado'}")
    md.append(f"- **Bounce rate:** {safe(bounce)+'%' if bounce is not None else 'Não disponível — GA4 não instalado'}")
    md.append(f"- **Tempo médio na página:** {safe(time_p)+'s' if time_p is not None else 'Não disponível — GA4 não instalado'}")
    ta = o.get("technical_audit") or {}
    if ta:
        md.append("")
        md.append("### Auditoria técnica")
        ps = ta.get("pagespeed") or {}
        if ps:
            ms = ps.get("mobile_scores", {}) or {}
            ds = ps.get("desktop_scores", {}) or {}
            md.append(f"- **PageSpeed Mobile:** Performance {safe(ms.get('performance'))}/100 · SEO {safe(ms.get('seo'))}/100 · A11y {safe(ms.get('accessibility'))}/100")
            md.append(f"- **PageSpeed Desktop:** Performance {safe(ds.get('performance'))}/100 · SEO {safe(ds.get('seo'))}/100 · A11y {safe(ds.get('accessibility'))}/100")
        cwv = ta.get("pagespeed", {}).get("mobile_cwv_lab", {}) or {}
        if cwv:
            lcp = cwv.get("lcp_ms")
            md.append(f"- **LCP mobile:** {round(lcp)}ms · **CLS:** {cwv.get('cls')} · **TBT:** {round(cwv.get('tbt_ms', 0))}ms" if lcp else "")
    md.append("")
    ca = o.get("copy_audit") or {}
    if ca and isinstance(ca, dict):
        af = ca.get("above_fold") or {}
        if af:
            md.append("### Hero (above the fold)")
            md.append(f"- **Headline atual:** {safe(af.get('current_headline'))}")
            md.append(f"- **Headline sugerida:** {safe(af.get('suggested_headline'))}")
            md.append(f"- **CTA atual:** {safe(af.get('current_cta'))}")
            md.append(f"- **CTA sugerido:** {safe(af.get('suggested_cta'))}")
            if af.get("value_prop_detail"):
                md.append("")
                md.append(f"*{af['value_prop_detail']}*")
    trust = o.get("trust_analysis") or {}
    if trust:
        md.append("")
        md.append(f"**Score de confiança:** {safe(trust.get('trust_score'))}/10")
        if trust.get("biggest_trust_gap"):
            md.append(f"*Maior gap:* {trust['biggest_trust_gap']}")
    md.append("")
    th = o.get("test_hypotheses") or []
    if th:
        md.append("### Hipóteses de teste (P1)")
        p1s = [t for t in th if isinstance(t, dict) and (t.get("priority") == "P1" or not t.get("priority"))][:3]
        for t in p1s:
            md.append(f"- **{safe(t.get('hypothesis'))}**")
            if t.get("element"):
                md.append(f"  *Elemento:* {t['element']}")
    return "\n".join(md)


def section_brand(client, outputs):
    b = client.get("briefing", {}).get("brand", {}) or {}
    md = []
    md.append("### Atributos de marca")
    md.append(f"- **Adjetivos:** {', '.join(b.get('adjectives') or []) or '—'}")
    md.append(f"- **Tom de voz:** {safe(b.get('voice_tone'))}")
    md.append(f"- **Marcas admiradas:** {', '.join(b.get('admired_brands') or []) or '—'}")
    md.append("")
    cc = b.get("current_colors") or {}
    if cc:
        md.append("### Paleta atual (HEX)")
        for k, v in cc.items():
            md.append(f"- **{k.replace('_', ' ').capitalize()}:** `{v}`")
    md.append("")
    if b.get("typography"):
        md.append(f"**Tipografia:** {b['typography']}")
    if b.get("graphic_elements"):
        md.append("")
        md.append("### Elementos gráficos")
        md.append(bullets(b["graphic_elements"]))
    if b.get("brand_rules"):
        md.append("")
        md.append(f"**Regras de uso:** {b['brand_rules']}")
    ai = b.get("assets_inventory") or {}
    if ai:
        md.append("")
        md.append("### Inventário de assets *[Semana 1]*")
        if ai.get("campaigns"):
            md.append("**Campanhas:**")
            md.append(bullets(ai["campaigns"]))
        if ai.get("photos"):
            md.append(f"**Fotos:** {ai['photos']}")
        if ai.get("videos"):
            md.append(f"**Vídeos:** {ai['videos']}")
        if ai.get("status"):
            md.append(f"*Status:* {ai['status']}")
    return "\n".join(md)


def section_diagnostico_comercial(client, outputs):
    d = outputs.get("ee-s4-diagnostico-comercial") or {}
    if not d:
        return "*Skill `ee-s4-diagnostico-comercial` ainda não executada.*"
    md = []
    if d.get("summary_headline"):
        md.append(f"> **{d['summary_headline']}**")
        md.append("")
    if d.get("summary"):
        md.append(d["summary"])
        md.append("")
    # Funnel extended (chevrons "Destrava Receita")
    fe = d.get("funnel_extended") or []
    if fe:
        md.append("### Funil em base mensal — Exposição → Retenção")
        md.append("")
        md.append("| Etapa | Volume | Taxa | Status | Observação |")
        md.append("|---|---|---|---|---|")
        for st in fe:
            status = st.get("status") or "—"
            stage = st.get("stage", "—")
            if st.get("is_active_constraint"):
                stage = f"🔴 **{stage}** (restrição ativa)"
            md.append(
                f"| {stage} | {safe(st.get('volume_label'))} | {safe(st.get('rate_label'))} | {safe(status)} | {safe(st.get('subtext')).replace(chr(10), ' ')} |"
            )
        md.append("")
    # Funil detalhado por etapa (com gap vs benchmark)
    fd = d.get("funnel_diagnosis") or []
    if fd:
        md.append("### Diagnóstico detalhado por etapa")
        md.append("")
        md.append("| Etapa | Atual | Benchmark | Gap | Status | Impacto Mensal |")
        md.append("|---|---|---|---|---|---|")
        for st in fd:
            cur = st.get("current_rate")
            bm = st.get("benchmark")
            gap = st.get("gap")
            cur_s = f"{cur}%" if cur is not None else "—"
            bm_s = f"{bm}%" if bm is not None else "—"
            gap_s = f"{gap:+}pp" if isinstance(gap, (int, float)) else "—"
            impact = st.get("financial_impact_monthly")
            impact_s = fmt_brl(impact) if impact else "—"
            md.append(
                f"| {safe(st.get('stage'))} | {cur_s} | {bm_s} | {gap_s} | {safe(st.get('status'))} | {impact_s} |"
            )
        md.append("")
    # Critérios de qualificação 1-5★
    qc = d.get("qualification_criteria") or {}
    if qc:
        md.append("### Critérios de Qualificação (1–5★) — validados pela cliente")
        md.append("")
        for star_key, label in [
            ("five_star", "⭐⭐⭐⭐⭐ 5★ — Qualificado pleno"),
            ("four_star", "⭐⭐⭐⭐ 4★ — Qualificado em construção"),
            ("three_star", "⭐⭐⭐ 3★ — Morno"),
            ("one_two_star", "⭐⭐ / ⭐ — Anti-persona / Frio"),
        ]:
            c = qc.get(star_key) or {}
            if not c:
                continue
            md.append(f"**{label}**")
            if c.get("profile"):
                md.append(f"- Perfil: {c['profile']}")
            if c.get("action"):
                md.append(f"- Ação: {c['action']}")
            if c.get("example"):
                md.append(f"- Exemplo canônico: *\"{c['example']}\"*")
            md.append("")
    # SLA
    sla = d.get("sla") or {}
    if sla:
        md.append("### SLA por estrela")
        md.append("")
        md.append(f"- **5★:** {safe(sla.get('five_star_minutes'))} min · responsável: {safe(sla.get('five_star_responsible'))}")
        md.append(f"- **4★:** {safe(sla.get('four_star_hours'))} h · responsável: {safe(sla.get('four_star_responsible'))}")
        md.append(f"- **3★:** {safe(sla.get('three_star_hours'))} h")
        if sla.get("escalation_5star_minutes") or sla.get("escalation_4star_hours"):
            md.append(f"- Escalação: 5★ {safe(sla.get('escalation_5star_minutes'))} min / 4★ {safe(sla.get('escalation_4star_hours'))} h — {safe(sla.get('escalation_responsible'))}")
        md.append("")
    # Top 3 objeções
    om = d.get("objection_map") or []
    if om:
        md.append("### Top objeções mapeadas")
        md.append("")
        for o in om[:3]:
            md.append(f"**{o.get('objection', '—')}** {f'_(tipo: {o.get(chr(34)+chr(116)+chr(121)+chr(112)+chr(101)+chr(34))})_' if o.get('type') else ''}")
            if o.get("recommended_response"):
                md.append(f"- *Resposta recomendada:* {o['recommended_response']}")
            if o.get("sdr_prevention"):
                md.append(f"- *Prevenção pelo SDR IA:* {o['sdr_prevention']}")
            md.append("")
    # Plano de ação 5 prioridades
    ap = d.get("action_plan") or []
    if ap:
        md.append("### Plano de ação")
        md.append("")
        md.append("| # | Ação | Responsável | Prazo | Impacto Esperado |")
        md.append("|---|---|---|---|---|")
        for a in ap:
            md.append(
                f"| {safe(a.get('priority'))} | {safe(a.get('action'))} | {safe(a.get('responsible'))} | {safe(a.get('timeline'))} | {safe(a.get('expected_impact')).replace(chr(10), ' ')} |"
            )
        md.append("")
    # Gargalo primário
    pb = d.get("primary_bottleneck") or {}
    if pb:
        md.append("### Gargalo primário")
        md.append("")
        md.append(f"**Etapa:** {safe(pb.get('stage'))}")
        md.append("")
        if pb.get("description"):
            md.append(pb["description"])
            md.append("")
        if pb.get("estimated_improvement"):
            md.append(f"**Impacto estimado da correção:** {pb['estimated_improvement']}")
            md.append("")
    return "\n".join(md)


def section_cliente_oculto(client, outputs):
    d = outputs.get("ee-s4-cliente-oculto") or {}
    if not d:
        return "*Skill `ee-s4-cliente-oculto` ainda não executada.*"
    md = []
    if d.get("summary_headline"):
        md.append(f"> **{d['summary_headline']}**")
        md.append("")
    if d.get("summary"):
        md.append(d["summary"])
        md.append("")
    ev = d.get("evaluation") or {}
    if ev:
        score = ev.get("overall_score")
        cls = ev.get("classification") or "—"
        cls_label = {"excelente": "EXCELENTE", "bom": "BOM", "regular": "REGULAR", "ruim": "RUIM", "critico": "CRÍTICO"}.get(str(cls).lower(), cls.upper())
        md.append("### Avaliação geral")
        md.append("")
        md.append(f"- **Nota:** {score}/10")
        md.append(f"- **Classificação:** {cls_label}")
        md.append("")
        cs = ev.get("criteria_scores") or []
        if cs:
            md.append("### Notas por critério")
            md.append("")
            md.append("| Critério | Nota | Observação |")
            md.append("|---|---|---|")
            for c in cs:
                md.append(
                    f"| {safe(c.get('criterion'))} | **{safe(c.get('score'))}/10** | {safe(c.get('observation')).replace(chr(10), ' ')} |"
                )
            md.append("")
        strengths = ev.get("strengths") or []
        if strengths:
            md.append("### Pontos fortes")
            md.append(bullets(strengths))
            md.append("")
        critical = ev.get("critical_improvements") or []
        if critical:
            md.append("### Melhorias críticas identificadas")
            md.append(bullets(critical))
            md.append("")
        impact = ev.get("overall_sdr_impact") or {}
        if impact:
            md.append("### Impacto projetado pelo SDR IA")
            md.append("")
            md.append(f"- Tempo de resposta antes: **{safe(impact.get('response_time_before'))}** → depois: **{safe(impact.get('response_time_after'))}**")
            md.append(f"- Taxa Lead→Contato: **{safe(impact.get('contact_rate_before'))}%** → **{safe(impact.get('contact_rate_after'))}%**")
            if impact.get("financial_impact_monthly"):
                md.append(f"- **Impacto financeiro mensal estimado:** {fmt_brl(impact['financial_impact_monthly'])}")
            md.append("")
    bp = d.get("buyer_profile") or {}
    if bp:
        md.append("### Perfil simulado")
        md.append(f"- Nome: {safe(bp.get('name'))} · Pet: {safe(bp.get('pet'))} · Cidade: {safe(bp.get('city'))}")
        if bp.get("scenario"):
            md.append(f"- Cenário: {bp['scenario']}")
        if bp.get("urgency"):
            md.append(f"- Urgência: {bp['urgency']}")
        md.append("")
    return "\n".join(md)


def section_roadmap(client, outputs):
    progress = client.get("progress", {}) or {}
    skills = progress.get("skills", {}) or {}
    history = client.get("history", []) or []
    md = []
    md.append("### Skills concluídas")
    for name, info in skills.items():
        if info.get("status") == "completed":
            md.append(f"- ✅ **{name}** — concluída em {safe(info.get('completed_at'))}")
        elif info.get("status") == "in_progress":
            md.append(f"- 🟡 **{name}** — em andamento")
    md.append("")
    md.append(f"**Semana atual:** {safe(progress.get('current_week'))}")
    md.append("")
    if history:
        md.append("### Histórico de refinamentos")
        for h in history[-8:]:
            note = h.get("note", "")
            md.append(f"- *{safe(h.get('ts'))}* — **{safe(h.get('skill'))}** ({safe(h.get('action'))}): {note}")
    return "\n".join(md)


RENDERERS = {
    "identity": section_identity,
    "product": section_product,
    "icp": section_icp,
    "market": section_market,
    "maturity_swot": section_maturity_swot,
    "positioning": section_positioning,
    "comms": section_comms,
    "organic": section_organic,
    "paid": section_paid,
    "cro": section_cro,
    "brand": section_brand,
    "diagnostico_comercial": section_diagnostico_comercial,
    "cliente_oculto": section_cliente_oculto,
    "roadmap": section_roadmap,
}


def render(client_path):
    client_path = os.path.abspath(client_path)
    with open(os.path.join(client_path, "client.json"), encoding="utf-8") as f:
        client = json.load(f)
    outputs = load_outputs(client_path)
    ident = client.get("briefing", {}).get("identification", {}) or {}
    slug = client.get("meta", {}).get("slug", "cliente")
    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    current_week = client.get("progress", {}).get("current_week", "—")

    parts = [
        f"# Visão Consolidada — {safe(ident.get('name'))}",
        "",
        f"*Gerado em {generated} · Ciclo atual: Semana {current_week} · Cliente: `{slug}`*",
        "",
        "> Este documento consolida tudo que foi produzido para o cliente ao longo do projeto.",
        "> Cada seção referencia o output estruturado original em `outputs/` para auditabilidade.",
        "> Informações refinadas ao longo das semanas estão marcadas entre colchetes.",
        "",
        "---",
        "",
        "## Sumário",
        "",
    ]
    for title, _ in SECTIONS:
        anchor = title.lower().replace(" ", "-").replace(".", "").replace("ç", "c").replace("ã", "a").replace("é", "e").replace("&", "").replace("--", "-")
        parts.append(f"- [{title}](#{anchor})")
    parts.append("")
    parts.append("---")

    for title, key in SECTIONS:
        parts.append("")
        parts.append(f"## {title}")
        parts.append("")
        parts.append(RENDERERS[key](client, outputs))
        parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(f"*Documento gerado automaticamente a partir de `client.json` + `outputs/*.json`. Re-execute `render_consolidated.py {slug}` após cada revisão para atualizar.*")

    out = "\n".join(parts)
    with open(os.path.join(client_path, "consolidated.md"), "w", encoding="utf-8") as f:
        f.write(out)
    print(f"OK — consolidated.md gerado em {client_path}/consolidated.md ({len(out)} chars)")

    # Gera consolidated.html (portal linear, apenas visualizações executivas)
    try:
        html = build_consolidated_html(client, outputs, ident, generated, current_week)
        with open(os.path.join(client_path, "consolidated.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"OK — consolidated.html gerado em {client_path}/consolidated.html ({len(html)} chars)")
    except Exception as e:
        print(f"WARN — falha ao gerar consolidated.html: {e}")
        import traceback
        traceback.print_exc()


# =============================================================================
# Geração de consolidated.html
# Herda CSS + helpers + renderers (objeto R) do portal.html, envelopa em layout
# linear (TOC + sessões empilhadas) e adiciona uma camada "Aprofundamento" por
# skill com dados que o portal não mostra.
# =============================================================================


LINEAR_LAYOUT_CSS = r"""
/* Consolidated linear layout overrides — OVERRIDE portal defaults */
html, body { overflow: auto !important; height: auto !important; }
body.consolidated { background: #F2F2F2 !important; min-height: 100vh; overflow: auto !important; }
body.consolidated .gate, body.consolidated .pres-overlay, body.consolidated .pres-bar,
body.consolidated .logout, body.consolidated .consolidated-btn,
body.consolidated #presOverlay, body.consolidated #presBar, body.consolidated #passwordGate,
body.consolidated #progress-bar { display: none !important; }

.cs-hero {
  background: linear-gradient(135deg, #560303 0%, #7A0A02 40%, #FB2E0A 100%);
  color: #fff; padding: 56px 32px 48px; text-align: center;
}
.cs-hero__eyebrow {
  font-size: 11px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.18em; opacity: 0.8; margin-bottom: 12px;
}
.cs-hero h1 { font-size: 34px; font-weight: 600; letter-spacing: -0.015em; margin-bottom: 10px; color: #fff; }
.cs-hero__meta { font-size: 13px; opacity: 0.85; font-weight: 300; }
.cs-hero__note { font-size: 12px; opacity: 0.7; font-weight: 300; margin-top: 14px; max-width: 640px; margin-left:auto; margin-right:auto; }

.cs-layout {
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 40px;
  max-width: 1280px;
  margin: 0 auto;
  padding: 40px 32px 80px;
  align-items: start;
}
.cs-toc {
  /* Default: dentro do flow do grid (1ª coluna), abaixo do hero. */
  position: relative;
  align-self: start;
  max-height: calc(100vh - 40px);
  background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 12px;
  padding: 16px 12px;
  display: flex; flex-direction: column;
  font-size: 13px;
  z-index: 50;
}
.cs-toc.cs-toc--fixed {
  /* Modo fixed: ativado via JS quando o hero rolou pra fora da viewport.
     Barra "desce junto" com o scroll, sempre visível na mesma posição da tela. */
  position: fixed;
  top: 20px;
  width: 260px;
  /* Alinha com a 1ª coluna do .cs-layout (max-width 1280px centralizado, padding 32px) */
  left: max(32px, calc((100vw - 1280px) / 2 + 32px));
}
.cs-toc__title {
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.14em;
  color: #909090; margin: 4px 0 10px; font-weight: 700; padding: 0 8px;
}
.cs-toc__list {
  flex: 1 1 auto;
  overflow-y: auto;
  padding-right: 2px;
  /* Custom scrollbar discreta */
  scrollbar-width: thin;
  scrollbar-color: rgba(0,0,0,0.15) transparent;
}
.cs-toc__list::-webkit-scrollbar { width: 6px; }
.cs-toc__list::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.12); border-radius: 3px; }
.cs-toc__list::-webkit-scrollbar-thumb:hover { background: rgba(0,0,0,0.22); }
.cs-toc a {
  display: block; padding: 8px 10px; color: #606060; text-decoration: none;
  border-radius: 6px; border-left: 2px solid transparent; transition: all .15s;
  font-size: 13px; line-height: 1.4; margin-bottom: 2px;
}
.cs-toc a:hover, .cs-toc a.active {
  background: rgba(251,46,10,0.08); color: #FB2E0A; border-left-color: #FB2E0A;
}

/* ===== Search box no topo do sumário ===== */
.cs-search {
  position: relative;
  padding: 0 4px 12px;
  margin-bottom: 4px;
  border-bottom: 1px solid rgba(0,0,0,0.06);
}
.cs-search__input-wrap {
  position: relative;
  display: flex; align-items: center;
}
.cs-search__icon {
  position: absolute; left: 10px;
  width: 14px; height: 14px;
  color: #909090; pointer-events: none;
}
.cs-search__input {
  width: 100%;
  padding: 8px 28px 8px 30px;
  border: 1px solid rgba(0,0,0,0.12);
  border-radius: 6px;
  background: #FAFAFA;
  font-size: 12.5px;
  font-family: inherit;
  color: #1E2124;
  outline: none;
  transition: all .15s;
}
.cs-search__input::placeholder { color: #B0B0B0; }
.cs-search__input:focus {
  background: #fff;
  border-color: #FB2E0A;
  box-shadow: 0 0 0 3px rgba(251,46,10,0.10);
}
.cs-search__clear {
  position: absolute; right: 6px;
  width: 18px; height: 18px;
  border: none; background: transparent;
  color: #909090; cursor: pointer;
  font-size: 14px; line-height: 1;
  display: none;
  border-radius: 4px;
}
.cs-search__clear:hover { color: #FB2E0A; background: rgba(251,46,10,0.08); }
.cs-search--has-value .cs-search__clear { display: flex; align-items: center; justify-content: center; }

.cs-search__suggest {
  position: absolute;
  top: calc(100% - 6px);
  left: 4px; right: 4px;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.12);
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.10);
  max-height: 320px;
  overflow-y: auto;
  z-index: 60;
  display: none;
  padding: 6px 0;
}
.cs-search--open .cs-search__suggest { display: block; }
.cs-search__group {
  padding: 8px 12px 4px;
  font-size: 9.5px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.14em;
  color: #B0B0B0;
}
.cs-search__item {
  display: block;
  padding: 8px 14px;
  font-size: 12.5px;
  color: #3a3f44;
  text-decoration: none;
  cursor: pointer;
  line-height: 1.4;
  border-left: 2px solid transparent;
  transition: all .12s;
}
.cs-search__item:hover, .cs-search__item--focused {
  background: rgba(251,46,10,0.06);
  color: #FB2E0A;
  border-left-color: #FB2E0A;
}
.cs-search__item-meta {
  display: block;
  font-size: 10.5px;
  color: #909090;
  margin-top: 2px;
}
.cs-search__item:hover .cs-search__item-meta,
.cs-search__item--focused .cs-search__item-meta {
  color: rgba(251,46,10,0.7);
}
.cs-search__item mark {
  background: rgba(251,46,10,0.18);
  color: #FB2E0A;
  font-weight: 600;
  padding: 0 1px;
  border-radius: 2px;
}
.cs-search__empty {
  padding: 14px 14px 12px;
  font-size: 12px;
  color: #909090;
  text-align: center;
  font-style: italic;
}

.cs-main {
  /* Sempre na 2ª coluna do grid — mesmo quando .cs-toc vira fixed (sai do flow).
     Sem isso, ao virar fixed, o main colapsava pra 1ª coluna e ficava atrás da barra. */
  grid-column: 2;
  min-width: 0;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 14px;
  padding: 48px 56px;
}

.cs-skill {
  padding: 0; margin-bottom: 56px; scroll-margin-top: 20px;
}
.cs-skill:last-child { margin-bottom: 0; }
.cs-skill + .cs-skill { padding-top: 48px; border-top: 1px solid rgba(0,0,0,0.08); }
.cs-skill__h { margin-bottom: 22px; }
.cs-skill__h h2 {
  font-size: 26px; font-weight: 600; color: #1E2124; letter-spacing: -0.015em;
  margin-bottom: 4px;
}
.cs-skill__meta { font-size: 11px; color: #909090; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; }
.cs-skill__meta .cs-status--completed { color: #16a34a; }
.cs-skill__meta .cs-status--in_progress { color: #F59E0B; }
.cs-skill__meta .cs-status--pending { color: #909090; }
.cs-skill__pending { color: #909090; font-style: italic; padding: 20px 0; font-size: 13px; }
.cs-skill__error { color: #DC2626; font-size: 13px; padding: 12px; background: rgba(220,38,38,0.04); border-radius: 8px; }

.cs-exec { }
.cs-exec .sc { margin-bottom: 20px; }

.cs-deep {
  margin-top: 28px;
  padding-top: 20px;
  border-top: 1px dashed rgba(0,0,0,0.12);
}
.cs-deep__label {
  display: inline-block;
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.14em;
  color: #fff; background: linear-gradient(135deg, #560303, #FB2E0A);
  padding: 4px 10px; border-radius: 6px; font-weight: 700;
  margin-bottom: 14px;
}
.cs-deep h4 {
  font-size: 15px; font-weight: 600; color: #1E2124;
  margin-top: 18px; margin-bottom: 8px;
}
.cs-deep h5 {
  font-size: 13px; font-weight: 600; color: #560303;
  margin-top: 14px; margin-bottom: 6px;
  text-transform: uppercase; letter-spacing: 0.06em;
}
.cs-deep p { font-size: 13.5px; color: #3a3f44; line-height: 1.7; margin-bottom: 10px; }
.cs-deep ul, .cs-deep ol { margin-left: 20px; margin-bottom: 12px; }
.cs-deep li { font-size: 13.5px; color: #3a3f44; margin-bottom: 5px; line-height: 1.55; }
.cs-deep li strong { color: #1E2124; }
.cs-deep table {
  width: 100%; border-collapse: collapse; margin: 10px 0 16px;
  font-size: 12.5px;
}
.cs-deep thead th {
  background: #F7F6F5; padding: 8px 10px; text-align: left; font-weight: 600;
  color: #1E2124; border-bottom: 2px solid rgba(0,0,0,0.08); font-size: 11.5px;
  text-transform: uppercase; letter-spacing: 0.04em;
}
.cs-deep tbody td {
  padding: 8px 10px; border-bottom: 1px solid rgba(0,0,0,0.06);
  color: #3a3f44; vertical-align: top;
}
.cs-deep tbody tr:hover td { background: rgba(251,46,10,0.02); }
.cs-deep .cs-callout {
  background: linear-gradient(135deg, rgba(86,3,3,0.04), rgba(251,46,10,0.03));
  border-left: 3px solid #FB2E0A;
  padding: 14px 18px; border-radius: 8px; margin: 14px 0;
  font-size: 13.5px; color: #1E2124;
}
.cs-deep .cs-callout strong { color: #560303; }
.cs-deep .cs-alert {
  background: rgba(220,38,38,0.04);
  border-left: 3px solid #DC2626;
  padding: 12px 16px; border-radius: 8px; margin: 14px 0;
  font-size: 13px; color: #1E2124;
}
.cs-deep .cs-alert strong { color: #DC2626; }
.cs-deep pre.cs-raw {
  background: #0F1014; color: #D5D7DC; font-family: 'SF Mono', Menlo, monospace;
  font-size: 11px; padding: 16px; border-radius: 8px; overflow-x: auto;
  max-height: 420px; overflow-y: auto; line-height: 1.5;
}
.cs-deep .cs-kv { display: grid; grid-template-columns: 160px 1fr; gap: 8px 16px; margin: 8px 0; }
.cs-deep .cs-kv dt { font-size: 11.5px; color: #909090; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; }
.cs-deep .cs-kv dd { font-size: 13px; color: #1E2124; }

.cs-footer {
  text-align: center; padding: 40px 24px; font-size: 12px; color: #909090;
  border-top: 1px solid rgba(0,0,0,0.06); margin-top: 40px;
}
.cs-footer a { color: #FB2E0A; text-decoration: none; }

/* ===== Botão "Retornar ao topo" — fixed canto inferior direito ===== */
.cs-back-to-top {
  position: fixed;
  bottom: 24px;
  right: 24px;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 6px 18px 6px 6px;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.10);
  border-radius: 999px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.10);
  cursor: pointer;
  font-family: inherit;
  font-size: 13px;
  font-weight: 600;
  color: #1E2124;
  text-decoration: none;
  opacity: 0;
  transform: translateY(20px);
  pointer-events: none;
  transition: opacity .25s ease, transform .25s ease, box-shadow .2s ease, background .2s ease, color .2s ease;
  z-index: 200;
}
.cs-back-to-top--visible {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}
.cs-back-to-top:hover {
  background: linear-gradient(135deg, #560303 0%, #FB2E0A 100%);
  color: #fff;
  border-color: transparent;
  box-shadow: 0 6px 20px rgba(251,46,10,0.32);
}
.cs-back-to-top:active {
  transform: translateY(2px);
}
.cs-back-to-top__icon {
  display: block;
  width: 36px;
  height: 36px;
  flex-shrink: 0;
  border-radius: 50%;
}
.cs-back-to-top__label {
  white-space: nowrap;
  letter-spacing: 0.01em;
}
@media (max-width: 600px) {
  .cs-back-to-top { padding: 6px; }
  .cs-back-to-top__label { display: none; }
}

@media (max-width: 960px) {
  .cs-layout { grid-template-columns: 1fr; }
  .cs-toc {
    position: relative;
    top: 0;
    left: auto;
    width: auto;
    max-height: none;
  }
  .cs-toc__list { max-height: 240px; }
  .cs-skill { padding: 20px; }
  .cs-hero h1 { font-size: 26px; }
}
"""


DRIVER_AND_DEEP_JS = r"""
/* ============================================================================
   Consolidated driver + deep-dive renderers
   ============================================================================ */

// Utilitários do deep-dive (usam helpers globais do portal quando possível).
const CSE = (typeof E === 'function') ? E : function(s){ return s == null ? '' : String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); };
const CSBRL = (typeof BRL === 'function') ? BRL : function(v){ return v == null ? '—' : 'R$ ' + Number(v).toLocaleString('pt-BR', {minimumFractionDigits:2, maximumFractionDigits:2}); };
const CSN = (typeof N === 'function') ? N : function(v){ return v == null ? '—' : Number(v).toLocaleString('pt-BR'); };
const CSPCT = (typeof PCT === 'function') ? PCT : function(v){ return v == null ? '—' : Number(v).toFixed(1).replace('.',',') + '%'; };

function cs_para(label, value) {
  if (value == null || value === '') return '';
  return '<p><strong>' + CSE(label) + ':</strong> ' + CSE(String(value)) + '</p>';
}
function cs_kv(pairs) {
  if (!pairs || !pairs.length) return '';
  let out = '<dl class="cs-kv">';
  pairs.forEach(function(p){
    if (p[1] == null || p[1] === '') return;
    out += '<dt>' + CSE(p[0]) + '</dt><dd>' + CSE(String(p[1])) + '</dd>';
  });
  return out + '</dl>';
}
function cs_list(items, fmt) {
  if (!items || !items.length) return '';
  fmt = fmt || function(x){ return CSE(String(x)); };
  return '<ul>' + items.map(function(i){ return '<li>' + fmt(i) + '</li>'; }).join('') + '</ul>';
}
function cs_table(heads, rows) {
  let out = '<table><thead><tr>';
  heads.forEach(function(h){ out += '<th>' + CSE(h) + '</th>'; });
  out += '</tr></thead><tbody>';
  rows.forEach(function(r){
    out += '<tr>' + r.map(function(c){ return '<td>' + (c == null ? '—' : String(c)) + '</td>'; }).join('') + '</tr>';
  });
  return out + '</tbody></table>';
}
function cs_section(title, html) {
  if (!html) return '';
  return '<h4>' + CSE(title) + '</h4>' + html;
}
function cs_callout(content) {
  return '<div class="cs-callout">' + content + '</div>';
}
function cs_alert(content) {
  return '<div class="cs-alert">' + content + '</div>';
}
function cs_keyInsight(ki) {
  if (!ki) return '';
  if (typeof ki === 'string') return cs_callout('<strong>Insight-chave:</strong> ' + CSE(ki));
  let out = '<strong>' + CSE(ki.headline || 'Insight-chave') + '</strong>';
  if (ki.context) out += '<p style="margin-top:6px">' + CSE(ki.context) + '</p>';
  if (ki.numbered_reasons && ki.numbered_reasons.length) {
    out += '<ol style="margin-top:6px">' + ki.numbered_reasons.map(function(r){
      return '<li>' + CSE(String(r)) + '</li>';
    }).join('') + '</ol>';
  }
  return cs_callout(out);
}
function cs_honestyAlert(ha) {
  if (!ha) return '';
  if (typeof ha === 'string') return cs_alert('<strong>Alerta de honestidade:</strong> ' + CSE(ha));
  let out = '<strong>' + CSE(ha.headline || 'Alerta de honestidade') + '</strong>';
  if (ha.message || ha.context) out += '<p style="margin-top:6px">' + CSE(ha.message || ha.context) + '</p>';
  return cs_alert(out);
}
function cs_rawDump(data) {
  return '<h4>Dump completo do output</h4>' +
         '<p style="font-size:12px;color:#909090">Campos não cobertos pelos renderers específicos — visualize o JSON completo abaixo.</p>' +
         '<pre class="cs-raw">' + CSE(JSON.stringify(data, null, 2)) + '</pre>';
}

// ----------------------------------------------------------------------------
// DEEP: renderers de aprofundamento por skill
// ----------------------------------------------------------------------------
const DEEP = {};

DEEP['ee-s1-diagnostico-maturidade'] = function(d){
  let out = '';
  out += cs_keyInsight(d.key_insight);
  out += cs_honestyAlert(d.honesty_alert);
  if (d.pillar_scores && d.pillar_scores.length) {
    out += cs_section('Pilares detalhados',
      cs_table(['Pilar','Score','Status','Destaque'],
        d.pillar_scores.map(function(p){
          const scoreTxt = p.score != null ? (p.score + '/100' + (p.estimated ? ' [E]' : '')) : '—';
          return [CSE(p.name || p.pillar), scoreTxt,
                  CSE(p.classification || '—'),
                  CSE(p.highlight || p.diagnosis || p.commentary || p.note || '—')];
        })
      ));
  }
  if (d.priorities && d.priorities.length) {
    out += cs_section('Todas as prioridades',
      cs_table(['#','Ação','Impacto','Esforço','Prazo','Justificativa'],
        d.priorities.map(function(p,i){
          return [i+1, CSE(p.action||p.title||'—'),
                  CSE(p.impact||'—'), CSE(p.effort||'—'),
                  CSE(p.timeframe||p.deadline||'—'),
                  CSE(p.rationale||p.justification||'—')];
        })
      ));
  }
  return out;
};

DEEP['ee-s1-swot'] = function(d){
  let out = '';
  out += cs_keyInsight(d.key_insight);
  if (d.tows_matrix) {
    const t = d.tows_matrix;
    out += cs_section('Matriz TOWS completa', '');
    const quads = [
      ['SO — Forças + Oportunidades','so_strategies'],
      ['ST — Forças + Ameaças','st_strategies'],
      ['WO — Fraquezas + Oportunidades','wo_strategies'],
      ['WT — Fraquezas + Ameaças','wt_strategies']
    ];
    quads.forEach(function(q){
      const items = t[q[1]];
      if (items && items.length) {
        out += '<h5>' + CSE(q[0]) + '</h5>';
        out += '<ul>' + items.map(function(i){
          if (typeof i === 'string') return '<li>' + CSE(i) + '</li>';
          let s = '<li><strong>' + CSE(i.strategy||i.title||'—') + '</strong>';
          if (i.rationale||i.justification) s += '<br><span style="color:#606060;font-size:12.5px">' + CSE(i.rationale||i.justification) + '</span>';
          return s + '</li>';
        }).join('') + '</ul>';
      }
    });
  }
  const priActs = d.priority_actions || d.priorities;
  if (priActs && priActs.length) {
    out += cs_section('Ações prioritárias detalhadas',
      cs_table(['#','Ação','Base SWOT','Impacto','Prazo','Track','Investimento','Retorno/mês','Score ajustado'],
        priActs.map(function(a,i){
          const fi = a.financial_impact || {};
          const ras = a.risk_adjusted_score || {};
          return [i+1,
                  CSE(a.action||a.title||'—'),
                  CSE(a.swot_basis||'—'),
                  CSE(a.impact||'—'),
                  CSE(a.suggested_timeline||a.timeframe||'—'),
                  CSE(a.track||'—'),
                  fi.investment_brl != null ? CSBRL(fi.investment_brl) : '—',
                  fi.monthly_return_brl != null ? CSBRL(fi.monthly_return_brl) : '—',
                  ras.score != null ? ras.score : '—'];
        })
      ));
  }
  return out;
};

DEEP['ee-s1-persona-icp'] = function(d){
  let out = '';
  const ob = d.objection_library || d.objections;
  if (ob && ob.objections && ob.objections.length) {
    out += cs_section('Biblioteca completa de objeções',
      cs_table(['Objeção','Subtexto (o que o tutor pensa)','Resposta recomendada','Quando usar'],
        ob.objections.map(function(o){
          return [CSE(o.objection||o.name||'—'),
                  CSE(o.subtext||o.trigger||o.context||'—'),
                  CSE(o.good_response||o.response||o.recommended_response||'—'),
                  CSE(o.when_to_use||o.tone||'—')];
        })
      ));
  }
  const bj = d.buyer_journey;
  if (bj && bj.stages && bj.stages.length) {
    out += cs_section('Jornada de compra — detalhamento por estágio', '');
    bj.stages.forEach(function(s){
      out += '<h5>' + CSE(s.stage||s.name||'Estágio') + '</h5>';
      out += cs_kv([
        ['Gatilho', s.trigger],
        ['Estado mental', s.mental_state||s.behavior],
        ['Canal principal', s.primary_channel||s.main_channel||s.channel],
        ['Pergunta dominante', s.dominant_question||s.dominant_pain||s.pain],
        ['Intervenção do cliente', s.client_intervention||s.ideal_content||s.content],
        ['Fricção atual', s.friction_today],
        ['Duração estimada', s.duration_estimate||s.avg_time||s.duration]
      ]);
    });
  }
  const ap = d.anti_persona;
  if (ap && ap.profiles && ap.profiles.length) {
    out += cs_section('Anti-personas (quem NÃO atender)', '');
    ap.profiles.forEach(function(p){
      out += '<h5>' + CSE(p.label||p.name||p.profile||'—') + '</h5>';
      out += cs_kv([
        ['Quem é', p.who],
        ['Sinais', Array.isArray(p.signals) ? p.signals.join(' · ') : p.signals],
        ['Por que não', p.why_not],
        ['Redirecionar para', p.redirect]
      ]);
    });
  }
  const wtp = d.willingness_to_pay;
  if (wtp && wtp.services && wtp.services.length) {
    out += cs_section('Disposição a pagar — precificação estratégica',
      cs_table(['Serviço','Ticket atual','Faixa percebida justa','Teto premium','Elasticidade','Alavanca de preço'],
        wtp.services.map(function(s){
          return [CSE(s.service||s.name||'—'),
                  CSE(s.current_ticket_range||s.min_price||'—'),
                  CSE(s.perceived_fair_range||s.max_price||'—'),
                  CSE(s.premium_ceiling||s.recommended_price||'—'),
                  CSE(s.elasticity||'—'),
                  CSE(s.pricing_lever||s.rationale||s.justification||'—')];
        })
      ));
    if (wtp.strategic_implication) {
      out += '<div style="margin-top:.75rem;padding:.75rem 1rem;background:#fafafa;border-left:3px solid #909090"><strong>Implicação estratégica:</strong> ' + CSE(wtp.strategic_implication) + '</div>';
    }
  }
  return out || cs_rawDump(d);
};

DEEP['ee-s1-auditoria-comunicacao'] = function(d){
  let out = '';
  out += cs_keyInsight(d.key_insight);
  if (d.gaps_by_channel && d.gaps_by_channel.length) {
    out += cs_section('Todos os gaps por canal',
      cs_table(['Canal','Gap','Alinhamento','Impacto','Esforço','Recomendação'],
        d.gaps_by_channel.map(function(g){
          return [CSE(g.channel||'—'),
                  CSE(g.gap||g.issue||'—'),
                  CSE(String(g.alignment||g.alignment_score||'—')),
                  CSE(g.impact||'—'),
                  CSE(g.effort||'—'),
                  CSE(g.recommendation||'—')];
        })
      ));
  }
  if (d.quick_wins && d.quick_wins.length) {
    out += cs_section('Quick wins priorizados',
      cs_table(['#','Quick win','Canal','Prazo','Impacto esperado'],
        d.quick_wins.map(function(q,i){
          return [i+1, CSE(q.action||q.title||'—'),
                  CSE(q.channel||'—'), CSE(q.timeframe||'—'),
                  CSE(q.expected_impact||q.impact||'—')];
        })
      ));
  }
  return out || cs_rawDump(d);
};

DEEP['ee-s2-pesquisa-mercado'] = function(d){
  let out = '';
  if (d.competitors && d.competitors.length) {
    out += cs_section('Análise profunda por concorrente', '');
    d.competitors.forEach(function(c){
      out += '<h5>' + CSE(c.name||'Concorrente') + '</h5>';
      out += cs_kv([
        ['Posicionamento', c.positioning||c.puv],
        ['Mensagem principal', c.main_message],
        ['Canais de aquisição', Array.isArray(c.acquisition_channels) ? c.acquisition_channels.join(', ') : c.acquisition_channels],
        ['Estimativa de preço/ticket', c.pricing||c.ticket_estimate],
        ['Pontos fortes', Array.isArray(c.strengths) ? c.strengths.join(' · ') : c.strengths],
        ['Pontos fracos', Array.isArray(c.weaknesses) ? c.weaknesses.join(' · ') : c.weaknesses],
        ['Score digital', c.digital_score != null ? c.digital_score + '/10' : '—'],
        ['Anúncios observados', c.ads_observed||c.active_ads]
      ]);
      if (c.commentary || c.analysis) {
        out += '<p style="margin-top:8px;color:#3a3f44;font-size:13px">' + CSE(c.commentary||c.analysis) + '</p>';
      }
    });
  }
  if (d.trends && d.trends.length) {
    out += cs_section('Tendências com evidência',
      '<ul>' + d.trends.map(function(t){
        let s = '<li><strong>' + CSE(t.trend||t.title||'—') + '</strong>';
        if (t.evidence) s += '<br><span style="color:#606060">Evidência: ' + CSE(t.evidence) + '</span>';
        if (t.source) s += '<br><em style="color:#909090;font-size:12px">Fonte: ' + CSE(t.source) + '</em>';
        return s + '</li>';
      }).join('') + '</ul>');
  }
  if (d.unexploited_opportunity) {
    const uo = d.unexploited_opportunity;
    out += cs_section('Oportunidade não explorada',
      cs_callout(
        '<strong>' + CSE(uo.headline||'Oportunidade') + '</strong>' +
        (uo.context ? '<p style="margin-top:6px">' + CSE(uo.context) + '</p>' : '') +
        (uo.why_uncompeted ? '<p style="margin-top:6px"><em>Por que ninguém ataca:</em> ' + CSE(uo.why_uncompeted) + '</p>' : '')
      ));
  }
  if (d.real_differentials) {
    const rd = d.real_differentials;
    if (Array.isArray(rd) && rd.length) {
      out += cs_section('Diferenciais reais (detalhado)',
        '<ul>' + rd.map(function(dif){
          if (typeof dif === 'string') return '<li>' + CSE(dif) + '</li>';
          const body = dif.icp_relevance || dif.rationale || dif.why || dif.description || '';
          const action = dif.action_needed || dif.action_required || '';
          const status = dif.status ? ' <span style="color:#909090;font-size:12px">['+CSE(dif.status)+']</span>' : '';
          return '<li><strong>' + CSE(dif.differential||dif.title||'—') + '</strong>' + status +
                 (body ? '<br><span style="color:#606060">' + CSE(body) + '</span>' : '') +
                 (action ? '<br><em style="color:#909090;font-size:12px">Ação: ' + CSE(action) + '</em>' : '') +
                 '</li>';
        }).join('') + '</ul>');
    } else if (rd && typeof rd === 'object') {
      if (rd.current && rd.current.length) {
        out += '<h5>Já tem hoje</h5><ul>' + rd.current.map(function(x){
          return '<li><strong>' + CSE(x.differential||x.title||'—') + '</strong>' +
                 (x.rationale ? ' — ' + CSE(x.rationale) : '') + '</li>';
        }).join('') + '</ul>';
      }
      if (rd.potential && rd.potential.length) {
        out += '<h5>Poderia ter</h5><ul>' + rd.potential.map(function(x){
          return '<li><strong>' + CSE(x.differential||x.title||'—') + '</strong>' +
                 (x.action_required ? ' — ' + CSE(x.action_required) : '') + '</li>';
        }).join('') + '</ul>';
      }
      if (rd.honesty_alert) out += cs_honestyAlert(rd.honesty_alert);
    }
  }
  return out || cs_rawDump(d);
};

DEEP['ee-s2-posicionamento'] = function(d){
  let out = '';
  const od = d.operator_direction;
  if (od) {
    out += cs_section('Direcionamento do operador',
      cs_kv([
        ['Diferencial mais forte', od.strongest_differential],
        ['Posição desejada', od.desired_position],
        ['Tom desejado', od.desired_tone],
        ['Restrições de posicionamento', Array.isArray(od.positioning_restrictions) ? od.positioning_restrictions.join(' · ') : od.positioning_restrictions]
      ]));
  }
  const puv = d.puv;
  if (puv && typeof puv === 'object') {
    out += cs_section('PUV — detalhamento',
      cs_kv([
        ['Headline', puv.headline||puv.main],
        ['Explicação', puv.explanation||puv.rationale],
        ['Versão curta', puv.short||puv.short_version],
        ['Versão expandida', puv.expanded||puv.long_version],
        ['Para quem', puv.for_whom||puv.target],
        ['Qual problema resolve', puv.problem_solved],
        ['Como diferente', puv.how_different]
      ]));
  }
  const canvas = d.canvas_4p || d.canvas;
  if (canvas && typeof canvas === 'object') {
    out += cs_section('Canvas 4P — justificativas completas', '');
    const pMap = { product:'Produto', price:'Preço', place:'Praça', promotion:'Promoção' };
    Object.keys(pMap).forEach(function(k){
      const p = canvas[k];
      if (!p) return;
      out += '<h5>' + pMap[k] + '</h5>';
      if (typeof p === 'string') { out += '<p>' + CSE(p) + '</p>'; return; }
      const pairs = [];
      Object.keys(p).forEach(function(sk){
        const v = p[sk];
        if (v == null || v === '') return;
        pairs.push([sk.replace(/_/g,' '), Array.isArray(v) ? v.join(' · ') : v]);
      });
      out += cs_kv(pairs);
    });
  }
  if (d.territory_of_brand || d.brand_territory) {
    const t = d.territory_of_brand || d.brand_territory;
    out += cs_section('Território de marca',
      typeof t === 'string' ? '<p>' + CSE(t) + '</p>' :
      cs_kv([
        ['Território', t.territory||t.name],
        ['Arquétipo', t.archetype],
        ['Narrativa', t.narrative||t.story],
        ['Atributos', Array.isArray(t.attributes) ? t.attributes.join(', ') : t.attributes]
      ]));
  }
  return out || cs_rawDump(d);
};

DEEP['ee-s2-diagnostico-midia'] = function(d){
  let out = '';
  // Cada plataforma
  ['google_ads','meta_ads','facebook_ads'].forEach(function(pk){
    const p = d[pk];
    if (!p) return;
    const label = pk === 'google_ads' ? 'Google Ads' : 'Meta Ads';
    out += '<h5>' + label + ' — campanhas completas</h5>';
    if (p.campaigns && p.campaigns.length) {
      out += cs_table(['Campanha','Status','Impressões','Cliques','CTR','Custo','Conversões','CPA/CPL'],
        p.campaigns.map(function(c){
          return [CSE(c.name||'—'), CSE(c.status||'—'),
                  c.impressions != null ? CSN(c.impressions) : '—',
                  c.clicks != null ? CSN(c.clicks) : '—',
                  c.ctr != null ? CSPCT(c.ctr*100) : '—',
                  c.cost != null ? CSBRL(c.cost) : (c.spend != null ? CSBRL(c.spend) : '—'),
                  c.conversions != null ? CSN(c.conversions) : '—',
                  c.cpa != null ? CSBRL(c.cpa) : (c.cpl != null ? CSBRL(c.cpl) : '—')];
        }));
    }
    if (p.monthly_evolution && p.monthly_evolution.length) {
      out += '<h5>Evolução mensal — ' + label + '</h5>';
      out += cs_table(['Mês','Custo','Conversões','CPA','CTR'],
        p.monthly_evolution.map(function(m){
          return [CSE(m.month||m.period||'—'),
                  m.cost != null ? CSBRL(m.cost) : (m.spend != null ? CSBRL(m.spend) : '—'),
                  m.conversions != null ? CSN(m.conversions) : '—',
                  m.cpa != null ? CSBRL(m.cpa) : '—',
                  m.ctr != null ? CSPCT(m.ctr*100) : '—'];
        }));
    }
    if (p.top_keywords && p.top_keywords.length) {
      out += '<h5>Todas as palavras-chave</h5>';
      out += cs_table(['Palavra-chave','Impressões','Cliques','CTR','CPC','Conv.','Veredicto'],
        p.top_keywords.map(function(k){
          return [CSE(k.keyword||'—'),
                  k.impressions != null ? CSN(k.impressions) : '—',
                  k.clicks != null ? CSN(k.clicks) : '—',
                  k.ctr != null ? CSPCT(k.ctr*100) : '—',
                  k.cpc != null ? CSBRL(k.cpc) : '—',
                  k.conversions != null ? CSN(k.conversions) : '—',
                  CSE(k.verdict||'—')];
        }));
    }
  });
  if (d.insights_cross_platform || d.cross_platform_insights) {
    out += cs_section('Insights cross-platform',
      cs_list(d.insights_cross_platform||d.cross_platform_insights));
  }
  return out || cs_rawDump(d);
};

DEEP['ee-s2-diagnostico-organico-ig'] = function(d){
  let out = '';
  if (d.posts_analyzed && d.posts_analyzed.length) {
    out += cs_section('Posts analisados em detalhe',
      cs_table(['Data','Formato','Tema','Curtidas','Comentários','Salvos','Alcance','Engajamento'],
        d.posts_analyzed.map(function(p){
          return [CSE(p.date||'—'), CSE(p.format||p.type||'—'),
                  CSE(p.theme||p.topic||'—'),
                  p.likes != null ? CSN(p.likes) : '—',
                  p.comments != null ? CSN(p.comments) : '—',
                  p.saves != null ? CSN(p.saves) : '—',
                  p.reach != null ? CSN(p.reach) : '—',
                  p.engagement_rate != null ? CSPCT(p.engagement_rate*100) : '—'];
        })
      ));
  }
  if (d.format_performance) {
    out += cs_section('Performance por formato',
      cs_kv(Object.keys(d.format_performance).map(function(k){
        const v = d.format_performance[k];
        return [k, typeof v === 'object' ? JSON.stringify(v) : v];
      })));
  }
  if (d.engagement_benchmark && d.engagement_benchmark.by_account) {
    const byAcc = d.engagement_benchmark.by_account;
    const hasNote = byAcc.some(a => a.note);
    const headers = hasNote
      ? ['Conta','Likes méd.','Comentários méd.','Engajamento proxy','Melhor formato','Observação']
      : ['Conta','Likes méd.','Comentários méd.','Engajamento proxy','Melhor formato'];
    out += cs_section('Benchmark de engajamento — todas as contas',
      cs_table(headers,
        byAcc.map(function(a){
          const row = [CSE(a.username||a.handle||'—'),
                  a.avg_likes != null ? a.avg_likes.toFixed(1) : '—',
                  a.avg_comments != null ? a.avg_comments.toFixed(1) : '—',
                  a.avg_engagement_proxy != null ? CSPCT(a.avg_engagement_proxy) : '—',
                  CSE(a.best_format_by_engagement||'—')];
          if (hasNote) row.push(CSE(a.note||'—'));
          return row;
        })
      ) + (d.engagement_benchmark.insight ? '<div style="margin-top:.75rem;padding:.75rem 1rem;background:#fafafa;border-left:3px solid #909090"><em>' + CSE(d.engagement_benchmark.insight) + '</em></div>' : ''));
  }
  if (d.content_recommendations && d.content_recommendations.length) {
    out += cs_section('Recomendações de conteúdo',
      '<ul>' + d.content_recommendations.map(function(r){
        if (typeof r === 'string') return '<li>' + CSE(r) + '</li>';
        return '<li><strong>' + CSE(r.title||r.theme||'—') + '</strong>' +
               (r.description ? '<br>' + CSE(r.description) : '') + '</li>';
      }).join('') + '</ul>');
  }
  return out || cs_rawDump(d);
};

DEEP['ee-s2-diagnostico-cro'] = function(d){
  let out = '';
  if (d.technical_audit && d.technical_audit.pagespeed) {
    const ps = d.technical_audit.pagespeed;
    const scoreLabels = {performance:'Performance', accessibility:'Acessibilidade', best_practices:'Boas práticas', seo:'SEO'};
    const cwvLabels = {
      lcp_ms:['LCP (Largest Contentful Paint)','ms'],
      fcp_ms:['FCP (First Contentful Paint)','ms'],
      tbt_ms:['TBT (Total Blocking Time)','ms'],
      cls:['CLS (Cumulative Layout Shift)',''],
      speed_index_ms:['Speed Index','ms'],
      tti_ms:['TTI (Time to Interactive)','ms'],
      ttfb_ms:['TTFB (Time to First Byte)','ms']
    };
    const fmtScore = v => v == null ? '—' : Math.round(v) + '/100';
    const fmtCwv = (k,v) => {
      if (v == null) return '—';
      const lbl = cwvLabels[k];
      if (!lbl) return v;
      const unit = lbl[1];
      if (unit === 'ms') return Math.round(v).toLocaleString('pt-BR') + ' ms';
      if (k === 'cls') return Number(v).toFixed(3);
      return v;
    };
    out += cs_section('PageSpeed — resultados completos', '');
    if (ps.mobile_scores) {
      out += '<h5>Mobile</h5>' +
        cs_kv(Object.keys(ps.mobile_scores).map(function(k){ return [scoreLabels[k]||k, fmtScore(ps.mobile_scores[k])]; }));
    }
    if (ps.desktop_scores) {
      out += '<h5>Desktop</h5>' +
        cs_kv(Object.keys(ps.desktop_scores).map(function(k){ return [scoreLabels[k]||k, fmtScore(ps.desktop_scores[k])]; }));
    }
    if (ps.mobile_cwv_lab || ps.cwv) {
      const cwv = ps.mobile_cwv_lab || ps.cwv;
      out += '<h5>Core Web Vitals (mobile lab)</h5>' +
        cs_kv(Object.keys(cwv).map(function(k){ return [cwvLabels[k] ? cwvLabels[k][0] : k, fmtCwv(k, cwv[k])]; }));
    }
    if (ps.critical_issues && ps.critical_issues.length) {
      out += '<h5>Problemas críticos</h5>' + cs_list(ps.critical_issues);
    }
  }
  if (d.copy_audit && d.copy_audit.above_fold) {
    const af = d.copy_audit.above_fold;
    out += cs_section('Above the fold — auditoria',
      cs_kv([
        ['Headline atual', af.current_headline],
        ['Headline sugerida', af.suggested_headline],
        ['CTA atual', af.current_cta],
        ['CTA sugerido', af.suggested_cta],
        ['Detalhe da proposta de valor', af.value_prop_detail],
        ['O que visitante do ICP pensa', af.icp_visitor_thought||af.first_impression]
      ]));
  }
  if (d.copy_audit && d.copy_audit.section_by_section) {
    out += cs_section('Estrutura da página — seção por seção',
      cs_table(['Seção','Existe?','Score','Problema principal','Recomendação'],
        d.copy_audit.section_by_section.map(function(s){
          return [CSE(s.section||s.name||'—'),
                  s.exists === true ? 'Sim' : (s.exists === false ? 'Não' : '—'),
                  s.score != null ? s.score + '/5' : '—',
                  CSE(s.main_problem||s.issue||'—'),
                  CSE(s.recommendation||'—')];
        })
      ));
  }
  if (d.trust_analysis) {
    const ta = d.trust_analysis;
    out += cs_section('Análise de confiança',
      cs_kv([
        ['Score de confiança', ta.trust_score != null ? ta.trust_score + '/10' : '—'],
        ['Maior gap', ta.biggest_trust_gap||ta.biggest_gap]
      ]));
    if (ta.signals_checklist) {
      out += '<h5>Checklist de sinais de confiança</h5>';
      out += cs_table(['Sinal','Status','Observação'],
        Object.keys(ta.signals_checklist).map(function(k){
          const v = ta.signals_checklist[k];
          if (typeof v === 'object' && v !== null) return [CSE(k), v.present ? '✓' : '✗', CSE(v.note||'—')];
          return [CSE(k), v ? '✓' : '✗', '—'];
        }));
    }
  }
  if (d.hypotheses && d.hypotheses.length) {
    out += cs_section('Todas as hipóteses de teste',
      cs_table(['#','Hipótese','Elemento','Impacto','Dificuldade','Prioridade'],
        d.hypotheses.map(function(h,i){
          return [i+1, CSE(h.hypothesis||h.title||'—'),
                  CSE(h.element||'—'),
                  CSE(h.impact||'—'), CSE(h.difficulty||h.effort||'—'),
                  CSE(h.priority||'—')];
        })
      ));
  }
  if (d.wireframe && d.wireframe.sections) {
    out += cs_section('Wireframe detalhado', '');
    d.wireframe.sections.forEach(function(s){
      out += '<h5>' + CSE(s.section||s.name||'Seção') + '</h5>';
      out += cs_kv([
        ['Conteúdo', s.content],
        ['Copy sugerida', s.copy||s.suggested_copy],
        ['Formato', s.format]
      ]);
    });
  }
  return out || cs_rawDump(d);
};

DEEP['ee-s2-diagnostico-criativos'] = function(d){
  let out = '';
  if (d.summary_highlights && d.summary_highlights.length) {
    out += cs_section('Destaques',
      '<div class="gr gr--3" style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.75rem">' +
      d.summary_highlights.map(function(h){
        const color = h.tone==='red'?'#b00020':h.tone==='yellow'?'#a87a00':h.tone==='green'?'#1f7a3a':'#333';
        return '<div style="padding:.75rem;border-left:3px solid '+color+';background:#fafafa">' +
               '<div style="font-size:11px;color:#909090;text-transform:uppercase;letter-spacing:.5px">' + CSE(h.category||'') + '</div>' +
               '<div style="font-weight:600;margin:.25rem 0">' + CSE(h.label||'—') + '</div>' +
               '<div style="font-size:20px;font-weight:700;color:'+color+'">' + CSE(h.value||'—') + '</div>' +
               (h.subtext ? '<div style="font-size:12px;color:#606060;margin-top:.25rem">' + CSE(h.subtext) + '</div>' : '') +
               '</div>';
      }).join('') + '</div>');
  }
  if (d.summary_key_findings && d.summary_key_findings.length) {
    out += cs_section('Principais achados',
      '<ul>' + d.summary_key_findings.map(function(f){
        const tag = f.category ? '<span style="display:inline-block;padding:.1rem .5rem;background:#eaeaea;border-radius:3px;font-size:11px;margin-right:.5rem;text-transform:uppercase">'+CSE(f.category)+'</span>' : '';
        return '<li style="margin-bottom:.5rem">' + tag + CSE(f.text||'—') + '</li>';
      }).join('') + '</ul>');
  }
  if (d.counts) {
    const c = d.counts;
    out += cs_section('Veredito dos criativos',
      cs_kv([
        ['Total analisado', d.total_creatives_analyzed],
        ['Score médio', d.average_score != null ? d.average_score + ' / 25' : '—'],
        ['Manter', c.keep_count],
        ['Otimizar', c.optimize_count],
        ['Eliminar', c.eliminate_count]
      ]));
  }
  if (d.creative_matrix && d.creative_matrix.length) {
    out += cs_section('Matriz de criativos — scores por dimensão',
      cs_table(['#','Tipo','Descrição','Hook','Clareza','ICP','CTA','Total'],
        d.creative_matrix.map(function(c){
          const total = (c.hook_score||0)+(c.clarity_score||0)+(c.icp_coherence_score||0)+(c.cta_score||0)+(c.production_score||0);
          return [c.number||'—', CSE(c.type||'—'), CSE(c.description||'—'),
                  c.hook_score!=null?c.hook_score:'—',
                  c.clarity_score!=null?c.clarity_score:'—',
                  c.icp_coherence_score!=null?c.icp_coherence_score:'—',
                  c.cta_score!=null?c.cta_score:'—',
                  total||'—'];
        })
      ));
  }
  if (d.patterns_identified && d.patterns_identified.length) {
    out += cs_section('Padrões identificados',
      '<ul>' + d.patterns_identified.map(function(p){
        const aff = (p.affected_creatives||[]).join(', ');
        return '<li><strong>' + CSE(p.pattern||'—') + '</strong>' +
               (aff ? ' <span style="color:#909090">(criativos: '+CSE(aff)+')</span>' : '') +
               (p.example ? '<br><span style="color:#606060;font-size:12.5px">' + CSE(p.example) + '</span>' : '') +
               '</li>';
      }).join('') + '</ul>');
  }
  if (d.what_works && d.what_works.length) {
    out += cs_section('O que já funciona',
      '<ul>' + d.what_works.map(function(w){
        return '<li><strong>' + CSE(w.element||'—') + '</strong>' +
               (w.reason ? '<br><span style="color:#606060;font-size:12.5px">' + CSE(w.reason) + '</span>' : '') +
               '</li>';
      }).join('') + '</ul>');
  }
  if (d.competitor_patterns_missing && d.competitor_patterns_missing.length) {
    out += cs_section('Padrões de concorrência não explorados',
      '<ul>' + d.competitor_patterns_missing.map(function(p){
        return '<li><strong>' + CSE(p.pattern||'—') + '</strong>' +
               (p.why_it_works ? '<br><span style="color:#606060;font-size:12.5px"><em>Por que funciona:</em> ' + CSE(p.why_it_works) + '</span>' : '') +
               (p.how_client_could_implement ? '<br><span style="color:#606060;font-size:12.5px"><em>Como implementar:</em> ' + CSE(p.how_client_could_implement) + '</span>' : '') +
               '</li>';
      }).join('') + '</ul>');
  }
  if (d.production_briefing) {
    const pb = d.production_briefing;
    out += cs_section('Briefing de produção', '');
    if (pb.hook_direction) out += '<p><strong>Direção de hook:</strong> ' + CSE(pb.hook_direction) + '</p>';
    if (pb.hook_examples && pb.hook_examples.length) {
      out += '<p><strong>Exemplos de hook:</strong></p><ul>' + pb.hook_examples.map(h => '<li>' + CSE(h) + '</li>').join('') + '</ul>';
    }
    const others = ['cta_direction','visual_direction','copy_direction','format_mix'];
    others.forEach(function(k){
      if (pb[k]) out += '<p><strong>' + k.replace(/_/g,' ').replace(/^./,c=>c.toUpperCase()) + ':</strong> ' + CSE(pb[k]) + '</p>';
    });
  }
  if (d.key_insight) {
    const ki = d.key_insight;
    out += cs_section('Insight estratégico',
      cs_callout(
        (ki.headline ? '<strong>' + CSE(ki.headline) + '</strong>' : '') +
        (ki.context ? '<p style="margin-top:.5rem">' + CSE(ki.context) + '</p>' : '') +
        (ki.numbered_reasons && ki.numbered_reasons.length ? '<ol>' + ki.numbered_reasons.map(r => '<li>' + CSE(r) + '</li>').join('') + '</ol>' : '')
      ));
  }
  if (d.honesty_alert) {
    out += cs_honestyAlert(d.honesty_alert);
  }
  return out || cs_rawDump(d);
};

// Fallback para skills sem DEEP renderer específico
function DEEP_fallback(d) {
  return cs_rawDump(d);
}

// ----------------------------------------------------------------------------
// Driver
// ----------------------------------------------------------------------------
(function(){
  document.addEventListener('DOMContentLoaded', function(){
    document.body.classList.add('consolidated');

    const data = PORTAL_DATA;
    if (!data || !data.client) {
      document.getElementById('cs-main').innerHTML =
        '<div class="cs-skill"><p class="cs-skill__pending">Nenhum dado disponível. Execute render_portal.sh primeiro.</p></div>';
      return;
    }

    const client = data.client;
    const progress = data.progress || {};
    const outputs = data.outputs || {};
    const hasSales = client.modelo_venda ? true : (client.modulo_vendas !== false);
    const escopoVendas = Array.isArray(client.modulo_vendas_escopo) ? client.modulo_vendas_escopo : null;

    document.title = 'Visão Consolidada — ' + (client.name || 'Cliente');
    const hN = document.getElementById('cs-client-name');
    if (hN) hN.textContent = client.name || 'Cliente';

    const activeWeeks = WEEKS
      .map(function(w){ return (w.sales && escopoVendas) ? Object.assign({}, w, { skills: w.skills.filter(function(s){ return escopoVendas.indexOf(s.id) !== -1; }) }) : w; })
      .filter(function(w){ return (!w.sales || hasSales) && w.skills.length > 0; });

    // Lista flat de skills completadas (ignora pendentes no documento consolidado)
    const completedSkills = [];
    activeWeeks.forEach(function(w){
      w.skills.forEach(function(sk){
        const status = (progress.skills && progress.skills[sk.id] && progress.skills[sk.id].status) || 'pending';
        if (status === 'completed' && outputs[sk.id]) {
          completedSkills.push({ id: sk.id, name: sk.name, data: outputs[sk.id] });
        }
      });
    });

    // TOC flat — apenas título de cada seção + search box com sugestões
    const tocEl = document.getElementById('cs-toc');
    if (tocEl) {
      // Mapeamento skill → semana para mostrar contexto na sugestão
      const skillToWeek = {};
      activeWeeks.forEach(function(w){
        w.skills.forEach(function(sk){
          skillToWeek[sk.id] = { n: w.n, title: w.title };
        });
      });

      let tocHtml = ''
        + '<div class="cs-toc__title">Sumário</div>'
        + '<div class="cs-search" id="cs-search">'
        +   '<div class="cs-search__input-wrap">'
        +     '<svg class="cs-search__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round">'
        +       '<circle cx="7" cy="7" r="5"/><line x1="11" y1="11" x2="14" y2="14"/>'
        +     '</svg>'
        +     '<input type="text" class="cs-search__input" id="cs-search-input" '
        +       'placeholder="Buscar tópico…" autocomplete="off" spellcheck="false" '
        +       'aria-label="Buscar tópicos no sumário" />'
        +     '<button type="button" class="cs-search__clear" id="cs-search-clear" aria-label="Limpar busca">×</button>'
        +   '</div>'
        +   '<div class="cs-search__suggest" id="cs-search-suggest" role="listbox"></div>'
        + '</div>'
        + '<div class="cs-toc__list" id="cs-toc-list">';
      completedSkills.forEach(function(sk){
        tocHtml += '<a href="#' + sk.id + '">' + CSE(sk.name) + '</a>';
      });
      tocHtml += '</div>';
      tocEl.innerHTML = tocHtml;

      // ===== Search box: sugestões + navegação =====
      const searchEl = document.getElementById('cs-search');
      const inputEl = document.getElementById('cs-search-input');
      const clearEl = document.getElementById('cs-search-clear');
      const suggestEl = document.getElementById('cs-search-suggest');

      // Highlight matches no nome da skill
      function escRe(s){ return s.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&'); }
      function highlight(text, query){
        if (!query) return CSE(text);
        const re = new RegExp('(' + escRe(query) + ')', 'gi');
        // CSE primeiro, depois substitui — pra evitar que o <mark> vire &lt;mark&gt;
        const safe = CSE(text);
        return safe.replace(re, '<mark>$1</mark>');
      }

      // Filtro: por substring case-insensitive (com normalização de acentos)
      function norm(s){
        return String(s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();
      }
      function filterSuggestions(query){
        const q = norm(query.trim());
        if (!q) return completedSkills.slice(0, 30);
        return completedSkills.filter(function(sk){
          return norm(sk.name).indexOf(q) !== -1 || norm(sk.id).indexOf(q) !== -1;
        });
      }

      let focusedIdx = -1;
      let currentItems = [];

      function renderSuggestions(query){
        currentItems = filterSuggestions(query);
        focusedIdx = currentItems.length > 0 ? 0 : -1;
        if (currentItems.length === 0) {
          suggestEl.innerHTML = '<div class="cs-search__empty">Nenhum tópico encontrado</div>';
          return;
        }
        let html = '';
        const groupLabel = query.trim() ? 'Resultados' : 'Sugestões — todos os tópicos';
        html += '<div class="cs-search__group">' + groupLabel + ' (' + currentItems.length + ')</div>';
        currentItems.forEach(function(sk, i){
          const w = skillToWeek[sk.id];
          const meta = w ? ('Semana ' + w.n + ' · ' + CSE(w.title)) : '';
          html += '<a class="cs-search__item' + (i === focusedIdx ? ' cs-search__item--focused' : '') + '" '
            + 'href="#' + sk.id + '" data-idx="' + i + '" role="option">'
            +   highlight(sk.name, query.trim())
            + (meta ? '<span class="cs-search__item-meta">' + meta + '</span>' : '')
            + '</a>';
        });
        suggestEl.innerHTML = html;
      }

      function openSuggest(){
        searchEl.classList.add('cs-search--open');
        renderSuggestions(inputEl.value || '');
      }
      function closeSuggest(){
        searchEl.classList.remove('cs-search--open');
        focusedIdx = -1;
      }
      function navigateTo(skillId){
        const target = document.getElementById(skillId);
        if (!target) return;
        // Update hash sem disparar scroll nativo
        if (history && history.pushState) {
          history.pushState(null, '', '#' + skillId);
        } else {
          window.location.hash = '#' + skillId;
        }
        const top = target.getBoundingClientRect().top + window.scrollY - 12;
        window.scrollTo({ top: top, behavior: 'smooth' });
        closeSuggest();
        inputEl.blur();
      }

      // Eventos
      inputEl.addEventListener('focus', openSuggest);
      inputEl.addEventListener('click', openSuggest);
      inputEl.addEventListener('input', function(){
        const v = inputEl.value;
        searchEl.classList.toggle('cs-search--has-value', v.length > 0);
        renderSuggestions(v);
        searchEl.classList.add('cs-search--open');
      });
      inputEl.addEventListener('keydown', function(e){
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          if (currentItems.length === 0) return;
          focusedIdx = (focusedIdx + 1) % currentItems.length;
          updateFocus();
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (currentItems.length === 0) return;
          focusedIdx = (focusedIdx - 1 + currentItems.length) % currentItems.length;
          updateFocus();
        } else if (e.key === 'Enter') {
          e.preventDefault();
          if (focusedIdx >= 0 && currentItems[focusedIdx]) {
            navigateTo(currentItems[focusedIdx].id);
          }
        } else if (e.key === 'Escape') {
          e.preventDefault();
          closeSuggest();
          inputEl.blur();
        }
      });
      function updateFocus(){
        const items = suggestEl.querySelectorAll('.cs-search__item');
        items.forEach(function(it, i){
          it.classList.toggle('cs-search__item--focused', i === focusedIdx);
          if (i === focusedIdx) it.scrollIntoView({ block: 'nearest' });
        });
      }
      // Click numa sugestão
      suggestEl.addEventListener('click', function(e){
        const a = e.target.closest('.cs-search__item');
        if (!a) return;
        e.preventDefault();
        const idx = parseInt(a.getAttribute('data-idx'), 10);
        if (currentItems[idx]) navigateTo(currentItems[idx].id);
      });
      // Botão limpar
      clearEl.addEventListener('click', function(){
        inputEl.value = '';
        searchEl.classList.remove('cs-search--has-value');
        renderSuggestions('');
        inputEl.focus();
      });
      // Fecha ao clicar fora
      document.addEventListener('click', function(e){
        if (!searchEl.contains(e.target)) closeSuggest();
      });
      // Atalho de teclado: "/" foca a busca (estilo GitHub/Linear)
      document.addEventListener('keydown', function(e){
        if (e.key === '/' && document.activeElement !== inputEl &&
            !['INPUT','TEXTAREA','SELECT'].includes(document.activeElement?.tagName)) {
          e.preventDefault();
          inputEl.focus();
        }
      });
    }

    // Main: documento único fluido (sem cards/boxes por entrega)
    const mainEl = document.getElementById('cs-main');
    const parts = [];

    completedSkills.forEach(function(sk){
      parts.push('<section class="cs-skill" id="' + sk.id + '">');
      parts.push('<header class="cs-skill__h"><h2>' + CSE(sk.name) + '</h2></header>');

      // Executive render (reutiliza renderer do portal)
      parts.push('<div class="cs-exec">');
      if (R[sk.id]) {
        try { parts.push(R[sk.id](sk.data)); }
        catch(e) { parts.push('<div class="cs-skill__error">Erro na renderização executiva: ' + CSE(e.message) + '</div>'); }
      } else {
        parts.push('<p style="color:#909090;font-size:13px">Renderer executivo não disponível para esta skill.</p>');
      }
      parts.push('</div>');

      // Aprofundamento removido — entrega consolidada usa apenas a renderização executiva.
      parts.push('</section>');
    });

    if (completedSkills.length === 0) {
      parts.push('<p class="cs-skill__pending">Nenhuma entrega finalizada ainda.</p>');
    }

    mainEl.innerHTML = parts.join('');

    // ===== Sidebar híbrida: relative dentro do grid quando hero visível,
    //       fixed na viewport quando hero rolou pra fora =====
    const heroEl = document.querySelector('.cs-hero');
    function updateTocFixed(){
      if (!heroEl || !tocEl) return;
      const heroBottom = heroEl.getBoundingClientRect().bottom;
      // Quando o hero saiu (ou está quase saindo) pelo topo, fixa a barra
      const shouldFix = heroBottom < 20;
      tocEl.classList.toggle('cs-toc--fixed', shouldFix);
    }
    window.addEventListener('scroll', updateTocFixed, { passive: true });
    window.addEventListener('resize', updateTocFixed, { passive: true });
    updateTocFixed();

    // ===== Botão "Retornar ao topo": aparece quando passou da 1ª seção =====
    const backToTopEl = document.getElementById('cs-back-to-top');
    if (backToTopEl) {
      backToTopEl.addEventListener('click', function(e){
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        // Limpa o hash sem disparar scroll
        if (history && history.pushState) {
          history.pushState(null, '', window.location.pathname + window.location.search);
        }
      });

      function updateBackToTop(){
        const firstSection = document.querySelector('.cs-skill');
        if (!firstSection) {
          // Sem seções renderizadas — usa altura da viewport como threshold
          backToTopEl.classList.toggle('cs-back-to-top--visible', window.scrollY > window.innerHeight);
          return;
        }
        // Visível quando o final da primeira seção passou pela borda superior
        const rect = firstSection.getBoundingClientRect();
        backToTopEl.classList.toggle('cs-back-to-top--visible', rect.bottom < 0);
      }
      window.addEventListener('scroll', updateBackToTop, { passive: true });
      window.addEventListener('resize', updateBackToTop, { passive: true });
      // Roda após o conteúdo ser injetado no main (próximo tick do event loop)
      setTimeout(updateBackToTop, 0);
    }

    // TOC active state on scroll — apenas links da lista principal (não do dropdown de busca)
    const tocListEl = document.getElementById('cs-toc-list');
    const links = tocListEl ? tocListEl.querySelectorAll('a') : [];
    const sections = document.querySelectorAll('.cs-skill');
    function updateActive(){
      let active = null;
      sections.forEach(function(s){
        const r = s.getBoundingClientRect();
        if (r.top < 120) active = s.id;
      });
      links.forEach(function(l){
        const isActive = l.getAttribute('href') === '#' + active;
        l.classList.toggle('active', isActive);
        if (isActive && tocListEl) {
          // Scroll no sumário para manter o item ativo visível
          const lr = l.getBoundingClientRect();
          const cr = tocListEl.getBoundingClientRect();
          if (lr.top < cr.top || lr.bottom > cr.bottom) {
            l.scrollIntoView({ block: 'nearest' });
          }
        }
      });
    }
    window.addEventListener('scroll', updateActive, { passive: true });
    updateActive();
  });
})();
"""


def _extract_portal_assets():
    """Lê portal.html e extrai o bloco <style>, o script principal (PORTAL_DATA) e as tags de favicon."""
    with open(PORTAL_TEMPLATE_PATH, encoding="utf-8") as f:
        portal = f.read()

    # Extract CSS
    css_match = re.search(r"<style>(.*?)</style>", portal, re.DOTALL)
    css_block = css_match.group(1) if css_match else ""

    # Extract favicon tags (logo V4 base64) — pega <link rel="icon"> e <link rel="apple-touch-icon">
    favicon_tags = re.findall(
        r'<link\s+rel="(?:icon|apple-touch-icon|shortcut icon)"[^>]*>',
        portal,
        re.IGNORECASE,
    )
    favicon_block = "\n  ".join(favicon_tags)

    # Encontra o <script> que contém PORTAL_DATA (ignora o pre-gate script inline de ~13 linhas)
    script_blocks = re.findall(r"<script>(.*?)</script>", portal, re.DOTALL)
    main_script = ""
    for blk in script_blocks:
        if "PORTAL_DATA" in blk and "const WEEKS" in blk:
            main_script = blk
            break

    if not main_script:
        raise RuntimeError("Não foi possível localizar o bloco <script> principal do portal.")

    # Neutraliza o bootstrap (init do portal tradicional) — driver novo assume o DOMContentLoaded
    main_script = re.sub(
        r"document\.addEventListener\(\s*['\"]DOMContentLoaded['\"]\s*,\s*init\s*\)\s*;",
        "/* portal init skipped in consolidated mode */",
        main_script,
    )

    return css_block, main_script, favicon_block


BACK_TO_TOP_SVG = '<svg class="cs-back-to-top__icon" width="36" height="36" viewBox="0 0 256 256" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><rect width="256" height="256" rx="128" fill="url(#pattern0_35_2)"/><defs><pattern id="pattern0_35_2" patternContentUnits="objectBoundingBox" width="1" height="1"><use xlink:href="#image0_35_2" transform="scale(0.00390625)"/></pattern><image id="image0_35_2" width="256" height="256" preserveAspectRatio="none" xlink:href="data:image/png;base64,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"/></defs></svg>'


def build_consolidated_html(client, outputs, ident, generated_at, current_week):
    """Gera consolidated.html herdando CSS + renderers executivos do portal.html (sem aprofundamento)."""
    portal_css, portal_js, favicon_block = _extract_portal_assets()

    # Monta PORTAL_DATA como o portal faz
    portal_data = {
        "client": client.get("meta", {}),
        "progress": client.get("progress", {}),
        "outputs": outputs,
        "briefing": client.get("briefing", {}),
    }
    data_json = json.dumps(portal_data, ensure_ascii=False, separators=(",", ":"))

    # Substitui o marcador de dados no script do portal
    portal_js = portal_js.replace("/*%%DATA%%*/ {}", data_json)

    client_name = ident.get("name", "Cliente")
    client_name_html = re.sub(r"[<>&\"]", "", client_name)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visão Consolidada — {client_name_html}</title>
  {favicon_block}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <style>
{portal_css}
{LINEAR_LAYOUT_CSS}
  </style>
</head>
<body>
  <header class="cs-hero">
    <div class="cs-hero__eyebrow">V4 Company · Estruturação Estratégica</div>
    <h1 id="cs-client-name">{client_name_html}</h1>
    <div class="cs-hero__meta">Visão Consolidada · Gerado em {generated_at} · Semana atual: {current_week}</div>
    <div class="cs-hero__note">Este documento reúne tudo que foi produzido para o cliente — todas as entregas em uma só visualização, para entrega e auditabilidade.</div>
  </header>

  <div class="cs-layout">
    <aside class="cs-toc" id="cs-toc"></aside>
    <main class="cs-main" id="cs-main"></main>
  </div>

  <footer class="cs-footer">
    Documento gerado a partir de <code>client.json</code> + <code>outputs/*.json</code>
  </footer>

  <a href="#" id="cs-back-to-top" class="cs-back-to-top" aria-label="Retornar ao topo" title="Retornar ao topo">
    {BACK_TO_TOP_SVG}
    <span class="cs-back-to-top__label">Retornar ao topo</span>
  </a>

<script>
{portal_js}
</script>
<script>
{DRIVER_AND_DEEP_JS}
</script>
</body>
</html>
"""
    return html


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 render_consolidated.py <path_cliente>")
        sys.exit(1)
    render(sys.argv[1])
