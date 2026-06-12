---
name: ee-s3-pdv-base-ativa
description: "[STUB — conteúdo em desenvolvimento] Consolida e qualifica a base ativa (ERP/planilha/caixa), revela a curva de Pareto e o comportamento de recompra, e crava o gargalo da base com receita recuperável. Use quando o operador disser /ee-s3-pdv-base-ativa ou o nome do entregável."
dependencies:
  - ee-s1-persona-icp
  - ee-s2-posicionamento
  - ee-s2-pesquisa-mercado
outputs: ["ee-s3-pdv-base-ativa.json"]
week: 3
modelo_venda: pdv
estimated_time: "2h"
status: stub
---

# Diagnóstico da Base Ativa e Controle de Vendas

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 3.1 (PDV)** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Consolida e qualifica a base ativa (ERP/planilha/caixa), revela a curva de Pareto e o comportamento de recompra, e crava o gargalo da base com receita recuperável.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `pdv`)
- Outputs das dependências: ee-s1-persona-icp,ee-s2-posicionamento,ee-s2-pesquisa-mercado
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 3.1 (PDV). Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s3-pdv-base-ativa.json`
2. Atualizar `client.json`: progress.skills["ee-s3-pdv-base-ativa"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
