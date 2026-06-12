---
name: ee-s3-ecom-crm-regua
description: "[STUB — conteúdo em desenvolvimento] Mapeia o ciclo de vida, segmenta a base por RFM e desenha as réguas (boas-vindas, carrinho abandonado, pós-compra, recompra, reativação, datas-chave) com KPIs por régua. Use quando o operador disser /ee-s3-ecom-crm-regua ou o nome do entregável."
dependencies:
  - ee-s3-ecom-funil
outputs: ["ee-s3-ecom-crm-regua.json"]
week: 3
modelo_venda: e-commerce
estimated_time: "1h"
status: stub
---

# Régua de Relacionamento e CRM (E-mail + WhatsApp)

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 3.4 (E-commerce)** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Mapeia o ciclo de vida, segmenta a base por RFM e desenha as réguas (boas-vindas, carrinho abandonado, pós-compra, recompra, reativação, datas-chave) com KPIs por régua.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `e-commerce`)
- Outputs das dependências: ee-s3-ecom-funil
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 3.4 (E-commerce). Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s3-ecom-crm-regua.json`
2. Atualizar `client.json`: progress.skills["ee-s3-ecom-crm-regua"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
