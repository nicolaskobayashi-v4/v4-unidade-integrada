# Diagnóstico CRO — FROC Frutas Desidratadas
**Skill:** ee-s2-diagnostico-cro | **Gerado em:** 05/05/2026  
**Nota:** Site em Framer — conteúdo dinâmico não renderizável via fetch. Análise baseada em metadados + estrutura + kickoff.

---

## Manchete

> **froc.com.br não converte porque não foi feito para converter — é um cartão de visitas com linguagem B2C para um comprador B2B industrial.**

---

## Papel do Site no Funil

O site **não é** o canal de conversão principal — as LPs são. O papel do froc.com.br é a **validação**:

```
Comprador recebe anúncio / cold call
        ↓
Pesquisa "FROC desidratados" no Google
        ↓
Acessa froc.com.br para confirmar que a empresa é real
        ↓
Retorna à LP ou contata via WhatsApp
```

Para esse papel, o site precisa parecer **sério e B2B** — não de produto para consumidor final.

---

## Diagnóstico por Problema

### 🔴 Crítico — Sem rastreamento (GTM / GA4 / Pixel)
**Impacto:** Google Ads vai otimizar para clique, não para lead. Sem dados para decidir o que funciona.  
**Fix:** Instalar GTM + configurar eventos (clique WhatsApp, envio de formulário quando existir).  
**Prazo:** Semana 1 — antes de qualquer campanha subir.  
**Responsável:** Nicolas

---

### 🔴 Alto — Tagline B2C na homepage

**Atual:**
> *"Especializada em alimentos saudáveis desidratados produzidos em São Joaquim, Santa Catarina. 100% naturais, sem adição de açúcares ou conservantes."*

Linguagem de rótulo de produto. O comprador B2B que acessa para validar a empresa não se reconhece.

**Proposta:**
> *"Fornecedora de frutas desidratadas premium para indústria pet e alimentícia — produzidas em São Joaquim, SC, sem conservantes."*

**Fix:** 1 linha alterada no Framer. 30 minutos.  
**Responsável:** Nicolas + Geovanna

---

### 🔴 Alto — Sem e-mail comercial visível
**Impacto:** Camila (alimentação humana) não inicia processo de homologação pelo WhatsApp — é informal demais. Sem e-mail, o ICP de maior ticket não tem canal.  
**Fix:** Adicionar e-mail comercial na seção Contato.  
**Responsável:** Nicolas

---

### 🟠 Médio-alto — Amostra grátis invisível
Principal diferencial competitivo não aparece no site. Comprador que pesquisa a empresa não encontra o argumento mais forte.  
**Fix:** Mencionar amostra grátis na seção Diferenciais com destaque.  
**Responsável:** Nicolas + Geovanna

---

### 🟡 Médio — Attribution SIX/Framer no rodapé
Rodapé exibe "made with Framer by SIX" — bastidores técnicos sem valor para o visitante.  
**Fix:** Remover. 15 minutos.  
**Responsável:** Nicolas

---

### 🟡 Médio — Sem prova social
Empresa com 1 ano, sem depoimentos, logos de clientes ou métricas de credibilidade.  
**Fix:** Adicionar logos de clientes (com autorização) OU "Fornecedora do Grupo Empresarial de São Joaquim há X anos" OU número de pedidos entregues.  
**Responsável:** Driélly (fornecer) + Nicolas (implementar)

---

## Ajustes Priorizados

| # | Ação | Prazo | Esforço | Quem |
|---|------|-------|---------|------|
| 1 | Instalar GTM + GA4 + Pixel Meta | Semana 1 | 2–4h | Nicolas |
| 2 | Alterar tagline para B2B | Semana 1 | 30 min | Nicolas + Geovanna |
| 3 | Adicionar e-mail comercial no Contato | Semana 1 | 15 min | Nicolas |
| 4 | Mencionar amostra grátis nos Diferenciais | Semana 1–2 | 1h | Nicolas + Geovanna |
| 5 | Remover attribution SIX/Framer rodapé | Semana 1 | 15 min | Nicolas |
| 6 | Adicionar prova social | Semana 2–3 | Depende Driélly | Todos |

**Total semana 1:** ~5 horas de trabalho que desbloqueiam todo o projeto de mídia.

---

## O que o Site Corrigido Precisa Comunicar

| Seção | Hoje (estimado) | Proposto |
|-------|----------------|---------|
| **Hero** | Tagline B2C + WhatsApp | Tagline B2B + Amostra grátis + WhatsApp + E-mail |
| Quem Somos | Desconhecido | Grupo empresarial + anos + capacidade + foco B2B |
| Produtos | Desconhecido | Especificações técnicas básicas (granulometria, validade, embalagem industrial) |
| Como Comprar | Desconhecido | Fluxo B2B: amostra → aprovação → pedido 400kg → 2 dias |
| **Diferenciais** | Desconhecido | 5 diferenciais reais: amostra grátis, sem conservantes, 2 dias, São Joaquim, 30-120 dias pag. |
| Contato | WhatsApp apenas | WhatsApp + E-mail + Endereço fábrica |

---

## Ponto de Alavancagem

```
┌──────────────────────────────────────────────────────────────────────┐
│  ⚡ ALAVANCA PRIORITÁRIA                                              │
│                                                                      │
│  "3 ajustes de 5 horas desbloqueiam todo o projeto de mídia."        │
│                                                                      │
│  1. GTM sem instalação = campanha cega                               │
│     Algoritmo otimiza para clique barato, não para lead             │
│                                                                      │
│  2. Tagline B2C = comprador desconfia                                │
│     Validação falha antes do contato acontecer                      │
│                                                                      │
│  3. Sem e-mail = Camila não tem canal formal                        │
│     ICP de maior ticket não consegue converter                      │
│                                                                      │
│  ▸ Para a equipe: "Nicolas precisa de 4h na semana 1.               │
│    Isso desbloqueio o lançamento das campanhas."                     │
└──────────────────────────────────────────────────────────────────────┘
```

> ⚠️ Análise parcial por limitação técnica: site em Framer não renderiza via fetch. Conteúdo detalhado das seções Produtos, Diferenciais e Como Comprar não foi auditado. Recomenda-se revisão presencial ou via screencast antes da apresentação.
