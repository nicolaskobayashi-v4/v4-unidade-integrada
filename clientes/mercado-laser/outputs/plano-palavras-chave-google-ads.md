# Plano de Palavras-Chave — Google Ads — Mercado Laser
**Gerado em:** 26/06/2026
**Fonte:** ee-s1-persona-icp (ICPs e jornada) + ee-s1-diagnostico-maturidade (estado atual da mídia) + catálogo/produtos citados no kick-off

> ⚠️ **Sem dado de volume/CPC real.** Não tenho acesso ao Google Keyword Planner nem à conta de Ads do cliente — os termos abaixo são estratégicos (baseados no catálogo real e nos dois ICPs mapeados), não validados por volume de busca. **Antes de subir, o Daniel deve rodar isso no Keyword Planner** para confirmar volume, CPC estimado e descartar termos sem busca real.

> ⚠️ **Pré-requisito do diagnóstico de maturidade:** não existe pixel/conversão instalada ainda. Recomendo rodar as campanhas abaixo em **CPC manual ou Maximize Clicks com teto de lance** nas primeiras semanas — Target CPA/ROAS automatizado não tem dados suficientes pra funcionar bem (regra geral: precisa de ~30 conversões/mês registradas para o algoritmo aprender) e vai desperdiçar budget enquanto isso não existir.

---

## Lógica do plano

Segue a segmentação de `ee-s1-persona-icp`: **dois funis permanentes**, orçamento desproporcionalmente maior para máquina (onde está a margem e a dor que motivou a contratação), mas peça mantida ativa porque sustenta ~90% do volume de pedidos e tem CPC mais barato/conversão mais rápida.

| Campanha | Funil | ICP | Prioridade de budget |
|---|---|---|---|
| 1. Máquina — Fundo de funil | Decisão/Consideração | Rodrigo / Patrícia | **Alta — maior fatia do orçamento** |
| 2. Máquina — Topo/Meio de funil | Pesquisa/Gatilho | Marcelo | Média — descoberta, CPC mais barato mas exige conteúdo de suporte |
| 3. Peças e Componentes | Decisão imediata | Anderson | Média — CPC baixo, decisão rápida, mantém caixa girando |
| 4. BestBeam Premium | Decisão consultiva | Patrícia (indústria) | Alta — ticket mais alto, mas volume de busca menor |

---

## Campanha 1 — Máquina, Fundo de Funil (Search)

**Objetivo:** capturar quem já decidiu comprar e está comparando onde.

### Ad Group 1.1 — Máquina de Corte a Laser (genérico, alta intenção)
| Termo | Match type |
|---|---|
| máquina de corte a laser preço | Frase |
| máquina de corte a laser comprar | Frase |
| [máquina de corte a laser profissional] | Exata |
| importadora de máquina de corte a laser | Frase |
| máquina de corte a laser CO2 130w | Frase |
| onde comprar máquina de corte a laser | Frase |

### Ad Group 1.2 — Máquina de Gravação a Laser / Fiber
| Termo | Match type |
|---|---|
| máquina de gravação a laser fibra preço | Frase |
| [máquina laser fiber 30w] | Exata |
| máquina de gravação a laser portátil comprar | Frase |
| máquina de gravação a laser para empresa de brindes | Frase |
| máquina laser galvo preço | Frase |

### Ad Group 1.3 — Aplicação específica (conecta com o catálogo real)
| Termo | Match type |
|---|---|
| máquina de corte a laser para acrílico | Frase |
| máquina de corte a laser para MDF | Frase |
| máquina de corte a laser para tecido | Frase |
| máquina de gravação a laser para joias | Frase |
| máquina de gravação a laser para chaveiro | Frase |

### Ad Group 1.4 — Concorrência (captura comparativa)
| Termo | Match type | Nota |
|---|---|---|
| translaser máquina laser | Frase | Captura quem está comparando — anúncio deve reforçar suporte/garantia, não preço |
| multivis máquina laser | Frase | Idem — esse público já é descrito pelo Júlio como o que mais migra pro Mercado Laser depois de problema |
| alternativa a [concorrente] máquina laser | Frase | Só ativar se o volume confirmado no Keyword Planner justificar |

---

## Campanha 2 — Máquina, Topo/Meio de Funil (Search, CPC mais baixo)

**Objetivo:** capturar o perfil "Marcelo" — ainda decidindo se vale o investimento, pesquisa antes de pesquisar marca.

| Termo | Match type | Estágio |
|---|---|---|
| quanto rende uma máquina de gravação a laser | Frase | Topo |
| máquina de corte a laser vale a pena | Frase | Topo |
| como ganhar dinheiro com máquina de corte a laser | Frase | Topo |
| renda extra gravação a laser | Frase | Topo |
| melhor máquina de corte a laser | Frase | Meio |
| diferença máquina laser CO2 e fiber | Frase | Meio |
| quanto custa uma máquina de gravação a laser | Frase | Meio |

**Recomendação:** essas campanhas precisam de uma landing page ou conteúdo de suporte (ex: página "vale a pena?" com cases reais) — sem isso, o CPC fica barato mas a conversão tende a ser baixa porque o lead ainda não decidiu. Direcionar pra um conteúdo educativo antes do checkout/WhatsApp direto pode render mais.

---

## Campanha 3 — Peças e Componentes (Search, alta intenção, CPC baixo)

**Objetivo:** capturar quem já tem máquina e precisa repor — decisão rápida, alta recorrência (ICP Anderson).

| Termo | Match type |
|---|---|
| tubo laser CO2 reposição | Frase |
| [tubo laser 100w preço] | Exata |
| lente para máquina de corte a laser | Frase |
| espelho refletor laser CO2 | Frase |
| exaustor para máquina de corte a laser | Frase |
| bomba de refrigeração máquina laser | Frase |
| peça de reposição máquina laser fiber | Frase |
| manutenção máquina de corte a laser | Frase |

**Nota estratégica:** o pico histórico de venda de exaustor/refrigerador (2019-2021, registrado no `research` do client.json) veio de clientes de concorrentes com máquina de baixa qualidade. Vale considerar um Ad Group específico testando termos como "minha máquina laser não refrigera" ou "tubo laser superaquecendo" para capturar esse padrão de novo.

---

## Campanha 4 — BestBeam Premium (Search, B2B/industrial)

**Objetivo:** capturar o ICP Patrícia — empresa estabelecida buscando máquina de linha premium.

| Termo | Match type |
|---|---|
| máquina de corte a laser industrial | Frase |
| máquina de corte a laser para indústria têxtil | Frase |
| máquina de corte a laser para calçados | Frase |
| máquina de gravação a laser para comunicação visual | Frase |
| máquina laser linha de produção | Frase |
| fornecedor máquina laser industrial | Frase |

**Atenção:** o site bestbeam.com.br ainda estava em construção no kick-off (15/06) — confirmar com Igor/Vinícius se já está publicado antes de direcionar tráfego pago pra esse domínio. Se ainda não estiver, usar a aba correspondente dentro do site Mercado Laser como destino temporário.

---

## Lista de negativas (aplicar na conta ou nas campanhas 1, 2 e 4)

Termos que sinalizam o público de baixo ticket que o Mercado Laser explicitamente não disputa (`future_buyer_segment` do ee-s1-persona-icp — não é prioridade de conversão paga hoje):

```
máquina laser diodo
máquina de corte a laser barata
máquina de corte a laser 1000 reais
máquina de corte a laser caseira
máquina de corte a laser brinquedo
máquina laser shopee
máquina laser aliexpress
aluguel de máquina laser
curso máquina de corte a laser
tutorial máquina de corte a laser
como fazer máquina de corte a laser
peça usada máquina laser
peça segunda mão máquina laser
```

---

## Antes de subir — checklist pro Daniel

1. Validar volume real de busca de cada termo no Keyword Planner (alguns termos de nicho/B2B podem ter volume baixíssimo — ajustar lista conforme dado real)
2. Confirmar pixel Meta + Google instalado e disparando evento de conversão (pré-requisito do diagnóstico de maturidade — sem isso, otimizar essas campanhas é decisão no escuro)
3. Confirmar destino de cada anúncio: CTA de WhatsApp precisa apontar pro número oficial da empresa, não o número antigo configurado no teste do Guilherme (ver ee-s1-diagnostico-maturidade, pilar CRO)
4. Decidir orçamento por campanha — sugestão de proporção: 40% Campanha 1, 15% Campanha 2, 20% Campanha 3, 25% Campanha 4 (ajustável conforme a conversa de forecast da Semana 3)
5. Confirmar se bestbeam.com.br já está publicado antes de ativar a Campanha 4

---

*Alimenta: ee-s2-diagnostico-midia, ee-s3-forecast-midia, ee-s3-copy-anuncios*
