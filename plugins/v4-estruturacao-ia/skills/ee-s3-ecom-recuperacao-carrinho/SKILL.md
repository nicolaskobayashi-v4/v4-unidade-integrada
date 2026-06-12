---
name: ee-s3-ecom-recuperacao-carrinho
description: "[STUB — conteúdo em desenvolvimento] Fluxo multi-canal de carrinho abandonado (T+1h/24h/72h) com variação de copy por objeção, política de cupom, régua pós-compra e cross-sell/up-sell. Use quando o operador disser /ee-s3-ecom-recuperacao-carrinho ou o nome do entregável."
dependencies:
  - ee-s3-ecom-funil
  - ee-s3-ecom-crm-regua
outputs: ["ee-s3-ecom-recuperacao-carrinho.json"]
week: 3
modelo_venda: e-commerce
estimated_time: "1h"
status: stub
---

# Recuperação de Carrinho e Pós-Venda

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 3.5 (E-commerce)** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Fluxo multi-canal de carrinho abandonado (T+1h/24h/72h) com variação de copy por objeção, política de cupom, régua pós-compra e cross-sell/up-sell.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `e-commerce`)
- Outputs das dependências: ee-s3-ecom-funil,ee-s3-ecom-crm-regua,ee-s3-manual-marca
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 3.5 (E-commerce). Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s3-ecom-recuperacao-carrinho.json`
2. Atualizar `client.json`: progress.skills["ee-s3-ecom-recuperacao-carrinho"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
