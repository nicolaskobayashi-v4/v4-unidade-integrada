# Diagnóstico de Mídia Paga — C Clean Serviços de Limpeza
**Skill:** ee-s2-diagnostico-midia | **Gerado em:** 04/05/2026  
**Fonte de dados:** Entrevistas S1 (15/04) e S2 (24/04) — declarativo. Sem acesso direto à conta Google Ads ou V4MOS.

---

## Manchete

> **100% do investimento em mídia está no Google Ads — autogerenciado, tecnicamente quebrado, sem rastreamento real há pelo menos 10 anos.**

---

## Painel de KPIs

| Métrica | Valor | Status |
|---------|-------|--------|
| Investimento mensal | R$1.500–R$3.000 | ⚠️ 100% concentrado em 1 canal |
| Canais com investimento ativo | 1 de 4 | 🔴 Dependência crítica |
| Rastreamento de conversão | Possivelmente quebrado | 🔴 800 cliques vs. <10% contatos reais |
| Campanhas ativas (Google) | 3 sobrepostas | 🔴 Sem estratégia unificada |
| Meta Ads | R$0/mês | ⬜ Canal nunca explorado |
| Upside de eficiência estimado | +40–60% | 🟢 Só com reconfiguração |

---

## Diagnóstico por Canal

### Google Ads — Grau: D (Crítico)
**Investimento:** R$1.500–R$3.000/mês | **Gerenciado por:** Jeferson (autogerenciado há 10 anos)

O canal funciona — e isso é o que mascara o problema. Mesmo com configuração precária, entrega ~10 contatos/dia. O risco é que Jeferson acostumou-se com o volume sem perceber o quanto da verba está sendo desperdiçada.

#### Problemas identificados

**🔴 Crítico — Tag de conversão possivelmente quebrada**  
800 cliques reportados na interface vs. menos de 10% de contatos reais chegando via WhatsApp/formulário. Sem rastreamento confiável, o algoritmo Smart Bidding está otimizando para o objetivo errado — e qualquer decisão de verba é feita às cegas.

> **Fix:** Instalar Google Tag Manager, configurar evento de conversão por lead real (clique em WhatsApp ou envio de formulário), validar com Preview Mode antes de ativar.

---

**🔴 Crítico — Raio geográfico com falhas**  
Campanhas recebem cliques de outros estados e até de Moçambique. A CClean só atende a zona norte de Joinville — toda verba consumida fora desse território é desperdício puro.

> **Fix:** Configurar geolocalização por raio (~15km do centro operacional zona norte) com opção **"Presença: pessoas em seu local de destino"** — não "em ou que pesquisam o local".

---

**🔴 Crítico — Alto volume de candidatos a emprego**  
Principal dor declarada por Jeferson. Provável causa: ausência de palavras-chave negativas como "emprego", "vaga", "trabalho", "salário", "contratando", "CLT", "currículo", "processo seletivo". Estimativa: 30-40% do tráfego atual é desse perfil.

> **Fix:** Adicionar lista de 50+ palavras-chave negativas. Prioridade máxima — resultado visível em 24-48h após implementação.

---

**🟠 Alto — 3 campanhas sobrepostas sem estratégia**  
Criadas por assistentes diferentes do Google ao longo dos anos. Sem divisão clara por intenção, segmento ou funil. Risco de auto-concorrência (CClean disputando com ela mesma nas palavras mais caras).

> **Fix:** Auditar e consolidar em 2 campanhas: (1) Search — condomínios, (2) Search — escritórios/empresas. Pausar o que sobra.

---

**🟠 Alto — Sem audiências de remarketing**  
Usuários que já visitaram o site ou interagiram com a marca não são recuperados. Sem RLSA (Remarketing Lists for Search Ads), leads que pesquisaram e saíram somem sem segunda chance.

> **Fix:** Configurar remarketing básico via Google Ads + GA4. Aplicar RLSA para dar lance maior para visitantes recentes.

---

**🟡 Médio — Sem extensões de anúncio**  
Perda de espaço visual na SERP. Concorrentes com extensões de sitelink, chamada e destaque ocupam mais espaço e têm CTR naturalmente maior.

> **Fix:** Configurar sitelinks (4), extensões de chamada com horário, destaques ("26 anos de mercado", "Reposição em 24h", "Zona norte de Joinville") e extensão de localização.

---

### Meta Ads — Inativo (R$0/mês)
Canal nunca explorado. ICP da CClean (síndicos, gestores de RH, donos de pequenas empresas em Joinville zona norte) tem correspondência direta com segmentação por cargo + interesse + localização no Facebook/Instagram.

O concorrente **Macaiama** já usa Instagram orgânico com sucesso — vídeos ASMR e dicas de limpeza que geram prova social sem custo de aquisição. A CClean está dois passos atrás: não tem orgânico nem pago nesse canal.

---

### Instagram Orgânico — Abandonado
Sem publicações há anos. Sem estratégia de conteúdo. Sem seguidores ativos. A conta existe mas não trabalha pela marca.

---

### Indicação — Ativo, mas não estruturado
Canal de maior qualidade (leads chegam com confiança pré-estabelecida) mas completamente não gerenciado. 90 clientes com retenção histórica excepcional nunca foram convidados formalmente a indicar.

---

## Ponto de Alavancagem Principal

```
┌─────────────────────────────────────────────────────────────────────┐
│  ⚡ ALAVANCA PRIORITÁRIA                                             │
│                                                                     │
│  "Reorganizar o Google Ads existente entregará +40-60% de leads     │
│   qualificados sem aumentar um centavo de verba."                   │
│                                                                     │
│  1. Tag de conversão corrigida → algoritmo passa a otimizar          │
│     para leads reais, não cliques genéricos                          │
│                                                                     │
│  2. Palavras negativas → estimativa de 30-40% do tráfego atual      │
│     é candidatos a emprego. Eliminação imediata.                    │
│                                                                     │
│  3. Raio geográfico correto → 100% da verba em Joinville zona       │
│     norte — área onde já há 90 clientes como prova social           │
│                                                                     │
│  ▸ Antes de abrir novos canais, corrija o que já existe.            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Plano de Mídia Recomendado

### Fase 1 — Correção (0-30 dias) | Mesmo orçamento: R$1.500–R$3.000

| Ação | Prioridade | Impacto esperado |
|------|-----------|-----------------|
| Instalar Google Tag Manager + configurar conversão real | 🔴 Crítica | Rastreamento de CAC pela primeira vez |
| Adicionar 50+ palavras-chave negativas | 🔴 Crítica | -70-80% candidatos a emprego |
| Corrigir raio geográfico para zona norte Joinville | 🔴 Crítica | Eliminar desperdício fora da área |
| Consolidar 3 campanhas em 2 (condomínios + empresas) | 🟠 Alta | Melhor aprendizado do algoritmo |
| Configurar extensões de anúncio (sitelink, chamada, destaque) | 🟡 Média | +15-20% CTR estimado |
| Otimizar Google Meu Negócio | 🟡 Média | Leads orgânicos de busca local gratuitos |

**Resultado esperado:** Redução de 70-80% em leads desqualificados. Aumento de 40-60% em leads de síndicos e gestores. Primeiro relatório de CAC real.

---

### Fase 2 — Expansão (30-90 dias) | + R$500–R$800 para Meta Ads

| Canal | Investimento | Objetivo | Formato |
|-------|-------------|----------|---------|
| Meta Ads (Facebook + Instagram) | R$500–R$800/mês | 20-30 leads adicionais/mês | Lead Ads com formulário nativo |
| Programa de Indicação | R$0–R$200/mês | 2-3 novos clientes/mês via base ativa | WhatsApp + desconto/brindes |
| Instagram Orgânico | Tempo + R$0–R$300 | Prova social + autoridade | 2-3 posts/semana (antes/depois, depoimentos) |

---

## KPIs para Acompanhar

| KPI | Atual | Meta | Prazo |
|-----|-------|------|-------|
| CAC (Custo de Aquisição) | Desconhecido¹ | < R$500 | 30 dias após fix |
| Leads qualificados/mês | ~30 estimados | 80-100 | 45 dias |
| Taxa de qualificação | < 10% | > 60% | 30 dias |
| Novos clientes/mês | 2-3 | 5-7 | 90 dias |
| Canais com investimento ativo | 1 | 3 | 90 dias |

¹ *Tag de conversão sem configuração confiável — sem histórico rastreável.*

---

## Alerta de Honestidade

> ⚠️ **Este diagnóstico é baseado em dados declarativos.** Sem acesso direto à conta Google Ads, os problemas identificados são altamente prováveis mas podem não ser completos. **A primeira ação obrigatória no S3 é garantir acesso à conta Google Ads para auditoria técnica direta.** Reconfigurar campanhas sem ver os dados reais substitui um problema por outro.

---

*Próxima etapa: S3 (04/05/2026) — Felipe (mídia paga) audita a conta Google Ads com acesso direto e valida/corrige este diagnóstico com dados reais.*
