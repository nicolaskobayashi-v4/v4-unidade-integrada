# Briefing Fields — Referência Completa

Lista de todos os campos do briefing, organizados por seção. Para cada campo:
- **Nome:** identificador no JSON
- **Descrição:** o que coletar
- **Fonte:** "V4MOS" (pode vir da API) ou "manual" (sempre perguntar ao operador)
- **Obrigatório:** sim ou não

---

## 1. Identificação (`identification`)

| Campo | Descrição | Fonte | Obrigatório |
|---|---|---|---|
| `name` | Nome da empresa | V4MOS | Sim |
| `contact_name` | Nome do responsável/ponto de contato | Manual | Sim |
| `contact_role` | Cargo do responsável | Manual | Não |
| `segment` | Setor ou segmento de atuação (ex: odontologia, e-commerce de moda) | V4MOS | Sim |
| `annual_revenue` | Faturamento anual aproximado em R$ | Manual | Sim |
| `years_in_market` | Tempo de mercado (em anos) | Manual | Não |
| `location` | Cidade e estado da sede | V4MOS | Sim |
| `website` | URL do site atual (se tiver) | V4MOS | Não |
| `instagram` | Handle do Instagram (ex: @empresa) | V4MOS | Não |
| `whatsapp` | Número do WhatsApp Business | Manual | Não |
| `gmb` | Tem Google Meu Negócio? (true/false) | V4MOS | Não |

---

## 2. Produto e Serviço (`product`)

| Campo | Descrição | Fonte | Obrigatório |
|---|---|---|---|
| `main_product` | Descrição do principal produto ou serviço vendido | Manual | Sim |
| `ticket` | Ticket médio de venda em R$ | Manual | Sim |
| `billing_model` | Forma de cobrança: "unico", "recorrente", ou "projeto" | Manual | Sim |
| `sales_cycle` | Tempo médio do ciclo de venda (ex: "7 dias", "2 meses") | Manual | Sim |
| `active_customers` | Quantidade de clientes ativos hoje | Manual | Não |
| `most_profitable` | Produto/serviço mais lucrativo | Manual | Não |
| `growth_potential` | Produto/serviço com maior potencial de crescimento | Manual | Não |

---

## 3. Cliente Ideal (`icp`)

| Campo | Descrição | Fonte | Obrigatório |
|---|---|---|---|
| `best_customers` | Descrição detalhada dos 3 melhores clientes (quem são, o que compram, por que são bons) | Manual | Sim |
| `not_customers` | Quem NÃO é cliente ideal (perfis que não dão certo) | Manual | Sim |
| `problems_before` | 3 problemas que os clientes têm ANTES de contratar | Manual | Sim |
| `results_after` | 3 resultados concretos que os clientes alcançam | Manual | Sim |
| `churn_reasons` | O que faz um cliente sair (principais razões de churn) | Manual | Não |

---

## 4. Concorrência (`competition`)

| Campo | Descrição | Fonte | Obrigatório |
|---|---|---|---|
| `competitors` | Array com 3 concorrentes. Cada um com `name` (nome) e `perceived_differential` (o que o mercado acha que eles fazem melhor) | Manual | Sim |
| `real_differential` | Diferencial real da empresa em relação aos concorrentes listados | Manual | Sim |
| `why_choose_us` | Por que um cliente escolheria esta empresa em vez dos concorrentes | Manual | Sim |

---

## 5. Marca e Identidade (`brand`)

| Campo | Descrição | Fonte | Obrigatório |
|---|---|---|---|
| `adjectives` | 3 adjetivos que descrevem a personalidade da marca (ex: "confiável", "inovadora", "acolhedora") | Manual | Sim |
| `voice_tone` | Tom de voz desejado: "formal", "profissional", "descontraido", ou "informal" | Manual | Sim |
| `admired_brands` | 3 a 5 marcas que a empresa admira visualmente (qualquer setor) | Manual | Sim |
| `current_colors` | Cores atuais da marca (hex, nomes, ou descrição). Null se não definido | Manual | Não |
| `has_logo` | Tem logo atual? (true/false) | Manual | Não |
| `restrictions` | O que NÃO pode aparecer na comunicação da marca (restrições visuais, termos proibidos, etc.) | Manual | Não |

---

## 6. Situação Digital (`digital_situation`)

| Campo | Descrição | Fonte | Obrigatório |
|---|---|---|---|
| `paid_traffic` | Investe em tráfego pago hoje? (true/false) | V4MOS | Sim |
| `platforms` | Plataformas de mídia paga ativas (array: "meta_ads", "google_ads", "tiktok_ads", etc.) | V4MOS | Se paid_traffic=true |
| `monthly_investment` | Investimento mensal em mídia paga (R$) | V4MOS | Se paid_traffic=true |
| `current_results` | Resultado atual: CPL, leads/mês, ROAS (o que o operador souber) | V4MOS | Se paid_traffic=true |
| `crm` | Nome do CRM usado (ex: "Kommo", "HubSpot") ou null se não usa | V4MOS | Sim |
| `lead_sources` | Como os leads chegam hoje — principais fontes (ex: "indicação, Google, Instagram") | Manual | Sim |
| `conversion_rate` | Taxa de conversão estimada de lead para cliente (%) | Manual | Não |
| `biggest_pain` | Maior dor no marketing/vendas atual (resposta aberta) | Manual | Sim |

---

## 7. Acessos (`accesses`)

| Campo | Descrição | Fonte | Obrigatório |
|---|---|---|---|
| `meta_business` | Tem acesso ao Meta Business Manager? (true/false) | V4MOS | Não |
| `google_ads` | Tem acesso ao Google Ads? (true/false) | V4MOS | Não |
| `google_analytics` | Tem acesso ao Google Analytics / Tag Manager? (true/false) | V4MOS | Não |
| `google_search_console` | Tem acesso ao Google Search Console? (true/false) | V4MOS | Não |
| `instagram_admin` | Tem acesso admin ao Instagram? (true/false) | Manual | Não |
| `website_admin` | Tem acesso admin ao site (painel/FTP)? (true/false) | Manual | Não |
| `crm` | Tem acesso ao CRM? (true/false) | Manual | Não |
| `gmb` | Tem acesso ao Google Meu Negócio? (true/false) | V4MOS | Não |
| `whatsapp_business` | Tem acesso ao WhatsApp Business? (true/false) | Manual | Não |

Os campos com fonte "V4MOS" podem ser pré-preenchidos verificando o status de integrações no `client.json` (seção `connectors`). Se a integração existe e está ativa, marque como true.

---

## 8. Módulo Vendas (`sales_module`)

Seção coletada APENAS se o módulo vendas (SDR IA) foi contratado. Se não foi contratado, todo o campo `sales_module` deve ser `null` no client.json (briefing).

| Campo | Descrição | Fonte | Obrigatório |
|---|---|---|---|
| `active_sellers` | Quantidade de vendedores ativos | Manual | Sim |
| `sales_process` | Etapas do processo comercial atual (descrição textual ou lista) | Manual | Sim |
| `objections` | 3 principais objeções que o time comercial enfrenta | Manual | Sim |
| `conversion_rate` | Taxa de conversão proposta para venda (%) | Manual | Não |
| `sales_cycle` | Tempo médio do ciclo de venda | Manual | Não |
| `has_scripts` | Existe script ou roteiro de vendas atual? (true/false) | Manual | Sim |

---

## Notas para o agente

1. **Campos V4MOS:** Quando o dado vem do V4MOS, mostre ao operador e peça confirmação. O dado pode estar desatualizado.
2. **Campos manuais obrigatórios:** Se o operador não sabe, insista gentilmente. Ofereça ajuda ("Uma estimativa já ajuda. Pode ser um range?").
3. **Campos opcionais:** Se o operador não sabe, registre como `null` e siga em frente.
4. **Fluxo conversacional:** Pergunte um campo por vez ou agrupe 2-3 campos da mesma seção quando fizer sentido natural (ex: "Sobre o produto: qual é o principal e qual o ticket médio?").
5. **Nunca despeje formulário:** Não liste todos os campos de uma vez. Conduza uma conversa.
