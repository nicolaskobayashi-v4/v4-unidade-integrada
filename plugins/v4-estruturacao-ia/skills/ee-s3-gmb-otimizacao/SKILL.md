---
name: ee-s3-gmb-otimizacao
description: "Otimiza perfil do Google Meu Negocio com descricao SEO, categorias, servicos, posts e Q&As. Use quando o operador mencionar 'Google Meu Negocio', 'GMB', 'Google Business', 'perfil Google', 'SEO local'."
dependencies: ["ee-s1-persona-icp"]
outputs: ["ee-s3-gmb-otimizacao.json"]
week: 3
estimated_time: "45-60 min"
semi_manual: true
---

# Google Meu Negocio — Otimizacao Completa do Perfil

Voce e um especialista em SEO local e Google Business Profile. Vai construir, junto com o operador, a otimizacao completa do perfil GMB do cliente para maximizar visibilidade local e conversao organica.

> **IMPORTANTE:** Esta skill gera o conteudo e as orientacoes. O operador executa a configuracao diretamente no Google Business Profile — a IA nao tem acesso direto a plataforma.

## Dados necessarios

1. `client.json` (seção `briefing`) — dados base do cliente (OBRIGATORIO)
2. `outputs/ee-s1-persona-icp.json` — ICP e persona (OBRIGATORIO)

Extraia do briefing:
- `identification.name`, `identification.segment`, `identification.region`
- `product.main_product`, `product.ticket`, `product.all_products`
- `contact.whatsapp`, `contact.website`, `contact.address`, `contact.hours`

Extraia do ee-s1-persona-icp.json:
- `where_to_find.keywords` → palavras-chave do ICP
- `icp.pains` → dores (para Q&As)
- `icp.jobs.functional` → job funcional (para descricao)
- `key_message.chosen_message` → mensagem-chave

Consulte `references/seo-local-gmb.md` para boas praticas.

---

## Geração

Gere o output COMPLETO de uma vez usando os dados de `client.json` (briefing) e outputs de skills dependentes em `outputs/`.

### Descricao SEO do perfil (max 750 caracteres)

Inclua palavras-chave relevantes para {segmento} em {cidade/estado} de forma natural. Diga o que a empresa faz e para quem. Mencione diferenciais. Termine com CTA. NAO use emojis, hashtags, links ou linguagem promocional (Google penaliza). Apresente com contagem de caracteres.

### Categorias

- **Categoria principal:** a mais específica possível
- **Categorias secundárias (até 9):** complementares que ampliem visibilidade

### Atributos

Relevantes para o segmento (acessibilidade, estacionamento, pagamento, etc.).

### Lista de serviços

Para cada produto/serviço: nome (como o cliente buscaria no Google), descrição (1-2 frases com keywords), preço (se aplicável).

### Posts para 30 dias (4 posts)

Distribuição: apresentação, oferta, educativo, prova social.
Para cada: título, texto (até 1.500 chars), CTA (botão), tipo (novidade/oferta/evento).

### Q&As (5 perguntas e respostas)

Baseadas nas dores e objeções do ICP. Linguagem coloquial. Respostas completas com CTAs e keywords.

### Checklist de implementação

**Perfil Básico:** nome, endereço, telefone, site, horário, WhatsApp
**Descrição e Categorias:** descrição publicada, categorias configuradas, atributos ativados
**Serviços:** todos cadastrados
**Fotos (mínimo 10):** capa, logo, fachada, interior, equipe, produtos (specs: JPG/PNG, 720x720px+)
**Posts e Q&As:** publicados/agendados
**Extras:** solicitar avaliações, resposta padrão para reviews, mensagens ativadas, verificação

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Todos os campos do schema preenchidos (ou com `null` + `unavailable_reason` no pai)?
- [ ] Nenhuma string vazia (`""`) — substituí por `null` + reason quando o dado não existe?
- [ ] Estimativas marcadas com `estimated: true` ou `[E]`?
- [ ] Consistente com outputs anteriores (ICP)?
- [ ] Descrição tem <= 750 caracteres?
- [ ] Posts têm tom alinhado com a mensagem-chave?
- [ ] Q&As endereçam as 5 principais dúvidas/objeções do ICP?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

Revise o output. O que está errado, exagerado ou faltando?

- "A descricao representa bem o negocio? Algum diferencial que faltou?"
- "As categorias estao corretas?"
- "A lista de servicos esta completa?"
- "Os posts tem o tom certo para este cliente?"
- "As perguntas sao as que os clientes realmente fazem?"
- "O cliente ja tem acesso ao Google Meu Negocio?"
- "Ja tem fotos disponiveis ou precisa solicitar?"

**Próximo passo (semi-manual):** Operador executa o checklist de implementação no Google Business Profile.

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s3-gmb-otimizacao.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph
   - "Conteúdo GMB gerado e checklist entregue. O operador deve executar a configuração."
   - "Acompanhar: verificar em 7 dias se o perfil atingiu 100% de completude."
