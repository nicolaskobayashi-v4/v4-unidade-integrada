---
name: ee-s3-is-pipeline
description: "[STUB — conteúdo em desenvolvimento] Pipeline de 5-7 etapas com critério de avanço, réguas (boas-vindas, nutrição, no-show, reativação), script consultivo SPIN e mapa de objeções para respostas. Use quando o operador disser /ee-s3-is-pipeline ou o nome do entregável."
dependencies:
  - ee-s4-diagnostico-comercial
  - ee-s4-cliente-oculto
  - ee-s1-persona-icp
  - ee-s2-posicionamento
outputs: ["ee-s3-is-pipeline.json"]
week: 3
modelo_venda: inside-sales
estimated_time: "1h"
status: stub
---

# Pipeline Comercial + Réguas + Script Consultivo

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 3.5 (Inside Sales)** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Pipeline de 5-7 etapas com critério de avanço, réguas (boas-vindas, nutrição, no-show, reativação), script consultivo SPIN e mapa de objeções para respostas.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `inside-sales`)
- Outputs das dependências: ee-s4-diagnostico-comercial,ee-s4-cliente-oculto,ee-s1-persona-icp,ee-s2-posicionamento
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 3.5 (Inside Sales). Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s3-is-pipeline.json`
2. Atualizar `client.json`: progress.skills["ee-s3-is-pipeline"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
