# V4 Estruturação IA — Marketplace Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a Claude Code plugin marketplace (`v4-estruturacao-marketplace`) that transforms 21 manual marketing strategy squads into interactive, checkpoint-driven skills with V4MOS API integration, structured outputs, and automated state management.

**Architecture:** Plugin marketplace repo on GitHub (private). Single plugin `v4-estruturacao-ia` containing 25+ skills, 2 agents, utility scripts, and HTML templates. Operator installs via `/plugin install`, creates a local workspace, and operates clients interactively. State persisted in JSON files per client. Deliverables rendered as HTML (deployed to Vercel) or Google Sheets (via GOG CLI).

**Tech Stack:** Claude Code plugins, Markdown skills with YAML frontmatter, JSON Schema (Zod-style), Bash scripts, HTML/CSS templates, Vercel CLI, GOG CLI (Google Workspace), V4MOS REST API (Service Account auth).

**Source repo (read-only reference):** `/Users/guilippert/Trabalho/Chief-of-Staff/01-Projects/V4MOS AI/8 - Estruturacao Estrategica com IA/v4-estruturacao-ia/`

**Decisions doc:** See `memory/project_estruturacao_ia_decisoes.md` for all architectural decisions.

---

## Phase 0: Repo Scaffold

### Task 1: Create marketplace repo structure

**Files:**
- Create: `v4-estruturacao-marketplace/.claude-plugin/marketplace.json`
- Create: `v4-estruturacao-marketplace/plugins/v4-estruturacao-ia/.claude-plugin/plugin.json`
- Create: `v4-estruturacao-marketplace/README.md`

- [ ] **Step 1: Create GitHub repo**

```bash
gh repo create guilhermelippert/v4-estruturacao-marketplace --private --description "Marketplace de skills para estruturação estratégica com IA - V4 Company"
git clone git@github.com:guilhermelippert/v4-estruturacao-marketplace.git
cd v4-estruturacao-marketplace
```

- [ ] **Step 2: Create marketplace.json**

```json
// .claude-plugin/marketplace.json
{
  "name": "v4-estruturacao-marketplace",
  "description": "Skills de estruturação estratégica com IA para operadores V4",
  "owner": {
    "name": "V4 Company",
    "email": "tech@v4company.com"
  },
  "plugins": [
    {
      "name": "v4-estruturacao-ia",
      "source": "./plugins/v4-estruturacao-ia",
      "description": "Sistema completo de estruturação estratégica com IA. 20+ skills interativas com checkpoints, integração V4MOS, e entregáveis automatizados.",
      "version": "0.1.0"
    }
  ]
}
```

- [ ] **Step 3: Create plugin.json**

```json
// plugins/v4-estruturacao-ia/.claude-plugin/plugin.json
{
  "name": "v4-estruturacao-ia",
  "version": "0.1.0",
  "description": "Estruturação estratégica com IA para clientes V4. Skills interativas, integração V4MOS, entregáveis em HTML/Sheets.",
  "skills": ["./skills/"],
  "agents": ["./agents/"]
}
```

- [ ] **Step 4: Create directory skeleton**

```bash
cd plugins/v4-estruturacao-ia
mkdir -p skills/{onboarding,novo-cliente,continuar,feedback,duvida}
mkdir -p skills/{diagnostico-maturidade,swot,persona-icp,auditoria-comunicacao}
mkdir -p skills/{pesquisa-mercado,posicionamento,diagnostico-midia,diagnostico-criativos,diagnostico-cro}
mkdir -p skills/{identidade-visual,brandbook,landing-page,copy-anuncios,criativos-anuncios}
mkdir -p skills/{crm-setup,forecast-midia,gmb-otimizacao}
mkdir -p skills/{diagnostico-comercial,cliente-oculto,scripts-sdr,sdr-ia-config}
mkdir -p agents
mkdir -p scripts
mkdir -p shared-templates
```

- [ ] **Step 5: Create README.md**

```markdown
# V4 Estruturação IA — Marketplace

Sistema de estruturação estratégica com IA para operadores V4.

## Setup (cada operador roda uma vez)

### 1. Adicionar o marketplace

No Claude Code:
```
/plugin marketplace add guilhermelippert/v4-estruturacao-marketplace
```

### 2. Instalar o plugin

```
/plugin install v4-estruturacao-ia@v4-estruturacao-marketplace
```

### 3. Criar workspace de trabalho

```bash
mkdir ~/estruturacao-ia && cd ~/estruturacao-ia
claude
```

Dentro do Claude Code:
```
/onboarding
```

### 4. Verificar instalação

Rode `/plugin` e vá na aba Installed. Você deve ver `v4-estruturacao-ia`.
Digite `/` no Claude Code e veja as skills no autocomplete.

## Uso diário

```bash
cd ~/estruturacao-ia
claude
> "continuar"
```

O sistema mostra o panorama de todos os clientes e propõe o próximo passo.

## Skills disponíveis

### Utilidade
- `/onboarding` — Setup inicial da workspace
- `/novo-cliente` — Cadastrar novo cliente
- `/continuar` — Retomar trabalho (mostra panorama + próximo passo)
- `/feedback` — Reportar problema numa skill (cria GitHub Issue)
- `/duvida` — Tirar dúvida sobre o sistema

### Semana 1 — Diagnóstico
- `diagnostico-maturidade` — Análise de maturidade digital (dados V4MOS)
- `swot` — Matriz SWOT acionável
- `persona-icp` — ICP + Persona com Jobs-to-be-Done
- `auditoria-comunicacao` — Auditoria de touchpoints digitais

### Semana 2 — Pesquisa e Posicionamento
- `pesquisa-mercado` — TAM/SAM/SOM + concorrentes + tendências
- `posicionamento` — PUV + Canvas 4P + território de marca
- `diagnostico-midia` — Análise de mídia paga (dados V4MOS)
- `diagnostico-criativos` — Avaliação de criativos (multimodal)
- `diagnostico-cro` — Análise de conversão + wireframe

### Semana 3 — Produção e Implementação
- `identidade-visual` — Conceito + paleta + tipografia + logo
- `brandbook` — Manual de copy + tom de voz + narrativa
- `landing-page` — Copy + código + deploy Vercel
- `copy-anuncios` — 30+ variações por funil (Google Sheets)
- `criativos-anuncios` — Briefing criativo + prompts Midjourney
- `crm-setup` — Pipeline Kommo + réguas de automação
- `forecast-midia` — Modelagem 3 meses (Google Sheets)
- `gmb-otimizacao` — Google Meu Negócio otimizado

### Semana 4-5 — Vendas (opcional)
- `diagnostico-comercial` — Análise do funil + critérios de qualificação
- `cliente-oculto` — Simulação + relatório
- `scripts-sdr` — Scripts de qualificação WhatsApp
- `sdr-ia-config` — Configuração Patagon + integração Kommo
```

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: scaffold marketplace repo with plugin structure"
```

---

## Phase 1: Core Infrastructure

### Task 2: Create CLAUDE.md — the orchestrator brain

**Files:**
- Create: `plugins/v4-estruturacao-ia/CLAUDE.md`

This is the most critical file. It defines how Claude behaves when the plugin is active.

- [ ] **Step 1: Write CLAUDE.md**

```markdown
# V4 Estruturação IA

Você é o sistema de Estruturação Estratégica com IA da V4 Company. Você opera interativamente com um analista (operador) para criar entregáveis estratégicos de marketing para clientes PMEs.

## Princípios

1. **Co-criação, não automação.** Você trabalha COM o operador. Cada skill tem checkpoints onde você para, mostra o que gerou, e pede input. O operador refina. Só avança com aprovação.
2. **Dados reais, não genéricos.** Sempre use dados do cliente (briefing.json, V4MOS API, outputs anteriores). Se falta dado, pergunte — nunca invente.
3. **Determinismo máximo.** Gere outputs como JSON estruturado seguindo o schema da skill. O template visual é fixo — você só preenche o conteúdo.
4. **State sempre atualizado.** Após cada checkpoint, atualize state.json e appende em decisions.jsonl. O operador nunca deveria repetir informação.

## Ao iniciar qualquer conversa

1. Identifique a workspace do operador (diretório atual ou mais próximo com `clientes/`)
2. Leia `clientes/*/state.json` de todos os clientes
3. Apresente o panorama: clientes ativos, progresso, próximo passo recomendado
4. Pergunte qual cliente trabalhar

Se o operador disser "continuar [nome]" ou apenas "continuar", carregue o state do cliente e retome de onde parou.

## Ao executar uma skill

1. Leia `clientes/{cliente}/briefing.json` — dados base do cliente
2. Leia `clientes/{cliente}/decisions.jsonl` — decisões anteriores relevantes
3. Leia outputs anteriores (.json) que a skill depende (ver dependency_graph.json)
4. Se a skill precisa de dados V4MOS, rode o script `scripts/v4mos_fetch.sh`
5. Execute os checkpoints da skill em ordem
6. Em cada checkpoint:
   a. Mostre o que gerou
   b. Peça validação ou ajuste do operador
   c. Após aprovação, appende a decisão em decisions.jsonl
   d. Atualize state.json
7. No final: salve output .json + renderize entregável (HTML ou Sheets)
8. Atualize dashboard

## Formato de state.json

```json
{
  "client": "Nome do Cliente",
  "workspace_id": "workspace-uuid",
  "started_at": "2026-04-06",
  "current_week": 1,
  "skills": {
    "skill-name": {
      "status": "pending|in_progress|completed",
      "checkpoint": 0,
      "started_at": null,
      "completed_at": null
    }
  }
}
```

## Formato de decisions.jsonl

Uma linha JSON por decisão, append-only:
```json
{"ts":"2026-04-06T10:30","skill":"persona-icp","checkpoint":2,"decision":"Tom mais informal, foco em donas de casa 35-50","operator":"nome"}
```

## Dependency graph

Antes de iniciar uma skill, verifique dependency_graph.json. Se a skill depende de outra que não está completa, avise o operador e sugira rodar a dependência primeiro.

## Entregáveis

- Relatórios/diagnósticos → HTML deployado na Vercel (operador compartilha link)
- Planilhas (copy, forecast) → Google Sheets via GOG CLI
- Landing Page → HTML deployado na Vercel
- Scripts SDR → Markdown (configurado no Patagon)
- Dashboard → HTML local gerado do state.json

## Regras críticas

- NUNCA gere output genérico. Todo output deve mencionar o cliente pelo nome e usar dados reais.
- NUNCA pule checkpoints. O operador precisa validar cada etapa.
- NUNCA modifique outputs anteriores sem pedir. Se precisar ajustar algo da semana 1 na semana 3, pergunte primeiro.
- NUNCA exponha credenciais. .credentials/ é privado.
- Sempre salve o JSON estruturado ANTES de renderizar o template. O JSON é a verdade, o HTML é a visualização.
```

- [ ] **Step 2: Commit**

```bash
git add plugins/v4-estruturacao-ia/CLAUDE.md
git commit -m "feat: add CLAUDE.md orchestrator brain"
```

---

### Task 3: Create AGENTS.md for multi-LLM compatibility

**Files:**
- Create: `plugins/v4-estruturacao-ia/AGENTS.md`

- [ ] **Step 1: Write AGENTS.md**

O AGENTS.md replica as instruções do CLAUDE.md em formato compatível com OpenAI/Gemini (sem features específicas do Claude Code como skills e subagents). Conteúdo idêntico ao CLAUDE.md mas sem referências a `/plugin`, `skills/`, ou features Claude-specific. Usar linguagem genérica de agente.

```markdown
# V4 Estruturação IA — Agent Instructions

Você é o sistema de Estruturação Estratégica com IA da V4 Company.

[Mesmo conteúdo do CLAUDE.md, substituindo:
- "skill" → "módulo"
- "checkpoint" → mantém
- Remover referências a /plugin, skills/, subagents
- Manter toda a lógica de state.json, decisions.jsonl, briefing.json
- Manter dependency_graph.json
- Manter regras críticas]
```

- [ ] **Step 2: Commit**

```bash
git add plugins/v4-estruturacao-ia/AGENTS.md
git commit -m "feat: add AGENTS.md for multi-LLM compatibility"
```

---

### Task 4: Create dependency graph

**Files:**
- Create: `plugins/v4-estruturacao-ia/dependency_graph.json`

- [ ] **Step 1: Write dependency_graph.json**

```json
{
  "persona-icp": [],
  "diagnostico-maturidade": [],
  "swot": ["diagnostico-maturidade"],
  "auditoria-comunicacao": ["persona-icp"],
  "pesquisa-mercado": ["persona-icp"],
  "posicionamento": ["pesquisa-mercado", "persona-icp", "swot"],
  "diagnostico-midia": ["persona-icp"],
  "diagnostico-criativos": ["persona-icp"],
  "diagnostico-cro": ["persona-icp", "posicionamento"],
  "identidade-visual": ["posicionamento"],
  "brandbook": ["posicionamento", "persona-icp"],
  "landing-page": ["posicionamento", "brandbook", "diagnostico-cro"],
  "copy-anuncios": ["brandbook", "persona-icp", "posicionamento"],
  "criativos-anuncios": ["brandbook", "identidade-visual", "diagnostico-criativos"],
  "crm-setup": ["persona-icp"],
  "forecast-midia": ["diagnostico-midia"],
  "gmb-otimizacao": ["persona-icp"],
  "diagnostico-comercial": ["persona-icp"],
  "cliente-oculto": ["diagnostico-comercial"],
  "scripts-sdr": ["diagnostico-comercial", "brandbook"],
  "sdr-ia-config": ["scripts-sdr", "crm-setup"]
}
```

- [ ] **Step 2: Commit**

```bash
git add plugins/v4-estruturacao-ia/dependency_graph.json
git commit -m "feat: add skill dependency graph"
```

---

### Task 5: Create V4MOS API client script

**Files:**
- Create: `plugins/v4-estruturacao-ia/scripts/v4mos_fetch.sh`

- [ ] **Step 1: Write v4mos_fetch.sh**

```bash
#!/bin/bash
# v4mos_fetch.sh — Fetch client data from V4MOS API
# Usage: ./v4mos_fetch.sh <client_dir>
# Reads credentials from .credentials/clients.json
# Saves cache to <client_dir>/v4mos-cache.json

set -euo pipefail

CLIENT_DIR="$1"
CREDENTIALS_FILE="$(dirname "$CLIENT_DIR")/../.credentials/clients.json"

if [ ! -f "$CREDENTIALS_FILE" ]; then
  echo "ERROR: .credentials/clients.json not found"
  exit 1
fi

# Extract client name from state.json
CLIENT_NAME=$(jq -r '.client' "$CLIENT_DIR/state.json")
WORKSPACE_ID=$(jq -r '.workspace_id' "$CLIENT_DIR/state.json")

# Find credentials for this workspace
CLIENT_ID=$(jq -r --arg ws "$WORKSPACE_ID" '.[$ws].client_id // empty' "$CREDENTIALS_FILE")
CLIENT_SECRET=$(jq -r --arg ws "$WORKSPACE_ID" '.[$ws].client_secret // empty' "$CREDENTIALS_FILE")

if [ -z "$CLIENT_ID" ] || [ -z "$CLIENT_SECRET" ]; then
  echo "ERROR: No credentials found for workspace $WORKSPACE_ID"
  exit 1
fi

V4MOS_BASE_URL="${V4MOS_BASE_URL:-https://api.v4.marketing}"

# Fetch integrations status
INTEGRATIONS=$(curl -s -H "x-client-id: $CLIENT_ID" \
  -H "x-client-secret: $CLIENT_SECRET" \
  -H "x-workspace-id: $WORKSPACE_ID" \
  "$V4MOS_BASE_URL/workspaces/$WORKSPACE_ID/integrations/status" 2>/dev/null || echo "[]")

# Fetch diagnoses
DIAGNOSES=$(curl -s -H "x-client-id: $CLIENT_ID" \
  -H "x-client-secret: $CLIENT_SECRET" \
  -H "x-workspace-id: $WORKSPACE_ID" \
  "$V4MOS_BASE_URL/workspaces/$WORKSPACE_ID/diagnoses" 2>/dev/null || echo "[]")

# Fetch workspace details
WORKSPACE=$(curl -s -H "x-client-id: $CLIENT_ID" \
  -H "x-client-secret: $CLIENT_SECRET" \
  -H "x-workspace-id: $WORKSPACE_ID" \
  "$V4MOS_BASE_URL/workspaces/$WORKSPACE_ID" 2>/dev/null || echo "{}")

# Compose cache
jq -n \
  --argjson integrations "$INTEGRATIONS" \
  --argjson diagnoses "$DIAGNOSES" \
  --argjson workspace "$WORKSPACE" \
  --arg fetched_at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  '{
    fetched_at: $fetched_at,
    workspace: $workspace,
    integrations: $integrations,
    diagnoses: $diagnoses
  }' > "$CLIENT_DIR/v4mos-cache.json"

echo "V4MOS data cached at $CLIENT_DIR/v4mos-cache.json"
```

- [ ] **Step 2: Make executable and commit**

```bash
chmod +x plugins/v4-estruturacao-ia/scripts/v4mos_fetch.sh
git add plugins/v4-estruturacao-ia/scripts/v4mos_fetch.sh
git commit -m "feat: add V4MOS API fetch script"
```

---

### Task 6: Create state management scripts

**Files:**
- Create: `plugins/v4-estruturacao-ia/scripts/update_state.sh`
- Create: `plugins/v4-estruturacao-ia/scripts/append_decision.sh`
- Create: `plugins/v4-estruturacao-ia/scripts/render_dashboard.sh`

- [ ] **Step 1: Write update_state.sh**

```bash
#!/bin/bash
# update_state.sh — Update skill status in state.json
# Usage: ./update_state.sh <client_dir> <skill_name> <status> [checkpoint]

set -euo pipefail

CLIENT_DIR="$1"
SKILL="$2"
STATUS="$3"
CHECKPOINT="${4:-0}"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)

STATE_FILE="$CLIENT_DIR/state.json"

# Update skill status
jq --arg skill "$SKILL" \
   --arg status "$STATUS" \
   --arg checkpoint "$CHECKPOINT" \
   --arg now "$NOW" \
   '.skills[$skill].status = $status |
    .skills[$skill].checkpoint = ($checkpoint | tonumber) |
    if $status == "in_progress" and .skills[$skill].started_at == null
      then .skills[$skill].started_at = $now else . end |
    if $status == "completed"
      then .skills[$skill].completed_at = $now else . end' \
   "$STATE_FILE" > "$STATE_FILE.tmp" && mv "$STATE_FILE.tmp" "$STATE_FILE"

echo "Updated $SKILL → $STATUS (checkpoint $CHECKPOINT)"
```

- [ ] **Step 2: Write append_decision.sh**

```bash
#!/bin/bash
# append_decision.sh — Append decision to decisions.jsonl
# Usage: ./append_decision.sh <client_dir> <skill> <checkpoint> <decision_text>

set -euo pipefail

CLIENT_DIR="$1"
SKILL="$2"
CHECKPOINT="$3"
DECISION="$4"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)

jq -cn \
  --arg ts "$NOW" \
  --arg skill "$SKILL" \
  --arg cp "$CHECKPOINT" \
  --arg decision "$DECISION" \
  '{ts: $ts, skill: $skill, checkpoint: ($cp | tonumber), decision: $decision}' \
  >> "$CLIENT_DIR/decisions.jsonl"

echo "Decision logged for $SKILL checkpoint $CHECKPOINT"
```

- [ ] **Step 3: Write render_dashboard.sh**

```bash
#!/bin/bash
# render_dashboard.sh — Generate dashboard.html from state.json
# Usage: ./render_dashboard.sh <client_dir>
# For general dashboard: ./render_dashboard.sh <workspace_root> --general

set -euo pipefail

if [ "${2:-}" = "--general" ]; then
  # General dashboard: scan all clients
  WORKSPACE="$1"
  OUTPUT="$WORKSPACE/dashboard-geral.html"
  
  CLIENTS_JSON="["
  FIRST=true
  for STATE_FILE in "$WORKSPACE"/clientes/*/state.json; do
    [ -f "$STATE_FILE" ] || continue
    if [ "$FIRST" = true ]; then FIRST=false; else CLIENTS_JSON+=","; fi
    CLIENTS_JSON+=$(cat "$STATE_FILE")
  done
  CLIENTS_JSON+="]"
  
  # Generate HTML
  cat > "$OUTPUT" << 'HTMLEOF'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Estruturação IA — Dashboard Geral</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0a0a0a; color: #e5e2e1; padding: 2rem; }
  h1 { font-size: 1.5rem; margin-bottom: 1.5rem; color: #fff; }
  .client-card { background: #1a1a1a; border: 1px solid #333; border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem; }
  .client-name { font-size: 1.2rem; font-weight: 700; color: #fff; }
  .client-week { color: #888; font-size: 0.9rem; }
  .progress-bar { height: 8px; background: #333; border-radius: 4px; margin: 0.75rem 0; overflow: hidden; }
  .progress-fill { height: 100%; background: #e50914; border-radius: 4px; transition: width 0.3s; }
  .stats { display: flex; gap: 1rem; font-size: 0.85rem; color: #aaa; }
</style>
</head>
<body>
<h1>ESTRUTURAÇÃO IA — CLIENTES ATIVOS</h1>
<div id="clients"></div>
<script>
HTMLEOF

  echo "const clients = $CLIENTS_JSON;" >> "$OUTPUT"
  
  cat >> "$OUTPUT" << 'HTMLEOF2'
clients.forEach(c => {
  const skills = Object.values(c.skills || {});
  const total = skills.length;
  const done = skills.filter(s => s.status === 'completed').length;
  const inProgress = skills.filter(s => s.status === 'in_progress').length;
  const pct = total > 0 ? Math.round((done / total) * 100) : 0;
  
  document.getElementById('clients').innerHTML += `
    <div class="client-card">
      <div class="client-name">${c.client}</div>
      <div class="client-week">Semana ${c.current_week || '?'} · ${done}/${total} skills</div>
      <div class="progress-bar"><div class="progress-fill" style="width:${pct}%"></div></div>
      <div class="stats">
        <span>✅ ${done} completas</span>
        <span>🔄 ${inProgress} em andamento</span>
        <span>⏳ ${total - done - inProgress} pendentes</span>
      </div>
    </div>`;
});
</script>
</body>
</html>
HTMLEOF2

  echo "Dashboard geral gerado: $OUTPUT"
else
  # Client-specific dashboard
  CLIENT_DIR="$1"
  STATE_FILE="$CLIENT_DIR/state.json"
  OUTPUT="$CLIENT_DIR/dashboard.html"
  
  STATE=$(cat "$STATE_FILE")
  
  # Similar logic but with skill-level detail per week
  # (same HTML structure, expanded with per-skill rows)
  cat > "$OUTPUT" << HTMLEOF
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>$(echo "$STATE" | jq -r '.client') — Dashboard</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0a0a0a; color: #e5e2e1; padding: 2rem; }
  h1 { font-size: 1.5rem; margin-bottom: 0.5rem; color: #fff; }
  .meta { color: #888; margin-bottom: 1.5rem; }
  .week { background: #1a1a1a; border: 1px solid #333; border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem; }
  .week-title { font-weight: 700; margin-bottom: 0.75rem; }
  .skill-row { display: flex; justify-content: space-between; padding: 0.4rem 0; border-bottom: 1px solid #222; }
  .skill-name { font-size: 0.9rem; }
  .status-completed { color: #4ade80; }
  .status-in_progress { color: #facc15; }
  .status-pending { color: #666; }
</style>
</head>
<body>
<h1>$(echo "$STATE" | jq -r '.client')</h1>
<div class="meta">Semana $(echo "$STATE" | jq -r '.current_week') · Início: $(echo "$STATE" | jq -r '.started_at')</div>
<div id="weeks"></div>
<script>
const state = $STATE;
</script>
</body>
</html>
HTMLEOF

  echo "Dashboard do cliente gerado: $OUTPUT"
fi
```

- [ ] **Step 4: Make executable and commit**

```bash
chmod +x plugins/v4-estruturacao-ia/scripts/*.sh
git add plugins/v4-estruturacao-ia/scripts/
git commit -m "feat: add state management and dashboard scripts"
```

---

## Phase 2: Utility Skills

### Task 7: Create /onboarding skill

**Files:**
- Create: `plugins/v4-estruturacao-ia/skills/onboarding/SKILL.md`

- [ ] **Step 1: Write onboarding SKILL.md**

```markdown
---
name: onboarding
description: "Setup inicial da workspace de estruturação IA. Configura diretórios, credenciais, e ensina o operador a usar o sistema. Use quando o operador disser /onboarding ou 'configurar workspace' ou 'primeiro uso'."
---

# Onboarding — Setup da Workspace

Você está configurando a workspace de estruturação IA para um novo operador.

## Pré-requisitos

Verifique se o operador tem:
- Claude Code instalado e funcionando
- Acesso ao V4MOS (vai precisar de workspace_id de pelo menos 1 cliente)
- GOG CLI instalado (`gog --version`) — se não tiver, instrua: `npm install -g @nicecode/gog`
- Vercel CLI instalado (`vercel --version`) — se não tiver: `npm install -g vercel`
- jq instalado (`jq --version`) — se não tiver: `brew install jq` (Mac) ou `apt install jq` (Linux) ou `choco install jq` (Windows)

## Etapas

### Etapa 1: Criar estrutura de diretórios

Crie no diretório atual:

```
.credentials/
  clients.json    (arquivo vazio: {})
clientes/
dashboard-geral.html
```

Adicione um `.gitignore`:
```
.credentials/
clientes/
dashboard-geral.html
```

### Etapa 2: Configurar credenciais

Pergunte ao operador:
1. "Você já tem um Service Account no V4MOS para algum cliente?"
   - Se sim: peça client_id, client_secret, workspace_id e salve em .credentials/clients.json
   - Se não: explique como criar em V4MOS > Settings > Data API > Create Service Account

Formato do clients.json:
```json
{
  "f854f2c6-exemplo-uuid": {
    "client_id": "xxx",
    "client_secret": "yyy",
    "client_name": "Padaria Silva"
  }
}
```

### Etapa 3: Tutorial rápido

Explique ao operador:
1. **Para começar um cliente:** diga `/novo-cliente`
2. **Para continuar trabalho:** diga `continuar` ou `continuar [nome do cliente]`
3. **Para tirar dúvida:** diga `/duvida [sua pergunta]`
4. **Para reportar problema:** diga `/feedback`
5. **Para ver progresso:** abra `clientes/{nome}/dashboard.html` ou `dashboard-geral.html` no browser

### Etapa 4: Teste rápido

Se o operador já tem credenciais, faça um teste:
1. Rode `scripts/v4mos_fetch.sh` com um client_dir fictício
2. Verifique se os dados chegaram
3. Se funcionou: "Tudo configurado! Pode começar com /novo-cliente"
4. Se falhou: debug da credencial/URL

### Finalização

Mostre o link do guia completo (quando existir na Vercel) e pergunte se quer cadastrar o primeiro cliente agora.
```

- [ ] **Step 2: Commit**

```bash
git add plugins/v4-estruturacao-ia/skills/onboarding/
git commit -m "feat: add /onboarding skill"
```

---

### Task 8: Create /novo-cliente skill

**Files:**
- Create: `plugins/v4-estruturacao-ia/skills/novo-cliente/SKILL.md`
- Create: `plugins/v4-estruturacao-ia/skills/novo-cliente/references/briefing-fields.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: novo-cliente
description: "Cadastra um novo cliente no sistema. Cria pasta, puxa dados do V4MOS, faz briefing complementar interativo. Use quando o operador disser /novo-cliente, 'novo cliente', 'cadastrar cliente', ou 'começar projeto'."
---

# Novo Cliente — Cadastro e Briefing

## Etapa 1: Identificação

Pergunte:
1. "Qual o nome da empresa?"
2. "Tem workspace no V4MOS? Se sim, qual o workspace_id?"
3. "Módulo vendas (SDR IA) contratado? (sim/não)"

## Etapa 2: Criar estrutura

Com o nome do cliente (slug: lowercase, hifenizado), crie:

```
clientes/{slug}/
  state.json
  decisions.jsonl  (arquivo vazio)
  briefing.json    (será preenchido)
  semana-1/
  semana-2/
  semana-3/
  semana-4-5/      (só se módulo vendas)
```

Inicialize state.json com todas as skills em "pending":
```json
{
  "client": "Nome Real",
  "workspace_id": "workspace-uuid",
  "started_at": "YYYY-MM-DD",
  "current_week": 1,
  "modulo_vendas": true/false,
  "skills": {
    "diagnostico-maturidade": {"status":"pending","checkpoint":0,"started_at":null,"completed_at":null},
    "swot": {"status":"pending","checkpoint":0,"started_at":null,"completed_at":null},
    ...todas as skills da semana 1-3, e semana 4-5 se módulo vendas
  }
}
```

## Etapa 3: Puxar dados V4MOS

Se tem workspace_id:
1. Verifique se já existe credencial em `.credentials/clients.json`
2. Se não existe, instrua o operador a criar Service Account no V4MOS
3. Rode `scripts/v4mos_fetch.sh clientes/{slug}/`
4. Mostre resumo dos dados obtidos:
   - Integrações ativas (Meta, Google, Kommo, etc.)
   - Diagnóstico de maturidade (se existir)
   - Dados do workspace (nome, site, modelo de negócio)

## Etapa 4: Briefing complementar interativo

Consulte `references/briefing-fields.md` para a lista completa de campos.

Para cada campo que JÁ EXISTE no V4MOS cache, mostre o valor e peça confirmação.
Para cada campo que NÃO EXISTE, pergunte ao operador.

Campos que SEMPRE precisam ser coletados manualmente (não existem no V4MOS):
- 3 concorrentes com diferencial percebido
- Diferencial real vs concorrentes
- 3 adjetivos de personalidade da marca
- Tom de voz desejado
- 3-5 marcas admiradas visualmente
- Restrições visuais (o que NÃO pode aparecer)
- Descrição dos 3 melhores clientes
- 3 problemas que clientes têm antes de contratar
- 3 resultados que clientes alcançam

Fluxo: pergunte um campo por vez, conversacionalmente. Não despeje formulário.

## Etapa 5: Salvar briefing

Salve tudo em `clientes/{slug}/briefing.json` com estrutura:
```json
{
  "identification": { "name": "...", "segment": "...", ... },
  "product": { "main_product": "...", "ticket": "...", ... },
  "icp": { "best_customers": "...", "not_customers": "...", ... },
  "competition": { "competitors": [...], "differentials": "...", ... },
  "brand": { "adjectives": [...], "voice_tone": "...", ... },
  "digital_situation": { "paid_traffic": "...", "crm": "...", ... },
  "accesses": { "meta": false, "google_ads": false, ... },
  "sales_module": { ... }  // se contratado
}
```

## Etapa 6: Confirmar e gerar dashboard

1. Mostre resumo do briefing ao operador
2. Pergunte se quer ajustar algo
3. Gere dashboard inicial: `scripts/render_dashboard.sh clientes/{slug}/`
4. Gere dashboard geral: `scripts/render_dashboard.sh . --general`
5. "Cliente cadastrado! Para começar a semana 1, diga: continuar {nome}"
```

- [ ] **Step 2: Write references/briefing-fields.md**

Copie a estrutura completa do `templates/briefing-cliente.md` do repo do Figueiredo, organizada por seção, indicando para cada campo:
- Nome do campo
- Descrição
- Fonte: "V4MOS" ou "manual"
- Obrigatório: sim/não

(Usar o conteúdo completo do briefing já mapeado pelo subagent)

- [ ] **Step 3: Commit**

```bash
git add plugins/v4-estruturacao-ia/skills/novo-cliente/
git commit -m "feat: add /novo-cliente skill with interactive briefing"
```

---

### Task 9: Create /continuar skill

**Files:**
- Create: `plugins/v4-estruturacao-ia/skills/continuar/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: continuar
description: "Retoma o trabalho com um cliente. Mostra panorama de todos os clientes e propõe próximo passo. Use quando o operador disser /continuar, 'continuar', 'retomar', 'voltar', ou simplesmente cumprimentar sem contexto."
---

# Continuar — Retomar Trabalho

## Ao ser invocado

1. Leia todos os `clientes/*/state.json` no diretório de trabalho
2. Se nenhum cliente existe: sugira `/novo-cliente`
3. Se existe 1 cliente: carregue direto
4. Se existem múltiplos: mostre panorama e pergunte qual

## Panorama (múltiplos clientes)

Para cada cliente, mostre:
- Nome
- Semana atual
- Progresso (X/Y skills completas)
- Status: qual skill está in_progress ou qual é a próxima
- Última decisão (última linha de decisions.jsonl)

## Ao selecionar um cliente

1. Leia `clientes/{slug}/state.json`
2. Leia `clientes/{slug}/decisions.jsonl` (últimas 5 decisões)
3. Verifique `dependency_graph.json`

Determine o próximo passo:
- Se tem skill `in_progress`: retome essa skill do checkpoint atual
- Se não: encontre a próxima skill `pending` cujas dependências estão `completed`
- Se todas as skills da semana atual estão `completed`: avance `current_week` e encontre próxima

Apresente:
```
{Cliente} — Semana {N}
{emoji} {skill completa 1}
{emoji} {skill completa 2}
🔄 {skill em andamento} (checkpoint X)
⏳ {próxima skill}

Última decisão: "{decisão}" ({data})

Quer continuar {skill em andamento} ou prefere outra coisa?
```

## Se o operador deu o nome do cliente no comando

Ex: "continuar Padaria Silva" — resolva o slug e carregue direto sem mostrar panorama.
```

- [ ] **Step 2: Commit**

```bash
git add plugins/v4-estruturacao-ia/skills/continuar/
git commit -m "feat: add /continuar skill with client panorama"
```

---

### Task 10: Create /feedback skill

**Files:**
- Create: `plugins/v4-estruturacao-ia/skills/feedback/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: feedback
description: "Reporta problema ou sugestão sobre uma skill. Cria GitHub Issue estruturada. Use quando o operador disser /feedback, 'problema', 'bug na skill', 'isso deveria ser diferente'."
---

# Feedback — Reportar Problema

## Fluxo

1. Pergunte: "Sobre qual skill é o feedback?" (se não ficou claro pelo contexto)
2. Pergunte: "O que rolou?" (descrição do problema)
3. Pergunte: "Como deveria ter sido?" (expectativa)
4. Pergunte: "O que poderia ser melhor?" (sugestão de melhoria)

## Classificação automática

Com base nas respostas, classifique:
- **Tipo:** qualidade do output | checkpoint faltando | schema incompleto | template ruim | bug no script | UX confusa
- **Severidade:** alta (operador reescreveu do zero) | média (ajustes manuais) | baixa (cosmético)

## Criar Issue

Use o gh CLI:

```bash
gh issue create \
  --repo guilhermelippert/v4-estruturacao-marketplace \
  --title "Feedback: {skill} — {resumo curto}" \
  --label "feedback,skill:{skill-name},{severidade}" \
  --body "$(cat <<'EOF'
## Skill: {skill}
**Checkpoint:** {N} (se aplicável)
**Cliente:** {nome} (anonimizado se necessário)
**Tipo:** {tipo}
**Severidade:** {severidade}

### O que rolou
{resposta 1}

### Como deveria ter sido
{resposta 2}

### O que poderia ser melhor
{resposta 3}

### Contexto adicional
- Dados relevantes do briefing/decisions se aplicável
EOF
)"
```

Mostre o link da issue criada ao operador.
```

- [ ] **Step 2: Commit**

```bash
git add plugins/v4-estruturacao-ia/skills/feedback/
git commit -m "feat: add /feedback skill with GitHub Issue creation"
```

---

### Task 11: Create /duvida skill

**Files:**
- Create: `plugins/v4-estruturacao-ia/skills/duvida/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: duvida
description: "Responde dúvidas do operador sobre como usar o sistema, o que cada skill faz, como funciona o fluxo, etc. Use quando o operador disser /duvida, 'como funciona', 'o que é', 'pra que serve', 'help'."
---

# Dúvida — Ajuda sobre o Sistema

Você é o assistente de dúvidas do sistema de Estruturação IA.

## Conhecimento base

Leia o CLAUDE.md e o README.md do plugin para responder sobre:
- Fluxo geral (semanas, skills, checkpoints)
- Como funciona cada skill (leia o SKILL.md correspondente)
- Como funciona o state management (state.json, decisions.jsonl)
- Como acessar dashboards
- Como dar feedback
- Como gerenciar credenciais
- Dependency graph entre skills

## Regras

- Responda de forma direta e curta
- Se a dúvida é sobre uma skill específica, leia o SKILL.md dela e resuma
- Se a dúvida é sobre o V4MOS, explique a integração via Service Account
- Se não sabe, diga que não sabe e sugira /feedback para registrar
- Nunca invente funcionalidades que não existem
```

- [ ] **Step 2: Commit**

```bash
git add plugins/v4-estruturacao-ia/skills/duvida/
git commit -m "feat: add /duvida help skill"
```

---

## Phase 3: Agents

### Task 12: Create orchestrator agent

**Files:**
- Create: `plugins/v4-estruturacao-ia/agents/orquestrador.md`

- [ ] **Step 1: Write orquestrador.md**

```markdown
---
name: orquestrador
description: "Agente principal que gerencia o ciclo de vida dos clientes. Lê state.json, propõe próximos passos, gerencia transições entre skills e semanas."
tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]
---

# Orquestrador de Estruturação IA

Você é o agente orquestrador do sistema de Estruturação Estratégica com IA.

## Responsabilidades

1. **Ao iniciar:** ler todos os `clientes/*/state.json` e apresentar panorama
2. **Ao selecionar cliente:** carregar contexto completo (state + decisions + briefing)
3. **Ao iniciar skill:** verificar dependency_graph.json, carregar inputs necessários
4. **Ao finalizar skill:** atualizar state, gerar dashboard, sugerir próxima
5. **Ao trocar de semana:** atualizar current_week, recalcular próximas skills

## Regras de routing

- Se todas as dependências de uma skill estão completas → pode iniciar
- Se falta dependência → avise e sugira rodar a dependência primeiro
- Se tem skill in_progress → priorize retomá-la
- Se operador pede skill fora de ordem → verifique dependências, avise dos riscos, mas permita se operador insistir

## Context loading

Ao carregar contexto de um cliente:
1. state.json → progresso
2. briefing.json → dados do cliente
3. decisions.jsonl → filtrar decisões relevantes para a skill atual
4. Outputs anteriores (.json) → carregar SUMÁRIO (campo "summary" no JSON), não o JSON completo
5. v4mos-cache.json → dados do V4MOS (verificar se tem mais de 7 dias e sugerir refresh)
```

- [ ] **Step 2: Commit**

```bash
git add plugins/v4-estruturacao-ia/agents/orquestrador.md
git commit -m "feat: add orchestrator agent"
```

---

### Task 13: Create quality reviewer agent

**Files:**
- Create: `plugins/v4-estruturacao-ia/agents/revisor-qualidade.md`

- [ ] **Step 1: Write revisor-qualidade.md**

```markdown
---
name: revisor-qualidade
description: "Agente que revisa outputs antes do export final. Verifica schema, consistência com outputs anteriores, e qualidade do conteúdo."
tools: ["Read", "Grep", "Glob"]
---

# Revisor de Qualidade

Você é o revisor de qualidade do sistema de Estruturação IA. Você é invocado automaticamente ANTES de qualquer export final (HTML ou Sheets).

## Checklist de revisão

Para cada output, verifique:

### 1. Consistência com o cliente
- [ ] Output menciona o cliente pelo nome (não é genérico)
- [ ] Dados usados batem com briefing.json
- [ ] Segmento/setor está correto
- [ ] Concorrentes mencionados são os do briefing

### 2. Consistência com outputs anteriores
- [ ] Se usa ICP, bate com persona-icp.json
- [ ] Se usa PUV, bate com posicionamento.json
- [ ] Se usa tom de voz, bate com brandbook.json (se existir)
- [ ] Decisões do operador (decisions.jsonl) foram respeitadas

### 3. Qualidade do conteúdo
- [ ] Nenhum item genérico (ex: "boa equipe", "qualidade e compromisso")
- [ ] Todos os campos do schema preenchidos
- [ ] Tamanho adequado (nem telegráfico nem verborrágico)
- [ ] Ações recomendadas são específicas e executáveis

### 4. Schema
- [ ] JSON output valida contra schema.json da skill
- [ ] Todos os campos obrigatórios presentes
- [ ] Tipos corretos (arrays são arrays, números são números)

## Resultado

Retorne:
```json
{
  "approved": true/false,
  "issues": [
    {"type": "consistency|quality|schema", "field": "...", "message": "..."}
  ],
  "auto_fixed": ["lista de problemas que você corrigiu automaticamente"]
}
```

Se `approved: false`, liste os issues e sugira correções. O operador decide se aceita ou ajusta.
```

- [ ] **Step 2: Commit**

```bash
git add plugins/v4-estruturacao-ia/agents/revisor-qualidade.md
git commit -m "feat: add quality reviewer agent"
```

---

## Phase 4: Week 1 Skills (Diagnóstico)

### Task 14: Create persona-icp skill (ROOT — mais referenciada)

**Files:**
- Create: `plugins/v4-estruturacao-ia/skills/persona-icp/SKILL.md`
- Create: `plugins/v4-estruturacao-ia/skills/persona-icp/schema.json`
- Create: `plugins/v4-estruturacao-ia/skills/persona-icp/references/jtbd-framework.md`
- Create: `plugins/v4-estruturacao-ia/skills/persona-icp/references/exemplos-bom-vs-ruim.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: persona-icp
description: "Cria ICP (Ideal Customer Profile) e Persona com Jobs-to-be-Done. Skill mais fundamental — alimenta todas as outras. Use quando o operador iniciar semana 1 ou pedir 'definir ICP', 'criar persona', 'quem é o cliente ideal'."
---

# Persona e ICP — Perfil do Cliente Ideal

Esta é a skill mais crítica do sistema. Se o ICP estiver errado, tudo downstream está errado.

## Inputs necessários

Leia de `briefing.json`:
- `product.main_product` — produto/serviço principal
- `product.ticket` — ticket médio
- `identification.segment` — segmento
- `identification.location` — região
- `icp.best_customers` — descrição dos 3 melhores clientes
- `icp.not_customers` — quem NÃO é cliente
- `icp.problems_before` — 3 problemas pré-contratação
- `icp.results_after` — 3 resultados pós-contratação

Se dados do V4MOS existirem (`v4mos-cache.json`):
- Verificar se já tem MarketingProfile com dados de ICP
- Usar como base, não como verdade absoluta

## Checkpoints

### Checkpoint 1: Validar inputs
Apresente ao operador um resumo dos dados que você tem:
```
Produto: {x}
Ticket: R${y}
Segmento: {z}
Melhores clientes: {descrição}
```
Pergunte: "Esses dados estão corretos? Algo que eu deveria saber que não está aqui?"

### Checkpoint 2: ICP draft
Gere o ICP completo seguindo o framework JTBD (leia `references/jtbd-framework.md`):
- Dados demográficos
- Dados comportamentais
- Jobs: funcional, emocional, social
- Dores (3-5, ordenadas por intensidade)
- Ganhos desejados (3-5)

Apresente ao operador. Pergunte: "Esse ICP faz sentido pro mercado desse cliente? Algo exagerado ou faltando?"

### Checkpoint 3: Persona
Com o ICP aprovado, crie a Persona:
- Nome fictício realista
- Descrição da foto de perfil (para referência visual)
- História de 1 parágrafo
- Frase que ela diria sobre o problema
- Onde encontrar (canais, keywords, influenciadores, comunidades)

Apresente. Pergunte: "O tom está certo? Essa pessoa existe no mercado desse cliente?"

### Checkpoint 4: Mensagem chave
Em 1 frase: como comunicar o valor para este ICP.
Apresente 3 opções. Operador escolhe ou pede variação.

## Output

Salve `persona-icp.json` seguindo o schema.json, incluindo campo `summary` no topo:
```json
{
  "summary": "ICP: [perfil em 1 linha]. Persona: [nome], [perfil em 1 linha]. PUV: [mensagem chave escolhida]",
  "icp": { ... },
  "persona": { ... },
  "where_to_find": { ... },
  "key_message": "..."
}
```

## Quality gates (verificados pelo revisor-qualidade)
- Jobs-to-be-Done são específicos (não "quer crescer")
- Dores são genuinamente dolorosas (cliente se reconhece)
- Mensagem chave difere do que o cliente já usa
- Persona tem detalhes concretos (não é genérica)

## Referências
- `references/jtbd-framework.md` — Framework completo de Jobs-to-be-Done com exemplos
- `references/exemplos-bom-vs-ruim.md` — 5 exemplos de ICPs bons vs ruins para calibrar
```

- [ ] **Step 2: Write schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["summary", "icp", "persona", "where_to_find", "key_message"],
  "properties": {
    "summary": { "type": "string", "description": "Resumo de 1-2 linhas para contexto rápido" },
    "icp": {
      "type": "object",
      "required": ["demographics", "behavior", "jobs", "pains", "gains"],
      "properties": {
        "demographics": {
          "type": "object",
          "properties": {
            "revenue_or_income": { "type": "string" },
            "sector_niche": { "type": "string" },
            "location": { "type": "string" },
            "company_size_or_profile": { "type": "string" }
          }
        },
        "behavior": {
          "type": "object",
          "properties": {
            "purchase_decision": { "type": "string" },
            "research_channels": { "type": "string" },
            "main_objections": { "type": "string" },
            "switching_triggers": { "type": "string" }
          }
        },
        "jobs": {
          "type": "object",
          "required": ["functional", "emotional", "social"],
          "properties": {
            "functional": { "type": "string" },
            "emotional": { "type": "string" },
            "social": { "type": "string" }
          }
        },
        "pains": {
          "type": "array",
          "items": { "type": "object", "properties": { "pain": {"type":"string"}, "intensity": {"type":"string","enum":["alta","media","baixa"]} } },
          "minItems": 3,
          "maxItems": 5
        },
        "gains": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 3,
          "maxItems": 5
        }
      }
    },
    "persona": {
      "type": "object",
      "required": ["name", "photo_description", "story", "quote"],
      "properties": {
        "name": { "type": "string" },
        "photo_description": { "type": "string" },
        "story": { "type": "string" },
        "quote": { "type": "string" }
      }
    },
    "where_to_find": {
      "type": "object",
      "properties": {
        "digital_channels": { "type": "array", "items": { "type": "string" } },
        "keywords": { "type": "array", "items": { "type": "string" } },
        "influencers": { "type": "array", "items": { "type": "string" } },
        "communities": { "type": "array", "items": { "type": "string" } }
      }
    },
    "key_message": { "type": "string" }
  }
}
```

- [ ] **Step 3: Write references/jtbd-framework.md**

```markdown
# Framework Jobs-to-be-Done para ICP

## O que é JTBD

Clientes não compram produtos — eles "contratam" soluções para "jobs" que precisam fazer.

## Os 3 tipos de jobs

### Job Funcional
O que o cliente precisa FAZER na prática.
- BOM: "Preciso gerar 50 leads qualificados por mês para minha equipe de vendas"
- RUIM: "Precisa de marketing" (genérico demais)

### Job Emocional
Como o cliente quer se SENTIR.
- BOM: "Quero sentir que meu investimento em marketing está sob controle e previsível"
- RUIM: "Quer se sentir bem" (genérico)

### Job Social
Como o cliente quer ser VISTO pelos outros.
- BOM: "Quero que meus concorrentes olhem meu Instagram e pensem 'eles estão em outro nível'"
- RUIM: "Quer ser reconhecido" (genérico)

## Como extrair jobs dos dados do briefing

1. Leia a descrição dos "melhores clientes" — o que eles tinham em comum?
2. Leia os "problemas antes de contratar" — esses são os jobs não resolvidos
3. Leia os "resultados após contratar" — esses são os jobs resolvidos
4. A lacuna entre 2 e 3 é o job real

## Dores: como priorizar

Ordene por intensidade:
- **Alta:** o cliente PERDE dinheiro ou clientes por causa disso
- **Média:** o cliente gasta TEMPO demais lidando com isso
- **Baixa:** é inconveniente mas não urgente

Uma dor só é "alta" se tem consequência financeira ou operacional concreta.
```

- [ ] **Step 4: Write references/exemplos-bom-vs-ruim.md**

```markdown
# Exemplos: ICP Bom vs Ruim

## Exemplo 1: Clínica de Estética

### RUIM ❌
- ICP: "Mulheres que querem ficar bonitas"
- Job: "Quer melhorar a aparência"
- Dor: "Não gosta do que vê no espelho"

### BOM ✅
- ICP: "Mulheres 35-50, classe B+, profissionais ativas, que percebem sinais de envelhecimento e sentem que isso impacta sua confiança em reuniões de trabalho"
- Job funcional: "Preciso de um tratamento que dê resultado visível em 3 sessões porque não tenho tempo para procedimentos longos"
- Job emocional: "Quero me olhar no espelho de manhã e não pensar 'preciso resolver isso'"
- Dor alta: "Já gastei R$3.000 em tratamentos que não funcionaram e agora desconfio de todos"

## Exemplo 2: Consultoria Financeira B2B

### RUIM ❌
- ICP: "Empresas que precisam de consultoria financeira"
- Persona: "João, empresário, quer crescer"

### BOM ✅
- ICP: "Empresas de serviços com 10-50 funcionários, faturamento R$2-10M/ano, que cresceram rápido nos últimos 2 anos e agora não sabem se estão lucrando de verdade ou só movimentando dinheiro"
- Persona: "Carlos, 42, sócio-fundador de agência de TI. Fatura R$5M/ano mas não sabe o lucro líquido real. Perdeu o sono quando o contador disse que o imposto do trimestre seria 3x o esperado."
- Job funcional: "Preciso saber exatamente quanto sobra no fim do mês e quanto posso reinvestir sem risco"
- Dor alta: "Tomei uma decisão de contratar 5 pessoas baseado no faturamento e quase quebrei — a margem era 8%, não os 25% que eu achava"

## Exemplo 3: Escola de Idiomas

### RUIM ❌
- Mensagem chave: "Aprenda inglês com qualidade e compromisso"

### BOM ✅  
- Mensagem chave: "Inglês fluente em 8 meses ou devolvemos seu investimento — para profissionais que já tentaram outras escolas e desistiram"

## O teste do ICP bom

Se você ler o ICP e pensar "isso poderia ser qualquer empresa do setor" → está genérico.
Se você ler e pensar "eu conheço alguém exatamente assim" → está específico.
```

- [ ] **Step 5: Commit**

```bash
git add plugins/v4-estruturacao-ia/skills/persona-icp/
git commit -m "feat: add persona-icp skill with JTBD framework and examples"
```

---

### Task 15: Create diagnostico-maturidade skill

**Files:**
- Create: `plugins/v4-estruturacao-ia/skills/diagnostico-maturidade/SKILL.md`
- Create: `plugins/v4-estruturacao-ia/skills/diagnostico-maturidade/schema.json`
- Create: `plugins/v4-estruturacao-ia/skills/diagnostico-maturidade/references/scoring-framework.md`

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: diagnostico-maturidade
description: "Análise de maturidade digital usando dados do V4MOS. Gera relatório com score por pilar, gaps, benchmarks e prioridades. Use quando iniciar semana 1 ou operador pedir 'diagnóstico', 'maturidade digital', 'score digital'."
---

# Diagnóstico de Maturidade Digital

## Inputs necessários

**Do V4MOS (v4mos-cache.json):**
- `diagnoses` — diagnóstico já processado (5 steps: market, company, communication, actionPlan, digitalMaturity)
- `integrations` — integrações ativas e status

**Do briefing.json:**
- `identification.segment` — para benchmark do setor
- `identification.name` — nome do cliente

## Checkpoints

### Checkpoint 1: Verificar dados V4MOS
Leia v4mos-cache.json. Se existe diagnóstico:
- Mostre o score geral e breakdown por pilar
- Pergunte: "Esses números fazem sentido? Algo que o diagnóstico automático pode ter errado?"

Se NÃO existe diagnóstico:
- Avise o operador: "Não encontrei diagnóstico no V4MOS. Preciso que você registre o cliente na plataforma V4 Marketing (v4.marketing) e conecte os acessos. Leva ~30min. Quer instruções?"
- Se operador não quer esperar: gere diagnóstico baseado nos dados do briefing (inferior mas funcional)

### Checkpoint 2: Análise contextualizada
Com os dados (V4MOS ou briefing), gere:
1. Resumo executivo (3 parágrafos máximo):
   - Score geral e o que significa na prática
   - 2 maiores gaps custando resultado agora
   - 2 pontos fortes a aproveitar
2. Prioridades de ação (5, em ordem de impacto)
3. Benchmark do setor (consulte references/scoring-framework.md)

Apresente ao operador. Pergunte: "Ajustar algum ponto?"

### Checkpoint 3: Aprovação final
Mostre o output completo formatado. Operador aprova → salvar.

## Output

Salve `diagnostico-maturidade.json` seguindo schema.json.

## Referências
- `references/scoring-framework.md` — Critérios de scoring e benchmarks por setor
```

- [ ] **Step 2: Write schema.json e references/scoring-framework.md** (seguindo o mesmo padrão de persona-icp)

- [ ] **Step 3: Commit**

```bash
git add plugins/v4-estruturacao-ia/skills/diagnostico-maturidade/
git commit -m "feat: add diagnostico-maturidade skill with V4MOS integration"
```

---

### Task 16: Create swot skill

Mesma estrutura. SKILL.md com 3 checkpoints:
1. Validar inputs (dados maturidade + briefing + concorrentes)
2. Draft SWOT (4-6 itens por quadrante, todos específicos)
3. Síntese estratégica (2 parágrafos)

Schema: strengths[], weaknesses[], opportunities[], threats[] (cada com title, description, implication), strategic_synthesis.

References: exemplos-swot-bom-vs-ruim.md

Dependencies: diagnostico-maturidade

---

### Task 17: Create auditoria-comunicacao skill

Mesma estrutura. SKILL.md com 4 checkpoints:
1. Validar inputs (ICP, URLs, handles)
2. Auditar cada canal (site, Instagram, anúncios, GMB, WhatsApp)
3. Gerar matriz de gaps
4. Quick wins (3 ações em <1 semana)

Schema: channels[] (name, gaps[], score), gap_matrix[], executive_summary, quick_wins[].

References: checklist-auditoria-por-canal.md

Dependencies: persona-icp

Note: esta skill usa capacidade multimodal do Claude (análise de screenshots). O operador fornece prints.

---

## Phase 5: Week 2 Skills (Pesquisa e Posicionamento)

### Task 18: Create pesquisa-mercado skill

SKILL.md com 4 checkpoints:
1. Validar escopo (segmento, região, concorrentes)
2. TAM/SAM/SOM (com fontes e metodologia)
3. Análise de concorrentes (posicionamento, canais, forças, fraquezas)
4. Tendências e JTBD do mercado

Schema: tam_sam_som{}, competitors[], trends[], market_jtbd{}, real_differentials[].

References: framework-tam-sam-som.md, template-analise-concorrente.md

Dependencies: persona-icp. Usa WebSearch do Claude Code.

---

### Task 19: Create posicionamento skill

**SKILL MAIS IMPORTANTE DA SEMANA 2.** SKILL.md com 5 checkpoints:
1. Carregar inputs (ICP, pesquisa-mercado, SWOT)
2. Análise de concorrentes posicionais (mapa 2x2)
3. 3 opções de PUV (operador escolhe direção)
4. Canvas 4P completo (Produto, Preço, Praça, Promoção)
5. Território de marca + 3 opções de tagline

Schema: positioning_statement (3 versions), puv, canvas_4p{}, brand_territory, taglines[].

References: exemplos-puv.md, canvas-4p-guide.md, territorio-de-marca.md

Dependencies: pesquisa-mercado, persona-icp, swot

---

### Task 20: Create diagnostico-midia skill

SKILL.md com 3 checkpoints:
1. Puxar dados V4MOS (MediaInvestment, integrações Meta/Google ativas)
2. Métricas atuais vs benchmarks do setor
3. Top 3 problemas + plano de ação 30 dias + meta realista 90 dias

Schema: current_metrics{}, benchmarks{}, diagnosis_by_dimension{}, top_problems[], action_plan[], realistic_goal{}.

Dependencies: persona-icp. Grande ganho V4MOS — dados reais.

---

### Task 21: Create diagnostico-criativos skill

SKILL.md com 3 checkpoints:
1. Receber screenshots de criativos do operador (multimodal)
2. Matriz de avaliação (hook, clareza, coerência ICP, CTA, visual — score 1-5 cada)
3. Briefing para produção semana 3

Schema: creative_matrix[], patterns_identified[], what_works[], competitor_analysis[], production_briefing{}.

Dependencies: persona-icp

---

### Task 22: Create diagnostico-cro skill

SKILL.md com 4 checkpoints:
1. Dados técnicos (PageSpeed via API ou operador cola resultado)
2. Auditoria de copy (above the fold, seção por seção)
3. Hipóteses de teste priorizadas
4. Wireframe de melhorias (para a skill landing-page usar)

Schema: technical_diagnosis{}, copy_audit{}, trust_analysis{}, test_hypotheses[], wireframe_improvements[].

Dependencies: persona-icp, posicionamento

---

## Phase 6: Week 3 Skills (Produção e Implementação)

### Task 23: Create identidade-visual skill

Semi-manual. SKILL.md com 3 checkpoints:
1. Conceito estratégico (paleta, tipografia, diretrizes de forma)
2. Prompts para Midjourney/Ideogram (3 direções de logo)
3. Operador executa no Midjourney, traz resultado, skill organiza o manual

Schema: creative_concept, color_palette[], typography{}, shape_guidelines{}, logo_prompts[].

Dependencies: posicionamento

---

### Task 24: Create brandbook skill

SKILL.md com 4 checkpoints:
1. Propósito e posicionamento verbal
2. Identidade verbal (tom de voz, como escrevemos, como NÃO escrevemos)
3. Narrativa da marca (3 atos + template narrativo)
4. Banco de copy (10 headlines por formato + CTAs + frases-chave + vocabulário)

Schema: purpose{}, verbal_identity{}, brand_narrative{}, copy_bank{}, vocabulary{}.

Dependencies: posicionamento, persona-icp

---

### Task 25: Create landing-page skill

SKILL.md com 4 checkpoints:
1. Copy completa seção por seção (hero, problema, solução, como funciona, prova social, FAQ, CTA)
2. Operador revisa copy
3. Geração de código (React/Next.js + Tailwind via Claude Code)
4. Deploy na Vercel (`vercel --yes --prod`)

Schema: sections[] (name, headline, body, cta), faq[], social_proof{}.

Dependencies: posicionamento, brandbook, diagnostico-cro

---

### Task 26: Create copy-anuncios skill

SKILL.md com 3 checkpoints:
1. Gerar 30+ variações (topo/meio/fundo funil × Meta/Google)
2. Operador revisa variações
3. Exportar para Google Sheets via GOG

Schema: funnel_stages[] → variations[] (platform, text, headline, description, cta).

Dependencies: brandbook, persona-icp, posicionamento

Output: Google Sheets via `gog sheets create`

---

### Task 27: Create criativos-anuncios skill

Semi-manual. SKILL.md com 3 checkpoints:
1. Briefing criativo (5 variações com hooks diferentes: dor, resultado, curiosidade, prova social, urgência)
2. Prompts para Midjourney/Ideogram por variação
3. Operador executa geração visual, skill organiza o pack

Schema: variations[] (hook_type, short_copy, medium_copy, headline, description, visual_concept, format).

Dependencies: brandbook, identidade-visual, diagnostico-criativos

---

### Task 28: Create crm-setup skill

Semi-manual. SKILL.md com 3 checkpoints:
1. Gerar copy das réguas (boas-vindas + nutrição 30 dias)
2. Guia passo-a-passo de configuração no Kommo
3. Checklist de teste (operador testa com lead fictício)

Schema: welcome_sequence[] (message, timing), nurture_sequence[] (week, channel, message), pipeline_stages[].

Dependencies: persona-icp

---

### Task 29: Create forecast-midia skill

SKILL.md com 3 checkpoints:
1. Modelagem financeira 3 meses (budget, CPL, leads, vendas, ROAS)
2. Distribuição por plataforma e funil
3. Alertas e critérios de pausa

Schema: financial_model[] (month, metrics{}), platform_distribution[], funnel_distribution[], timeline[], alerts[].

Dependencies: diagnostico-midia

Output: Google Sheets via `gog sheets create`

---

### Task 30: Create gmb-otimizacao skill

Guia interativo. SKILL.md com 3 checkpoints:
1. Gerar descrição otimizada + categorias + serviços
2. Gerar 4 posts para 30 dias + 5 Q&As
3. Checklist de implementação (operador executa no GMB)

Schema: profile_description, categories{}, services[], posts[], qas[].

Dependencies: persona-icp

---

## Phase 7: Week 4-5 Skills (Vendas)

### Task 31: Create diagnostico-comercial skill

SKILL.md com 4 checkpoints:
1. Diagnóstico do funil (taxa por etapa vs benchmark)
2. Mapa de objeções (tipo, momento, resposta recomendada)
3. Critérios de qualificação (1-5 estrelas)
4. SLA de atendimento

Schema: funnel_diagnosis[], objection_map[], action_plan[], qualification_criteria{}, sla{}.

Dependencies: persona-icp

---

### Task 32: Create cliente-oculto skill

SKILL.md com 3 checkpoints:
1. Criar perfil do comprador simulado + roteiro
2. Operador executa a simulação (envia mensagens reais)
3. Colar conversa no Claude, gerar relatório com nota 0-10

Schema: buyer_profile{}, simulation_script{}, evaluation{score, strengths[], improvements[], sdr_impact[]}.

Dependencies: diagnostico-comercial

---

### Task 33: Create scripts-sdr skill

SKILL.md com 5 checkpoints:
1. Mensagem de boas-vindas
2. Perguntas de qualificação (4-5)
3. Fluxo por score (4-5★, 3★, 1-2★)
4. Tratamento de objeções
5. Follow-up e transferência para humano

Schema: welcome_message, qualification_questions[], score_flows{}, objection_responses[], followup_messages[], human_handoff.

Dependencies: diagnostico-comercial, brandbook

---

### Task 34: Create sdr-ia-config skill

Guia interativo. SKILL.md com 4 checkpoints:
1. Configuração no Patagon (passo-a-passo)
2. Integração Kommo (API key, mapeamento de campos)
3. Configuração de alertas WhatsApp
4. Testes com 5 leads simulados

Schema: patagon_config{}, kommo_integration{}, alerts_config{}, test_results[].

Dependencies: scripts-sdr, crm-setup

---

## Phase 8: Templates HTML

### Task 35: Create base HTML template

**Files:**
- Create: `plugins/v4-estruturacao-ia/shared-templates/base.html`
- Create: `plugins/v4-estruturacao-ia/shared-templates/base.css`

O template base segue a identidade V4:
- Fundo escuro (#0a0a0a)
- Texto claro (#e5e2e1)
- Acento vermelho (#e50914)
- Tipografia: system-ui como fallback (Bebas Neue + Montserrat quando disponíveis)
- Layout responsivo, mobile-first
- Logo V4 no header
- Data e nome do cliente no header

Cada skill que gera HTML entregável terá seu template específico que extends do base. Os templates específicos serão criados quando o Gui disponibilizar os Google Docs/Slides existentes do Figueiredo.

---

### Task 36: [BLOQUEADO] Criar templates HTML por entregável

**Status: Aguardando Gui disponibilizar acesso aos templates existentes em Google Docs/Slides.**

Quando disponível:
1. Listar todos os 14 templates HTML necessários
2. Para cada um, verificar se já existe versão no Docs/Slides
3. Converter cada um para HTML + CSS que consome JSON do schema da skill
4. Testar renderização com dados de exemplo

Templates necessários:
| # | Template | Skill | Existe no Docs? |
|---|----------|-------|-----------------|
| 1 | Diagnóstico de Maturidade | diagnostico-maturidade | ? |
| 2 | SWOT | swot | ? |
| 3 | Persona / ICP | persona-icp | ? |
| 4 | Auditoria de Comunicação | auditoria-comunicacao | ? |
| 5 | Pesquisa de Mercado | pesquisa-mercado | ? |
| 6 | Canvas de Posicionamento | posicionamento | ? |
| 7 | Diagnóstico de Mídia | diagnostico-midia | ? |
| 8 | Diagnóstico de Criativos | diagnostico-criativos | ? |
| 9 | Diagnóstico CRO | diagnostico-cro | ? |
| 10 | Brandbook | brandbook | ? |
| 11 | Diagnóstico Comercial | diagnostico-comercial | ? |
| 12 | Cliente Oculto | cliente-oculto | ? |
| 13 | Dashboard do Cliente | state.json | N/A (novo) |
| 14 | Dashboard Geral | state.json | N/A (novo) |

---

## Execution Order Summary

**Pode ser paralelizado:**
- Phase 0 (scaffold) → sequencial
- Phase 1 (infra) → sequencial
- Phase 2 (utility skills) → paralelo entre si
- Phase 3 (agents) → paralelo entre si
- Phase 4 (week 1 skills) → persona-icp primeiro, depois os outros 3 em paralelo
- Phase 5 (week 2 skills) → pesquisa-mercado primeiro, depois posicionamento, depois os outros 3 em paralelo
- Phase 6 (week 3 skills) → paralelo exceto landing-page (depende de brandbook + diagnostico-cro)
- Phase 7 (week 4-5 skills) → diagnostico-comercial primeiro, depois os outros em sequência
- Phase 8 (templates) → bloqueado até Gui dar acesso

**Estimativa:** ~34 tasks, cada uma produzindo 2-5 arquivos. Skills são majoritariamente markdown com JSON schemas. Tempo estimado de implementação: 2-3 sessões de trabalho intensivo.

---

## Checklist final antes de v0.1.0

- [ ] Todas as 25 skills têm SKILL.md + schema.json
- [ ] Todos os skills têm pelo menos 1 arquivo em references/
- [ ] dependency_graph.json cobre todas as skills
- [ ] Scripts bash funcionam em Mac, Linux, e Windows (via WSL/Git Bash)
- [ ] README.md com instruções completas de setup
- [ ] Testado end-to-end com 1 cliente fictício (semana 1 completa)
- [ ] Templates HTML base funcionando para pelo menos 3 entregáveis
- [ ] /onboarding funciona do zero
- [ ] /feedback cria issue no GitHub
- [ ] Dashboard geral renderiza corretamente com 2+ clientes
