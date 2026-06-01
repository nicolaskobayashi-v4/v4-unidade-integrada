#!/bin/bash
# meta_ads_fetch.sh — Orquestra scraping da Meta Ads Library com cache de 7 dias.
#
# Uso:
#   meta_ads_fetch.sh <client_dir> [--force]
#
# Ex:
#   meta_ads_fetch.sh clientes/<slug-do-cliente>
#   meta_ads_fetch.sh clientes/<slug-do-cliente> --force
#
# Paginas a raspar:
#   Por padrao, le de <client_dir>/meta-ads-pages.txt (uma por linha, formato slug:page_id_or_search).
#   Se o arquivo nao existir, tenta ler de client.json (meta.meta_ads_pages[]).
#
# Override via env:
#   META_PAGES="slug1:pageid1,slug2:search2" meta_ads_fetch.sh <client_dir>
#   MAX_ADS=30 COUNTRY=BR HEADLESS=true meta_ads_fetch.sh <client_dir>
#
# Cache:
#   Se <client_dir>/assets/creatives/meta/_latest.json existir e fetched_at < 7 dias,
#   pula scraping. Use --force para ignorar o cache.

set -euo pipefail

CLIENT_DIR="${1:?Uso: meta_ads_fetch.sh <client_dir> [--force]}"
FORCE="${2:-}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PY_SCRIPT="$SCRIPT_DIR/meta_ads_fetch.py"

if [ ! -f "$PY_SCRIPT" ]; then
  echo "ERROR: meta_ads_fetch.py nao encontrado em $PY_SCRIPT" >&2
  exit 1
fi

if [ ! -d "$CLIENT_DIR" ]; then
  echo "ERROR: client_dir $CLIENT_DIR nao existe" >&2
  exit 1
fi

LATEST_FILE="$CLIENT_DIR/assets/creatives/meta/_latest.json"

# Cache check (7 dias = 604800 segundos)
if [ "$FORCE" != "--force" ] && [ -f "$LATEST_FILE" ]; then
  FETCHED_AT=$(python3 -c "import json,sys; d=json.load(open('$LATEST_FILE')); print(d.get('fetched_at',''))" 2>/dev/null || echo "")
  if [ -n "$FETCHED_AT" ]; then
    AGE_SEC=$(python3 -c "
import datetime as dt
try:
    t = dt.datetime.fromisoformat('$FETCHED_AT'.replace('Z','+00:00'))
    now = dt.datetime.now(dt.timezone.utc)
    print(int((now - t).total_seconds()))
except Exception:
    print(999999999)
" 2>/dev/null || echo "999999999")
    if [ "$AGE_SEC" -lt 604800 ]; then
      AGE_DAYS=$((AGE_SEC / 86400))
      echo ">> Cache fresco (${AGE_DAYS}d < 7d). Pulando scraping."
      echo ">> Use --force para forcar refetch."
      echo ">> Manifesto: $LATEST_FILE"
      exit 0
    fi
  fi
fi

# Resolve lista de paginas
PAGES_ARG=""

if [ -n "${META_PAGES:-}" ]; then
  PAGES_ARG="$META_PAGES"
elif [ -f "$CLIENT_DIR/meta-ads-pages.txt" ]; then
  PAGES_ARG=$(grep -vE '^\s*(#|$)' "$CLIENT_DIR/meta-ads-pages.txt" | paste -sd "," -)
elif [ -f "$CLIENT_DIR/client.json" ]; then
  PAGES_ARG=$(python3 -c "
import json
d = json.load(open('$CLIENT_DIR/client.json'))
pages = d.get('meta', {}).get('meta_ads_pages', [])
out = []
for p in pages:
    slug = p.get('slug')
    target = p.get('page_id') or p.get('search')
    if slug and target:
        out.append(f'{slug}:{target}')
print(','.join(out))
" 2>/dev/null || echo "")
fi

if [ -z "$PAGES_ARG" ]; then
  echo "ERROR: nenhuma pagina definida." >&2
  echo "  Defina META_PAGES env, ou crie $CLIENT_DIR/meta-ads-pages.txt," >&2
  echo "  ou adicione meta.meta_ads_pages[] em client.json" >&2
  exit 1
fi

MAX_ADS="${MAX_ADS:-30}"
COUNTRY="${COUNTRY:-BR}"
HEADLESS="${HEADLESS:-true}"

mkdir -p "$CLIENT_DIR/cache"
mkdir -p "$CLIENT_DIR/assets/creatives/meta"

echo ">> Rodando meta_ads_fetch para $CLIENT_DIR ..."
echo ">> Paginas: $PAGES_ARG"
echo ">> max-ads=$MAX_ADS country=$COUNTRY headless=$HEADLESS"
echo

python3 "$PY_SCRIPT" "$CLIENT_DIR" \
  --pages "$PAGES_ARG" \
  --max-ads "$MAX_ADS" \
  --country "$COUNTRY" \
  --headless "$HEADLESS"

echo
echo ">> Manifesto consolidado: $LATEST_FILE"
