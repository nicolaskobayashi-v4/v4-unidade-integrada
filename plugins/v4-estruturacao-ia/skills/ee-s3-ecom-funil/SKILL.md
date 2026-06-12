---
name: ee-s3-ecom-funil
description: "[STUB — conteúdo em desenvolvimento] Mapeia o funil completo (Aquisição→Visita→PDP→Carrinho→Checkout→Pago→Entregue→Recompra), crava o gargalo primário e quantifica a receita recuperável. Use quando o operador disser /ee-s3-ecom-funil ou o nome do entregável."
dependencies:
  - ee-s3-ecom-cro
  - ee-s1-persona-icp
  - ee-s2-pesquisa-mercado
outputs: ["ee-s3-ecom-funil.json"]
week: 3
modelo_venda: e-commerce
estimated_time: "2h"
status: stub
---

# Diagnóstico do Funil de Vendas E-commerce

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 3.2 (E-commerce)** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Mapeia o funil completo (Aquisição→Visita→PDP→Carrinho→Checkout→Pago→Entregue→Recompra), crava o gargalo primário e quantifica a receita recuperável.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `e-commerce`)
- Outputs das dependências: ee-s3-ecom-cro,ee-s1-persona-icp,ee-s2-pesquisa-mercado
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 3.2 (E-commerce). Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s3-ecom-funil.json`
2. Atualizar `client.json`: progress.skills["ee-s3-ecom-funil"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
