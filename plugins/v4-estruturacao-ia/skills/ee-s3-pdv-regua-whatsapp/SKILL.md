---
name: ee-s3-pdv-regua-whatsapp
description: "[STUB — conteúdo em desenvolvimento] Réguas pré/durante/pós-visita, handoff digital para físico, pós-compra, reativação, listas segmentadas e política API vs comum (HSM). Reduz no-show. Use quando o operador disser /ee-s3-pdv-regua-whatsapp ou o nome do entregável."
dependencies:
  - ee-s3-pdv-gmn
  - ee-s3-pdv-experiencia
outputs: ["ee-s3-pdv-regua-whatsapp.json"]
week: 3
modelo_venda: pdv
estimated_time: "0.75h"
status: stub
---

# Régua de WhatsApp para Fluxo de Loja

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 3.5 (PDV)** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Réguas pré/durante/pós-visita, handoff digital para físico, pós-compra, reativação, listas segmentadas e política API vs comum (HSM). Reduz no-show.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `pdv`)
- Outputs das dependências: ee-s3-pdv-gmn,ee-s3-pdv-experiencia,ee-s3-manual-marca
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 3.5 (PDV). Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s3-pdv-regua-whatsapp.json`
2. Atualizar `client.json`: progress.skills["ee-s3-pdv-regua-whatsapp"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
