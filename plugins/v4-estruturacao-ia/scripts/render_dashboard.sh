#!/bin/bash
# render_dashboard.sh — Generate dashboard HTML from client.json
# Usage:
#   Single client:  ./render_dashboard.sh <client_dir>
#   All clients:    ./render_dashboard.sh <workspace_root> --general

set -euo pipefail

if [ "${2:-}" = "--general" ]; then
  WORKSPACE="$1"
  OUTPUT="$WORKSPACE/dashboard-geral.html"

  CLIENTS_JSON="["
  FIRST=true
  for CLIENT_FILE in "$WORKSPACE"/clientes/*/client.json; do
    [ -f "$CLIENT_FILE" ] || continue
    if [ "$FIRST" = true ]; then FIRST=false; else CLIENTS_JSON+=","; fi
    # Extract the fields the dashboard needs
    CLIENTS_JSON+=$(jq '{
      name: .meta.name,
      slug: .meta.slug,
      current_week: .progress.current_week,
      skills: .progress.skills,
      created_at: .meta.created_at
    }' "$CLIENT_FILE")
  done
  CLIENTS_JSON+="]"

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
  .client-week { color: #888; font-size: 0.9rem; margin-top: 0.25rem; }
  .progress-bar { height: 6px; background: #333; border-radius: 3px; margin: 0.75rem 0; overflow: hidden; }
  .progress-fill { height: 100%; background: #FB2E0A; border-radius: 3px; transition: width 0.3s; }
  .stats { display: flex; gap: 1rem; font-size: 0.8rem; color: #aaa; }
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
  const wip = skills.filter(s => s.status === 'in_progress').length;
  const pct = total > 0 ? Math.round((done / total) * 100) : 0;
  document.getElementById('clients').innerHTML += `
    <div class="client-card">
      <div class="client-name">${c.name}</div>
      <div class="client-week">Semana ${c.current_week || 1} · ${done}/${total} skills · ${pct}%</div>
      <div class="progress-bar"><div class="progress-fill" style="width:${pct}%"></div></div>
      <div class="stats">
        <span>${done} completas</span>
        <span>${wip} em andamento</span>
        <span>${total - done - wip} pendentes</span>
      </div>
    </div>`;
});
</script>
</body>
</html>
HTMLEOF2

  echo "✓ Dashboard geral: $OUTPUT"

else
  # Single client dashboard
  CLIENT_DIR="$1"
  CLIENT_JSON="$CLIENT_DIR/client.json"
  OUTPUT="$CLIENT_DIR/dashboard.html"

  if [ ! -f "$CLIENT_JSON" ]; then
    echo "ERROR: client.json não encontrado em $CLIENT_DIR"
    exit 1
  fi

  CLIENT_NAME=$(jq -r '.meta.name' "$CLIENT_JSON")
  CURRENT_WEEK=$(jq -r '.progress.current_week // 1' "$CLIENT_JSON")
  CREATED_AT=$(jq -r '.meta.created_at // ""' "$CLIENT_JSON")
  STATE=$(jq '{
    name: .meta.name,
    current_week: .progress.current_week,
    created_at: .meta.created_at,
    skills: .progress.skills
  }' "$CLIENT_JSON")

  cat > "$OUTPUT" << HTMLEOF
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>$CLIENT_NAME — Dashboard</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0a0a0a; color: #e5e2e1; padding: 2rem; }
  h1 { font-size: 1.5rem; margin-bottom: 0.5rem; color: #fff; }
  .meta { color: #888; margin-bottom: 1.5rem; font-size: 0.9rem; }
  .week { background: #1a1a1a; border: 1px solid #333; border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem; }
  .week-title { font-weight: 700; margin-bottom: 0.75rem; color: #FB2E0A; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 0.05em; }
  .skill-row { display: flex; justify-content: space-between; align-items: center; padding: 0.4rem 0; border-bottom: 1px solid #222; font-size: 0.875rem; }
  .skill-row:last-child { border-bottom: none; }
  .status-completed { color: #4ade80; font-weight: 600; }
  .status-in_progress { color: #facc15; font-weight: 600; }
  .status-pending { color: #555; }
</style>
</head>
<body>
<h1>$CLIENT_NAME</h1>
<div class="meta">Semana $CURRENT_WEEK · Início: $CREATED_AT</div>
<div id="weeks"></div>
<script>
const state = $STATE;
const skills = state.skills || {};
const rows = Object.entries(skills).map(([id, s]) => \`
  <div class="skill-row">
    <span>\${id.replace('ee-s','S').replace(/-/g,' ')}</span>
    <span class="status-\${s.status}">\${s.status}</span>
  </div>\`).join('');
document.getElementById('weeks').innerHTML = \`<div class="week"><div class="week-title">Skills</div>\${rows}</div>\`;
</script>
</body>
</html>
HTMLEOF

  echo "✓ Dashboard do cliente: $OUTPUT"
fi
