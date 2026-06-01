---
name: ee-feedback
description: "Reporta problema ou sugestão sobre uma skill. Cria GitHub Issue estruturada. Use quando o operador disser /ee-feedback, 'problema', 'bug na skill', 'isso deveria ser diferente'."
---

# Feedback — Reportar Problema

Você vai coletar ee-feedback estruturado do operador e criar uma GitHub Issue no repositório do marketplace.

## Fluxo

Faça 3 perguntas, uma por vez, de forma conversacional:

### Pergunta 1: Contexto
"Sobre qual skill é o ee-feedback?"

Se não ficou claro pelo contexto da conversa, pergunte. Se ficou claro (ex: o operador acabou de rodar uma skill e reclamou de algo), confirme: "Entendi que é sobre a skill {nome}. Correto?"

Se o operador não sabe o nome exato da skill, ajude a identificar: "Em que momento do processo você estava? (diagnóstico, pesquisa, produção, etc.)"

### Pergunta 2: O que aconteceu
"O que rolou? Descreva o problema ou o que ficou estranho."

Deixe o operador falar livremente. Extraia os detalhes relevantes.

### Pergunta 3: Expectativa
"Como deveria ter sido? O que você esperava que acontecesse?"

### Pergunta 4: Sugestão
"O que poderia ser melhor? Tem alguma ideia de como resolver?"

Se o operador não tiver sugestão, registre como "Operador não sugeriu solução específica."

## Classificação automática

Com base nas respostas, classifique o ee-feedback em duas dimensões:

**Tipo** (escolha 1):
- `qualidade-output` — Output gerado era genérico, errado, ou baixa qualidade
- `checkpoint-faltando` — Faltou um checkpoint (avançou sem validar algo importante)
- `schema-incompleto` — Campo faltando no JSON ou estrutura inadequada
- `template-ruim` — HTML/visual do entregável tem problemas
- `bug-script` — Script (v4mos_fetch, update_state, etc.) deu erro
- `ux-confusa` — Fluxo confuso, instruções ambíguas, operador ficou perdido

**Severidade** (escolha 1):
- `alta` — Operador teve que reescrever o output do zero ou a skill travou
- `media` — Operador teve que fazer ajustes manuais significativos
- `baixa` — Cosmético, preferência pessoal, ou melhoria desejável

Mostre a classificação ao operador para confirmação:

```
Classificação:
  Skill: {nome}
  Tipo: {tipo}
  Severidade: {severidade}

Correto?
```

Ajuste se o operador discordar.

## Criar Issue no GitHub

Use o `gh` CLI para criar a issue:

```bash
gh issue create \
  --repo guilhermelippert/v4-estruturacao-marketplace \
  --title "Feedback: {skill} — {resumo em max 50 chars}" \
  --label "ee-feedback,skill:{skill-name},{severidade}" \
  --body "$(cat <<'EOF'
## Skill
**Nome:** {skill}
**Checkpoint:** {N} (se aplicável, senão "N/A")
**Cliente:** {nome anonimizado — só iniciais ou segmento, ex: "Cliente do setor odontológico"}
**Tipo:** {tipo}
**Severidade:** {severidade}

## O que rolou
{resposta da pergunta 2 — editada para clareza, mantendo a essência}

## Como deveria ter sido
{resposta da pergunta 3}

## O que poderia ser melhor
{resposta da pergunta 4}

## Contexto técnico
- State do cliente: semana {N}, checkpoint {X}
- Skills completas até o momento: {lista}
- Dados relevantes do briefing: {se aplicável}

---
*Reportado via /ee-feedback por operador em {data}*
EOF
)"
```

**Regras para a issue:**
- Nunca inclua dados sensíveis do cliente (nome completo, faturamento, credenciais)
- Anonimize: use iniciais ou descrição do segmento
- O título deve ser acionável: "Feedback: ee-s1-persona-icp — ICP gerado muito genérico para clínica"
- Labels devem existir no repo. Se não existirem, crie sem labels e avise

## Finalização

Após criar a issue, mostre ao operador:

```
Issue criada: {URL da issue}

Obrigado pelo ee-feedback! A equipe vai analisar.
Quer ee-continuar trabalhando ou tem mais algo para reportar?
```

Se o `gh` CLI não estiver autenticado ou der erro:
1. Salve o conteúdo da issue em `ee-feedback-{timestamp}.md` na raiz da workspace
2. Avise: "Não consegui criar a issue no GitHub (gh não autenticado). Salvei em {arquivo}. Quando puder, rode `gh auth login` e me diga que eu crio a issue."
