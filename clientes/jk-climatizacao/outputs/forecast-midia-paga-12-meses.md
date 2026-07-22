# Forecast de Investimento em Mídia Paga com ROAS — JK Climatização
**12 meses (Ago/2026 a Jul/2027)** | **Gerado em:** 09/07/2026 · **Atualizado em:** 10/07/2026
**Fonte:** Planilha de keywords (Google Keyword Planner) + reunião V4+JK Máquinas (08/05) + ee-s1-persona-icp + ee-s4-diagnostico-comercial + ee-s5-scripts-sdr + benchmarks de mercado (pesquisa jul/2026)

> Estudo ad-hoc solicitado antes do fechamento do módulo de vendas. Não é uma das skills do catálogo padrão — mais próximo em espírito de `ee-s3-forecast-midia`, mas essa depende de `ee-s2-diagnostico-midia`, ainda pendente.

---

## ⟳ Atualização 10/07/2026 — nova planilha de keywords

O operador subiu uma planilha nova (1.517 linhas vs. 535 da anterior). A Keyword Planner repete o **mesmo volume** para variações quase idênticas ("instalação de ar condicionado" / "instalacao de ar condicionado" / "instalação de um ar condicionado" — todas vol=590) — sem deduplicar isso, o total parece 2,5x maior do que é de fato. Depois de deduplicar por cluster de variantes:

- **Volume real triplicou:** ~819/mês (v1) → **~2.534/mês** (v2)
- **O ganho é quase todo de "instalação de ar condicionado"** (~2.750/mês dedup) — praticamente ausente na pesquisa anterior
- **Volume B2B/PMOC específico não mudou:** 62 → 68/mês — a conclusão de que esse segmento depende de venda ativa, não busca, **continua de pé**
- **Sazonalidade ficou mais concentrada em dezembro:** índice subiu de 170 para **218**; maio/junho caíram mais fundo (baixa de inverno mais funda)
- **Totais anuais do forecast não mudam** (a curva é normalizada por sazonalidade) — muda a distribuição mês a mês, mais pesada em dezembro, mais enxuta em mai/jun
- **Nova oportunidade a considerar:** "instalação" pode ser um *wedge* de entrada pro B2B (empresa que instala vira contrato de manutenção depois) — não tratar como tráfego genérico de baixa prioridade, segmentar por geografia/perfil de imóvel

Tabela e gráficos abaixo já refletem os números atualizados (v2).

---

## Manchete

> **O maior alavancador deste forecast não é o canal — é implementar o scoring de 1-5 estrelas e os scripts de follow-up já entregues nesta consultoria. Isso muda o LTV:CAC de 1,8x (arriscado) para 4,6x (saudável) no Comercial Geral, com o MESMO orçamento de mídia.**

---

## Os Indicadores Solicitados

| Indicador | Valor | Fonte |
|---|---|---|
| **CPL — Comercial Geral (Google)** | R$ 55 (faixa R$40-70) | Estimado: CPC da planilha × 1/CVR típico (10%) |
| **CPL — B2B Industrial (Google)** | R$ 140 (faixa R$80-200) | Benchmark de mercado Brasil 2026 |
| **CPL — Meta Ads (comparativo)** | R$ 180 (faixa R$155-260) | Benchmark internacional convertido (USD→BRL a 5,15) |
| **CR Lead → MQL** | 65% (hoje) / 75% (com scoring) | Estimado, ajustado ao contexto real |
| **CR MQL → SQL** | 20% (hoje) / 35% (com scripts SDR) | Benchmark RD Station Panorama 2026 |
| **CR SQL → Venda** | 20% (mediana, faixa 5-30%) | **Dado real** — discutido na reunião de 08/05 |
| **Ticket Médio** | R$320/mês (geral) · R$714/mês (B2B) | **Dado real** — confirmado por André |
| **LTV** | R$3.840 (Comercial, 12m) · R$25.704 (B2B, 36m) | Estimado — ver nota abaixo |

⚠️ **Atenção:** a reunião de venda da V4 (08/05) usou CPL de R$10 (B2C) e R$25 (B2B) — mas isso foi **ilustração comercial para fechar o André**, não benchmark real. Os valores pesquisados agora (R$80-200 para B2B industrial) são **3-8x mais altos**. Usei os benchmarks desta tabela, não os da reunião de venda.

**Sobre o LTV:** a reunião "chutou baixo" 12 meses de recorrência para qualquer segmento, só pra ser conservadora no pitch. Mas a JK relata só 2 empresas perdidas *desde sempre* (`ee-s1-persona-icp`) — muito acima do benchmark de mercado B2B (~72,5% retenção anual ≈ 3,6 anos de tenure). Por isso usei 36 meses no B2B (mais realista) e mantive 12 meses conservador no Comercial Geral.

---

## O Que a Planilha de Keywords Revelou (v2, deduplicada)

- **1.517 linhas de palavra-chave** (v1 tinha 535), jun/2025-mai/2026. Deduplicado por cluster de variantes com o mesmo padrão mensal: **~2.534 buscas/mês reais** (era ~819/mês na v1, também deduplicada — o crescimento é real, não é ruído de duplicata).
- **O maior cluster de demanda de toda a planilha é "instalação de ar condicionado"** (~2.750/mês dedup) — quase ausente na pesquisa anterior. É volume que serve B2C avulso (não prioritário), mas também o B2B2C alto padrão/litoral (a segmentação certa por geografia/perfil captura o wedge de maior valor) e pode virar contrato de manutenção depois.
- **Termos B2B/industriais específicos (PMOC, câmara fria, preventiva industrial) seguem baixíssimos:** 62→68 buscas/mês dedup — **não mudou a conclusão central:** esse segmento depende de venda ativa, não de busca. PMOC como termo de busca tem volume ~0.
- **Volume dentro do raio real da JK cresceu** (1→18/mês dedup), concentrado em Balneário Camboriú — reforça a oportunidade do litoral já identificada em `ee-s1-persona-icp`. Zero busca pela marca "JK Climatização".
- **Sazonalidade real** (índice, média=100) — **atualizada**:

| Jun | Jul | Ago | Set | Out | Nov | **Dez** | Jan | Fev | Mar | Abr | Mai |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 51 | 64 | 67 | 92 | 105 | 128 | **218** | 145 | 122 | 95 | 67 | 47 |

*(v1 para comparação: Jun 69, Jul 76, Ago 61, Set 90, Out 94, Nov 115, Dez 170, Jan 155, Fev 130, Mar 110, Abr 67, Mai 64)*

O pico ficou **ainda mais concentrado em dezembro** (170→218) — "instalação" se decide mais em cima da hora do calor chegar do que "manutenção", que se distribui mais ao longo do verão inteiro. Maio/junho caíram mais fundo (baixa de inverno mais funda que antes).

---

## Benchmarks de Mercado Pesquisados

| Fonte | Achado |
|---|---|
| RD Station — Panorama 2026 | MQL→SQL: <15% fraco, 15-25% médio, **35-50% com SLA marketing-vendas formal** (62% das empresas não têm isso) |
| Google Ads Brasil — Indústria 2026 | CPC R$3-9 (média R$5); **CPL B2B industrial R$80-200** |
| Meta Ads B2B 2026 | CPL cross-industry ~US$27,66; serviços profissionais US$25-70; qualificado US$150-250 |
| WordStream 2026 | CPC médio global US$5,42; CVR médio 8,18% |
| CustomerGauge/Emulent | Retenção B2B média ~72,5%/ano; meta universal CAC:CLTV = 1:3 |
| Investing.com | USD/BRL ≈ 5,11-5,12 (jul/2026) |

---

## Plano de Investimento Mensal (cenário recomendado: com scripts SDR ativos)

| Mês | Índice Sazonal | Budget Comercial | Budget B2B | Budget Total | Vendas Com. | Vendas B2B | MRR Novo | ROAS M1 |
|---|---|---|---|---|---|---|---|---|
| Ago/26 | 67 | R$1.006 | R$1.253 | R$2.259 | 1,20 | 0,59 | R$803 | 0,36x |
| Set/26 | 92 | R$1.384 | R$1.442 | R$2.826 | 1,65 | 0,68 | R$1.011 | 0,36x |
| Out/26 | 105 | R$1.575 | R$1.537 | R$3.112 | 1,88 | 0,72 | R$1.116 | 0,36x |
| Nov/26 | 128 | R$1.919 | R$1.709 | R$3.628 | 2,29 | 0,80 | R$1.305 | 0,36x |
| **Dez/26** | **218** | **R$3.267** | R$2.384 | **R$5.651** | 3,90 | 1,12 | R$2.045 | 0,36x |
| Jan/27 | 145 | R$2.172 | R$1.836 | R$4.008 | 2,59 | 0,86 | R$1.444 | 0,36x |
| Fev/27 | 122 | R$1.829 | R$1.664 | R$3.493 | 2,18 | 0,78 | R$1.255 | 0,36x |
| Mar/27 | 95 | R$1.426 | R$1.463 | R$2.889 | 1,70 | 0,69 | R$1.034 | 0,36x |
| Abr/27 | 67 | R$1.000 | R$1.250 | R$2.250 | 1,19 | 0,59 | R$800 | 0,36x |
| Mai/27 | 47 | R$699 | R$1.100 | R$1.799 | 0,83 | 0,52 | R$635 | 0,35x |
| Jun/27 | 51 | R$770 | R$1.135 | R$1.905 | 0,92 | 0,53 | R$674 | 0,35x |
| Jul/27 | 64 | R$952 | R$1.226 | R$2.178 | 1,14 | 0,57 | R$774 | 0,36x |
| **TOTAL** | | **R$18.000** | **R$18.000** | **R$36.000** | **21,5** | **8,4** | | |

*Dezembro agora concentra 15,7% do orçamento anual (era 12,7% na v1) — o pico ficou mais afiado. Totais anuais (budget, vendas, CAC, ROAS-LTV) não mudam.*

**Sobre o "ROAS mês 1" (~0,35x):** parece ruim isolado, mas **não é alerta** — negócio de contrato recorrente não se paga no primeiro mês. O retorno real está no ROAS-LTV abaixo.

*(Orçamento base pré-sazonalidade: R$1.500/mês em cada segmento. O B2B tem sazonalidade amortecida pela metade — contratos corporativos/PMOC não dependem do calor extremo, como a própria V4 argumentou na reunião de venda.)*

---

## Resumo Anual — Três Cenários

| | **Hoje** (sem scoring/SDR) | **Melhorado** (com ee-s5-scripts-sdr) | **Meta Ads** (comparativo, não recomendado) |
|---|---|---|---|
| Vendas/ano | 11,8 | **29,9** | 2,2 |
| CAC Comercial | R$2.115 | R$838 | R$2.743 |
| CAC B2B | R$5.385 | R$2.133 | — |
| LTV:CAC Comercial | 1,8x ⚠️ | **4,6x** | 1,4x ⚠️ |
| LTV:CAC B2B | 4,8x | **12,1x** | — |
| ROAS-LTV Comercial | 1,82x | **4,58x** | 1,40x |
| ROAS-LTV B2B | 4,77x | **12,05x** | — |
| MRR ativo final do ano | R$5.110 | **R$12.900** | — |

**Piso saudável de mercado: LTV:CAC de 1:3.** O cenário "hoje" fica *abaixo* desse piso no Comercial Geral — investir em mídia sem implementar o scoring/scripts primeiro é uma aposta de risco mais alto do que parece.

---

## Google Ads x Meta Ads — Recomendação

**100% Google Ads (Search) no cenário base.** Meta Ads não é recomendado para captação fria — e os números confirmam sua leitura:

- **Google Ads:** captura intenção de busca ativa (quem já está procurando) — o único sinal que este nicho de baixo volume consegue aproveitar com eficiência. ROAS-LTV 4,6x (Comercial) a 12,1x (B2B).
- **Meta Ads:** ROAS-LTV de apenas 1,4x — **abaixo do piso saudável de mercado mesmo no cenário com funil melhorado**. Consistente com o diagnóstico de marketing (S3): Meta funciona melhor como remarketing do que captação fria para este perfil de cliente B2B/nicho.
- **Nota lateral (não pedida, mas relevante):** o LinkedIn Ads já tem CPC mínimo validado (R$4/clique, R$50/dia) e foi citado como canal B2B promissor na S3 — vale considerar se o volume de Google Ads B2B saturar (ver abaixo).

---

## 💬 Ponto de Alavancagem — Discussão com Stakeholder

> **O maior alavancador não é o canal de mídia — é implementar o scoring 1-5⭐ e os scripts de follow-up já entregues nesta consultoria.**

1. O ganho MQL→SQL (20%→35%) é o maior driver — está amarrado ao scoring e à cadência D+1/D+3/D+7 de `ee-s4-diagnostico-comercial`/`ee-s5-scripts-sdr`, não a mais investimento em anúncio
2. O B2B Industrial tem ROAS-LTV 2,6x maior que o Comercial Geral (12,05x vs 4,58x) mesmo com CPL 2,5x mais caro — reforça a priorização do ICP de 10+ aparelhos já recomendada em `ee-s1-persona-icp`
3. O volume de busca regional B2B é muito baixo — não dá pra simplesmente "colocar mais dinheiro" nesse segmento sem esbarrar em teto de impressões; expandir volume B2B provavelmente vai exigir LinkedIn Ads ou Display/remarketing

**Vale sequenciar com André:** validar e ativar os scripts/scoring primeiro (sem custo de mídia adicional), rodar 4-6 semanas medindo CPL e conversão REAL, e só então recalibrar este forecast com dado próprio.

---

## ⚠️ Alerta de Honestidade

Este forecast mistura três níveis de confiança:

1. **Dado real da JK:** ticket médio R$320, margem 23%, projeção B2B R$714, retenção histórica altíssima, sazonalidade de busca
2. **Estimativa ilustrativa da reunião de venda V4** (08/05): CPL R$10/R$25, funil 85%/70%/20% — otimistas, feitos pra tangibilizar a venda do serviço, **não usar como meta**
3. **Benchmark de mercado pesquisado agora:** CPL B2B R$80-200, MQL→SQL 15-50%, Meta CPL convertido de USD

**A JK não tem, até hoje, nenhum CPL ou taxa de conversão real medida** (sem CRM — ver `ee-s4-diagnostico-comercial`). Este forecast inteiro é uma **estimativa de planejamento** — a primeira responsabilidade ao rodar a campanha de verdade é substituir estes números por dado observado nas primeiras 4-6 semanas.

---

## Pendente de Confirmação

- Orçamento total real disponível (este forecast usa R$3.000/mês médio como cenário de trabalho, não confirmado)
- Se os scripts SDR e o scoring serão de fato implementados antes de escalar mídia (o cenário "melhorado" pressupõe isso)
- Se vale reservar uma fatia pequena de teste para Meta Ads remarketing, ou excluir 100%
- Revalidar CPL e conversão reais após 4-6 semanas de campanha ativa

---

### Sources (pesquisa de benchmarks)

- [Panoramas RD Station 2026](https://www.rdstation.com/pesquisas/panorama-marketing-vendas/edicao-2026/introducao/)
- [WordStream Google Ads Benchmarks 2026](https://www.wordstream.com/blog/2026-google-ads-benchmarks)
- [CustomerGauge — Average Customer Lifetime Value by Industry](https://customergauge.com/blog/average-customer-lifetime-value-by-industry)
- [Investing.com — USD/BRL](https://br.investing.com/currencies/usd-brl)

**Alimenta:** `ee-s3-forecast-midia` (quando `ee-s2-diagnostico-midia` rodar formalmente)
