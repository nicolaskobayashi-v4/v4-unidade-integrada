#!/bin/bash
# render_portal.sh — Gera portal.html para um diretório de cliente
# Uso: render_portal.sh <client_dir>
# Exemplo: render_portal.sh clientes/meu-cliente
#
# Lê client.json e outputs/*.json, injeta no template portal.html
# Gera: <client_dir>/portal.html

set -euo pipefail

CLIENT_DIR="${1:?Uso: render_portal.sh <client_dir>}"

# Resolve paths
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE="$SCRIPT_DIR/../shared-templates/portal.html"
CLIENT_JSON="$CLIENT_DIR/client.json"
OUTPUTS_DIR="$CLIENT_DIR/outputs"
OUTPUT_FILE="$CLIENT_DIR/portal.html"

# Validate
if [ ! -f "$TEMPLATE" ]; then
  echo "Erro: Template não encontrado em $TEMPLATE" >&2
  exit 1
fi

if [ ! -f "$CLIENT_JSON" ]; then
  echo "Erro: client.json não encontrado em $CLIENT_JSON" >&2
  exit 1
fi

# Build portal data using Python (handles large JSON safely)
CLIENT_JSON_P="$CLIENT_JSON" OUTPUTS_DIR_P="$OUTPUTS_DIR" TEMPLATE_P="$TEMPLATE" OUTPUT_P="$OUTPUT_FILE" DELIVERY_MAP_P="$SCRIPT_DIR/../delivery-map.json" python3 << 'PYEOF'
import json, sys, os, glob

client_json_path = os.environ['CLIENT_JSON_P']
outputs_dir = os.environ['OUTPUTS_DIR_P']
template_path = os.environ['TEMPLATE_P']
output_path = os.environ['OUTPUT_P']

# Read client.json
with open(client_json_path, 'r', encoding='utf-8') as f:
    client_data = json.load(f)

# Build outputs object from all JSON files in outputs/
outputs = {}
if os.path.isdir(outputs_dir):
    for fpath in sorted(glob.glob(os.path.join(outputs_dir, '*.json'))):
        skill_id = os.path.splitext(os.path.basename(fpath))[0]
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                outputs[skill_id] = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Aviso: Não foi possível ler {fpath}: {e}", file=sys.stderr)

# Resolve a estrutura de semanas a partir do delivery-map conforme meta.modelo_venda (model-aware).
# Fallback: se não houver delivery-map ou modelo_venda, o portal usa o WEEKS legado embutido.
weeks = None
modelo = (client_data.get('meta', {}) or {}).get('modelo_venda')
dm_path = os.environ.get('DELIVERY_MAP_P', '')
if modelo and os.path.isfile(dm_path):
    try:
        with open(dm_path, 'r', encoding='utf-8') as f:
            dm = json.load(f)
        comum = dm.get('comum', {})
        semana3 = (dm.get('semana_3', {}) or {}).get(modelo, [])
        modelo_titulo = {'e-commerce': 'E-commerce', 'inside-sales': 'Inside Sales', 'pdv': 'PDV / Loja Física'}.get(modelo, modelo)
        weeks = [
            {'n': 1, 'title': 'Descoberta do Negócio e Pesquisa de Mercado', 'desc': 'Onboarding, persona/ICP, concorrência, arquitetura de presença e sizing', 'skills': list(comum.get('semana_1', []))},
            {'n': 2, 'title': 'Diagnóstico Digital e Posicionamento Estratégico', 'desc': 'Mídia, orgânico, criativos, maturidade e posicionamento + PUV', 'skills': list(comum.get('semana_2', []))},
            {'n': 3, 'title': 'Estrutura da Operação de Venda — ' + modelo_titulo, 'desc': 'Diagnósticos e estrutura específicos do modelo de venda', 'skills': list(semana3)},
            {'n': 4, 'title': 'Identidade de Comunicação e Plano de Mídia', 'desc': 'Manual de marca, LP, copy, criativos, CRM, SDR IA e forecast (comum a todos)', 'skills': list(comum.get('semana_4', []))},
        ]
    except (json.JSONDecodeError, IOError) as e:
        print(f"Aviso: não foi possível resolver weeks do delivery-map: {e}", file=sys.stderr)

# Assemble portal data
portal_data = {
    'client': client_data.get('meta', {}),
    'progress': client_data.get('progress', {}),
    'outputs': outputs,
    'briefing': client_data.get('briefing', {}),
}
if weeks is not None:
    portal_data['weeks'] = weeks

data_json = json.dumps(portal_data, ensure_ascii=False, separators=(',', ':'))

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

marker = '/*%%DATA%%*/ {}'
if marker not in template:
    print("Erro: Marcador /*%%DATA%%*/ {} não encontrado no template", file=sys.stderr)
    sys.exit(1)

result = template.replace(marker, data_json)

# Inject Funnel "Destrava Receita" SVG inline as JSON-stringified literal
# (filters/feGaussianBlur só renderizam confiavelmente quando o SVG é inline, não em data: URLs)
funnel_svg_path = os.path.join(os.path.dirname(template_path), 'assets', 'funil-destrava-receita.svg')
if os.path.isfile(funnel_svg_path):
    with open(funnel_svg_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    svg_js_literal = json.dumps(svg_content, ensure_ascii=False)
    result = result.replace('/*%%FUNNEL_SVG_INLINE%%*/""', svg_js_literal)
    result = result.replace('/*%%FUNNEL_SVG_INLINE%%*/', svg_js_literal)

os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Portal gerado: {output_path}")
PYEOF

echo "✓ Portal atualizado: $OUTPUT_FILE"

# Valida completude dos outputs contra schema (não bloqueia — apenas avisa)
VALIDATOR="$SCRIPT_DIR/validate_output.py"
if [ -f "$VALIDATOR" ]; then
  VALIDATION_REPORT=$(python3 "$VALIDATOR" "$CLIENT_DIR" 2>&1 || true)
  if echo "$VALIDATION_REPORT" | grep -qE "^Resumo: [1-9]"; then
    echo ""
    echo "⚠ Validação de completude encontrou gaps:"
    echo "$VALIDATION_REPORT" | tail -40
    echo ""
    echo "  (aviso — deploy continua. Rode: python3 $VALIDATOR $CLIENT_DIR para detalhe completo)"
  fi
fi

# Gera/atualiza consolidated.md + consolidated.html (visão narrativa end-to-end)
CONSOLIDATED_SCRIPT="$SCRIPT_DIR/../shared-templates/render_consolidated.py"
CONSOLIDATED_HTML="$CLIENT_DIR/consolidated.html"
if [ -f "$CONSOLIDATED_SCRIPT" ]; then
  if python3 "$CONSOLIDATED_SCRIPT" "$CLIENT_DIR" >/dev/null 2>&1; then
    echo "✓ Consolidated atualizado: $CONSOLIDATED_HTML"
  else
    echo "⚠ Falha ao gerar consolidated (seguindo sem atualizar)" >&2
  fi
fi

# Gera/atualiza apresentacao.html (slide deck progressivo — cresce conforme skills S1/S2 completam)
APRESENTACAO_SCRIPT="$SCRIPT_DIR/../shared-templates/render_apresentacao.py"
APRESENTACAO_HTML="$CLIENT_DIR/apresentacao.html"
if [ -f "$APRESENTACAO_SCRIPT" ]; then
  if python3 "$APRESENTACAO_SCRIPT" "$CLIENT_DIR" >/dev/null 2>&1; then
    echo "✓ Apresentação atualizada: $APRESENTACAO_HTML"
  else
    echo "⚠ Falha ao gerar apresentação (seguindo sem atualizar)" >&2
  fi
fi

# Gera/atualiza apresentacao-entrega.html (apresentação educativa cliente-facing — jornada Atrair/Converter/Reter)
APRESENTACAO_ENTREGA_SCRIPT="$SCRIPT_DIR/../shared-templates/render_apresentacao_entrega.py"
APRESENTACAO_ENTREGA_HTML="$CLIENT_DIR/apresentacao-entrega.html"
if [ -f "$APRESENTACAO_ENTREGA_SCRIPT" ]; then
  if python3 "$APRESENTACAO_ENTREGA_SCRIPT" "$CLIENT_DIR" >/dev/null 2>&1; then
    echo "✓ Apresentação da entrega atualizada: $APRESENTACAO_ENTREGA_HTML"
  else
    echo "⚠ Falha ao gerar apresentação da entrega (seguindo sem atualizar)" >&2
  fi
fi

# Deploy para Vercel se existir vercel-project.json no diretório do cliente
VERCEL_CFG="$CLIENT_DIR/vercel-project.json"
if [ -f "$VERCEL_CFG" ] && command -v vercel >/dev/null 2>&1; then
  PROJECT_NAME=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1])).get('projectName',''))" "$VERCEL_CFG")
  DEPLOY_DIR=$(mktemp -d)
  cp "$OUTPUT_FILE" "$DEPLOY_DIR/index.html"
  if [ -f "$CONSOLIDATED_HTML" ]; then
    cp "$CONSOLIDATED_HTML" "$DEPLOY_DIR/consolidated.html"
  fi
  # Copia páginas HTML adicionais do diretório raiz do cliente (ex: diretrizes-sdr.html)
  # — exclui portal.html (já virou index.html) e consolidated.html (já copiado acima)
  for extra_html in "$CLIENT_DIR"/*.html; do
    [ -f "$extra_html" ] || continue
    base=$(basename "$extra_html")
    case "$base" in
      portal.html|consolidated.html) continue ;;
      *) cp "$extra_html" "$DEPLOY_DIR/$base" ;;
    esac
  done
  # Copia assets (imagens de criativos, logos, etc) — paths relativos no portal dependem disso
  if [ -d "$CLIENT_DIR/assets" ]; then
    cp -R "$CLIENT_DIR/assets" "$DEPLOY_DIR/assets"
  fi
  mkdir -p "$DEPLOY_DIR/.vercel"
  cp "$VERCEL_CFG" "$DEPLOY_DIR/.vercel/project.json"
  echo "🚀 Deployando para Vercel ($PROJECT_NAME)..."
  cd "$DEPLOY_DIR"
  vercel --prod --yes --scope v4-company 2>&1 | grep -E "Production:|Error|✓" || true
  rm -rf "$DEPLOY_DIR"
  echo "✓ Deploy concluído: https://${PROJECT_NAME}.vercel.app"
fi
