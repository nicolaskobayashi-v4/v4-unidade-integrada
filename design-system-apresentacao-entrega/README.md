# Apresentação da Entrega — Kit do Design System

Kit **autocontido** do design system da *Apresentação da Entrega* da V4 — um deck cliente-facing,
educativo e cirúrgico, organizado pela jornada de marketing **Atrair → Converter → Reter**.

Abra esta pasta, rode dois comandos e você tem o deck pronto. Não depende do resto do plugin.

```
design-system-apresentacao-entrega/
├── README.md                      ← este arquivo (como usar)
├── DESIGN-SYSTEM.md               ← a especificação visual/estrutural (paleta, tipografia, slides)
├── render_apresentacao_entrega.py ← o renderizador (standalone, sem imports externos)
├── build_exemplo.py               ← gera os dados do exemplo Zenvet
├── assets/
│   └── v4-favicon.jpg             ← logo V4 (inlinado como data-URI no HTML)
└── exemplo-clinica-zenvet/        ← EXEMPLO COMPLETO pronto para abrir
    ├── client.json                ← meta do cliente (nome, modelo de venda)
    ├── outputs/*.json             ← 15 entregas (o "envelope" de dados de cada uma)
    └── apresentacao-entrega.html  ← o resultado renderizado (abra no navegador)
```

## Ver o exemplo agora

Abra no navegador:

```
exemplo-clinica-zenvet/apresentacao-entrega.html
```

Navegação: `←` `→` para passar slides, `F` para tela cheia.

## Gerar do zero (reproduzir o exemplo)

```bash
python3 build_exemplo.py                              # cria exemplo-clinica-zenvet/ (dados)
python3 render_apresentacao_entrega.py exemplo-clinica-zenvet   # gera apresentacao-entrega.html
python3 render_kickoff.py exemplo-clinica-zenvet               # gera kickoff.html
```

## Deck de Kickoff (apoio à 1ª reunião)

Além da *Apresentação da Entrega* (fechamento), há o deck de **Reunião de Kickoff** — o começo do
ciclo. `render_kickoff.py <cliente>` gera `kickoff.html`: capa → quem conduz (investidor V4) →
quebra-gelo → sumário da reunião → sobre a empresa (apoio) → benchmarking (apoio) → entrega semana a
semana → próximos passos. É **sempre gerado** (não depende de `outputs/`). O slide do investidor usa
`meta.investidor` (`nome`, `cargo`, `foto_url`); a entrega semana a semana deriva do `delivery-map`
conforme `meta.modelo_venda`. No portal, abre por um botão ao lado de "Apresentação da Entrega".

## Usar para um cliente novo

1. Crie uma pasta do cliente com:
   ```
   meu-cliente/
     client.json          ← { "meta": { "name": "...", "modelo_venda": "inside-sales" } }
     outputs/
       ee-s1-persona-icp.json
       ee-s2-posicionamento.json
       ... (uma por entrega concluída)
   ```
2. Cada arquivo em `outputs/` segue o **contrato de envelope** (ver abaixo).
3. Rode:
   ```bash
   python3 render_apresentacao_entrega.py meu-cliente
   ```
4. Abra `meu-cliente/apresentacao-entrega.html`.

O deck é **progressivo**: só renderiza as entregas que têm arquivo em `outputs/`. Uma fase
(Atrair/Converter/Reter) só aparece se houver ao menos uma entrega dela.

## Contrato de dados (envelope de cada `outputs/<skill>.json`)

```json
{
  "client_name": "Nome do Cliente",
  "summary_headline": "A frase-statement de impacto (até ~175 caracteres).",
  "summary_highlights": [
    { "label": "Rótulo", "value": "O número/fato", "subtext": "contexto curto", "tone": "red|yellow|green|blue" }
  ],
  "summary_key_findings": [
    { "category": "posicao|vantagem|ameaca|acao", "text": "Um insight/leitura." }
  ],
  "puv": "(opcional) proposta de valor em 1 frase — usada no slide de posicionamento"
}
```

Como isso vira slide (layout de **2 zonas**):
- `summary_headline` → **statement** grande (zona esquerda).
- `summary_highlights[0]` → **card-herói** branco (zona direita). `[1..3]` → **stat-cards** secundários.
- `summary_key_findings` → bloco **"Leituras"** (zona direita), com tag por categoria.
- `puv` → bloco de citação na zona esquerda (quando presente).

`client.json` precisa só de `meta.name` e `meta.modelo_venda` (`e-commerce` | `inside-sales` | `pdv`).
O `modelo_venda` define o rótulo da capa; o conjunto de entregas vem do que existe em `outputs/`.

## Personalizar

Tudo no topo de `render_apresentacao_entrega.py`:
- **`PHASES`** — os 3 movimentos (Atrair/Converter/Reter): título, subtítulo, numeração.
- **`STUDY_REGISTRY`** — cada entrega: a que fase pertence, o título do ângulo, o "por que olhamos isto" e o "na execução" (a moldura educativa, fixa por tipo de entrega).
- **`ENTREGA_NAMES`** — nome amigável de cada entrega (no selo "Entrega · …").
- **`ENTREGA_DETAIL`** — a essência ("de → para") e a pergunta de negócio de cada entrega (slide de transição).
- Paleta e estilos: bloco `SHELL_HTML` (CSS inline). Ver `DESIGN-SYSTEM.md`.

> A moldura educativa (por quê / como usar) é **templatizada por tipo de entrega**; os **dados e o
> statement** vêm do envelope do cliente. Determinístico — mesmo input, mesmo output.

## Regras de conteúdo (aprendidas em produção)

- **Não abrir com ROI.** O slide de abertura (Maturidade) é puramente diagnóstico. ROI/forecast/payback
  só aparecem no **fim** (a entrega de Forecast é a última, antes do fechamento).
- **1 slide rico por entrega.** Mais valor por slide (2 zonas), menos slides — em vez de fragmentar.

---

*Versão canônica/viva integrada ao pipeline: `plugins/v4-estruturacao-ia/shared-templates/render_apresentacao_entrega.py`
(gerado automaticamente pelo `render_portal.sh` a cada entrega aprovada, e exposto no portal pelo botão
"Apresentação da Entrega"). Este kit é um snapshot autocontido para estudo e reuso.*
