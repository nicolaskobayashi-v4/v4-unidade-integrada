# CRM Setup — Chopp Colina Orlandia
**Skill:** ee-s3-crm-setup | **Gerado em:** 21/06/2026
**Plataforma recomendada:** Kommo
**Fonte:** Diagnóstico Comercial (S4) + Entrevista Comercial (05/06) + Persona/ICP + Estimativa de Recompra

---

## Manchete

> **O Cláudio já sabe priorizar lead, já sabe quando reativar cliente, já sabe o motivo de cada venda perdida — só não está escrito em lugar nenhum. O CRM não vai ensinar nada novo a ele: vai registrar o que ele já faz de cabeça, pra sobreviver no dia em que ele não estiver disponível para responder.**

---

## O Problema Atual

Toda a operação comercial roda no WhatsApp pessoal do Cláudio, sem registro estruturado. Base de clientes não mapeada. Decisões de priorização e motivo de perda existem só na memória dele.

**Risco central** (já identificado no diagnóstico comercial, S4): a estrutura de venda está baseada numa pessoa — não escalável sem documentar o processo.

**Consequência prática:** a taxa de recompra que estimamos (~47% blendada) e o CAC usado no forecast são hipóteses, não dados medidos. Sem CRM, nenhuma decisão de investimento em mídia paga pode ser validada com número real.

---

## Estrutura de Pipelines

Dois pipelines separados, espelhando a separação de WhatsApp Business já decidida pela equipe — os ciclos de venda são radicalmente diferentes (fechamento no mesmo dia vs. negociação de semanas).

### Pipeline 1 — Delivery B2C (Anfitrião)
**Ciclo esperado:** mesmo dia a 48h

```
Lead novo → Diagnóstico feito → Orçamento enviado → Confirmação → Entregue/instalado → Pós-venda
                                                          ↓ (sem resposta)
                                                  Não fechou (motivo registrado)
```

### Pipeline 2 — Eventos & Ponto de Revenda
**Ciclo esperado:** 7 a 60 dias

```
Lead/Indicação/Visita → Diagnóstico de necessidade → Proposta enviada → Negociação → Fechado → Cliente ativo recorrente
                                                                              ↓ (sem resposta)
                                                                    Não fechou (motivo registrado)
```

---

## Motivos de Perda Padronizados

Campo obrigatório ao mover um lead para "Não fechou" — sem isso, é impossível saber se o problema é preço ou é velocidade de atendimento.

| Motivo | Nota |
|---|---|
| **Preço** | Identificado na reunião S4 — comparar sempre com a revenda informal (R$9,90/L) |
| **Equipamento** | Ex: cliente queria trave congelada e só foi oferecida chopeira comum |
| **Demora no atendimento** | Cliente oculto comprovou: 5min de atraso = -30% de chance; 20min+ = -95%. Motivo mais evitável e mais crítico de monitorar |
| **Cliente sumiu** | Motivo mais comum, segundo a própria experiência relatada pelo Cláudio na entrevista comercial |
| **Já tem fornecedor** | Aplica principalmente ao Ponto de Revenda |
| **Marca desconhecida / não confiou** | Objeção universal mapeada no persona/ICP — esperado principalmente nos primeiros meses em Franca |

---

## Tags de Segmentação

| Categoria | Tags |
|---|---|
| **Origem do lead** | Orgânico Instagram \| Google Ads \| Meta Ads — Aniversariantes \| Meta Ads — Churrasco/Chopp \| Meta Ads — Casamentos/Eventos \| Indicação \| Visita comercial direta \| PDV mapeado |
| **ICP** | Anfitrião \| Organizador de evento \| Ponto de Revenda |
| **Cidade** | Orlândia \| Franca |

Tags de origem permitem calcular **CAC real por canal** — hoje impossível de medir. Tags de ICP disparam a régua de reativação correta.

---

## Réguas de Automação

### 1. Boas-vindas / triagem inicial
**Gatilho:** primeira mensagem recebida
> *"Opa, boa tarde! Você precisa de chope para delivery (churrasco/evento) ou é sobre a choperia (mesa/reserva)?"*

Replica a triagem que o Cláudio já faz manualmente, formalizada para não perder tempo na pergunta genérica mais recorrente.

### 2. Reativação — Anfitrião
**Gatilho:** 30-45 dias sem novo pedido
> *"Já faz um tempinho que você não pede com a gente — vai ter churrasco esse mês? Separo o barril certo pra você."*

### 3. Reativação — Organizador de evento
**Gatilho:** aproximação de data anual relevante
> *"Faz [X tempo] desde [evento anterior] — já está pensando na próxima edição? Garanto sua data com antecedência."*

### 4. Checagem de reposição — Ponto de Revenda
**Gatilho:** semanal, automático para clientes ativos com comodato
> *"Bom dia! Como está o estoque por lá? Já separo a reposição se precisar."*

### 5. Resgate de orçamento parado
**Gatilho:** orçamento enviado, sem resposta em 48h
> *"Ainda dá tempo de garantir o barril pra sua data — fico no aguardo, é só confirmar."*

Ataca diretamente o motivo de perda mais citado pelo próprio Cláudio: cliente que recebe preço e simplesmente não responde.

---

## Mensagens Rápidas Padronizadas

Cláudio já criou isso intuitivamente no WhatsApp (recurso de atalho "/") — aqui formalizado e expandido:

| Atalho | Mensagem |
|---|---|
| `/tabela` | "O valor do litro do chope é R$11. Barril de 30L sai R$330, barril de 50L sai R$550 — chopeira já inclusa. A gente deixa pronto, instalado no cliente em 5 minutos." |
| `/domingo` | "A gente atende domingo de manhã. Pode mandar mensagem até às 14h." |
| `/consignado` | "Posso deixar um barril extra consignado pro seu evento — você só paga o que consumir." |
| `/duvida_geral` | "Trabalhamos com delivery de chope (entrega na sua casa/evento com chopeira) e também temos a choperia em Orlândia (mesa/reserva). Qual dos dois você precisa?" |

---

## Playbook Comercial Mínimo

Identificado na reunião S4 como necessidade explícita: documentar o que o Cláudio decide de cabeça, para qualquer pessoa nova vender no padrão dele.

**Regras de priorização:**
- Responder por ordem de chegada, exceto quando há cliente de alto volume já em negociação ativa (priorizar volume sobre velocidade pura)
- Cliente recorrente tem prioridade de resposta sobre lead frio
- Fora do horário comercial: ainda responder se possível — dado validado no cliente oculto: resposta rápida fecha mais, independente do horário

**Regras de desconto:** a definir com Cláudio — hoje não documentado. Recomendação: regra fixa por volume (ex: a partir de 300L) para não depender de negociação caso a caso.

**Regras de consignação:** oferecer proativamente para primeiro pedido de cliente novo em Franca, eventos grandes (50+ pessoas), e parcerias B2B em teste.

---

## Integração de Canais

| Canal | Ação |
|---|---|
| **WhatsApp Business** | Separar número delivery/distribuição (qualquer horário) do número da choperia (horário comercial) — decisão já tomada, falta implementar |
| **Meta Ads** | UTM/source tracking nos 3 grupos de campanha alimentando a tag de origem no CRM |
| **Google Ads** | Mesma lógica — permite comparar CAC entre canais com dado real, não estimado |

---

## Métricas de Acompanhamento

- Taxa de conversão por etapa do pipeline (onde está o maior gargalo)
- Taxa de conversão por origem de lead (Google vs. Meta vs. Indicação vs. PDV)
- **CAC real por canal** — substitui a estimativa usada no forecast
- **Taxa de recompra real por ICP** em 90/180/365 dias — substitui a estimativa de ~47% blendada
- Distribuição de motivos de perda
- Tempo médio de resposta (correlacionar com taxa de fechamento)

---

## Plano de Implementação

| Fase | Entrega |
|---|---|
| **Sprint 1** (semana 1) | Criar conta Kommo, configurar os 2 pipelines, migrar contatos existentes |
| **Sprint 2** (semana 2) | Mensagens rápidas + triagem automática + tags de origem/ICP |
| **Sprint 3** (semana 3-4) | Ativar réguas de reativação + integrar UTM dos anúncios |
| **Sprint 4** (mês 2) | Primeiro relatório de métricas reais |
| **Sprint 5** (mês 3) | Validar/corrigir estimativa de recompra e CAC do forecast com dado real |

---

## Ponto de Alavancagem

```
┌──────────────────────────────────────────────────────────────────────┐
│  ⚡ ALAVANCA PRIORITÁRIA                                              │
│                                                                      │
│  "A régua de 'Resgate de orçamento parado' é a peça de maior        │
│   retorno imediato — ataca o motivo de perda mais citado pelo       │
│   próprio Cláudio com automação de custo zero."                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Alerta Operacional

Não migrar toda a operação para o CRM de uma vez. Cláudio já é validado como o melhor atendimento da praça — o risco real é que a ferramenta engesse a flexibilidade de tom que ele usa (formal com médico, descontraído com cliente "mano", conforme mapeado no brandbook). **O CRM deve registrar e automatizar a logística, nunca substituir o tom da conversa.**

---

*Dependências: ee-s1-persona-icp ✅*
*Alimenta: ee-s5-scripts-sdr · ee-s5-sdr-ia-config · ee-revisao-semanal*
