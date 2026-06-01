#!/bin/bash
# update_state.sh — Update skill status in client.json
# Usage: ./update_state.sh <client_dir> <skill_name> <status> [checkpoint]
#
# Status values: pending | in_progress | completed

set -euo pipefail

CLIENT_DIR="$1"
SKILL="$2"
STATUS="$3"
CHECKPOINT="${4:-0}"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)

CLIENT_JSON="$CLIENT_DIR/client.json"

if [ ! -f "$CLIENT_JSON" ]; then
  echo "ERROR: client.json não encontrado em $CLIENT_DIR"
  exit 1
fi

TMP="$CLIENT_JSON.tmp"

jq \
  --arg skill "$SKILL" \
  --arg status "$STATUS" \
  --argjson checkpoint "$CHECKPOINT" \
  --arg now "$NOW" \
  '
  .progress.skills[$skill].status = $status |
  .progress.skills[$skill].version = ((.progress.skills[$skill].version // 0) + (if $status == "completed" then 1 else 0 end)) |
  if $status == "in_progress" and (.progress.skills[$skill].started_at == null)
    then .progress.skills[$skill].started_at = $now else . end |
  if $status == "completed"
    then .progress.skills[$skill].completed_at = $now else . end
  ' "$CLIENT_JSON" > "$TMP" && mv "$TMP" "$CLIENT_JSON"

echo "✓ $SKILL → $STATUS (checkpoint $CHECKPOINT)"
