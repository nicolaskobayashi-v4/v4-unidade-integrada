# Diagnóstico de Mídia Paga — Chopp Colina Orlandia
**Skill:** ee-s2-diagnostico-midia | **Gerado em:** 20/06/2026
**Fonte:** Briefing + Reunião S3 (29/05) + Diagnóstico de Criativos + Auditoria de Comunicação

> ⚠️ **Nota metodológica:** executado sem dados V4MOS — este cliente não tem `workspace_id` nem conectores ativos (Meta Ads/Google Ads não estão integrados via API). O diagnóstico usa os dados levantados em reunião e no briefing.

---

## Manchete

> **R$50 por semana, zero pixel, objetivo de engajamento — isso não é mídia paga, é doação para o algoritmo mostrar show ao vivo para quem já segue a conta. Em Franca tem 11.590 buscas por mês sobre chope e chopeira, e ninguém está pagando para aparecer nelas.**

---

## Situação Atual

### Meta Ads

| Item | Status |
|------|--------|
| Investimento | R$50/semana (~R$200-215/mês) |
| Pixel instalado | ❌ Não |
| Objetivo de campanha | Engajamento (errado para o funil de venda) |
| Criativo impulsionado | Show ao vivo — público errado para delivery |
| Segmentação | Inexistente |
| Engajamento resultante | 0,91% — abaixo da faixa esperada (1,5%-3,5%) para varejo alimentício local |

### Google Ads

| Item | Status |
|------|--------|
| Investimento | R$0 |
| Status | Inexistente — zero presença em busca |
| Oportunidade | **11.590 buscas/mês em Franca** sobre chope/chopeira (CPC R$0,34-R$2,00) |
| Busca de marca | ~60 buscas/mês por "Chope Colina" em Franca — demanda reprimida sem captura |

### Landing Page de destino

Inexistente. Qualquer verba de tráfego pago hoje cai no perfil do Instagram, que não converte (conforme `ee-s2-diagnostico-criativos`).

---

## Diagnóstico de Funil

**Topo:** zero captura de demanda de busca. Alcance orgânico baixo (0,91% de engajamento). Mas existe demanda real e medida — 11.590 buscas/mês relacionadas + 60 buscas/mês de marca.

**Meio:** sem pixel, sem remarketing. Quem visualiza conteúdo de delivery e não converte na hora se perde completamente — não há como reabordar.

**Fundo:** WhatsApp sem automação (já mapeado na auditoria). Boosting atual gera curtida, não lead — porque o objetivo de campanha está configurado errado.

---

## Estrutura Recomendada

### Google Ads — R$500/mês

Recomendação validada em reunião S3 (29/05) com Gustavo (INBEB) e Cláudio. Foco total em Search de alta intenção — **não dispersar verba em YouTube** nesse estágio inicial.

**Palavras-chave prioritárias:**
- disk chope franca
- barril de chope franca
- chope delivery franca
- chope colina franca
- chopeira para festa franca

---

### Meta Ads — R$600/mês (mínimo)

Reorganizar o R$50/semana atual numa estrutura de 3 grupos de campanha, definida em reunião S3:

| Grupo | Segmentação | Objetivo | Criativo base |
|-------|-------------|----------|---------------|
| **Aniversariantes do mês** | Pessoas com aniversário no mês, raio Franca/Orlândia | Mensagem WhatsApp | C5 ou C9 (do diagnóstico de criativos) |
| **Churrasco/chopp** | Interesse em churrasco, eventos, cerveja artesanal | Mensagem WhatsApp | C1 (hero shot) + C4 (Reel "como funciona") |
| **Casamentos e eventos** | Noivos, organizadores de evento (Meta identifica datas com precisão) | Mensagem WhatsApp | Foco em confiabilidade + trave congelada |

**Pré-requisito crítico:** instalar pixel Meta antes de qualquer campanha estruturada. Sem isso, não há dado de conversão nem remarketing.

---

## Pré-requisitos Bloqueadores

Antes de qualquer escala de investimento:

1. **Landing Page de Franca** (`ee-s3-landing-page`) — sem ela, todo tráfego pago cai num lugar que não converte
2. **Pixel Meta + Google Tag Manager** instalados na LP
3. **Highlight "Delivery" + carrossel de pilares** no Instagram (já mapeados em `ee-s2-diagnostico-criativos`) — tráfego pago indo para um perfil sem essa informação perde conversão

---

## Investimento Total Recomendado

### Mês 1 — Lançamento Franca

| Canal | Valor |
|-------|-------|
| Google Ads | R$500 |
| Meta Ads | R$600 |
| **Total** | **R$1.100** |

*Mês de lançamento — captura de demanda reprimida + ativação dos 3 grupos de campanha.*

### Mês 2-3 — Consolidação

| Canal | Valor |
|-------|-------|
| Google Ads | R$500-700 (escalar se CPC permitir) |
| Meta Ads | R$600-900 (escalar grupos com melhor performance) |
| **Total estimado** | **R$1.100-1.600** |

*Ajustar com base no CAC real observado no mês 1.*

---

## Métricas de Acompanhamento

- **CAC** (custo de aquisição por cliente fechado)
- **Taxa de conversão mensagem → venda** — Cláudio já cita intuitivamente ~33% na entrevista comercial; formalizar com CRM
- **CPC médio** por grupo de campanha
- **Engajamento orgânico** — meta: saltar de 0,91% para a faixa 1,5%-3,5%
- **Volume de busca de marca** "Chope Colina Franca" ao longo dos meses — indicador de brand awareness orgânico

---

## Ponto de Alavancagem

```
┌──────────────────────────────────────────────────────────────────────┐
│  ⚡ ALAVANCA PRIORITÁRIA                                              │
│                                                                      │
│  "Mudar o objetivo de campanha de 'engajamento' para 'mensagens'    │
│   custa R$0 e pode ser feito hoje, antes de qualquer aumento        │
│   de orçamento."                                                     │
│                                                                      │
│  ▸ É a correção de maior impacto por menor esforço deste            │
│    diagnóstico.                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Alerta Operacional

Não escalar Google Ads ou Meta Ads para Franca antes da Landing Page estar no ar com pixel instalado. Investir em tráfego sem destino de conversão estruturado é o erro mais caro e mais comum em lançamento de praça nova.

---

*Dependências: ee-s1-auditoria-comunicacao ✅ | ee-s2-diagnostico-criativos ✅*
*Alimenta: ee-s3-forecast-midia · ee-s3-landing-page · ee-s3-copy-anuncios · ee-s3-criativos-anuncios*
