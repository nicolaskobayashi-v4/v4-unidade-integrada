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
