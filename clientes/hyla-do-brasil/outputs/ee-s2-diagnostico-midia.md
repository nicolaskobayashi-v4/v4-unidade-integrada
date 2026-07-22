# Diagnóstico de Mídia Paga — Hyla do Brasil
**Skill:** ee-s2-diagnostico-midia | **Gerado em:** 08/07/2026
**Período analisado:** 1 de janeiro a 6-7 de julho de 2026 (6 meses)
**Fonte:** Exports manuais Google Ads + Meta Ads (base-de-conhecimento/dados-midia-paga) + acesso direto ao GA4 + teste ao vivo do operador (Pixel Helper, Tag Assistant, GA4 DebugView) + ee-s1-persona-icp + ee-s1-swot + ee-s2-posicionamento

> ⚠️ **Honestidade dos dados.** Este diagnóstico usa exports manuais e acesso direto ao GA4 (não o conector V4MOS, ainda bloqueado). O achado central: **nenhum dos 3 eventos GA4 candidatos a sinal de lead do Google (`form_submit`, `ads_conversion`, `contact`) dispara no envio do formulário de demonstração** — confirmado em teste ao vivo, repetido em 2 landing pages com Google Tag Assistant e GA4 DebugView. Todo número de leads/CPL/CPA do Google Ads reportado neste relatório (e em diagnósticos anteriores, como o CAC de ~R$900/venda do kick-off) deve ser tratado como não confiável até um evento dedicado ser implementado e validado.

---

## Manchete

> **Não é possível medir hoje quantos leads reais o Google Ads gera — nenhum dos 3 eventos candidatos (form_submit, ads_conversion, contact) dispara no envio do formulário de demonstração.**

---

## Números-chave

| Métrica | Valor |
|---|---|
| Investimento combinado (6 meses) | **R$75.550** (R$27.647 Google + R$47.903 Meta) |
| Investimento médio mensal | ~R$12.306/mês (bate com a faixa do briefing, R$13,5-15k) |
| Leads reais do Google | **não mensurável** — 3 eventos testados ao vivo, nenhum dispara no envio |
| Leads Meta (período) | 1.172 (métrica nativa "Leads", confiável — exceto jun/jul, sob suspeita) |
| Budget Google em mobile | **82,5%** |
| Desperdício em Pesquisa tradicional (termos zero engajamento) | R$3.901 (28% do gasto nessas campanhas) |
| Melhor segmento Meta | Adset Bairros Nobres SP — CPL R$34,63, 61% do budget Meta |
| Pior segmento Meta | Campanha "Conversão WPP" — CPL R$321,27 |

---

## Achado #1 — Não existe hoje nenhum evento que capture o pedido de demonstração (Google Ads)

**Investigação por eliminação, testada ao vivo:**

1. **`form_submit`** (590 no período de 6 meses) — evento genérico do GA4. No relatório de páginas dos últimos 28 dias, só **2 dos 75 disparos** vieram da landing page principal (`/aspirador-hyla-do-brasil/`, 70,75% do tráfego). O resto: recuperação de senha, carrinho, checkout de acessórios (Air Odorizer).
2. **`ads_conversion`** (448 no período) — corretamente classificado como "Enviar formulário de lead" no Google Ads, mas com o **mesmo padrão**: só 2 de 57 disparos na landing page.
3. **`contact`** (378 no período completo) — concentra **92,6%** dos disparos nas páginas certas (52,9% landing page + 39,7% home) e parecia o candidato certo. Mas em **teste ao vivo, repetido em 2 landing pages com Tag Assistant e GA4 DebugView, não disparou no momento do envio bem-sucedido do formulário** — só `form_start` e engajamento genérico foram registrados. Hipótese mais provável: `contact` está amarrado ao clique no botão flutuante de WhatsApp, não ao formulário (não confirmado com o time de dev).

**Impacto:** o Google Ads está otimizando o lance automático (Smart Bidding) sem nenhum sinal confiável de lead real há pelo menos os 6 meses cobertos por este diagnóstico. Isso explica, de forma mais direta que qualquer hipótese anterior, por que dobrar o orçamento no passado não dobrou o resultado (relatado no kick-off). **Nenhuma decisão de aumento de investimento em Google Ads deve ser tomada antes de implementar e validar um evento dedicado.**

*Contexto adicional: as 4 metas de conversão da conta (Compra, Adicionar ao carrinho, Enviar formulário de lead, Contato) estão todas marcadas como "Ação principal" — mesmo antes desse achado, isso já misturava sinais de qualidade muito diferente no mesmo lance automático.*

---

## Achado #2 — Budget de busca concentrado no território errado

**Evidência:** agrupando os termos de busca reais (Pesquisa tradicional + insights de categoria da PMAX) em clusters temáticos:

| Cluster | Custo (real, Pesquisa tradicional) | Cliques |
|---|---|---|
| Genérico ("aspirador de pó", "vassoura elétrica", "purificador de ar") | R$4.320 | 1.729 |
| Saúde/alergia (asma, rinite, bronquite, ácaros) | R$407 | 88 |
| Branded (Hyla) | R$839 | 2.910 |
| Adjacente/pouco relevante (pet, roupa, vidro) | R$580 | 385 |

O cluster genérico recebe **mais de 10x** o investimento do cluster de saúde — o oposto do território "saúde respiratória doméstica, não limpeza" que `ee-s2-posicionamento` acabou de definir. A PMAX (63% do budget do Google) usa um único grupo de recursos com 60+ temas de pesquisa misturando saúde, concorrentes e limpeza genérica, sem segmentação.

**Impacto:** a Hyla paga para competir no espaço genérico, onde tem menos diferenciação, em vez do espaço de saúde, onde tem o argumento técnico mais forte (separador autolimpante patenteado).

---

## Achado #3 — 82,5% do budget do Google vai para mobile, o dispositivo com problema técnico já conhecido

**Evidência:** R$22.807 de R$27.647 (82,5%) do investimento total em Google Ads foi em celular (CTR mobile 4,55%, mais que o dobro do desktop 1,96%) — mas o site (WordPress + Elementor) já foi classificado no diagnóstico de maturidade (`ee-s1-diagnostico-maturidade`) como instável em mobile dependendo do navegador.

**Impacto:** tráfego caro e qualificado sendo entregue à pior versão técnica de um funil que, agora sabemos, também não está sendo medido corretamente no fim — ponto de intersecção direta com `ee-s2-diagnostico-cro`.

---

## Google Ads — visão geral

- **Budget médio:** ~R$4.489/mês | **Campanhas:** PMAX (ativa, 63% do budget), Branding-SP (ativa), Branding-BR (pausada), [C] Aspirador (pausada, sem atividade)
- **CTR médio (90d):** 3,10%
- **CPA/conversões:** não mensurável — ver Achado #1

**Evolução mensal (só dados confiáveis — custo, cliques, CTR):**

| Mês | Custo | Cliques | CTR |
|---|---|---|---|
| Jan | R$4.178 | 10.418 | 5,56% |
| Fev | R$3.903 | 10.443 | 9,01% |
| Mar | R$3.783 | 5.418 | 6,15% |
| Abr | R$5.429 | 16.702 | 4,28% |
| Mai | R$5.605 | 10.414 | 2,94% |
| Jun | R$3.779 | 3.257 | 2,58% |
| Jul (6d) | R$969 | 556 | 1,60% |

*Colunas de conversão/CPA foram removidas: nenhum evento GA4 disponível mede o pedido de demonstração de forma confiável (ver Achado #1).*

### Clusters de palavras-chave (Pesquisa tradicional)

| Cluster | % budget (Pesquisa) | CPC esperado | Risco |
|---|---|---|---|
| Genérico | 42% | R$1,50-4,30 | Maior investimento, menor diferenciação |
| Branded | 8% | R$1,35-1,40 | Baixo — CTR até 21% |
| Saúde/alergia | 4% | R$4,30-8,50 | Volume muito baixo frente ao posicionamento definido |
| Adjacente/irrelevante | 3% | R$0,50-3,00 | Termos como "escova para cachorro", "brizza pet" — 0 conversões |

---

## Meta Ads — visão geral

- **Budget médio:** ~R$8.375/mês | **CTR médio (90d):** 4,85% | **CPM médio (90d):** R$7,51
- **Otimização correta:** campanhas otimizam para "Leads" nativo (confirmado pelo operador) — diferente do Google, o alvo do algoritmo aqui está certo e a métrica é confiável.

**Problemas críticos:**
1. Campanha "Instagram | Conversão WPP": CPL R$321,27 (10x a melhor campanha) — nome sugere otimização para WhatsApp, o que contradiz a decisão de remover o botão direto de WhatsApp dos anúncios (já tomada pelo time para elevar qualificação).
2. Dois anúncios do adset "RS SC ES MS MG AL PE - WPP" somam R$1.268,25 gastos com **zero leads**.
3. CPM saltou de ~R$5 (jan-mai) para R$15,22 (jun) e R$30,35 (jul), coincidindo com o salto de leads não explicado por mudança de campanha e com o crescimento acelerado do evento `contact` do GA4 no mesmo período — pode ser o mesmo evento causador (ex.: mudança de tag/GTM no site), ainda não identificado. **Não tratar jun/jul como novo patamar de eficiência ainda.**

**Melhor performer:** adset "[SP] BAIRROS NOBRES" — 61% do budget Meta, CPL R$34,63, alinhado ao ICP primário. Dentro dele, o criativo "PRATICIDADE" (CPL R$21,00) supera "Nimbus Tapete" (CPL R$175,14) em 8x — o ângulo de mensagem importa mais que a segmentação geográfica.

> **Achado estratégico (validado com o operador, 16/07):** o gargalo não é volume de lead — é capacidade de atender. A conta oficial da Hyla no Instagram (~47-49 mil seguidores) já tem mais audiência que a própria Hyla França (~14 mil), que vende o triplo por associada. Recomendação: concentrar o budget de consumo em São Paulo (onde já funciona) e abrir uma campanha de **recrutamento de associadas** separada, nacional, financiada redirecionando o que já era desperdício (campanha WPP) — não com aumento de investimento. Ver `outputs/benchmark-internacional-associados-e-midia.md` e `ee-s4-diagnostico-comercial`.

**Benchmarks (referência EUA/global 2026, uso direcional — [E]):**

| Métrica | Hyla | Benchmark [E] | Status |
|---|---|---|---|
| CPM | R$7,51 (90d) | ~R$22 (Brasil, Tier 3) | ✅ abaixo |
| CTR | 4,85% (90d) | 2,92% (Home & Decor) | ✅ acima |
| CPL | R$27-41 | R$122-150 (Lead Gen) | ✅ abaixo |

---

## Top 3 Problemas Críticos

1. **Não existe evento de conversão dedicado ao pedido de demonstração** — os 3 candidatos testados ao vivo (`form_submit`, `ads_conversion`, `contact`) não disparam no envio do formulário.
2. **Budget de busca no território errado** — genérico "aspirador de pó" recebe 10x mais investimento que "saúde/alergia", invertendo o posicionamento definido.
3. **82,5% do budget Google em mobile**, dispositivo com instabilidade técnica já reconhecida no site.

## Plano de Ação — 30 dias

| # | Ação | Prioridade | Impacto esperado | Prazo |
|---|---|---|---|---|
| 1 | Implementar evento de conversão dedicado ao formulário de demonstração (ex.: `lead_demonstracao`) | P1 | Pré-requisito para qualquer métrica de lead do Google | Até 15/07 |
| 2 | Validar o novo evento ao vivo (Tag Assistant + GA4 DebugView) em 2+ landing pages | P1 | Evita repetir o erro de evento configurado mas não disparando | Junto com item 1 |
| 3 | Confirmar com dev/GTM se `contact` está amarrado ao WhatsApp | P2 | Evita reaproveitar por engano um evento que não mede o formulário | 15 dias |
| 4 | Rebaixar metas Compra/Carrinho/Contato para "Secundária" no Google Ads, após o novo evento validado | P1 | Realinha o Smart Bidding para lead real | Logo após item 2 |
| 5 | Negativar termos de zero engajamento na Pesquisa tradicional | P2 | Recupera parte dos R$3.901 desperdiçados | 15 dias |
| 6 | Pausar/realocar campanha "Conversão WPP" (Meta) para Bairros Nobres SP | P2 | Reduz CPL blended do Meta | 15 dias |
| 7 | Criar grupo de recursos dedicado ao cluster de saúde/alergia na PMAX | P2 | Testa demanda real no território de posicionamento | 30 dias |
| 8 | Replicar ângulo "PRATICIDADE" em outras praças Meta | P3 | Pode reduzir CPL em Curitiba/Brasília/Goiânia | 30 dias |
| 9 | Rodar cliente oculto em São Paulo (mesmo formato do teste de Londrina) antes de comprometer budget na reestruturação geográfica | P1 | Confirma se o handoff quebrado é de praça sem cobertura ou de processo/CRM — muda a prioridade | Antes de 17/07, se possível |
| 10 | Estruturar campanha de recrutamento de associadas separada da campanha de consumo (público/criativo/CTA distintos), alcance nacional, testando o formato "embaixadora digital" via @hyladobrasilbusiness | P2 | Ataca o gargalo real (capacidade de atendimento), não o sintoma (volume de lead) | 30 dias |

## Cenários de Realocação de Budget

Google não entra com meta numérica de leads/CPL até o evento dedicado ser implementado e validado (pré-requisito, não escolha). Os números abaixo refletem só o Meta, exceto o Cenário Agressivo, que já pressupõe o Google mensurável.

| | Conservador | **Realista (recomendado após validar o evento)** | Agressivo |
|---|---|---|---|
| Budget/mês | R$12.306 | R$12.306 | R$16.000 (+30%) |
| Leads/mês projetados | 195 (só Meta) | 220 (só Meta, melhorado) | 290 (Google + Meta, baixa confiança) |
| CPL projetado | R$40 | R$34 | R$37 |
| Esforço | 1 semana | 4 semanas | 8 semanas |
| Confiança | Alta (Meta) | Média (Meta) | Baixa (Google ainda sem histórico) |

**A partir do Cenário Realista, duas frentes distintas:** (1) consumo concentrado em São Paulo, onde já funciona e há cobertura densa de associada; (2) recrutamento nacional financiado cortando a campanha WPP — não pede budget novo. Pré-requisito: validar com cliente oculto em SP (item 9) que o handoff funciona em praça de cobertura densa antes de comprometer a reestruturação.

**Recomendação:** Cenário Conservador **agora** (implementar e validar o evento — não é opcional) e Cenário Realista com a reestruturação em duas frentes assim que o evento estiver validado, antes de cogitar qualquer aumento de investimento. Escalar (Agressivo) antes disso arrisca decidir sobre um canal (Google, 37% do investimento total) sem saber quantos leads ele realmente gera — além do risco já conhecido de inflar a fila além da capacidade de demonstração (SWOT Fr3, agora confirmado com prova de campo em `ee-s4-diagnostico-comercial`).

## Meta Realista — 90 dias

- **CPL alvo:** R$34 (Meta — única plataforma com meta numérica neste ciclo)
- **Leads/mês alvo:** 220 (Meta)
- **Agendamentos/mês alvo:** 32 (conservador — não pressupõe resolução do gargalo de associados)
- Google: sem meta numérica até o evento de conversão ser implementado e validado.

---

## Ponto de Alavancagem

> **O caminho de maior alavancagem agora não é aumentar budget — é implementar um evento de conversão que realmente meça o pedido de demonstração.**

1. Sem um evento dedicado, o Smart Bidding do Google nunca teve o dado certo para otimizar — explica por que dobrar o orçamento no passado não dobrou o resultado.
2. O Meta já mostra o caminho: com métrica confiável, dá para agir hoje — cortar a campanha WPP e realocar para Bairros Nobres SP é decisão de baixo risco.
3. O cluster de saúde/alergia recebeu 10x menos investimento que o genérico — testável em paralelo à correção do evento, não depende dela.

**💬 Momento de validar com Davi/Fábio:** até o evento do Google ser corrigido e validado, qualquer leitura de CPL ou volume de leads do Google — inclusive o CAC de ~R$900/venda estimado no kick-off — deve ser tratada como não confiável.

---

*Alimenta: `ee-s2-diagnostico-cro`, `ee-s3-forecast-midia`, `ee-s2-diagnostico-organico-ig`, `ee-s4-diagnostico-comercial`, `ee-revisao-semanal`*
