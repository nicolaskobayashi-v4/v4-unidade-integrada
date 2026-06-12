---
name: ee-s3-ecom-cro
description: "[STUB — conteúdo em desenvolvimento] Audita PDP, carrinho e checkout, mapeia o funil de conversão por etapa e gera hipóteses de teste A/B priorizadas por ICE. Deriva de ee-s2-diagnostico-cro. Use quando o operador disser /ee-s3-ecom-cro ou o nome do entregável."
dependencies:
  - ee-s2-posicionamento
  - ee-s1-persona-icp
outputs: ["ee-s3-ecom-cro.json"]
week: 3
modelo_venda: e-commerce
estimated_time: "1h"
status: stub
---

# Diagnóstico de CRO de E-commerce (Checkout + PDP + Carrinho)

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 3.1 (E-commerce)** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Audita PDP, carrinho e checkout, mapeia o funil de conversão por etapa e gera hipóteses de teste A/B priorizadas por ICE. Deriva de ee-s2-diagnostico-cro.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `e-commerce`)
- Outputs das dependências: ee-s2-posicionamento,ee-s1-persona-icp
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 3.1 (E-commerce). Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s3-ecom-cro.json`
2. Atualizar `client.json`: progress.skills["ee-s3-ecom-cro"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
