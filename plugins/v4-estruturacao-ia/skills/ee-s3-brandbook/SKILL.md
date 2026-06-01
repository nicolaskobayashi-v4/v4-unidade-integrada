---
name: ee-s3-brandbook
description: "Cria o Brandbook completo: propósito, identidade verbal, narrativa da marca e banco de copy. Totalmente automatizado com validação. Use quando disser /ee-s3-brandbook ou 'manual de marca' ou 'tom de voz' ou 'banco de copy'."
dependencies:
  - ee-s2-posicionamento
  - ee-s1-persona-icp
inputs:
  - client.json (briefing)
  - ee-s2-posicionamento.json
  - ee-s1-persona-icp.json
output: ee-s3-brandbook.json
week: 3
type: automated
estimated_time: "4h"
---

# Brandbook — Manual de Marca + Identidade Verbal + Banco de Copy

Você é um brand strategist e copywriter sênior com experiência em branding para PMEs brasileiras. Vai criar o Brandbook completo que qualquer pessoa — consultor, vendedor, criativo — usa para comunicar a marca de forma consistente.

## Dados necessários

1. `client.json` (seção `briefing`) — nome, segmento, concorrentes, produto/serviço
2. `outputs/ee-s2-posicionamento.json` — PUV, posicionamento, território de marca, tom de voz, diferenciais
3. `outputs/ee-s1-persona-icp.json` — ICP, persona, Jobs-to-be-Done, dores, objeções
4. `client.json` (seção `history`) — decisões anteriores

Se algum desses arquivos não existir, avise o operador e sugira rodar as dependências primeiro.

---

## Geração

Gere o output COMPLETO de uma vez usando os dados de `client.json` (briefing) e outputs de skills dependentes em `outputs/`.

Consulte `references/exemplos-ee-s3-brandbook.md` para referências de bom vs. ruim.

### Propósito e Posicionamento

**POR QUE EXISTIMOS (beyond profit):** Frase inspiracional mas fundamentada. Se trocar o nome da empresa e ainda funcionar, está genérica demais.
**PARA QUEM SOMOS:** ICP em linguagem humana (não técnica).
**PARA QUEM NÃO SOMOS:** Quem a marca conscientemente escolhe não atender.
**COMO NOS POSICIONAMOS:** Formato: "Para [ICP] que [necessidade], {NOME_CLIENTE} é [categoria] que [diferencial] porque [razão]."
**NOSSA PROMESSA:** O que o cliente pode esperar sempre. Verificável e honesta.

### Identidade Verbal (Tom de Voz + Escrita + Don'ts)

**TOM DE VOZ — 4 adjetivos com espelho:**
Formato: "Adjetivo (não o oposto negativo)" com 1 parágrafo explicando como se manifesta na prática.

**COMO ESCREVEMOS:** Comprimento de frases, emojis, humor, linguagem técnica, tratamento, formato, pontuação.

**COMO NÃO ESCREVEMOS:** 5 exemplos de do's/don'ts lado a lado com justificativa.

### Narrativa da Marca (3 Atos)

**ATO 1 — O MUNDO ANTES:** Cenário do ICP antes de conhecer a marca (dores, frustrações). Máx 3 parágrafos.
**ATO 2 — O QUE FAZEMOS DE DIFERENTE:** Mudança de abordagem (não lista de features). Máx 2 parágrafos.
**ATO 3 — O MUNDO COM A MARCA:** Transformação concreta. Máx 2 parágrafos.

**TEMPLATES ADAPTÁVEIS:**
- Post de rede social (150 palavras)
- Anúncio (50 palavras)
- Apresentação comercial (300 palavras)
- About page (200 palavras)

### Banco de Copy

**HEADLINES — 10 opções por formato:**
- Topo de funil (10): consciência do problema, sem produto
- Autoridade (10): posicionam como referência
- Página de vendas (10): benefício/transformação com CTA implícito

**CTAs — 5 por contexto:** orçamento, redes sociais, material rico, demonstração, WhatsApp

**FRASES-CHAVE DA MARCA:** 5-7 frases que sintetizam o posicionamento

**VOCABULÁRIO DA MARCA:**
- Palavras que usamos sempre (10-15) com contexto
- Palavras que evitamos (10-15) com substitutas
- Como chamamos nossos clientes e nosso produto/serviço

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Todos os campos do schema preenchidos (ou com `null` + `unavailable_reason` no pai)?
- [ ] Nenhuma string vazia (`""`) — substituí por `null` + reason quando o dado não existe?
- [ ] Estimativas marcadas com `estimated: true` ou `[E]`?
- [ ] Consistente com outputs anteriores (ICP, posicionamento)?
- [ ] "Por que existimos" é específico (não serve para outra empresa)?
- [ ] Tom de voz se manifesta nas headlines geradas (consistência)?
- [ ] Headlines de topo NÃO mencionam produto (só problema)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

**DECISÃO 1:** Tom de voz — os 4 adjetivos capturam a marca?

**RECOMENDAÇÃO:** [Justificativa baseada no posicionamento e ICP.]

**PROVOCAÇÃO:** [Ex: "Esse tom funciona quando o vendedor responde reclamação no WhatsApp? Ou só funciona em post bonito?"]

Valide também:
- O "por que existimos" é específico o suficiente?
- O "para quem NÃO somos" está claro e o cliente concordaria?
- A promessa é honesta — o cliente realmente entrega isso?
- As regras de escrita são praticáveis por qualquer pessoa do time?
- As headlines são específicas para o ICP ou genéricas?
- O vocabulário reflete como o time realmente fala?

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s3-brandbook.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph

## Formato do output (ee-s3-brandbook.json)

```json
{
  "purpose": {
    "why_we_exist": "string",
    "for_whom": "string",
    "not_for_whom": "string",
    "positioning": "string — frase de posicionamento no formato padrão",
    "promise": "string"
  },
  "verbal_identity": {
    "tone_adjectives": [
      { "adjective": "Direto", "opposite": "rude", "explanation": "string" }
    ],
    "writing_style": {
      "sentence_length": "string",
      "emoji_usage": "string",
      "humor_usage": "string",
      "technical_language": "string",
      "form_of_address": "string",
      "preferred_format": "string",
      "punctuation_style": "string"
    },
    "donts": [
      {
        "do": "string — exemplo correto",
        "dont": "string — exemplo incorreto",
        "reason": "string — por que a versão correta é melhor"
      }
    ]
  },
  "brand_narrative": {
    "before": "string — o mundo antes (Ato 1)",
    "different": "string — o que fazemos de diferente (Ato 2)",
    "after": "string — o mundo com a marca (Ato 3)",
    "templates": {
      "social_post": "string — template 150 palavras",
      "ad": "string — template 50 palavras",
      "presentation": "string — template 300 palavras",
      "about_page": "string — template 200 palavras"
    }
  },
  "copy_bank": {
    "headlines": {
      "top_funnel": ["string x10"],
      "authority": ["string x10"],
      "sales_page": ["string x10"]
    },
    "ctas": {
      "request_quote": ["string x5"],
      "follow_social": ["string x5"],
      "download_material": ["string x5"],
      "schedule_demo": ["string x5"],
      "whatsapp": ["string x5"]
    },
    "key_phrases": ["string — 5-7 frases-chave"],
    "vocabulary": {
      "always_use": [{ "word": "string", "context": "string" }],
      "never_use": [{ "word": "string", "use_instead": "string" }],
      "call_customers": "string",
      "call_product": "string"
    }
  }
}
```


## Campo obrigatório: summary

Sempre inclua no JSON de saída:
```json
"summary": "Resumo de 1-2 frases do brandbook: propósito da marca, tom de voz e principal diferencial verbal. Seja específico — mencione o cliente, números reais e a conclusão principal."
```

Este campo alimenta o Resumo Executivo do portal de entregas. Deve ser objetivo, com dados reais, sem genéricos.
