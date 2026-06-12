---
name: ee-s3-pdv-experiencia
description: "[STUB — conteúdo em desenvolvimento] Cliente oculto remoto (WhatsApp/telefone) mais análise estruturada de reviews por tema e sentimento, com avaliação por dimensão e gaps críticos priorizados. Use quando o operador disser /ee-s3-pdv-experiencia ou o nome do entregável."
dependencies:
  - ee-s3-pdv-gmn
  - ee-s1-persona-icp
outputs: ["ee-s3-pdv-experiencia.json"]
week: 3
modelo_venda: pdv
estimated_time: "1h"
status: stub
---

# Diagnóstico de Experiência do PDV (Remoto)

> **⚠️ STUB** — Esqueleto criado na reorganização do modelo de entrega. Implementa **POP 3.4 (PDV)** dos POP-books da V4. O conteúdo de geração (frameworks, passo a passo, schema detalhado, references/) será preenchido na rodada de conteúdo.

## Objetivo

Cliente oculto remoto (WhatsApp/telefone) mais análise estruturada de reviews por tema e sentimento, com avaliação por dimensão e gaps críticos priorizados.

## Dados necessários

- `client.json` (briefing, meta.modelo_venda = `pdv`)
- Outputs das dependências: ee-s3-pdv-gmn,ee-s1-persona-icp
- `base-de-conhecimento/` relevante
<!-- TODO: listar inputs específicos (connectors, acessos, exports) conforme o POP -->

## Geração

<!-- TODO: passo a passo da geração seguindo POP 3.4 (PDV). Gerar output COMPLETO de uma vez, seguindo o schema.json. -->

## Auto-validação

- [ ] Mencionou o cliente pelo nome e usou dados reais (não genérico)
- [ ] Schema validou
<!-- TODO: checks específicos do entregável -->

## Apresentação e decisões

<!-- TODO: como apresentar ao operador, com pontos de decisão (recomendar, justificar, provocar). -->

## Finalização

1. Salvar output em `clientes/{cliente}/outputs/ee-s3-pdv-experiencia.json`
2. Atualizar `client.json`: progress.skills["ee-s3-pdv-experiencia"] → completed, version bump, append em history[]
3. Rodar o renderer do portal/apresentação

## Campo `summary` (obrigatório)

Todo output traz `summary`, `summary_headline`, `summary_highlights` (4-6 KPIs) e `summary_key_findings` (3-5 achados). Ver `shared-templates/PADRAO-OUTPUT.md`.
