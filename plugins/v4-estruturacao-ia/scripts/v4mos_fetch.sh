#!/bin/bash
# v4mos_fetch.sh — Fetch media data from V4MOS Data API
# Usage: ./v4mos_fetch.sh <client_dir> [date_start] [date_end]
#
# Reads:  <client_dir>/client.json (meta.workspace_id, meta.name)
#         .credentials/clients.json (client_id, client_secret)
# Writes: <client_dir>/client.json (connectors section)
#
# API: https://api.data.v4.marketing/v1
# Auth: x-client-id + x-client-secret headers
# workspaceId is a QUERY PARAMETER on every request
#
# Endpoints usados:
#   google/ads/campaigns   → totais + monthly_evolution + day_of_week
#   google/ads/gender      → gender_breakdown
#   google/ads/keywords    → top_keywords
#   facebook/ads/campaigns → totais + monthly_evolution (por date_start)
#   facebook/ads/ad        → ads agregados (métricas por ad)
#   facebook/ads/creatives → metadata visual dos criativos

set -euo pipefail

CLIENT_DIR="$1"
DATE_START="${2:-$(date -u -v-90d +%Y-%m-%dT00:00:00Z 2>/dev/null || date -u -d '90 days ago' +%Y-%m-%dT00:00:00Z)}"
DATE_END="${3:-$(date -u +%Y-%m-%dT23:59:59Z)}"
CLIENT_JSON="$CLIENT_DIR/client.json"
V4MOS_API="https://api.data.v4.marketing/v1"

if [ ! -f "$CLIENT_JSON" ]; then
  echo "ERROR: client.json não encontrado em $CLIENT_DIR"
  exit 1
fi

CLIENT_NAME=$(jq -r '.meta.name // "Cliente"' "$CLIENT_JSON")
WORKSPACE_ID=$(jq -r '.meta.workspace_id // empty' "$CLIENT_JSON")

if [ -z "$WORKSPACE_ID" ] || [ "$WORKSPACE_ID" = "null" ]; then
  echo "SKIP: workspace_id não definido — cliente sem integração V4MOS"
  exit 0
fi

# Find credentials file (search up from client dir)
CREDENTIALS_FILE=""
SEARCH_DIR="$CLIENT_DIR"
for i in 1 2 3 4 5; do
  SEARCH_DIR="$(dirname "$SEARCH_DIR")"
  if [ -f "$SEARCH_DIR/.credentials/clients.json" ]; then
    CREDENTIALS_FILE="$SEARCH_DIR/.credentials/clients.json"
    break
  fi
done

if [ -z "$CREDENTIALS_FILE" ]; then
  echo "ERROR: .credentials/clients.json não encontrado"
  exit 1
fi

CLIENT_ID=$(jq -r --arg ws "$WORKSPACE_ID" '.[$ws].client_id // empty' "$CREDENTIALS_FILE")
CLIENT_SECRET=$(jq -r --arg ws "$WORKSPACE_ID" '.[$ws].client_secret // empty' "$CREDENTIALS_FILE")

if [ -z "$CLIENT_ID" ] || [ -z "$CLIENT_SECRET" ]; then
  echo "ERROR: Credenciais não encontradas para workspace $WORKSPACE_ID"
  exit 1
fi

FETCHED_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "Buscando dados V4MOS: $CLIENT_NAME"
echo "Período: $DATE_START → $DATE_END"
echo ""

# ── Fetch all pages for an endpoint ─────────────────────────────────────────
# Envia createdStart/createdEnd; endpoints que ignoram o filtro retornam tudo e agregamos por data no Python.
fetch_all_pages() {
  local endpoint="$1"
  local all_data="[]"
  local page=1
  local has_next="true"

  while [ "$has_next" = "true" ]; do
    # V4MOS migrou o identity: o parâmetro antigo "workspaceId" foi descontinuado
    # e renomeado para "organizationId" (mesmo valor). Ver developers.v4.marketing.
    local url="${V4MOS_API}/${endpoint}?organizationId=${WORKSPACE_ID}&createdStart=${DATE_START}&createdEnd=${DATE_END}&limit=500&page=${page}"
    local response
    response=$(curl -s -w "\n%{http_code}" "$url" \
      -H "x-client-id: $CLIENT_ID" \
      -H "x-client-secret: $CLIENT_SECRET" \
      -H "Content-Type: application/json" 2>/dev/null || echo -e "\n000")

    local http_code body
    http_code=$(echo "$response" | tail -1)
    body=$(echo "$response" | sed '$d')

    if [ "$http_code" != "200" ] && [ "$http_code" != "201" ]; then
      echo "⚠️  $endpoint: HTTP $http_code (página $page)" >&2
      [ "$http_code" = "401" ] && echo "   Credenciais inválidas" >&2
      [ "$http_code" = "400" ] && echo "   Integração não disponível para este workspace" >&2
      echo "null"
      return
    fi

    local page_data meta
    page_data=$(echo "$body" | jq -r '.data // []')
    meta=$(echo "$body" | jq -r '.meta // {}')
    has_next=$(echo "$meta" | jq -r '.hasNextPage // false')

    all_data=$(echo "$all_data $page_data" | jq -s '.[0] + .[1]')
    page=$((page + 1))
    [ "$has_next" = "true" ] && sleep 0.2
  done

  echo "$all_data"
}

# ── Google Ads: campaigns + gender + keywords ────────────────────────────────
echo "→ Google Ads: campaigns..."
GADS_RAW=$(fetch_all_pages "google/ads/campaigns")
echo "→ Google Ads: gender..."
GADS_GENDER_RAW=$(fetch_all_pages "google/ads/gender")
echo "→ Google Ads: keywords..."
GADS_KW_RAW=$(fetch_all_pages "google/ads/keywords")

if [ "$GADS_RAW" = "null" ]; then
  GADS_AGGREGATED="null"
else
  [ "$GADS_GENDER_RAW" = "null" ] && GADS_GENDER_RAW="[]"
  [ "$GADS_KW_RAW" = "null" ] && GADS_KW_RAW="[]"

  GADS_TMP=$(mktemp); GG_TMP=$(mktemp); GK_TMP=$(mktemp)
  printf '%s' "$GADS_RAW" > "$GADS_TMP"
  printf '%s' "$GADS_GENDER_RAW" > "$GG_TMP"
  printf '%s' "$GADS_KW_RAW" > "$GK_TMP"
  GADS_AGGREGATED=$(GADS_FILE="$GADS_TMP" GG_FILE="$GG_TMP" GK_FILE="$GK_TMP" DS="$DATE_START" DE="$DATE_END" python3 << 'PYEOF'
import json, os
from datetime import datetime, timezone
from collections import defaultdict

def parse_iso(s):
    if not s: return None
    try:
        return datetime.fromisoformat(s.replace('Z','+00:00')).astimezone(timezone.utc)
    except Exception:
        return None

ds = parse_iso(os.environ['DS'])
de = parse_iso(os.environ['DE'])

def in_range(dt):
    if not dt: return True
    if ds and dt < ds: return False
    if de and dt > de: return False
    return True

with open(os.environ['GADS_FILE']) as f:
    data = json.load(f)
with open(os.environ['GG_FILE']) as f:
    gender_data = json.load(f)
with open(os.environ['GK_FILE']) as f:
    kw_data = json.load(f)

DOW_PT = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom']

campaigns = {}
monthly = defaultdict(lambda: {'cost':0, 'clicks':0, 'impressions':0, 'conversions':0})
dow = defaultdict(lambda: {'clicks':0, 'impressions':0, 'cost':0, 'conversions':0})

for r in data:
    sdate = r.get('segments_date')
    dt = parse_iso(sdate)
    if dt and not in_range(dt):
        continue
    name = r.get('campaign_name', 'unknown')
    cost = float(r.get('metrics_cost') or 0)
    clicks = int(r.get('metrics_clicks') or 0)
    imps = int(r.get('metrics_impressions') or 0)
    convs = float(r.get('metrics_conversions') or 0)

    if name not in campaigns:
        campaigns[name] = {
            'name': name,
            'type': r.get('campaign_advertising_channel_type'),
            'status': r.get('campaign_status'),
            'budget_daily': float(r.get('campaign_budget_amount') or 0),
            'cost': 0, 'clicks': 0, 'impressions': 0, 'conversions': 0
        }
    campaigns[name]['cost'] += cost
    campaigns[name]['clicks'] += clicks
    campaigns[name]['impressions'] += imps
    campaigns[name]['conversions'] += convs

    if dt:
        mk = dt.strftime('%Y-%m')
        m = monthly[mk]
        m['cost'] += cost; m['clicks'] += clicks; m['impressions'] += imps; m['conversions'] += convs
        dk = DOW_PT[dt.weekday()]
        dw = dow[dk]
        dw['clicks'] += clicks; dw['impressions'] += imps; dw['cost'] += cost; dw['conversions'] += convs

for c in campaigns.values():
    c['ctr'] = round(c['clicks']/c['impressions']*100, 2) if c['impressions'] else 0
    c['cost'] = round(c['cost'], 2)
    c['cpa'] = round(c['cost']/c['conversions'], 2) if c['conversions'] else None

# Monthly evolution (ordenado por mês asc)
monthly_evolution = []
for mk in sorted(monthly.keys()):
    m = monthly[mk]
    monthly_evolution.append({
        'month': mk,
        'cost': round(m['cost'], 2),
        'clicks': m['clicks'],
        'impressions': m['impressions'],
        'conversions': round(m['conversions'], 1),
        'ctr': round(m['clicks']/m['impressions']*100, 2) if m['impressions'] else 0,
        'cpa': round(m['cost']/m['conversions'], 2) if m['conversions'] else None,
    })

# Day of week (ordem Seg→Dom)
total_clicks = sum(d['clicks'] for d in dow.values()) or 1
day_of_week = []
for dk in DOW_PT:
    d = dow[dk]
    day_of_week.append({
        'day': dk,
        'clicks': d['clicks'],
        'impressions': d['impressions'],
        'cost': round(d['cost'], 2),
        'conversions': round(d['conversions'], 1),
        'pct': round(d['clicks']/total_clicks*100, 1),
        'ctr': round(d['clicks']/d['impressions']*100, 2) if d['impressions'] else 0,
    })

# Gender breakdown
gender_agg = defaultdict(lambda: {'clicks':0, 'impressions':0, 'cost':0, 'conversions':0})
for r in gender_data:
    dt = parse_iso(r.get('date'))
    if dt and not in_range(dt):
        continue
    g = (r.get('gender') or 'UNKNOWN').upper()
    ga = gender_agg[g]
    ga['clicks'] += int(r.get('clicks') or 0)
    ga['impressions'] += int(r.get('impressions') or 0)
    ga['cost'] += float(r.get('cost') or 0)
    ga['conversions'] += float(r.get('conversions') or 0)

GENDER_PT = {'FEMALE':'Feminino','MALE':'Masculino','UNDETERMINED':'Indefinido','UNKNOWN':'Desconhecido'}
total_gender_clicks = sum(v['clicks'] for v in gender_agg.values()) or 1
gender_breakdown = []
for g_key, g in sorted(gender_agg.items(), key=lambda kv: -kv[1]['clicks']):
    gender_breakdown.append({
        'gender': GENDER_PT.get(g_key, g_key.title()),
        'clicks': g['clicks'],
        'impressions': g['impressions'],
        'cost': round(g['cost'], 2),
        'conversions': round(g['conversions'], 1),
        'pct_clicks': round(g['clicks']/total_gender_clicks*100, 1),
        'ctr': round(g['clicks']/g['impressions']*100, 2) if g['impressions'] else 0,
        'cpa': round(g['cost']/g['conversions'], 2) if g['conversions'] else 0,
    })

# Keywords (agregadas por keyword_text + match_type, top 25 por custo)
MATCH_PT = {'EXACT':'Exata','PHRASE':'Frase','BROAD':'Ampla'}
kw_agg = {}
for r in kw_data:
    dt = parse_iso(r.get('date'))
    if dt and not in_range(dt):
        continue
    kt = (r.get('keyword_text') or '').strip()
    if not kt: continue
    mtype = r.get('keyword_match_type') or ''
    key = (kt.lower(), mtype)
    if key not in kw_agg:
        kw_agg[key] = {
            'keyword': kt,
            'match_type': MATCH_PT.get(mtype, mtype.title()),
            'ad_group': r.get('ad_group_name'),
            'campaign': r.get('campaign_name'),
            'clicks':0, 'impressions':0, 'cost':0, 'conversions':0,
        }
    k = kw_agg[key]
    k['clicks'] += int(r.get('clicks') or 0)
    k['impressions'] += int(r.get('impressions') or 0)
    k['cost'] += float(r.get('cost') or 0)
    k['conversions'] += float(r.get('conversions') or 0)

for k in kw_agg.values():
    k['ctr'] = round(k['clicks']/k['impressions']*100, 2) if k['impressions'] else 0
    k['cpc'] = round(k['cost']/k['clicks'], 2) if k['clicks'] else None
    k['cpa'] = round(k['cost']/k['conversions'], 2) if k['conversions'] else None
    k['cost'] = round(k['cost'], 2)
    k['conversions'] = round(k['conversions'], 1)

top_keywords = sorted(kw_agg.values(), key=lambda x: -x['cost'])[:25]

# Totais (soma das campanhas, consistente com agregação atual)
total_cost = round(sum(c['cost'] for c in campaigns.values()), 2)
total_conv = round(sum(c['conversions'] for c in campaigns.values()), 1)
total_imp = sum(c['impressions'] for c in campaigns.values())
total_clicks_all = sum(c['clicks'] for c in campaigns.values())

result = {
    'total_campaigns': len(campaigns),
    'total_cost': total_cost,
    'total_clicks': total_clicks_all,
    'total_impressions': total_imp,
    'total_conversions': total_conv,
    'avg_cpa': round(total_cost/total_conv, 2) if total_conv else None,
    'avg_ctr': round(total_clicks_all/total_imp*100, 2) if total_imp else 0,
    'campaigns': sorted(campaigns.values(), key=lambda x: x['cost'], reverse=True),
    'monthly_evolution': monthly_evolution,
    'day_of_week': day_of_week,
    'gender_breakdown': gender_breakdown,
    'top_keywords': top_keywords,
}
print(json.dumps(result, ensure_ascii=False))
PYEOF
  )
  rm -f "$GADS_TMP" "$GG_TMP" "$GK_TMP"
  echo "✅ Google Ads: $(echo "$GADS_AGGREGATED" | jq -r '.total_campaigns') campanhas · $(echo "$GADS_AGGREGATED" | jq -r '.monthly_evolution | length') meses · $(echo "$GADS_AGGREGATED" | jq -r '.top_keywords | length') keywords · $(echo "$GADS_AGGREGATED" | jq -r '.gender_breakdown | length') gêneros"
fi

# ── Facebook Ads (campaigns + ads + creatives) ──────────────────────────────
echo "→ Facebook Ads..."
FADS_CAMPAIGNS_RAW=$(fetch_all_pages "facebook/ads/campaigns")
FADS_ADS_RAW=$(fetch_all_pages "facebook/ads/ad")
FADS_CREATIVES_RAW=$(fetch_all_pages "facebook/ads/creatives")
FADS_ADSETS_RAW=$(fetch_all_pages "facebook/ads/adset")

if [ "$FADS_CAMPAIGNS_RAW" = "null" ]; then
  FADS_AGGREGATED="null"
else
  [ "$FADS_ADS_RAW" = "null" ] && FADS_ADS_RAW="[]"
  [ "$FADS_CREATIVES_RAW" = "null" ] && FADS_CREATIVES_RAW="[]"
  [ "$FADS_ADSETS_RAW" = "null" ] && FADS_ADSETS_RAW="[]"

  FC_TMP=$(mktemp); FA_TMP=$(mktemp); FCR_TMP=$(mktemp); FAS_TMP=$(mktemp)
  printf '%s' "$FADS_CAMPAIGNS_RAW" > "$FC_TMP"
  printf '%s' "$FADS_ADS_RAW" > "$FA_TMP"
  printf '%s' "$FADS_CREATIVES_RAW" > "$FCR_TMP"
  printf '%s' "$FADS_ADSETS_RAW" > "$FAS_TMP"
  FADS_AGGREGATED=$(FC_FILE="$FC_TMP" FA_FILE="$FA_TMP" FCR_FILE="$FCR_TMP" FAS_FILE="$FAS_TMP" DS="$DATE_START" DE="$DATE_END" python3 << 'PYEOF'
import json, os
from datetime import datetime, timezone
from collections import defaultdict

def parse_iso(s):
    if not s: return None
    try:
        if 'T' not in s and len(s) == 10:
            s = s + 'T00:00:00+00:00'
        return datetime.fromisoformat(s.replace('Z','+00:00')).astimezone(timezone.utc)
    except Exception:
        return None

ds = parse_iso(os.environ['DS'])
de = parse_iso(os.environ['DE'])

def in_range(dt):
    if not dt: return True
    if ds and dt < ds: return False
    if de and dt > de: return False
    return True

# O campo `actions` do Meta vem (frequentemente) DUPLO-codificado: uma string JSON
# que contém outra string JSON. decode_actions desempacota até virar lista.
def decode_actions(a):
    for _ in range(3):
        if isinstance(a, str):
            try: a = json.loads(a)
            except Exception: return []
        else: break
    return a if isinstance(a, list) else []

# Prioridade para definir "lead" da campanha (1 tipo por campanha, evita dupla contagem
# entre eventos equivalentes via pixel/form). O 1º com valor>0 é usado.
LEAD_PRIORITY = [
    'complete_registration',
    'offsite_complete_registration_add_meta_leads',
    'lead',
    'onsite_conversion.lead_grouped',
    'onsite_conversion.lead',
    'onsite_web_lead',
    'onsite_conversion.messaging_conversation_started_7d',
]

def actions_to_dict(actions):
    d = {}
    for it in decode_actions(actions):
        at = it.get('action_type')
        if not at: continue
        try: d[at] = d.get(at, 0) + float(it.get('value') or 0)
        except Exception: pass
    return d

def pick_leads(action_dict):
    """Retorna (leads, action_type_usado) pelo 1º tipo da prioridade com valor>0."""
    for at in LEAD_PRIORITY:
        v = action_dict.get(at, 0)
        if v and v > 0:
            return v, at
    return 0, None

with open(os.environ['FC_FILE']) as f:  campaigns_data = json.load(f)
with open(os.environ['FA_FILE']) as f:  ads_data = json.load(f)
with open(os.environ['FCR_FILE']) as f: creatives_data = json.load(f)
try:
    with open(os.environ.get('FAS_FILE','/dev/null')) as f: adsets_data = json.load(f)
except Exception:
    adsets_data = []

# Mapa adset_id → adset_name (qualquer nome não-nulo) + classificação de audiência.
adset_name_by_id = {}
for r in adsets_data:
    aid = r.get('adset_id'); nm = r.get('adset_name')
    if aid and nm and aid not in adset_name_by_id:
        adset_name_by_id[aid] = nm

def classify_audience(adset_name):
    """Temperatura (frio/quente) + afinidade com a audiência V4 (negócios/finanças),
    inferidas do NOME do adset. [I] inferido."""
    n = (adset_name or '').lower().replace('+', ' ')   # normaliza "ADV+" / "ADV +"
    warm_markers = ['remarketing','rmkt','retarget','lista','cliente','seguidor',
                    'envolvimento','engaj','visualiz','base ', ' fan', 'reimpacto']
    cold_markers = ['interesse','adv ','advantage','lookalike','lal','aberto','amplo',
                    'prospec','persona','esporte','independencia','frio','open']
    if any(m in n for m in warm_markers):
        temp = 'quente'
    elif any(m in n for m in cold_markers):
        temp = 'frio'
    else:
        temp = 'indef'
    if any(m in n for m in ['financ','mercado financeiro','seguro','investi','negócio','negocio','empreend']):
        aff = 'financeiro_negocios'
    elif any(m in n for m in ['pais','pai/mãe','pai/mae','familia','família','filho','vida','saude','saúde']):
        aff = 'familia_pais'
    else:
        aff = 'outro'
    return temp, aff

# 1) Campanhas agregadas (total + por mês)
campaigns = {}
monthly = defaultdict(lambda: {'spend':0, 'impressions':0, 'clicks':0, 'reach':0})
campaign_actions = defaultdict(lambda: defaultdict(float))  # name -> {action_type: soma}
monthly_actions = defaultdict(lambda: defaultdict(float))   # 'YYYY-MM' -> {action_type: soma}

for r in campaigns_data:
    dt = parse_iso(r.get('date_start') or r.get('date_stop'))
    if dt and not in_range(dt):
        continue
    name = r.get('campaign_name', 'unknown')
    spend = float(r.get('spend') or 0)
    imps = int(r.get('impressions') or 0)
    clicks = int(r.get('clicks') or 0)
    reach = int(r.get('reach') or 0)

    if name not in campaigns:
        campaigns[name] = {
            'name': name,
            'objective': r.get('objective'),
            'spend': 0, 'impressions': 0, 'clicks': 0, 'reach': 0
        }
    campaigns[name]['spend'] += spend
    campaigns[name]['impressions'] += imps
    campaigns[name]['clicks'] += clicks
    campaigns[name]['reach'] += reach

    row_actions = actions_to_dict(r.get('actions'))
    for at, v in row_actions.items():
        campaign_actions[name][at] += v

    if dt:
        mk = dt.strftime('%Y-%m')
        m = monthly[mk]
        m['spend'] += spend; m['impressions'] += imps; m['clicks'] += clicks; m['reach'] += reach
        for at, v in row_actions.items():
            monthly_actions[mk][at] += v

for name, c in campaigns.items():
    c['cpm'] = round(c['spend']/c['impressions']*1000, 2) if c['impressions'] else 0
    c['ctr'] = round(c['clicks']/c['impressions']*100, 2) if c['impressions'] else 0
    leads, lead_type = pick_leads(campaign_actions[name])
    c['leads'] = round(leads, 1)
    c['lead_action_type'] = lead_type
    c['cpl'] = round(c['spend']/leads, 2) if leads else None
    # snapshot dos eventos de conversão relevantes (para o diagnóstico inspecionar)
    c['conversion_actions'] = {k: round(v, 1) for k, v in campaign_actions[name].items()
                               if any(t in k for t in ['registration','lead','purchase','contact','submit','message'])}
    c['spend'] = round(c['spend'], 2)

monthly_evolution = []
for mk in sorted(monthly.keys()):
    m = monthly[mk]
    m_leads, _ = pick_leads(monthly_actions[mk])
    monthly_evolution.append({
        'month': mk,
        'spend': round(m['spend'], 2),
        'impressions': m['impressions'],
        'clicks': m['clicks'],
        'reach': m['reach'],
        'leads': round(m_leads, 1),
        'cpl': round(m['spend']/m_leads, 2) if m_leads else None,
        'cpm': round(m['spend']/m['impressions']*1000, 2) if m['impressions'] else 0,
        'ctr': round(m['clicks']/m['impressions']*100, 2) if m['impressions'] else 0,
    })

# 2) Ads agregados por ad_id (inclui actions → leads e registros no site por criativo)
ads = {}
ad_actions = defaultdict(lambda: defaultdict(float))  # ad_id -> {action_type: soma}
for r in ads_data:
    ad_id = r.get('ad_id')
    if not ad_id: continue
    # O endpoint facebook/ads/ad também ignora createdStart/createdEnd e devolve histórico
    # completo — filtra por date_start no Python (igual ao loop de campanhas).
    dt = parse_iso(r.get('date_start') or r.get('date_stop'))
    if dt and not in_range(dt):
        continue
    if ad_id not in ads:
        ads[ad_id] = {
            'ad_id': ad_id,
            'ad_name': r.get('ad_name'),
            'adset_id': r.get('adset_id'),
            'spend': 0, 'impressions': 0, 'clicks': 0, 'reach': 0, 'inline_link_clicks': 0,
            'quality_ranking': r.get('quality_ranking'),
            'engagement_rate_ranking': r.get('engagement_rate_ranking'),
            'conversion_rate_ranking': r.get('conversion_rate_ranking'),
        }
    ads[ad_id]['spend'] += float(r.get('spend') or 0)
    ads[ad_id]['impressions'] += int(r.get('impressions') or 0)
    ads[ad_id]['clicks'] += int(r.get('clicks') or 0)
    ads[ad_id]['reach'] += int(r.get('reach') or 0)
    try: ads[ad_id]['inline_link_clicks'] += int(float(r.get('inline_link_clicks') or 0))
    except: pass
    for at, v in actions_to_dict(r.get('actions')).items():
        ad_actions[ad_id][at] += v

for ad_id, a in ads.items():
    a['ctr'] = round(a['clicks']/a['impressions']*100, 2) if a['impressions'] else 0
    a['cpm'] = round(a['spend']/a['impressions']*1000, 2) if a['impressions'] else 0
    a['cpc'] = round(a['spend']/a['clicks'], 2) if a['clicks'] else None
    leads, lead_type = pick_leads(ad_actions[ad_id])
    a['leads'] = round(leads, 1)
    a['lead_action_type'] = lead_type
    a['cpl'] = round(a['spend']/leads, 2) if leads else None
    # "registro no site" = complete_registration (pixel/LP). Métrica nomeada pelo cliente.
    site_reg = ad_actions[ad_id].get('complete_registration', 0) \
               or ad_actions[ad_id].get('offsite_complete_registration_add_meta_leads', 0)
    a['site_registrations'] = round(site_reg, 1)
    a['cost_per_registration'] = round(a['spend']/site_reg, 2) if site_reg else None
    a['spend'] = round(a['spend'], 2)

# 3) Creatives: dedupe por ad_id
creatives_by_ad = {}
for c in creatives_data:
    ad_id = c.get('ad_id')
    if not ad_id: continue
    creatives_by_ad[ad_id] = {
        'creative_id': c.get('creative_id'),
        'creative_name': c.get('creative_name'),
        'title': c.get('title'),
        'object_type': c.get('object_type'),
        'status': c.get('status'),
        'thumbnail_url': c.get('thumbnail_url'),
        'image_url': c.get('image_url'),
        'video_id': c.get('video_id'),
        'instagram_permalink_url': c.get('instagram_permalink_url'),
        'website_link': c.get('website_link'),
        'ad_created_time': c.get('ad_created_time'),
    }

# 4) Join
joined = []
for ad_id, a in ads.items():
    cr = creatives_by_ad.get(ad_id, {})
    joined.append({
        **a,
        'creative_id': cr.get('creative_id'),
        'creative_name': cr.get('creative_name'),
        'title': cr.get('title'),
        'object_type': cr.get('object_type'),
        'status': cr.get('status'),
        'thumbnail_url': cr.get('thumbnail_url'),
        'image_url': cr.get('image_url'),
        'video_id': cr.get('video_id'),
        'instagram_permalink_url': cr.get('instagram_permalink_url'),
        'website_link': cr.get('website_link'),
        'ad_created_time': cr.get('ad_created_time'),
    })
joined.sort(key=lambda x: x.get('spend') or 0, reverse=True)

metric_ad_ids = set(ads.keys())
for ad_id, cr in creatives_by_ad.items():
    if ad_id in metric_ad_ids: continue
    joined.append({
        'ad_id': ad_id, 'ad_name': cr.get('creative_name'),
        'spend': 0, 'impressions': 0, 'clicks': 0, 'reach': 0, 'ctr': 0, 'cpm': 0, 'cpc': None,
        **cr, 'no_metrics_in_period': True,
    })

# 5) Backfill de assets visuais entre ads do mesmo criativo.
#    Ads de maior gasto às vezes não casam com o endpoint de creatives (thumbnail/permalink null).
#    Herdam o asset de uma variação irmã (mesmo ad_name normalizado) para GARANTIR preview na página.
import re
ASSET_KEYS = ['thumbnail_url', 'image_url', 'video_id', 'instagram_permalink_url',
              'website_link', 'object_type', 'creative_id', 'creative_name', 'title']

def norm_name(n):
    if not n: return ''
    n = n.lower().strip()
    n = re.sub(r'[—\-]+\s*c[oó]pia\b', '', n)        # "— cópia"
    n = re.sub(r'\bcopy\b', '', n)
    n = re.sub(r'[\(\[]\s*v?\d+\s*[\)\]]', '', n)     # (v2) (2) [3]
    n = re.sub(r'[\s\-_]+\d+$', '', n)                # trailing " - 3" / " 2"
    return re.sub(r'\s+', ' ', n).strip()

def has_asset(d):
    return bool(d.get('instagram_permalink_url') or d.get('thumbnail_url')
                or d.get('image_url') or d.get('video_id'))

asset_by_exact, asset_by_norm = {}, {}
for j in joined:
    if has_asset(j):
        nm = j.get('ad_name') or ''
        snap = {k: j.get(k) for k in ASSET_KEYS}
        asset_by_exact.setdefault(nm, snap)
        asset_by_norm.setdefault(norm_name(nm), snap)

inherited = 0
for j in joined:
    if has_asset(j): continue
    nm = j.get('ad_name') or ''
    src = asset_by_exact.get(nm) or asset_by_norm.get(norm_name(nm))
    if src and has_asset(src):
        for k in ASSET_KEYS:
            if not j.get(k) and src.get(k):
                j[k] = src.get(k)
        j['assets_inherited'] = True
        inherited += 1
if inherited:
    print(f"   ↳ {inherited} ads herdaram thumbnail/permalink de variação irmã (backfill)", file=__import__('sys').stderr)

# Enriquece cada criativo com a audiência (adset) em que rodou: nome, temperatura e afinidade.
for j in joined:
    aid = j.get('adset_id')
    anm = adset_name_by_id.get(aid)
    j['adset_name'] = anm
    temp, aff = classify_audience(anm)
    j['audience_temp'] = temp            # frio | quente | indef
    j['audience_affinity'] = aff         # financeiro_negocios | familia_pais | outro

total_spend = round(sum(c['spend'] for c in campaigns.values()), 2)
total_imp = sum(c['impressions'] for c in campaigns.values())
total_clicks = sum(c['clicks'] for c in campaigns.values())
total_reach = sum(c['reach'] for c in campaigns.values())
total_leads = round(sum((c.get('leads') or 0) for c in campaigns.values()), 1)

# Leads e gasto por objetivo (revela budget que não gera lead — ex.: awareness/engagement)
by_objective = defaultdict(lambda: {'spend':0.0, 'leads':0.0, 'campaigns':0})
for c in campaigns.values():
    o = c.get('objective') or 'UNKNOWN'
    by_objective[o]['spend'] += c['spend']
    by_objective[o]['leads'] += (c.get('leads') or 0)
    by_objective[o]['campaigns'] += 1
leads_by_objective = []
for o, v in sorted(by_objective.items(), key=lambda kv: -kv[1]['spend']):
    leads_by_objective.append({
        'objective': o,
        'spend': round(v['spend'], 2),
        'spend_pct': round(v['spend']/total_spend*100, 1) if total_spend else 0,
        'leads': round(v['leads'], 1),
        'cpl': round(v['spend']/v['leads'], 2) if v['leads'] else None,
        'campaigns': v['campaigns'],
    })

result = {
    'total_campaigns': len(campaigns),
    'total_ads': len([j for j in joined if not j.get('no_metrics_in_period')]),
    'total_creatives': len(creatives_by_ad),
    'total_spend': total_spend,
    'total_impressions': total_imp,
    'total_clicks': total_clicks,
    'total_reach': total_reach,
    'total_leads': total_leads,
    'avg_cpm': round(total_spend/total_imp*1000, 2) if total_imp else 0,
    'avg_ctr': round(total_clicks/total_imp*100, 2) if total_imp else 0,
    'avg_cpl': round(total_spend/total_leads, 2) if total_leads else None,
    'leads_by_objective': leads_by_objective,
    'campaigns': sorted(campaigns.values(), key=lambda x: x['spend'], reverse=True),
    'creatives': joined,
    'monthly_evolution': monthly_evolution,
}
print(json.dumps(result, ensure_ascii=False))
PYEOF
  )
  rm -f "$FC_TMP" "$FA_TMP" "$FCR_TMP" "$FAS_TMP"
  echo "✅ Facebook Ads: $(echo "$FADS_AGGREGATED" | jq -r '.total_campaigns') campanhas · $(echo "$FADS_AGGREGATED" | jq -r '.total_ads') ads · $(echo "$FADS_AGGREGATED" | jq -r '.monthly_evolution | length') meses · R\$$(echo "$FADS_AGGREGATED" | jq -r '.total_spend') gasto · $(echo "$FADS_AGGREGATED" | jq -r '.total_leads') leads (CPL R\$$(echo "$FADS_AGGREGATED" | jq -r '.avg_cpl'))"
fi

# ── Write back to client.json.connectors ────────────────────────────────────
TMP="$CLIENT_JSON.tmp"
jq \
  --arg fetched_at "$FETCHED_AT" \
  --arg period_start "$DATE_START" \
  --arg period_end "$DATE_END" \
  --argjson google_ads "$GADS_AGGREGATED" \
  --argjson facebook_ads "$FADS_AGGREGATED" \
  '.connectors = {
    fetched_at: $fetched_at,
    period: { start: $period_start, end: $period_end },
    google_ads: $google_ads,
    facebook_ads: $facebook_ads
  }' "$CLIENT_JSON" > "$TMP" && mv "$TMP" "$CLIENT_JSON"

echo ""
echo "✓ client.json atualizado (connectors.fetched_at: $FETCHED_AT)"
