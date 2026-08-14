# Mapeamento — operação Google Ads em voeuniair.com.br

**Data:** 2026-08-07
**Fontes:** Google Ads Transparency Center (API interna), HTML público de voeuniair.com.br,
whois registro.br, GitHub público, relatórios STD do nosso Google Ads.
**Método:** tudo aqui veio de fonte pública. Nada de acesso a conta, nada de submissão de
formulário no site deles.

---

## 1. Quem é o anunciante

O Transparency Center não mostra "outra agência" como anunciante. Mostra:

| campo | valor |
|---|---|
| Advertiser ID | `AR13265573025652146177` |
| Razão social verificada | UNIAIR ADMINISTRACAO PARTICIPACOES E SERVICOS MEDICOS DE URGENCIA LTDA |
| Conta Google Ads (obfuscated customer id) | `7429987497` |
| Domínio de destino | voeuniair.com.br |

Ou seja: **os anúncios rodam sob a identidade verificada do próprio cliente**, em uma conta
Google Ads diferente da nossa. Não é um concorrente de mercado disputando o leilão — é a
mesma marca, com dois fornecedores, duas contas e dois sites.

Domínio `voeuniair.com.br` (whois registro.br):
- titular **Fausto Villeroy dos Santos** (CNPJ 60.695.852/0001-72) — mesmo sobrenome de
  Daniele Villeroy, gerente comercial e uma das decisoras;
- registrado em **2025-10-14**;
- servido por Bunny CDN (`taxiaereo2156.b-cdn.net`);
- repositório público `github.com/FaustoVilleroy/voeuniair-static` criado em 2026-05-22.

---

## 2. Os anúncios (5 criativos ativos, todos ainda veiculando em 06–07/08/2026)

Screenshots em `criativos/`.

| # | Headline | Path exibido | Início | Fim |
|---|---|---|---|---|
| 1 | Táxi Aéreo Executivo - Voos Particulares Sob Demanda | /uniair/taxi-aereo | 2026-04-15 | 2026-08-07 |
| 2 | Táxi Aéreo Executivo - Cotação Táxi Aéreo | /taxi-aereo/cotacao | 2026-04-15 | 2026-08-07 |
| 3 | Orçamento Táxi Aéreo - Receba Sua Proposta | /taxi-aereo/cotacao | 2026-04-23 | 2026-08-06 |
| 4 | Cotação UTI Aérea - Cotação Remoção Aeromédica | /transporte/aeromedico | 2026-07-18 | 2026-08-06 |
| 5 | (criativo responsivo de display/HTML5, sem texto extraível) | — | 2026-04-22 | 2026-08-07 |

**Descriptions capturadas:**
- "Táxi aéreo executivo com agilidade, discrição e operação personalizada. Consulte
  disponibilidade e proposta para..."
- "Reduza horas de deslocamento e ganhe eficiência com voos executivos sob medida. Táxi aéreo..."
- "Informe origem, destino e data da viagem para receber uma proposta personalizada."
- "Preço de UTI aérea conforme a necessidade clínica e logística da remoção. Orçamento para
  remoção aeromédica com suporte especializado e agilidade."

**Sitelinks capturados:**
- Táxi Aéreo UniAir — "Solicite sua proposta com a UniAir para voos executivos sob demanda."
- Solicitar Cotação — "Informe rota e datas Retorno ágil com proposta"
- Voo Executivo Sob Consulta — "Informe sua rota e receba atendimento para análise operacional do voo."
- Quanto Custa UTI Aérea
- Preço Transporte Aeromédico

**Leitura:** a estratégia de copy é *bottom-of-funnel transacional pura*. Os termos que eles
espelham no anúncio são "cotação", "orçamento", "preço", "quanto custa" — intenção de compra
declarada. E abriram a frente aeromédica só em **18/07/2026**, ou seja, entraram no nosso
território mais lucrativo há três semanas.

---

## 3. A landing page — é aqui que está a diferença real

Estrutura do site (4 páginas + home, arquitetura enxuta):
`/` → `/sobre` → `/vooexecutivo` (money page executivo) → `/voomedico` (money page aeromédico)
→ `/contato`. Existe `/taxiaereo` citado no `llms.txt` mas está **404/vazio** — página
educacional planejada e não publicada.

### 3.1 Formulário: quiz de 6 passos, não formulário longo

Eles usam um formulário conversacional em etapas, com nome do lead injetado nas perguntas
seguintes. Sequência idêntica nas duas páginas, só muda o vocabulário:

| passo | executivo | aeromédico |
|---|---|---|
| 1 | "Para começar, como podemos te chamar?" | idem |
| 2 | "Prazer, {nome}! Qual o WhatsApp para nosso retorno?" | idem |
| 3 | "E o seu e-mail, caso precisemos enviar a cotação por escrito?" | "...enviar algum documento?" |
| 4 | "Agora sobre o voo: de onde vocês vão partir?" | "de qual cidade e estado o paciente sairá?" |
| 5 | "E qual o destino?" | "para qual cidade e estado ele precisa ser levado?" |
| 6 | "Por último, quando o voo precisa acontecer?" (Hoje / Amanhã / Ainda a definir) | "quando o transporte precisa acontecer?" |

Abertura: *"São 6 perguntas rápidas para nossa equipe montar o orçamento e retornar com agilidade."*
Ao final, redireciona para WhatsApp `5551992757845` com mensagem pré-preenchida.

**Nossa LP (`taxiaereo.uniair.com.br/aeromedico`) faz o oposto:** um único formulário com 10
campos visíveis de uma vez (nome, e-mail, telefone, motivo do contato, origem, cidade de
origem, destino, cidade de destino, "como podemos te ajudar", checkbox de privacidade).

Essa é a diferença mais copiável e de maior impacto imediato.

### 3.2 Promessas de topo

- H1 executivo: "Táxi aéreo executivo sob demanda para quem precisa ganhar tempo, conforto e
  controle da agenda"
- H1 aeromédico: "Transporte aeromédico para hospitais, operadoras, seguradoras, gestão
  pública e famílias" — **segmentação B2B explícita no H1**
- Selo repetido: "28 anos de operação • Frota própria • Atendimento 24h • Voos nacionais e
  internacionais"
- Micro-copy sob o botão: "Retorno ágil • Cotação sem compromisso • Atendimento 24h" e
  "🔒 Seus dados são confidenciais e utilizados apenas para retorno de contato."
- Bloco de dor antes da oferta: "Seus Deslocamentos Ainda Estão Travando Seus Resultados?" →
  Atrasos e Conexões / Estresse em Aeroportos Lotados / Oportunidades Perdidas / Falta de
  Flexibilidade
- Prova: "Empresas e Executivos que Confiam na UniAir", "Conheça nossos pilotos"
- FAQ próprio em cada página (8 perguntas na home, blocos de FAQ nas money pages)

### 3.3 Stack e mensuração

- GA4 `G-JDNKJ6TNQ5`
- Google Ads `AW-17995510704` (conta de conversão **diferente da nossa**)
- Duas conversões separadas por serviço:
  `AW-17995510704/4GsbCO-JgYQcELDn9oRD` (executivo) e `AW-17995510704/9luNCM3MjK0cELDn9oRD` (aeromédico)
- Leads gravados via Google Apps Script + redirect para WhatsApp; UTMs (`source/medium/campaign/term/content`) capturadas e enviadas junto
- Imagens hospedadas em Atomicat
- `llms.txt` publicado na raiz → estão jogando também para busca por IA (GEO/AEO)

---

## 4. Comparação com a nossa operação

Nosso Google Ads (relatórios STD em `../dados-de-midia/`):

| mês | cliques | custo | conv. | CVR | CPA |
|---|---|---|---|---|---|
| 2026-02 | 2.212 | R$ 14.099 | 226,0 | 10,22% | R$ 62 |
| 2026-03 | 1.692 | R$ 11.398 | 108,5 | 6,41% | R$ 105 |
| 2026-04 | 1.644 | R$ 6.119 | 9,0 | **0,55%** | R$ 680 |
| 2026-05 | 2.327 | R$ 7.818 | 11,3 | **0,49%** | R$ 690 |
| 2026-06 | 4.057 | R$ 8.915 | 64,0 | 1,58% | R$ 139 |
| 2026-07 | 8.228 | R$ 16.044 | 108,0 | 1,31% | R$ 149 |
| 2026-08 (1–5) | 586 | R$ 2.253 | 17,0 | 2,90% | R$ 133 |

**A CVR desabou em abril/2026 — o mesmo mês em que os anúncios deles entraram no ar
(15, 22 e 23/04).** Isso é correlação, não causa provada. Há duas hipóteses concorrentes e
ambas precisam ser testadas antes de qualquer conclusão:

1. **Tracking quebrou.** Queda de 6,4% para 0,55% em um mês é grande demais para
   competição. Conferir histórico de alterações de tags/conversões em abril.
2. **Tráfego ficou mais barato e pior.** CPC caiu de R$ 6,37 (fev) para R$ 1,95 (jul) —
   típico de abertura de correspondência ampla. Mais clique, menos intenção.

Só depois de descartar (1) e (2) faz sentido atribuir a queda ao segundo anunciante.

Diferenças estruturais que já dá para afirmar:

| | eles (voeuniair.com.br) | nós (taxiaereo.uniair.com.br) |
|---|---|---|
| Formulário | quiz de 6 passos + WhatsApp | 1 formulário, 10 campos |
| Conversões | 2, separadas por serviço | GTM único (`GTM-55L4KDJW`) |
| Copy do anúncio | transacional: cotação, orçamento, preço, quanto custa | a validar |
| Aeromédico | entrou em 18/07/2026 | nosso principal desde fev |
| Sitelinks | 3+ por anúncio, todos de cotação | a validar |
| GEO/AEO | `llms.txt` publicado | não |
| Canais | search (+1 criativo display) | 6 campanhas, só search |

---

## 5. Pendências deste mapeamento

- [ ] Confirmar quantos criativos **nossos** aparecem no Transparency Center para
      `taxiaereo.uniair.com.br` e `uniair.com.br` — a consulta foi bloqueada por captcha do
      Google no meio da coleta. Refazer.
- [ ] Auction Insights no nosso Google Ads: ver se a conta `7429987497` aparece como
      concorrente de leilão e com que impression share/overlap rate. **Esta é a única fonte
      que responde "eles estão nos ultrapassando?" com número.**
- [ ] Search Terms Report nosso vs. os termos que a copy deles espelha
      ("quanto custa uti aérea", "preço transporte aeromédico", "orçamento táxi aéreo").
- [ ] Auditar as tags de conversão de abril/2026 antes de atribuir a queda de CVR a eles.

## 6. Achado a comunicar ao cliente (segurança, não concorrência)

O endpoint que recebe os leads deles é um Google Apps Script chamado direto do JavaScript da
página, com token fixo em texto claro no HTML público. Qualquer pessoa que abrir o
código-fonte tem o endereço e o token. Isso é exposição real da base de leads da Uniair —
independente de quem gerencia a campanha. Vale reportar para Dani/Ana como risco, sem virar
munição política.
