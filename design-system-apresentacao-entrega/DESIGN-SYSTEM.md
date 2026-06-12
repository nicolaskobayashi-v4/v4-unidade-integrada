# Design System — Apresentação da Entrega

Especificação visual e estrutural do deck. Tudo é renderizado como HTML+CSS inline (um único arquivo,
autocontido) por `render_apresentacao_entrega.py`.

## Princípios

1. **Cirúrgico, não enciclopédico.** Uma ideia por slide. Statement de impacto + evidência de apoio.
2. **Educativo.** Cada entrega responde *por que olhamos isto* e *como vira execução* — não é dump de dados.
3. **Jornada de execução.** O fio condutor é o funil de marketing: **Atrair → Converter → Reter**.
4. **Contraste alto.** Vermelho + branco como base; bordô como pausa/estrutura.
5. **Determinístico.** Mesmo envelope de dados → mesmo slide. Sem geração livre no render.

## Paleta

| Token | Hex | Uso |
|---|---|---|
| Vermelho V4 | `#FB2E0A` | Fundo dos slides de conteúdo · CTA · acento em branco |
| Vermelho profundo | `#D61A0E` | Gradientes · variações de fundo |
| Vermelho escuro | `#8A0D05` / `#5A0802` | Âncoras de gradiente · texto sobre branco |
| Bordô | `#240705` · `#4A0D05` · `#2A0703` | **Divisores de fase** (escuro) · texto de valor em card branco |
| Branco | `#FFFFFF` | **Slides de transição** · texto · cards de dado · selos |
| Vermelho de card | `#C21A0A` | Texto/rótulo dentro de cards e selos brancos |

Texto secundário/terciário = branco com opacidade (`rgba(255,255,255,.85 / .7 / .55)`).
Os tons creme/areia foram **descartados** — branco puro dá o contraste.

## Tipografia

**IBM Plex Sans** (400/500/600/700/800), via Google Fonts.
- `title-mega` — nome do cliente / títulos de fase (clamp 3.2–7rem)
- `title-statement` — o statement do slide de conteúdo (clamp 1.7–3rem)
- `eyebrow` — sobrancelha (uppercase, pill translúcido)
- corpo / leituras — 0.85–1.18rem

## Os 8 arquétipos de slide

| # | Arquétipo | Fundo | Papel |
|---|---|---|---|
| 1 | **Capa** | Vermelho | Nome do cliente · "Da estratégia à execução · Plano de Marketing · {modelo}" |
| 2 | **Lógica** | Vermelho | "Como ler" + a jornada Atrair/Converter/Reter em 3 cards |
| 3 | **Ponto de partida** | Vermelho | Maturidade — **diagnóstico, sem ROI**. Layout de 2 zonas. |
| 4 | **Divisor de fase** | **Bordô** (escuro) | "Movimento 01/02/03 — Atrair / Converter / Reter" |
| 5 | **Transição de entrega** | **Branco** | "Entrega X de N · Fase" + nome + contraste *de onde viemos → agora* + a pergunta |
| 6 | **Conteúdo** | Vermelho | A entrega em 2 zonas (ver anatomia abaixo). Selo "Entrega · Nome" no topo. |
| 7 | **Plano** | Vermelho | "O que vem agora — Estratégia é o mapa. Execução é a viagem." Recap do ciclo. |
| 8 | **Fechamento** | Vermelho | "Bora executar." |

O ritmo alterna **bordô (divisor) → branco (transição) → vermelho (conteúdo)** a cada virada de
entrega, criando contraste forte e leitura clara das fronteiras.

## Anatomia do slide de conteúdo (2 zonas)

```
┌ logo ─────────────────────────────── selo: ENTREGA · NOME ┐
│                                                            │
│  ZONA ESQUERDA (narrativa)      │  ZONA DIREITA (evidência) │
│  ───────────────────────────   │  ──────────────────────── │
│  eyebrow  (FASE · título)       │  ┌ card-herói (branco) ─┐ │
│  "Por que olhamos isto: …"      │  │ RÓTULO               │ │
│  STATEMENT (a ideia, grande)    │  │ valor grande         │ │
│  [PUV em citação, se houver]    │  └──────────────────────┘ │
│                                 │  [stat] [stat] [stat]     │
│  → Na execução: …  (no rodapé)  │  LEITURAS                 │
│                                 │   • [tag] insight         │
│                                 │   • [tag] insight         │
└──────────────────────── cliente · entrega ──────── fase ───┘
```

- **Card-herói** = `summary_highlights[0]` — card branco sólido, rótulo vermelho, valor bordô.
- **Stat-cards** = `summary_highlights[1..3]` — chips translúcidos brancos, valor branco.
- **Leituras** = `summary_key_findings[0..2]` — cada uma com selo branco (texto vermelho) por categoria:
  `posicao → Posição`, `vantagem → Vantagem`, `ameaca → Atenção`, `acao → Ação`.
- **Degradação:** 1 só highlight → só o herói; 0 findings → sem bloco Leituras. Nunca fica zona vazia.

## Narrativa (a espinha)

```
Capa → Lógica → Ponto de partida (Maturidade, diagnóstico)
  │
  ├─ MOVIMENTO 01 · ATRAIR    (trazer as pessoas certas)
  │    persona, posicionamento, marca, pesquisa, SWOT, mídia, orgânico, presença local…
  ├─ MOVIMENTO 02 · CONVERTER (transformar atenção em cliente)
  │    auditoria, CRO, funil/comercial, cliente oculto, LP, copy, criativos, SDR…
  └─ MOVIMENTO 03 · RETER     (fazer voltar e crescer)
       CRM, réguas, base ativa, recuperação… e o FORECAST (ROI — sempre no fim)
  │
Plano (recap do ciclo) → Fechamento
```

Cada entrega = **uma transição branca** (marca a fronteira) **+ um slide de conteúdo** (2 zonas).

## Regra de ouro do conteúdo

**ROI/payback/projeção de curto prazo NUNCA na abertura.** A abertura é diagnóstica (onde estamos,
os gaps). A modelagem financeira é a **última entrega** (Forecast) — depois de toda a prova. Abrir com
"ROI 20x em 16 dias" é tiro no pé: cria expectativa que a agência não controla e soa vendedor.

## Mecânica de render (resumo)

- `PHASES` → os 3 movimentos. `PHASE_ORDER` → a ordem.
- `STUDY_REGISTRY` → lista de entregas: `{skill, phase, title, por_que, execucao}`. A ordem na lista é a
  ordem dos slides dentro da fase.
- `ENTREGA_NAMES` / `ENTREGA_DETAIL` → nome amigável e essência/pergunta (transição).
- `build_content()` → o **único** builder de slide de entrega (template de 2 zonas). Maturidade e Forecast
  passam pelo mesmo template.
- `SHELL_HTML` → o documento (CSS inline + navegação por teclado/touch). Logo entra como data-URI a
  partir de `assets/v4-favicon.jpg`.
