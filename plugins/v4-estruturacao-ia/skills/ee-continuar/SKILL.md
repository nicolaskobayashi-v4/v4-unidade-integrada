---
name: ee-continuar
description: "Retoma o trabalho com um cliente. Mostra panorama de todos os clientes e propõe próximo passo. Use quando o operador disser /ee-continuar, 'ee-continuar', 'retomar', 'voltar', ou simplesmente cumprimentar sem contexto."
---

# Continuar — Retomar Trabalho

## Ao ser invocado

1. Leia todos os `clientes/*/client.json (progress)` no diretório de trabalho
2. Se nenhum cliente existe: diga "Nenhum cliente cadastrado. Quer cadastrar? Diga /ee-novo-cliente" e encerre
3. Se existe 1 cliente: carregue direto (pule para "Ao selecionar um cliente")
4. Se existem múltiplos: mostre panorama e pergunte qual

## Se o operador deu o nome no comando

Ex: "ee-continuar Padaria Silva" — resolva o slug (lowercase, hifenizado, sem acento) e tente encontrar `clientes/{slug}/client.json (progress)`. Se encontrou, carregue direto sem mostrar panorama. Se não encontrou, faça busca parcial no nome dos clientes disponíveis e sugira.

## Panorama (múltiplos clientes)

Para cada cliente encontrado, mostre:

```
CLIENTES ATIVOS
━━━━━━━━━━━━━━━

1. {Nome do Cliente}
   Semana {N} · {X}/{Y} skills completas
   Status: {skill in_progress ou próxima pendente}
   Última decisão: "{texto}" ({data})

2. {Nome do Cliente}
   Semana {N} · {X}/{Y} skills completas
   Status: Todas completas — pronto para exportar
   Última decisão: "{texto}" ({data})
```

Calcule o progresso:
- Total de skills = quantidade de chaves em `state.skills`
- Completas = skills com `status: "completed"`
- Em andamento = skills com `status: "in_progress"`

Para a última decisão, leia a última linha de `clientes/{slug}/client.json (history)`. Se vazio, mostre "Nenhuma decisão registrada".

Pergunte: "Qual cliente quer trabalhar?"

## Ao selecionar um cliente

1. Leia `clientes/{slug}/client.json (progress)` — progresso completo
2. Leia `clientes/{slug}/client.json (history)` — últimas 5 decisões
3. Leia `dependency_graph.json` e `delivery-map.json` — do diretório raiz do plugin

**Monte a sequência de skills do cliente** a partir do `delivery-map.json`, conforme `meta.modelo_venda`:

```
comum.semana_1  +  comum.semana_2  +  semana_3[modelo_venda]  +  comum.semana_4
```

São **4 semanas**: 1, 2 e 4 comuns; a **Semana 3 é específica do modelo de venda**. Essa lista ordenada — e NÃO uma lista hardcoded — é a ordem oficial. `current_week` (1-4) reflete em qual bloco o cliente está.

Determine o próximo passo, seguindo esta prioridade:

**Prioridade 1 — Skill in_progress:**
Se existe uma skill com `status: "in_progress"`, retome-a do checkpoint atual. Essa é a prioridade porque significa que o operador começou algo e não terminou.

**Prioridade 2 — Próxima skill pending com dependências satisfeitas:**
Percorra a sequência montada acima na ordem. Pegue a primeira skill com `status: "pending"` (em `progress.skills`) cujas dependências (em `dependency_graph.json`) estão todas `completed`. Se a próxima skill da ordem tem dependência pendente, avise e sugira rodar a dependência antes.

> ⚠️ Skills marcadas `status: stub` no frontmatter ainda não têm conteúdo de geração. Se a próxima skill for um stub, avise o operador que o entregável está em desenvolvimento.

**Prioridade 3 — Avanço de semana:**
Se todas as skills da semana atual estão `completed`, atualize `current_week` no client.json (progress) e encontre a próxima skill disponível.

**Prioridade 4 — Todas completas:**
Se todas as skills estão `completed`, parabenize o operador e sugira gerar/revisar os dashboards finais.

Apresente o resultado ao operador:

```
{Nome do Cliente} — Semana {N}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Completas:
  ee-s1-diagnostico-maturidade
  ee-s1-persona-icp
  ee-s1-swot

Em andamento:
  ee-s1-auditoria-comunicacao (checkpoint 2/4)

Próximas disponíveis:
  ee-s2-pesquisa-mercado (dependências OK)
  ee-s2-diagnostico-midia (dependências OK)

Bloqueadas:
  ee-s2-posicionamento (falta: ee-s2-pesquisa-mercado)

Última decisão: "Tom mais informal, foco em donas de casa 35-50" (06/04)

Recomendo ee-continuar ee-s1-auditoria-comunicacao (checkpoint 2). Quer seguir ou prefere outra skill?
```

## Contexto a carregar ao retomar uma skill

Quando o operador confirmar qual skill trabalhar:

1. Carregue `clientes/{slug}/client.json (briefing)` — dados do cliente
2. Carregue `clientes/{slug}/client.json (history)` — filtre apenas decisões da skill atual
3. Verifique outputs de skills dependentes:
   - Leia o campo `summary` de cada output JSON das dependências (ex: `ee-s1-persona-icp.json` → campo `summary`)
   - Não carregue os JSONs completos, apenas o summary
4. Se existe `client.json` (seção `connectors`), verifique a data em `fetched_at`:
   - Se tem mais de 7 dias: sugira refresh ("Dados V4MOS de {data}. Quer atualizar?")
   - Se o operador concordar, rode `bash scripts/v4mos_fetch.sh clientes/{slug}`

Inicie a skill no checkpoint indicado pelo client.json (progress).
