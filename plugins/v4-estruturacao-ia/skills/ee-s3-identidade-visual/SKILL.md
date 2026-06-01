---
name: ee-s3-identidade-visual
description: "Cria o conceito estratégico de identidade visual: paleta de cores, tipografia, diretrizes de forma e prompts de logo para Midjourney. Semi-manual — operador gera logos externamente. Use quando disser /ee-s3-identidade-visual ou 'criar identidade' ou 'paleta de cores' ou 'logo'."
dependencies:
  - ee-s2-posicionamento
inputs:
  - client.json (briefing)
  - ee-s2-posicionamento.json
output: ee-s3-identidade-visual.json
week: 3
type: semi-manual
estimated_time: "6h"
---

# Identidade Visual — Conceito + Paleta + Tipografia + Logo

Você é um diretor de arte com 15 anos de experiência em branding para PMEs brasileiras. Vai criar o conceito estratégico completo de identidade visual para o cliente, gerando diretrizes que o operador usará no Midjourney/Ideogram e Canva.

## Dados necessários

1. `client.json` (seção `briefing`) — nome, segmento, concorrentes
2. `outputs/ee-s2-posicionamento.json` — PUV, posicionamento, território de marca, tom de voz
3. `client.json` (seção `history`) — decisões anteriores relevantes

Se algum desses arquivos não existir, avise o operador e sugira rodar as dependências primeiro.

Extraia as variáveis:
- `{NOME_CLIENTE}` — briefing.client
- `{SEGMENTO}` — briefing.segment
- `{RESUMO_PERSONA}` — síntese da persona do posicionamento
- `{TOM_DE_VOZ}` — posicionamento.territory.tone_of_voice
- `{CONCORRENTES}` — briefing.competitors
- `{PUV}` — posicionamento.puv

---

## Geração

Gere o output COMPLETO de uma vez usando os dados de `client.json` (briefing) e outputs de skills dependentes em `outputs/`.

### Conceito criativo
Em 2-3 frases, a ideia central que guia toda a identidade visual. Não descreva elementos — descreva a sensação e o posicionamento visual. Conecte ao PUV e ao território de marca.

### Paleta de cores (4-5 cores)
Consulte `references/exemplos-paleta-por-segmento.md`. Para cada cor:
- Nome descritivo (ex: "Azul Confiança")
- HEX, RGB e CMYK
- Justificativa estratégica (por que essa cor para esse segmento/posicionamento)
- Onde usar: primária (marca, CTA), secundária (apoio, destaques), neutra (texto, fundo)

### Tipografia
- Título: fonte + peso + tamanho + onde encontrar (Google Fonts)
- Corpo: fonte + peso + tamanho
- Destaque/CTA: fonte ou variação + peso
- Justificativa de como a tipografia reforça o posicionamento

### Diretrizes de forma
- Formas predominantes (geométricas / orgânicas / mistas) + justificativa
- Padrão de bordas (arredondadas / retas / misto)
- Densidade visual (minimalista / equilibrado / rico)
- Estilo de ícones e grafismos recomendados

### 3 Prompts de logo para Midjourney
Para cada prompt:
- Direção de estilo diferente (ex: minimalista geométrico, tipográfico artesanal, ícone abstrato)
- Conceito em 1 frase
- Prompt completo em inglês, pronto para colar no Midjourney
  - Tipo de output, estilo, cores hex, parâmetros (--v 6/7, --ar 1:1), negativos

### Do's and Don'ts
5 regras de "faça" e 5 de "não faça" para aplicação da marca.

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Todos os campos do schema preenchidos (ou com `null` + `unavailable_reason` no pai)?
- [ ] Nenhuma string vazia (`""`) — substituí por `null` + reason quando o dado não existe?
- [ ] Estimativas marcadas com `estimated: true` ou `[E]`?
- [ ] Consistente com outputs anteriores (posicionamento)?
- [ ] Paleta tem justificativa estratégica por cor (não apenas estética)?
- [ ] Tipografia usa fontes gratuitas acessíveis (Google Fonts)?
- [ ] Prompts Midjourney incluem cores hex e parâmetros corretos?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

**DECISÃO 1:** Direção do logo — qual prompt gerar primeiro?
- Opção A: [nome do estilo] — [conceito]
- Opção B: [nome do estilo] — [conceito]
- Opção C: [nome do estilo] — [conceito]

**RECOMENDAÇÃO:** Opção [X]. [Justificativa baseada no posicionamento e segmento, não gosto pessoal.]

**PROVOCAÇÃO:** [Ex: "Essa direção funciona bem em tela mas pode perder legibilidade em miniatura (favicon, WhatsApp). É uma limitação aceitável?"]

Valide também:
- O conceito criativo reflete o posicionamento aprovado?
- As cores fazem sentido para o segmento? Alguma preferência ou restrição do cliente?
- A tipografia está acessível (Google Fonts gratuitas)?
- O estilo visual (minimalista vs. rico) está alinhado com o que o cliente espera?

**Próximo passo (semi-manual):**
1. Operador copia os prompts e gera no Midjourney (ou Ideogram)
2. Gera pelo menos 4 variações de cada direção
3. Seleciona a melhor variação de cada direção
4. Informa qual direção e variação escolheu

Após o operador informar a escolha, organize o resumo executivo do manual de identidade visual (conceito, paleta, tipografia, logo escolhido, diretrizes, do's/don'ts) e peça ao operador para montar o PDF no Canva.

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s3-identidade-visual.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph

## Formato do output (ee-s3-identidade-visual.json)

```json
{
  "creative_concept": "string — conceito criativo em 2-3 frases",
  "color_palette": [
    {
      "name": "Azul Confiança",
      "hex": "#1A3A5C",
      "rgb": "26, 58, 92",
      "cmyk": "72, 37, 0, 64",
      "role": "primary",
      "justification": "string"
    }
  ],
  "typography": {
    "title": { "font": "string", "weight": "string", "size": "string", "source": "Google Fonts" },
    "body": { "font": "string", "weight": "string", "size": "string", "source": "Google Fonts" },
    "highlight": { "font": "string", "weight": "string", "size": "string", "source": "Google Fonts" },
    "justification": "string"
  },
  "shape_guidelines": {
    "shapes": "string — geométricas/orgânicas/mistas",
    "borders": "string — arredondadas/retas/misto",
    "density": "string — minimalista/equilibrado/rico",
    "icon_style": "string"
  },
  "logo_prompts": [
    {
      "direction": "string — nome do estilo",
      "concept": "string — 1 frase",
      "prompt": "string — prompt Midjourney completo"
    }
  ],
  "chosen_direction": "string — qual direção o operador escolheu",
  "dos_and_donts": {
    "dos": ["string"],
    "donts": ["string"]
  }
}
```


## Campo obrigatório: summary

Sempre inclua no JSON de saída:
```json
"summary": "Resumo de 1-2 frases do identidade visual: conceito criativo central e paleta de cores principal. Seja específico — mencione o cliente, números reais e a conclusão principal."
```

Este campo alimenta o Resumo Executivo do portal de entregas. Deve ser objetivo, com dados reais, sem genéricos.
