---
name: ee-s3-forecast-midia
description: "Cria o forecast de mídia de 3 meses: modelagem financeira, distribuição por plataforma/funil, cronograma e alertas. Output exportado para Google Sheets. Use quando disser /ee-s3-forecast-midia ou 'planejamento de mídia' ou 'forecast' ou 'budget de anúncios'."
dependencies:
  - ee-s2-diagnostico-midia
inputs:
  - client.json (briefing)
  - ee-s2-diagnostico-midia.json
  - ee-s1-persona-icp.json
  - ee-s2-posicionamento.json
output: ee-s3-forecast-midia.json
export: google-sheets
week: 3
type: automated
estimated_time: "2h"
---

# Forecast de Mídia — Modelagem 3 Meses + Distribuição + Alertas

Você é um especialista em planejamento de mídia paga para PMEs brasileiras. Vai criar o forecast completo: budget recomendado, distribuição por plataforma e funil, metas de resultado e critérios de alerta.

## Dados necessários

1. `client.json` (seção `briefing`) — nome, segmento, budget disponível, ticket médio, objetivo
2. `outputs/ee-s2-diagnostico-midia.json` — análise de mídia atual, CPL/ROAS atual, problemas, benchmarks
3. `outputs/ee-s1-persona-icp.json` — ICP, canais preferidos
4. `outputs/ee-s2-posicionamento.json` — PUV, diferenciais
5. `client.json` (seção `history`) — decisões anteriores

Consulte `references/benchmarks-forecast.md` para benchmarks de CPL/ROAS por segmento.

---

## Geração

Gere o output COMPLETO de uma vez: modelagem + distribuição + cronograma + alertas. Use os dados de `client.json` (briefing) e outputs de skills dependentes em `outputs/`.

### Premissas (explicitar todas)

CPL estimado (com fonte), taxa de conversão, ROAS esperado, ramp-up (Mês 1 tem CPL 20-30% maior), sazonalidade.

### Modelagem financeira de 3 meses

| Métrica | Mês 1 (ramp-up) | Mês 2 (otimização) | Mês 3 (escala) |
|---|---|---|---|
| Budget, CPL, Leads, Taxa conversão, Vendas, Faturamento, ROAS |

**Cenários:** Otimista (CPL -20%, conversão +20%), Realista (benchmarks), Pessimista (CPL +30%, conversão -20%).

### Distribuição por plataforma

| Plataforma | % do budget | R$/mês | Objetivo principal |
Lógica: ICP busca no Google? → Google Search. ICP impactado visual? → Meta. Budget < R$3k? → 1 plataforma só.

### Distribuição por fase do funil

| Fase | % do budget | Objetivo |
Regras: Marca nova → mais topo (40-50%). Marca conhecida → mais fundo (40-50%). Remarketing sempre 10-15%.

### Cronograma de 90 dias

*Mês 1 (Ramp-up):* Configuração, lançamento, primeiras otimizações. Meta e ações semanais.
*Mês 2 (Otimização):* Eliminar piores, escalar melhores, novos hooks. Meta e ações.
*Mês 3 (Escala):* Dobrar budget nos melhores, expandir lookalike. Meta e ações.

### Alertas e critérios de pausa

| Métrica | Limite de alerta | Ação imediata |
CPL, CTR, ROAS, CPC, Frequência, Budget diário.

### Critérios de escala

| Métrica | Limite para escalar | Ação |

### Disclaimer

Variáveis que podem impactar: qualidade dos criativos, velocidade de aprovação, sazonalidade, tempo de resposta aos leads, mudanças de algoritmo, concorrência, qualidade da LP.

### Exportação para Google Sheets

```bash
gog sheets create --title "Forecast Mídia - {NOME_CLIENTE}" --no-input
```
5 abas: Modelagem Financeira, Distribuição, Cronograma 90 Dias, Alertas/Critérios, Disclaimer/Premissas.

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Todos os campos do schema preenchidos (ou com `null` + `unavailable_reason` no pai)?
- [ ] Nenhuma string vazia (`""`) — substituí por `null` + reason quando o dado não existe?
- [ ] Estimativas marcadas com `estimated: true` ou `[E]`?
- [ ] Consistente com outputs anteriores (diagnóstico de mídia)?
- [ ] Premissas têm fonte (não "números mágicos")?
- [ ] Cenário pessimista é realista (não assustador demais)?
- [ ] Disclaimer é honesto sobre variáveis de risco?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

Revise o output. O que está errado, exagerado ou faltando?

- "O budget mensal de R$ {BUDGET_MENSAL} está confirmado?"
- "O ticket médio de R$ {TICKET_MEDIO} está correto?"
- "A taxa de conversão é realista para o processo comercial atual?"
- "O cronograma é factível com os recursos disponíveis?"
- "Os limites de alerta são adequados?"
- "O disclaimer é honesto? O cliente vai entender que forecast não é garantia?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s3-forecast-midia.json` (com campo `summary` no topo, incluindo link Sheets)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph

## Formato do output (ee-s3-forecast-midia.json)

```json
{
  "financial_model": [{ "month": 1, "label": "Ramp-up", "budget": 0, "cpl": 0, "leads": 0, "conversion_rate": 0, "sales": 0, "revenue": 0, "roas": 0 }],
  "assumptions": ["string"],
  "scenarios": { "optimistic": {}, "realistic": {}, "pessimistic": {} },
  "platform_distribution": [{ "platform": "Meta Ads", "percentage": 0, "monthly_value": 0, "objective": "string" }],
  "funnel_distribution": [{ "phase": "Topo", "percentage": 0, "objective": "string" }],
  "timeline": [{ "month": 1, "focus": "Ramp-up", "weekly_actions": ["string"], "goal": "string" }],
  "alerts": [{ "metric": "CPL", "threshold": "> R$ X", "action": "string" }],
  "scale_criteria": [{ "metric": "ROAS", "threshold": "> Xx", "action": "string" }],
  "disclaimer": ["string"],
  "sheets_url": "string"
}
```


## Campo obrigatório: summary

Sempre inclua no JSON de saída:
```json
"summary": "Resumo de 1-2 frases do forecast de mídia: investimento total, leads projetados e ROAS esperado. Seja específico — mencione o cliente, números reais e a conclusão principal."
```

Este campo alimenta o Resumo Executivo do portal de entregas. Deve ser objetivo, com dados reais, sem genéricos.
