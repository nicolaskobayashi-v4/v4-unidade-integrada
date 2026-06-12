---
name: ee-s1-arquitetura-presenca
description: "[STUB — conteúdo em desenvolvimento] Mapeia inventário de ativos digitais, identifica a porta de entrada real, mapeia hand-offs entre canais e recomenda a arquitetura mínima viável (Nível 1-4) adequada ao estágio do cliente. Use quando o operador disser /ee-s1-arquitetura-presenca ou o nome do entregável."
dependencies:
  - ee-s1-persona-icp
outputs: ["ee-s1-arquitetura-presenca.json"]
week: 1
modelo_venda: comum
estimated_time: "1h"
status: stub
---

# Arquitetura de Presença Digital

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 1.8** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Mapeia inventário de ativos digitais, identifica a porta de entrada real, mapeia hand-offs entre canais e recomenda a arquitetura mínima viável (Nível 1-4) adequada ao estágio do cliente.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `comum`)
- Outputs das dependências: ee-s1-persona-icp
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 1.8. Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s1-arquitetura-presenca.json`
2. Atualizar `client.json`: progress.skills["ee-s1-arquitetura-presenca"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
