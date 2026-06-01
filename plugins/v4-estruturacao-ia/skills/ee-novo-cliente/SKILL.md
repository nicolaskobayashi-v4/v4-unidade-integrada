---
name: ee-novo-cliente
description: "Cadastra um novo cliente no sistema. Cria pasta, puxa dados do V4MOS, faz briefing complementar interativo. Use quando o operador disser /ee-novo-cliente, 'novo cliente', 'cadastrar cliente', ou 'começar projeto'."
---

# Novo Cliente — Cadastro e Briefing

Você vai cadastrar um novo cliente no sistema de Estruturação IA. O processo tem 6 etapas sequenciais. Não pule etapas.

## Etapa 1: Identificação básica

Pergunte ao operador tudo de uma vez (pode ser numa mensagem só):

```
Para cadastrar o cliente, preciso de:

1. Nome da empresa
2. Site (URL)
3. Instagram (@handle)
4. Workspace V4MOS? (UUID ou "não tem")
5. Módulo vendas/SDR IA contratado? (sim/não)
6. Quer que eu pesquise a empresa na internet pra preencher o briefing automaticamente? (gasta mais tokens, economiza tempo)
```

Derive o slug do nome: lowercase, sem acentos, espaços viram hífens. Exemplo: "Padaria do João" → `padaria-do-joao`.

### Se o operador escolheu BUSCA AUTOMÁTICA:

Lance subagents em paralelo para pesquisar. Use o site e Instagram fornecidos como ponto de partida:

**Subagent 1 — Site e empresa:**
- WebFetch no site fornecido: extrair TUDO — hero text, about, serviços, preços, depoimentos, FAQ, rodapé (CNPJ, endereço)
- Navegar páginas internas se existirem: /sobre, /servicos, /contato
- Verificar SSL, responsividade, PageSpeed básico

**Subagent 2 — Redes sociais e reputação:**
- WebFetch no Instagram fornecido: bio completa, tipo de conteúdo, frequência, destaques
- WebSearch: "{nome_empresa} Google Meu Negócio" — extrair avaliações, horários, fotos
- WebSearch: "{nome_empresa} avaliações" ou reclame aqui

**Subagent 3 — Mercado e concorrentes:**
- A partir do segmento inferido do site: WebSearch "concorrentes de {nome_empresa}" ou "{segmento} {cidade}"
- WebSearch: "{segmento} mercado brasil tamanho"
- Para cada concorrente encontrado: WebFetch no site deles (hero, proposta de valor, preços)
- Identificar 3-5 concorrentes com diferenciais percebidos

### Salvar pesquisa como artefato permanente

**ANTES de mostrar o resumo ao operador**, salve TODA a pesquisa bruta em `clientes/{slug}/research.md`.

Este arquivo é o deep research do cliente — fonte de verdade pra todas as skills downstream. Formato:

```markdown
# Deep Research — {nome_empresa}
**Data:** {YYYY-MM-DD}
**Fontes:** site ({url}), Instagram ({handle}), Google, GMB

---

## 1. Site — Análise Completa

### Textos extraídos
**Hero:** {texto do hero}
**Sobre:** {texto da página sobre}
**Serviços:** {lista de serviços com descrições}
**Depoimentos:** {depoimentos encontrados}
**FAQ:** {perguntas e respostas se existirem}
**Rodapé:** {CNPJ, endereço, contatos}

### Dados técnicos
- SSL: {sim/não}
- Mobile-friendly: {sim/não}
- PageSpeed estimado: {rápido/médio/lento}
- Tecnologia: {WordPress, Wix, custom, etc.}

---

## 2. Instagram — @{handle}

### Bio
{bio completa}

### Conteúdo
- Tipo predominante: {fotos/carrossel/reels/stories}
- Frequência estimada: {X posts/semana}
- Tom de voz observado: {formal/casual/etc}
- Temas recorrentes: {lista}
- Engajamento: {alto/médio/baixo}

---

## 3. Google Meu Negócio

- Status: {ativo/não encontrado}
- Avaliações: {X estrelas, Y avaliações}
- Categoria: {categoria}
- Fotos: {quantidade}
- Posts recentes: {sim/não}

---

## 4. Reputação Online

- Reclame Aqui: {encontrado/não}
- Avaliações Google: {resumo}
- Menções relevantes: {links}

---

## 5. Mercado e Concorrentes

### Tamanho do mercado
{dados encontrados sobre TAM/segmento}

### Concorrentes identificados

#### {Concorrente 1}
- Site: {url}
- Proposta de valor: {hero text deles}
- Diferencial percebido: {o que parece diferente}
- Preço/ticket: {se visível}

#### {Concorrente 2}
[mesmo formato]

#### {Concorrente 3}
[mesmo formato]

### Posicionamento comparativo
{análise breve de como o cliente se posiciona vs concorrentes}

---

## 6. Dados inferidos (a confirmar com operador)

| Campo | Valor inferido | Confiança | Fonte |
|-------|---------------|-----------|-------|
| Segmento | {x} | alta/média/baixa | site |
| Localização | {x} | alta | rodapé site |
| Tempo de mercado | {x} | baixa | estimativa |
| Produto principal | {x} | alta | site |
| Ticket médio | {x} | baixa | estimativa |
```

### Apresentar resumo ao operador

Depois de salvar o research.md, mostre um resumo compacto para confirmação EM BATCH:

```
PESQUISA SALVA — {nome}
━━━━━━━━━━━━━━━━━━━━━━

Pesquisa completa em: clientes/{slug}/research.md

Confirme ou corrija os dados principais:

EMPRESA:
  Nome: {nome}                    ✅ correto?
  Segmento: {segmento}            ✅ correto?
  Localização: {cidade}           ✅ correto?
  Produto: {produto}              ✅ correto?

CONCORRENTES:
  1. {nome} — {diferencial}       ✅ correto?
  2. {nome} — {diferencial}       ✅ correto?
  3. {nome} — {diferencial}       ✅ correto?

PRESENÇA DIGITAL:
  Site: {status}
  Instagram: {status}
  GMB: {status}

O que está errado ou faltando?
```

O operador corrige. Itens confirmados vão pro client.json (briefing). research.md permanece como fonte de consulta para todas as skills.

**IMPORTANTE:** Campos que NUNCA podem ser inferidos (sempre perguntar manualmente):
- Descrição dos 3 melhores clientes
- Quem NÃO é cliente ideal
- 3 problemas que clientes têm antes de contratar
- 3 resultados que clientes alcançam
- Razões de churn
- Diferencial REAL vs concorrentes (não o percebido)
- Tom de voz desejado
- 3 adjetivos de personalidade da marca
- Restrições visuais
- Dados de vendas (ciclo, conversão, objeções)

Esses campos são subjetivos e só o operador/cliente sabe.

### Se o operador escolheu MANUAL:

Confirme com o operador:
```
Cliente: {nome}
Slug: {slug}
Workspace V4MOS: {workspace_id ou "sem integração"}
Módulo Vendas: {sim/não}

Correto?
```

E siga para Etapa 2.

## Etapa 2: Criar estrutura

Com o slug confirmado, crie:

```
clientes/{slug}/
  client.json              ← fonte única de verdade (meta, briefing, research, connectors, progress, history)
  base-de-conhecimento/    ← operador sobe docs, reuniões, emails aqui
  outputs/                 ← outputs das skills (versionados)
  semana-1/
  semana-2/
  semana-3/
  semana-4-5/              ← só criar se módulo vendas = sim
```

Inicialize `client.json` com a estrutura completa:

```json
{
  "meta": {
    "name": "Nome Real da Empresa",
    "slug": "slug",
    "workspace_id": "workspace-uuid",
    "created_at": "YYYY-MM-DD",
    "modulo_vendas": true
  },
  "briefing": {},
  "research": {"fetched_at": null},
  "connectors": {"fetched_at": null, "integrations": null},
  "progress": {
    "current_week": 1,
    "skills": {
    "ee-s1-diagnostico-maturidade": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s1-swot": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s1-persona-icp": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s1-auditoria-comunicacao": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s2-pesquisa-mercado": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s2-posicionamento": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s2-diagnostico-midia": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s2-diagnostico-criativos": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s2-diagnostico-cro": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s3-identidade-visual": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s3-brandbook": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s3-landing-page": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s3-copy-anuncios": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s3-criativos-anuncios": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s3-crm-setup": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s3-forecast-midia": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s3-gmb-otimizacao": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s4-diagnostico-comercial": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s4-cliente-oculto": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s5-scripts-sdr": {"status": "pending", "checkpoint": 0, "started_at": null, "completed_at": null},
    "ee-s5-sdr-ia-config": {"status": "pending", "version": 0, "started_at": null, "completed_at": null}
    }
  },
  "history": []
}
```

Se `modulo_vendas` = false, remova as 4 skills de semana 4-5 do progress.skills e não crie a pasta `semana-4-5/`.

## Etapa 3: Puxar dados V4MOS

**Se tem workspace_id:**

1. Verifique se já existe credencial em `.credentials/clients.json` para esse workspace_id
2. Se EXISTE, mostre ao operador e peça confirmação:
   - "Encontrei credenciais salvas para esse workspace (client_id: {primeiros 8 chars}...). Usar essas? Ou quer informar novas?"
   - Se operador confirma, use as existentes
   - Se operador quer novas, peça e sobrescreva
3. Se NÃO existe, pergunte ao operador:
   - "Preciso do client_id e client_secret do Service Account V4MOS para o workspace desse cliente."
   - Instrua como criar:
     ```
     Como criar o Service Account:
     1. Acesse v4.marketing e entre no workspace do cliente
     2. Vá em Settings (engrenagem) > Data API
     3. Lá você verá client_id, client_secret e workspace_id
     4. Copie os 3 valores e cole aqui
     
     URL de referência: https://developers.v4.marketing
     Base da API: https://api.data.v4.marketing
     ```
   - Salve em `.credentials/clients.json` com a chave sendo o workspace_id:
     ```json
     {
       "{workspace_id}": {
         "client_id": "...",
         "client_secret": "...",
         "client_name": "Nome do Cliente"
       }
     }
     ```
   - IMPORTANTE: cada cliente tem seu próprio Service Account vinculado ao workspace dele. Não reutilize credenciais entre clientes.

4. **Buscar dados de mídia via API V4MOS:**

   Use o script (que lida com paginação e agrega os dados):
   ```bash
   bash scripts/v4mos_fetch.sh clientes/{slug}
   ```

   Ou, se precisar buscar manualmente (atenção: `workspaceId` é QUERY PARAMETER, não path):
   ```bash
   # Google Ads
   curl -s "https://api.data.v4.marketing/v1/google/ads/campaigns?workspaceId={WORKSPACE_ID}&limit=500" \
     -H "x-client-id: {CLIENT_ID}" -H "x-client-secret: {CLIENT_SECRET}"

   # Facebook Ads
   curl -s "https://api.data.v4.marketing/v1/facebook/ads/campaigns?workspaceId={WORKSPACE_ID}&limit=500" \
     -H "x-client-id: {CLIENT_ID}" -H "x-client-secret: {CLIENT_SECRET}"
   ```

   **Auth:** apenas `x-client-id` + `x-client-secret`. Sem `x-workspace-id`. Sem Bearer token.
   **Documentação:** https://developers.v4.marketing

   **Se retornar 200:** dados salvos em `client.json.connectors` pelo script
   **Se retornar 401:** credenciais erradas — verifique em Configurações > API de Dados no V4MOS
   **Se retornar 400 "workspaceId obrigatório":** faltou o query param (erro de chamada)
   **Se workspace_id for null:** cliente sem V4MOS — siga com dados do briefing

5. Mostre ao operador um resumo:
   ```
   DADOS V4MOS — {nome}
   ━━━━━━━━━━━━━━━━━━━━
   Google Ads: {N} campanhas | R${X} gasto | CPA médio R${Y}
   Facebook Ads: {N} campanhas | R${X} gasto | CPM médio R${Y}
   Período: {start} → {end}
   ```

6. Dados de mídia serão usados nas skills de diagnóstico de mídia e maturidade

**Se não tem workspace_id:**

Avise: "Sem integração V4MOS." e prossiga para a Etapa 4.

## Etapa 4: Base de Conhecimento

Antes de fazer perguntas, convide o operador a subir contexto existente:

```
ANTES DE COMEÇAR O BRIEFING
━━━━━━━━━━━━━━━━━━━━━━━━━━

Você tem documentos, reuniões, emails ou anotações sobre esse cliente?
Quanto mais contexto você subir, menos perguntas eu faço.

Exemplos do que aceito:
  - Transcrições de reuniões (kick-off, alinhamento, etc.)
  - Emails com briefing ou proposta comercial
  - Documentos de apresentação do cliente
  - Anotações suas sobre o cliente
  - Screenshots de dashboards ou relatórios

Como fazer:
  1. Cole o conteúdo aqui que eu salvo automaticamente
  2. Ou use /ee-adicionar-base a qualquer momento pra adicionar mais

Quando terminar de subir, diga "pronto" que eu processo tudo e monto o briefing.
Se não tem nada, diga "não tenho" que eu pergunto tudo do zero.
```

### Se o operador subir conteúdo:

Para cada conteúdo recebido:
1. Identifique tipo (reunião, doc, email, anotação)
2. Salve em `clientes/{slug}/base-de-conhecimento/{YYYY-MM-DD}-{tipo}-{assunto}.md`
3. Preserve o conteúdo original na íntegra
4. Extraia dados relevantes pro briefing
5. Diga: "Salvo. Mais algum conteúdo ou posso processar?"

### Quando operador disser "pronto":

Leia TODOS os arquivos em `clientes/{slug}/base-de-conhecimento/` e cruze com os campos do briefing.

Para cada campo do briefing (ver `references/briefing-fields.md`):
- Se encontrou na base de conhecimento → marca como "encontrado" com confiança
- Se não encontrou → marca como "perguntar"

Apresente em batch:
```
DADOS ENCONTRADOS NA SUA BASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Com base nos {N} documentos que você subiu, encontrei:

  Segmento: Marketing digital (reunião kick-off)       ✅ correto?
  Produto: Gestão de tráfego pago (proposta comercial)  ✅ correto?
  Ticket: R$3.000/mês (proposta comercial)              ✅ correto?
  Concorrente: AgênciaX (mencionado em reunião)         ✅ correto?
  Tom de voz: Profissional (inferido do site)            ✅ correto?
  ...

DADOS NÃO ENCONTRADOS (vou perguntar):
  - Quem é o melhor cliente deles
  - Razões de churn
  - Restrições visuais
  - ...

Confirme os dados encontrados e eu pergunto só o que falta.
```

### Se operador disser "não tenho":

Siga direto pro briefing manual (Etapa 5).

## Etapa 5: Briefing complementar interativo

Consulte `references/briefing-fields.md` para a lista completa de campos por seção.

**Fontes de dados (em ordem de prioridade):**
1. **Base de conhecimento** (`base-de-conhecimento/`) — já confirmados na Etapa 4
2. **Research automático** (`client.json` (seção `research`) + `base-de-conhecimento/`) — pesquisa da internet, confirmada na Etapa 1
3. **Conectores V4MOS** (`client.json` (seção `connectors`)) — dados de integrações
4. **Perguntas ao operador** — só o que não foi encontrado nas fontes acima

Regras do fluxo:
- Campos já confirmados nas etapas anteriores: NÃO pergunte de novo, só inclua no briefing
- Campos encontrados mas não confirmados: confirme rapidamente ("Na reunião de kick-off você mencionou X. Correto?")
- Campos não encontrados em nenhuma fonte: pergunte ao operador
- Agrupe campos relacionados quando fizer sentido
- Se o operador não sabe um campo opcional, registre como null e siga
- Se o operador não sabe um campo obrigatório, insista gentilmente

Ordem das seções:
1. **Identificação** — nome, responsável, setor, faturamento, etc.
2. **Produto e Serviço** — produto principal, ticket, ciclo de venda
3. **Cliente Ideal** — melhor cliente, quem não é, problemas, resultados
4. **Concorrência** — 3 concorrentes, diferencial, por que escolheria
5. **Marca e Identidade** — adjetivos, tom de voz, marcas admiradas, restrições
6. **Situação Digital** — tráfego pago, CRM, fontes de leads, conversão
7. **Acessos** — Meta, Google Ads, GA, etc.
8. **Módulo Vendas** — só se contratado (vendedores, processo, objeções)

Campos que SEMPRE precisam ser coletados manualmente (não existem no V4MOS):
- Descrição dos 3 melhores clientes
- Quem NÃO é cliente ideal
- 3 problemas que clientes têm antes de contratar
- 3 resultados que clientes alcançam
- Razões de churn
- 3 concorrentes com diferencial percebido
- Diferencial real vs concorrentes
- Por que um cliente escolheria eles
- 3 adjetivos de personalidade da marca
- Tom de voz desejado
- 3-5 marcas admiradas visualmente
- Restrições visuais (o que NÃO pode aparecer)

## Etapa 5: Salvar briefing

Salve tudo em `clientes/{slug}/client.json (briefing)` com a estrutura:

```json
{
  "identification": {
    "name": "Nome da Empresa",
    "contact_name": "Nome do Responsável",
    "contact_role": "Cargo",
    "segment": "Setor/segmento",
    "annual_revenue": "R$ X",
    "years_in_market": "X anos",
    "location": "Cidade/Estado",
    "website": "https://...",
    "instagram": "@handle",
    "whatsapp": "+55...",
    "gmb": true
  },
  "product": {
    "main_product": "Descrição do produto/serviço principal",
    "ticket": "R$ X",
    "billing_model": "unico|recorrente|projeto",
    "sales_cycle": "X dias/semanas",
    "active_customers": "X",
    "most_profitable": "Produto mais lucrativo",
    "growth_potential": "Produto com maior potencial"
  },
  "icp": {
    "best_customers": "Descrição dos 3 melhores clientes",
    "not_customers": "Quem NÃO é cliente ideal",
    "problems_before": ["Problema 1", "Problema 2", "Problema 3"],
    "results_after": ["Resultado 1", "Resultado 2", "Resultado 3"],
    "churn_reasons": "Razões de churn"
  },
  "competition": {
    "competitors": [
      {"name": "Concorrente 1", "perceived_differential": "..."},
      {"name": "Concorrente 2", "perceived_differential": "..."},
      {"name": "Concorrente 3", "perceived_differential": "..."}
    ],
    "real_differential": "Diferencial real vs concorrentes",
    "why_choose_us": "Por que um cliente escolheria eles"
  },
  "brand": {
    "adjectives": ["Adjetivo 1", "Adjetivo 2", "Adjetivo 3"],
    "voice_tone": "formal|profissional|descontraido|informal",
    "admired_brands": ["Marca 1", "Marca 2", "Marca 3"],
    "current_colors": "Cores atuais (se tiver)",
    "has_logo": true,
    "restrictions": "O que NÃO pode aparecer"
  },
  "digital_situation": {
    "paid_traffic": true,
    "platforms": ["meta_ads", "google_ads"],
    "monthly_investment": "R$ X",
    "current_results": "CPL X, Y leads/mês",
    "crm": "Nome do CRM ou null",
    "lead_sources": "Como os leads chegam hoje",
    "conversion_rate": "X%",
    "biggest_pain": "Maior dor no marketing/vendas"
  },
  "accesses": {
    "meta_business": false,
    "google_ads": false,
    "google_analytics": false,
    "google_search_console": false,
    "instagram_admin": false,
    "website_admin": false,
    "crm": false,
    "gmb": false,
    "whatsapp_business": false
  },
  "sales_module": {
    "active_sellers": "X",
    "sales_process": "Etapas do processo",
    "objections": ["Objeção 1", "Objeção 2", "Objeção 3"],
    "conversion_rate": "X%",
    "sales_cycle": "X dias",
    "has_scripts": false
  }
}
```

Se `modulo_vendas` = false, o campo `sales_module` deve ser `null`.

## Etapa 6: Confirmar e gerar portal

1. Mostre ao operador um resumo formatado do briefing:
   ```
   BRIEFING — {nome}
   ━━━━━━━━━━━━━━━━━
   Segmento: {segmento}
   Produto: {produto} (ticket R$ {ticket})
   ICP resumo: {best_customers resumido}
   Concorrentes: {lista}
   Tom de voz: {tom}
   Tráfego pago: {sim/não} ({plataformas})
   Módulo vendas: {sim/não}
   ```

2. Pergunte: "Quer ajustar algum campo antes de salvar definitivamente?"
3. Se sim, ajuste e salve novamente
4. Execute `render_portal.sh clientes/{slug}` para gerar o portal inicial de entregas (todas skills pendentes)
5. Gere `clientes/{slug}/dashboard.html` com o estado inicial (todas skills pending)
6. Atualize `dashboard-geral.html` com o novo cliente
7. Appende em `clientes/{slug}/client.json (history)`:
   ```json
   {"ts":"YYYY-MM-DDTHH:MM:SSZ","skill":"ee-novo-cliente","checkpoint":0,"decision":"Cliente cadastrado. Briefing completo."}
   ```

Mensagem final:

```
Cliente {nome} cadastrado com sucesso!

Pasta: clientes/{slug}/
Briefing: clientes/{slug}/client.json (briefing)
Portal: clientes/{slug}/portal.html
Dashboard: clientes/{slug}/dashboard.html

Para começar a semana 1, diga: ee-continuar {nome}
```
