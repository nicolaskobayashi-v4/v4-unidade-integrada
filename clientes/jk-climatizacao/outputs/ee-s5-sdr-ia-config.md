# Configuração SDR IA (Patagon) — JK Climatização
**Skill:** ee-s5-sdr-ia-config | **Gerado em:** 09/07/2026
**Fonte:** ee-s5-scripts-sdr + ee-s4-diagnostico-comercial + ee-s1-persona-icp

---

## Manchete

> **A configuração está pronta pra ativar — falta só a JK decidir o CRM (Kommo ou outro) e o operador validar o tom com o time antes de ligar o agente de verdade.**

---

## ⚠️ Dependência em aberto

`ee-s3-crm-setup` segue pendente. A JK **não tem CRM hoje** — usa WhatsApp + planilha + um ERP interno ("RP"/"ORP") só de consulta, e uma tentativa anterior de sistema de gestão de campo (~R$80.000 investidos) nunca foi adotada pela equipe. Este documento assume, como **hipótese de trabalho**, uma estrutura de pipeline Kommo equivalente ao padrão usado em outras contas da V4 — a escolha real da ferramenta precisa ser confirmada com o operador antes de qualquer configuração entrar em produção.

**Enquanto isso:** o fluxo abaixo pode ser seguido manualmente por Pedro via WhatsApp, usando os scripts de `ee-s5-scripts-sdr`.

---

## Fluxo Único — Qualificação e Roteamento

Cobre da chegada do lead (WhatsApp direto, Instagram ou site) até o **handoff humano** — o agente não fecha orçamento sozinho em nenhum score.

| Etapa | Ação |
|---|---|
| Boas-vindas | Aplica roteiro por canal, identifica B2B vs B2C |
| Qualificação | 5 perguntas → calcula score 1-5⭐ |
| Roteamento | 4-5⭐ → handoff Marlon/André · 2-3⭐ → segue com Pedro · 1⭐ → desqualifica |
| Registro | Nome, telefone, canal, score, respostas → CRM (a confirmar) |
| Follow-up automatizado | Cadência D+1/D+3/D+7 para score 2-5⭐ |
| Escalonamento | Aciona gatilhos humanos quando aplicável |

---

## Campos Mapeados no CRM

| Campo | Origem |
|---|---|
| Nome e telefone | 1ª interação |
| Canal de origem | WhatsApp / Instagram / Site |
| Segmento (B2B/B2B2C/B2C) | Pergunta 1 |
| Nº de aparelhos (se B2B) | Pergunta 2 |
| Cidade / dentro do raio? | Pergunta 3 |
| Urgência | Pergunta 4 |
| Score 1-5⭐ | Calculado automaticamente |
| Status no funil | Lead → Conexão → Qualificação → Proposta → Follow-up → Ganho/Perdido → Onboarding → Retenção |
| Tentativas de follow-up | Contador incremental |

---

## Gatilhos de Escalonamento Humano

| Gatilho | Ação |
|---|---|
| Score 4-5⭐ qualificado | Handoff imediato Marlon (4⭐) / André (5⭐) |
| Objeção não resolvida em 2 tentativas | Escalar para humano |
| Cliente pede técnico/responsável | Handoff imediato |
| Sem resposta após 12 tentativas | Marca "frio" no CRM, não insiste mais |

---

## Testes com Leads Simulados

| Persona | Cenário esperado |
|---|---|
| CFO de indústria têxtil (15 aparelhos, Blumenau, máquina parando) | 5⭐ → handoff imediato pra André, com objeção de preço pronta |
| Arquiteta de BC, obra de luxo em alvenaria | 4⭐ → qualifica fase da obra, handoff com contexto resumido |
| Empresa pequena (6 aparelhos, sem urgência) | 3⭐ → segue com Pedro, cadência padrão |
| Residencial avulso, fora do raio (Rio do Sul) | 1⭐ → desqualificação educada, sem cadência |
| Lead comparando com MEI mais barato | Testa resposta de objeção (ART/checklist/SLA), não entra em guerra de preço |

---

## 💬 Ponto de Alavancagem — Discussão com Stakeholder

> **O agente não substitui o instinto comercial que Pedro já demonstrou — ele aplica essa mesma disciplina em escala, inclusive fora do horário comercial e no inverno, quando a JK hoje praticamente não trabalha o funil.**

1. A cadência D+1/D+3/D+7 só vira hábito real se algo executa sem depender de lembrete manual — hoje ninguém faz isso
2. O agente cobre o vale comercial do inverno — é onde a reativação sazonal (D+30/60/90) tem mais a ganhar
3. O critério de desqualificação (1⭐) precisa estar no agente, não só na cabeça de quem atende

**Ponto de discussão:** revisar os scripts com André, Sabrina e Pedro antes de ativar — e decidir junto qual CRM vai sustentar isso.

---

## ⚠️ Alerta de Honestidade

Este documento configura o **comportamento** do agente, mas não substitui a decisão pendente sobre CRM (`ee-s3-crm-setup`) nem testa com leads reais — os 5 cenários acima são hipotéticos, construídos a partir das personas já mapeadas. Validar com leads reais atendidos manualmente por Pedro antes de ativar em produção.

---

## Pendente de Confirmação

- Qual CRM a JK vai efetivamente adotar (Kommo ou outra ferramenta)
- Acesso ao Patagon e quem no time vai operar a ativação
- Validar os 5 leads simulados e o tom com André, Sabrina e Pedro
- Quem recebe o alerta humano de escalonamento no dia a dia (hoje ambíguo entre Marlon e André)
