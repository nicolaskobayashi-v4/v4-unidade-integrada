---
name: ee-s3-pdv-gmn
description: "[STUB — conteúdo em desenvolvimento] Audita o perfil (completude, fotos, reviews, posts, insights), faz benchmark vs concorrentes locais e gera plano de ação + tracking de ligações e rotas. Deriva de ee-s3-gmb-otimizacao. Use quando o operador disser /ee-s3-pdv-gmn ou o nome do entregável."
dependencies:
  - ee-s1-arquitetura-presenca
  - ee-s1-persona-icp
  - ee-s2-posicionamento
outputs: ["ee-s3-pdv-gmn.json"]
week: 3
modelo_venda: pdv
estimated_time: "0.75h"
status: stub
---

# Diagnóstico de GMN (Google Meu Negócio)

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 3.2 (PDV)** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Audita o perfil (completude, fotos, reviews, posts, insights), faz benchmark vs concorrentes locais e gera plano de ação + tracking de ligações e rotas. Deriva de ee-s3-gmb-otimizacao.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `pdv`)
- Outputs das dependências: ee-s1-arquitetura-presenca,ee-s1-persona-icp,ee-s2-posicionamento
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 3.2 (PDV). Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s3-pdv-gmn.json`
2. Atualizar `client.json`: progress.skills["ee-s3-pdv-gmn"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
