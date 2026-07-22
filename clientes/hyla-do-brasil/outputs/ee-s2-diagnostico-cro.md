# Diagnóstico de CRO — Hyla do Brasil
**Skill:** ee-s2-diagnostico-cro | **Gerado em:** 08/07/2026
**Fonte:** PageSpeed Insights (home + landing page, mobile + desktop, lab + campo) + export GA4 "Páginas e telas" + estrutura extraída do HTML da landing page

> ⚠️ **Achado prioritário, fora do escopo técnico usual.** O export do GA4 mostra mais de 150 URLs de spam (`/3ytn/...`, temas aleatórios sem relação com o negócio) recebendo tráfego — resíduo do hackeamento do site (conteúdo de apostas/cassino) já mencionado pelo time na reunião de 08/07. Tratar isso tem prioridade sobre qualquer otimização de conversão.

---

## Manchete

> **A landing page carrega 2,18MB de JavaScript não usado e reprova nas Core Web Vitals reais — e o site ainda carrega resíduo de spam do hackeamento recente.**

---

## Números-chave

| Métrica | Landing page | Home institucional |
|---|---|---|
| Performance (mobile) | 43/100 | **20/100** |
| Performance (desktop) | 44/100 | 22/100 |
| LCP — laboratório (mobile) | 6,5s | **21,1s(!)** |
| LCP — campo/real (mobile) | 4,1s — reprovado | não aplicável (dado insuficiente) |
| CLS — laboratório (mobile) | 0 (ótimo) | 0,183 |
| CLS — laboratório (desktop) | 0 (ótimo) | **0,586** (limite bom = 0,1) |
| TBT (mobile) | 670ms | 2.150ms |
| JS não usado | **2,18 MB** | — |
| Best Practices | 54/100 | 73/100 |
| Acessibilidade | 93/100 | 83/100 |
| SEO | 100/100 | 100/100 |
| Tempo médio de engajamento (GA4, LP) | **~4 segundos** | ~3,5 segundos |

---

## Achado de Segurança — Resíduo do Hackeamento

**Evidência:** no export completo do GA4 (1/jan-7/jul/2026), mais de 150 URLs distintas sob `/3ytn/` recebem tráfego (1-2 visualizações cada), com títulos totalmente alheios ao negócio — temas aleatórios em inglês, incluindo conteúdo adulto. Bate com o relato do próprio time na reunião de 08/07: o site foi hackeado com conteúdo de apostas/cassino, o que chegou a bloquear as campanhas do Google Ads.

**Impacto:** risco de penalização/desindexação pelo Google, desperdício de crawl budget, risco reputacional.

**Ação recomendada (prioridade máxima):**
1. Confirmar com o time de dev/hosting que a limpeza foi completa — não só o desbloqueio das campanhas
2. Rodar varredura de malware no servidor
3. Submeter as URLs de spam para remoção no Google Search Console
4. Verificar se há outras pastas suspeitas além de `/3ytn/`

---

## Diagnóstico Técnico

**Landing page (`/aspirador-hyla-do-brasil/`):**
- LCP real de usuários: 4,1s — **reprovado** pelas Core Web Vitals (limite bom: 2,5s)
- Maior oportunidade: 2,18MB de JavaScript não utilizado, causa raiz provável da lentidão
- HTTPS mal implementado: 22 solicitações inseguras, **HSTS com max-age=0** (efetivamente desativado), sem CSP, sem X-Frame-Options — Best Practices cai para 54/100

**Home institucional (pior que a LP):**
- Performance 20/100 mobile, LCP de laboratório de **21,1 segundos**
- CLS de laboratório de 0,586 em desktop — a página "pula" muito durante o carregamento

**SEO on-page da landing page:** já está bem cuidado — title (41 caracteres), meta description (158 caracteres, no limite superior do ideal), 1 H1 correto, 23 imagens todas com alt, 3 blocos de schema.org, SEO 100/100.

---

## Auditoria de Copy (Landing Page)

**Acima da dobra:**
- Headline: "HYLA do Brasil: O aspirador de pó que vai além da limpeza"
- Subheadline: sobre poluição do ar interno (5x mais que o externo)
- CTA: "Agendar uma demonstração"

**Estrutura:** Hero → Benefícios → Aplicações → 8 Depoimentos → Processo em 3 passos → FAQ (11 perguntas) → Selos de confiança → Formulário (7 campos) → Rodapé

**Problemas identificados:**
- Formulário só no final (já sinalizado por Natália em `ee-s2-diagnostico-criativos`)
- 7 campos no formulário — mais atrito que o necessário para topo de funil
- Selos de confiança (INMETRO, ISO 9001, "80+ países") só aparecem perto do formulário — quem abandona antes nunca vê

---

## Hipóteses de Teste

| # | Hipótese | Prioridade | Esforço | Impacto esperado |
|---|---|---|---|---|
| 1 | Resolver 2,18MB de JS não usado → LCP <2,5s | Alta | Médio-alto | Alto |
| 2 | Limpar infestação de spam (`/3ytn/`, 150+ URLs) | Alta (segurança) | Médio | Defensivo |
| 3 | Ativar HSTS corretamente, eliminar mixed content | Alta | Baixo | Médio |
| 4 | Formulário curto na primeira dobra | Média* | Baixo | Não mensurável ainda |
| 5 | Substituir imagem final de baixa qualidade | Média | Baixo | Médio |

*\*Só testável com confiança depois do evento de conversão dedicado ser implementado (ee-s2-diagnostico-midia, ação P1).*

## Melhorias para Wireframe (alimenta `ee-s3-landing-page`)

1. Formulário curto (nome + telefone + cidade) na primeira dobra, mantendo o completo no final
2. Resolver peso técnico antes de qualquer redesenho visual
3. Selo de confiança já na primeira dobra
4. Substituir imagem final por fotografia em maior resolução
5. Aplicar a nova identidade visual só depois do manual oficial (13/08) — evitar redesenhar duas vezes

---

## Ponto de Alavancagem

> **A landing page não precisa de mais copy nem de redesign agora — precisa parar de perder gente antes de carregar.**

1. 82,5% do tráfego pago vem de mobile — exatamente o dispositivo com LCP reprovado.
2. 2,18MB de JS não usado é o maior item de oportunidade técnica — resolver isso tem efeito cascata em LCP, TBT e Speed Index.
3. O resíduo de spam do hackeamento é risco de penalização do Google, não só de conversão — prioridade máxima.

**💬 Momento de validar com Davi/Fábio:** a sequência certa é (1) confirmar limpeza completa do hack, (2) resolver performance técnica, (3) só depois testar copy/layout — na ordem errada, qualquer ganho de mensagem é mascarado pela lentidão e pelo risco de segurança.

---

*Alimenta: `ee-s3-landing-page`, `ee-s3-forecast-midia`, `ee-revisao-semanal`*
