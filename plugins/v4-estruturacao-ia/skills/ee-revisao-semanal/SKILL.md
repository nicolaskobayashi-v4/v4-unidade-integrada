---
name: ee-revisao-semanal
description: "Executa pente-fino de fim de semana no consolidado + outputs. Lê de baixo pra cima (semana mais recente primeiro), mapeia a EVOLUÇÃO estratégica (briefing/hipótese inicial → diagnóstico → decisão), detecta divergências factuais reais e gaps narrativos, e propõe atualizações pontuais nos outputs que alimentam o portal. Após aprovação, regenera portal + consolidated automaticamente. Use quando o operador disser 'revisar semana', 'fechar ciclo', 'revisão semanal', ou ao final de qualquer semana com todas as skills completas."
dependencies: []
outputs: ["ee-revisao-semanal.json"]
week: "multi"
estimated_time: "20-40 min"
arguments:
  - name: cliente
    required: true
    description: "Slug do cliente em clientes/"
  - name: semana
    required: false
    description: "Número da semana a revisar (1, 2, 3, ...). Se omitido, detecta automaticamente a última semana com todas as skills completas."
---

# Revisão Semanal — Pente-Fino Consolidado

Você é um editor-revisor sênior. Ao final de uma semana de entregas, a sua missão é garantir que TODO o material produzido (outputs + portal + consolidated) conte uma história COERENTE E EVOLUTIVA: o stakeholder precisa ver como a visão estratégica amadureceu conforme os diagnósticos foram ficando mais profundos. Você NÃO refaz as skills — você ajusta pontualmente os outputs, registra a evolução, e deixa o portal/consolidado limpos.

> **REGRA DE OURO:** A consolidação precisa ficar SEMPRE atualizada após as revisões. Se você aplica um ajuste em qualquer output, é obrigatório re-rodar `render_portal.sh` no final. O portal e o consolidado são artefatos derivados — a verdade está nos outputs JSON.

## Filosofia — camadas de verdade

Os outputs não são todos equivalentes. Eles refletem momentos diferentes do aprendizado sobre o cliente:

| Camada | Natureza | Fonte | Autoridade |
|--------|----------|-------|-----------|
| **Briefing / Semana 1** | Hipótese inicial, visão declarada do cliente | Reunião de onboarding, formulário, documentos | BAIXA — é o ponto de partida, não a verdade final |
| **Semana 2 (diagnósticos)** | Evidência de campo, análise de dados, pesquisa | Mídia paga, CRO, pesquisa de mercado, criativos, orgânico | ALTA — é o que os fatos revelam |
| **Semana 3+ (decisões)** | Decisão estratégica informada | Posicionamento, identidade, landing page, forecast | MÁXIMA — é o que será executado |

**Regra de resolução de conflitos:** quando outputs de camadas diferentes discordam, a camada mais profunda/recente ganha. MAS o conflito NÃO é apagado — ele é **registrado como evolução estratégica** (ver Passe 1). O valor do sistema está justamente em mostrar "o cliente achava X; o diagnóstico revelou Y; a decisão foi Z".

Dentro da MESMA camada (ex: dois outputs da semana 2 se contradizendo), isso sim é bug factual — entra no Passe 2.

## Dados necessários

1. `client.json` do cliente (seções `meta`, `briefing`, `progress`, `history`)
2. `outputs/*.json` — todos os outputs das skills da semana alvo e das semanas anteriores
3. `consolidated.md` — narrativa consolidada atual (fonte para detectar gaps e redundâncias)
4. `consolidated.html` — visualização consolidada atual (para checar se o portal vai renderizar corretamente após as mudanças)

### Ordem de leitura — BOTTOM-UP

Leia na seguinte ordem (obrigatória):

1. **Outputs da semana mais recente primeiro** (ex: semana 2 antes de semana 1).
2. Dentro de cada semana, skills de decisão/síntese antes das de diagnóstico (ex: posicionamento antes de pesquisa-mercado).
3. **Por último**, releia o `briefing` em `client.json`.

Por quê: você começa ancorado na camada mais autoritativa (decisão/evidência) e desce em direção à hipótese inicial. Isso evita que vieses do briefing contaminem sua leitura dos diagnósticos.

### Detecção de semana (se argumento `semana` omitido)

Leia `client.json.meta.modelo_venda` e monte a sequência oficial a partir de `delivery-map.json` (fonte única): `comum.semana_1` + `comum.semana_2` + `semana_3[modelo_venda]` + `comum.semana_4`. A semana de cada skill é o **bloco em que ela aparece nesse mapa** (1–4) — **NÃO** use o prefixo `ee-sN-` do nome da skill: ele é um id histórico e NÃO corresponde à semana real (ex.: `ee-s1-diagnostico-maturidade` está na Semana 2; `ee-s2-diagnostico-cro`/`ee-s4-*` na Semana 3 do inside-sales; `ee-s5-*` na Semana 4). A semana alvo é a MAIOR semana onde TODAS as skills daquele bloco estão com `status: completed` em `client.json.progress.skills`. Se nenhuma semana está 100% completa, avise o operador e pare.

### Semanas e skills cobertas (referência)

A composição das 4 semanas vem de `delivery-map.json` e varia por `meta.modelo_venda` apenas na Semana 3 — **não mantenha listas de skills hardcoded aqui**:

- **Semana 1 (comum):** `delivery-map.comum.semana_1`
- **Semana 2 (comum):** `delivery-map.comum.semana_2`
- **Semana 3 (modelo):** `delivery-map.semana_3[meta.modelo_venda]`
- **Semana 4 (comum):** `delivery-map.comum.semana_4`

## Geração — 3 passes obrigatórios

### PASSE 1 — Evolução Estratégica (CROSS-LAYER)

Este passe é o coração da skill. Para cada TEMA relevante, identifique como a visão evoluiu da camada inicial até a mais recente. Registre em `evolucao_estrategica[]`.

Temas canônicos (adapte conforme as skills completadas):

1. **ICP / público-alvo** — quem o cliente achava que era o público vs quem o diagnóstico de mídia/orgânico/pesquisa revelou
2. **Proposta de valor / diferencial** — o que o cliente declarou como diferencial vs o que a pesquisa de mercado + análise de concorrentes confirmam ou refutam
3. **Canais** — onde o cliente achava que deveria investir vs onde o diagnóstico de mídia mostra melhor ROI/potencial
4. **Posicionamento de preço** — ticket/preço declarado vs faixa percebida justa (willingness to pay) vs prática de concorrentes
5. **Maturidade digital** — autoavaliação do briefing vs score real do diagnóstico de maturidade
6. **Problemas principais** — dores declaradas no briefing vs gaps priorizados por impacto no SWOT/auditoria
7. **Concorrência** — quem o cliente listou como concorrente vs quem realmente disputa o mesmo espaço (pesquisa de mercado)

Para cada tema com evolução relevante, preencha:

```json
{
  "id": "E1",
  "tema": "ICP / público-alvo",
  "hipotese_inicial": {
    "conteudo": "Cliente descreveu público como 'donas de casa 35-50 de classe média'",
    "origem": "briefing.icp (client.json)",
    "camada": "briefing"
  },
  "evidencia_diagnostico": {
    "conteudo": "Diagnóstico de mídia + orgânico mostram 78% do engajamento vindo de mulheres 28-42, urbanas, alto envolvimento emocional com o pet",
    "origem": "ee-s2-diagnostico-midia.json > audience_breakdown + ee-s2-diagnostico-organico-ig.json > engagement_by_demo",
    "camada": "semana_2"
  },
  "decisao_atual": {
    "conteudo": "ICP refinado: 'tutoras conscientes 28-42, urbanas, pet como família'. Mais específico que a hipótese inicial.",
    "origem": "ee-s1-persona-icp.json > primary_persona (atualizado pós-diagnóstico)",
    "camada": "decisao"
  },
  "impacto_estrategico": "Muda tom de voz (de funcional para emocional), canais (menos Facebook, mais Instagram + Google Search de emergência), e critérios de criativo.",
  "narrativa_sugerida": "A hipótese inicial de 'donas de casa 35-50' (briefing) foi refinada pelo diagnóstico de mídia: 78% do engajamento vem de tutoras 28-42 com relação emocional forte. O ICP final é mais específico e informa todas as decisões de posicionamento e canal."
}
```

Regra crítica: se a `hipotese_inicial` está hoje preservada em algum output (ex: o persona-icp ainda fala em "35-50"), isso vira uma **atualização proposta no Passe 3** — o output é reescrito para refletir a `decisao_atual`, mas o `_refinement_history[]` guarda o delta para rastreabilidade.

### PASSE 2 — Sincronização Factual (INTRA-CAMADA)

Agora varra inconsistências **entre outputs da mesma camada** (dois outputs de semana 2 que discordam, ou dois campos dentro da mesma skill). Essas são bugs factuais, não evolução. Registre em `divergencias_factuais[]`.

Categorias a checar:

1. **Nomes e grafias** — nome do cliente, marcas, concorrentes, pessoas, bairros, regiões. Garanta grafia única em todos os outputs (sem variações de caixa, abreviação ou prefixo).
2. **Números-chave** — ticket médio, faturamento, nº de clientes, scores, CACs, CPAs, TAM/SAM/SOM, datas. Se `ee-s1-diagnostico-maturidade` diz "score 4.2" e o resumo em `ee-s1-swot` diz "score 4,5", registre.
3. **Taxonomias** — nome de produtos/serviços, estágios de funil, personas, canais. Use o nome canônico da camada mais autoritativa.
4. **Referências cruzadas** — uma skill cita um item que existe noutra, mas com rótulo diferente (ex: priority_action P1 vira "ação crítica #2" noutro lugar).
5. **Contradições lógicas dentro da mesma camada** — dois outputs de semana 2 afirmando coisas opostas. (Se a contradição é cross-camada, vai no Passe 1 como evolução.)

Para cada divergência, preencha:
- `campo`: onde está o dado (ex: `ee-s1-swot.json > strengths[2].title`)
- `valor_atual`: o valor que está lá hoje
- `valor_recomendado`: o valor correto (escolha a fonte mais autoritativa dentro da mesma camada)
- `fonte_de_verdade`: qual output/seção tem a versão correta e por quê
- `arquivos_afetados`: lista dos outputs que precisam ser atualizados
- `severidade`: `critica` (muda decisão) | `media` (confunde leitor) | `baixa` (cosmética)

### PASSE 3 — Qualidade Narrativa (leitura do consolidated)

Releia `consolidated.md` de ponta a ponta, simulando ser o stakeholder do cliente. Capture em `gaps_narrativos[]`.

Categorias:

1. **Redundâncias** — a mesma informação repetida em 2+ lugares sem agregar contexto. Proponha corte ou consolidação.
2. **Lacunas** — algo prometido em uma skill que nunca é respondido pelas outras (ex: `ee-s1-swot` diz "janela de 12 meses" mas `ee-s2-pesquisa-mercado` não quantifica).
3. **Tom inconsistente** — uma skill fala do cliente em 3ª pessoa e outra em 2ª, ou mistura formal e informal sem razão.
4. **Transições abruptas** — pulos lógicos entre seções. Sugira frase-ponte a adicionar em `summary_headline` ou `key_insight`.
5. **Evolução não explicitada** — se o Passe 1 identificou uma evolução relevante mas o `consolidated` apresenta só o estado final sem mostrar o arco, isso é um gap. Proponha adicionar campo `evolution_note` na skill alvo OU ajustar `summary_headline`/`key_insight` para nomear a evolução.
6. **Honestidade** — algo foi vendido como "vantagem" em uma skill mas outro output revela que é fraqueza. Reforce ou adicione `honesty_alert`.

Para cada gap:
- `tipo`: `redundancia` | `lacuna` | `tom` | `transicao` | `evolucao_ausente` | `honestidade`
- `localizacao`: skill + seção
- `descricao`: o que está faltando/sobrando
- `ajuste_proposto`: texto exato do campo a adicionar/editar/remover
- `arquivo_afetado`: output a ser atualizado

### Síntese — `atualizacoes_propostas[]`

Consolide os achados dos três passes em uma LISTA DE EDIÇÕES CONCRETAS. Cada atualização deve ser autoexecutável:

```json
{
  "id": "U1",
  "arquivo": "outputs/ee-s1-persona-icp.json",
  "caminho_json": "primary_persona.age_range",
  "acao": "substituir",
  "valor_antigo": "35-50",
  "valor_novo": "28-42",
  "motivo": "Evolução E1 — diagnóstico de mídia revelou faixa etária real distinta da hipótese inicial do briefing. Registrar também o delta em evolution_note.",
  "severidade": "critica",
  "origem_achado": "evolucao",
  "referencia_evolucao": "E1"
}
```

Atualizações originadas de `evolucao_estrategica[]` devem sempre:
1. Reescrever o campo no output para refletir a `decisao_atual`
2. Adicionar/atualizar um campo `evolution_note` (string) no mesmo nível, narrando o arco (usar `narrativa_sugerida` da evolução como base)

Agrupe por severidade: críticas primeiro. Se uma mesma correção afeta múltiplos arquivos, liste cada arquivo como entrada separada com mesmo `motivo`.

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome e a semana específica revisada?
- [ ] Leu os outputs na ordem bottom-up (recente → antigo → briefing)?
- [ ] Passe 1 identificou ao menos 2 evoluções estratégicas relevantes (ou justificou ausência)?
- [ ] Cada evolução tem `hipotese_inicial`, `evidencia_diagnostico`, `decisao_atual` e `narrativa_sugerida`?
- [ ] Passe 2 só registra conflitos DENTRO da mesma camada (não confundiu evolução com bug)?
- [ ] Cada divergência cita arquivo + caminho JSON + valor atual vs recomendado?
- [ ] Cada gap narrativo tem ajuste proposto EXECUTÁVEL (não apenas "melhorar redação")?
- [ ] `atualizacoes_propostas[]` está ordenada por severidade (críticas primeiro)?
- [ ] Atualizações oriundas de evolução têm `origem_achado: "evolucao"` e `referencia_evolucao`?
- [ ] Cada atualização tem `valor_antigo` e `valor_novo` (ou `null` se adição/remoção)?
- [ ] Nenhum item genérico do tipo "revisar tom" — tudo é diff concreto?
- [ ] Schema validou?
- [ ] Todos os campos do schema preenchidos (ou com `null` + `unavailable_reason` no pai)?
- [ ] Nenhuma string vazia (`""`) — substituí por `null` + reason quando o dado não existe?
- [ ] Estimativas marcadas com `estimated: true` ou `[E]`?

Se falhou → regenere silenciosamente.

## Apresentação e decisões

Apresente ao operador em formato de RELATÓRIO com 4 seções:

1. **Evolução estratégica** — para cada evolução: tema, arco narrativo (hipótese → evidência → decisão), impacto. Esta é a seção-mãe.
2. **Divergências factuais** — tabela: `#`, `campo`, `atual → proposto`, `severidade`
3. **Gaps narrativos** — lista numerada com `tipo` + `localização` + `ajuste`
4. **Atualizações propostas** — tabela de diffs `#`, `arquivo`, `caminho`, `antigo → novo`, `motivo`, `origem` (evolução/factual/narrativa)

Para cada atualização (U1, U2, ...) peça decisão explícita ao operador:

> Para cada item abaixo, diga: **ACEITAR**, **REJEITAR** ou **AJUSTAR: <nova versão>**. Você pode responder em bloco (ex: "U1 aceitar, U2 rejeitar, U3 ajustar: ...").

Aguarde a decisão. Não aplique nada antes.

## Finalização

Após o operador decidir item a item:

1. **Salve a revisão**: grave `clientes/{slug}/outputs/ee-revisao-semanal.json` (com campo `summary` no topo resumindo: N evoluções mapeadas, N divergências, N gaps, N atualizações aceitas, N rejeitadas, N ajustadas). Se já existir (revisão anterior), versione adicionando a data ao summary e preserve o `_refinement_history[]` acumulado.

2. **Aplique as atualizações aceitas nos outputs alvo**. Para cada arquivo editado:
   - Leia o JSON, navegue pelo `caminho_json`, aplique a ação (`substituir` | `adicionar` | `remover`).
   - Se a atualização tem `origem_achado: "evolucao"`, adicione ou atualize o campo `evolution_note` no mesmo nível do campo editado, com a `narrativa_sugerida` da evolução correspondente.
   - Adicione no topo do objeto do output editado (nível raiz):
     ```json
     "refined_in": "ee-revisao-semanal",
     "_refinement_history": [
       {
         "ts": "2026-04-21T10:30:00Z",
         "review": "ee-revisao-semanal",
         "semana": 2,
         "updates": ["U1", "U3", "U5"],
         "evolutions_applied": ["E1", "E2"],
         "note": "ICP refinado de 35-50 para 28-42 com base no diagnóstico de mídia. Diferencial 'atendimento humanizado' removido por falta de evidência de unicidade."
       }
     ]
     ```
   - Se `_refinement_history` já existe, **acrescente** o novo registro ao array (não substitua).
   - Incremente `version` do output se o schema tiver esse campo.

3. **Atualize `client.json`**:
   - `progress.skills["ee-revisao-semanal"]` → `{status: "completed", version: version+1, completed_at: now}`
   - Append em `history[]`:
     ```json
     {
       "ts": "2026-04-21T10:30:00Z",
       "skill": "ee-revisao-semanal",
       "action": "completed",
       "note": "Revisão semana 2: 2 evoluções aplicadas (ICP, diferencial), 3 divergências corrigidas, 2 gaps fechados. Outputs ajustados: ee-s1-persona-icp, ee-s1-swot, ee-s2-posicionamento."
     }
     ```

4. **OBRIGATÓRIO — regenere portal + consolidated**:
   ```bash
   plugins/v4-estruturacao-ia/scripts/render_portal.sh clientes/{slug}
   ```
   Este passo garante que o consolidated fica atualizado após cada revisão. NÃO PULE.

5. Reporte ao operador:
   - "Revisão da semana {N} concluída. {NE} evoluções estratégicas registradas. Aplicadas {X} de {Y} atualizações propostas. Portal + consolidated regenerados."
   - Link da Vercel (se `vercel-project.json` existir).
   - Sugira próximo passo:
     - Se ainda há semanas pendentes: "Próxima semana começa com /ee-s{N+1}-..."
     - Se esta foi a última semana do ciclo: "Todas as semanas revisadas. Ciclo de estruturação fechado."
