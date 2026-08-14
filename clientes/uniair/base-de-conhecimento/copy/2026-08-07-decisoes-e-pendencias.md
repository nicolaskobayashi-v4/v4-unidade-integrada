# Copy das LPs Uniair — decisões, pendências e checklist de publicação

**Data:** 2026-08-07 · **Escopo:** Fase 1 — LPs A, B e C.
**Arquivos:** `2026-08-07-lp-a-taxi-aereo-executivo.md`, `...-lp-b-transporte-aeromedico.md`,
`...-lp-c-uti-aerea.md`.

---

## 0. Divergência assumida em relação ao briefing — campo "finalidade do voo"

**O briefing está errado neste ponto e a copy não o segue.**

A seção 5 do `briefing-lps-copy-design.md` manda eliminar "qual o motivo do seu contato",
classificando-o entre os "4 campos de atrito que o time comercial descobre na primeira ligação de
qualquer jeito". O raciocínio olha só para o custo do campo e ignora para que ele serve.

**Por que ele fica:**

1. **É a origem da classificação de MQL.** O qualificado que aparece no relatório sai da resposta
   do formulário — não da ligação do comercial. Sem o campo, não existe MQL automático.
2. **É o MQL que vai para o Google Ads como conversão.** Sem ele, a conversão enviada vira lead
   bruto, e o Smart Bidding passa a otimizar lance para quem manda currículo, procura curso de
   enfermagem aeromédica ou quer passagem de linha aérea. Isso encarece o leilão comprando a
   audiência errada — e é justamente o oposto do que o plano de mídia está tentando corrigir.
3. **Descobrir na ligação não resolve.** Quando o comercial descobre, o clique já foi pago e o
   sinal errado já foi enviado ao Google. O prejuízo é de mídia, não de tempo do comercial.
4. **A automação de descarte já roda sobre esse campo** desde 25/03/2026 na LP de aeromédico
   (passagem aérea e currículo saem da planilha automaticamente). Remover o campo quebraria a
   única classificação automática que existe hoje.

**Como ficou, minimizando o atrito que o briefing queria evitar:**

- O campo vira a **etapa 1**, de **seleção única e sem digitação** — a etapa mais barata do
  formulário em esforço.
- Vem **primeiro**, para que quem não é lead pare antes de investir tempo e antes de disparar
  conversão.
- Os formulários passam de 6 para **7 etapas**. É uma etapa a mais de toque, nenhuma a mais de
  digitação.
- **Está fora do teste A/B do formulário.** Se algum teste precisar encurtar, o primeiro campo a
  sair é o e-mail, não este.
- Os outros três campos que o briefing mandava cortar **saem mesmo**: "como podemos te ajudar"
  (texto aberto), e a duplicidade origem/cidade de origem.

**Regra de ouro que sai daqui, e que vale para a implementação inteira:**

> **Só dispara conversão no Google Ads quem termina o formulário com finalidade classificada como
> MQL.** Descarte não converte. Lead marcado como `revisar` ou `passeio` vai para o comercial mas
> não conta como conversão até a classificação ser confirmada.

Detalhamento por página: seção 3.1 de cada arquivo de copy. Telas de descarte: seção 3.2 das
LPs A e B.

**Pendência aberta:** o `briefing-lps-copy-design.md` continua com a instrução antiga na seção 5 e
no checklist da seção 9. Ou corrigimos o briefing, ou este documento passa a valer como errata —
mas as duas versões não podem circular soltas com o designer e o gestor de tráfego.

---

## 1. Como os pedidos da Ana (31/07, grupo UNIAIR + V4) foram atendidos

| Pedido da Ana | Onde entrou |
|---|---|
| Remover menus, links e rotas de fuga | Todas as LPs: barra superior sem menu, rodapé sem link institucional |
| Reformular a primeira dobra com proposta de valor objetiva | H1 + subheadline + linha de prova, com termo-cabeça literal |
| Remover o pop-up "Conheça o King Air" | LP A, nota de implementação — o pop-up sai; a frota vira seção |
| Substituir banner rotativo por comunicação fixa | Todas — hero estático |
| Revisar o formulário, reduzir etapas, incluir data de retorno e nº de passageiros | LP A, etapa 7 agrupa data de ida, data de retorno (opcional) e passageiros |
| Deixar "Táxi Aéreo Executivo" pré-selecionado | **Atendido em parte** — a opção vem primeira e destacada na etapa 1, mas exige o toque. Pré-seleção com avanço automático anularia o filtro de finalidade (ver seção 0). Levar para a homologação com ela. |
| Elementos de confiança **antes** do formulário | Linha de prova no hero + bloco "Os motivos para confiar não ficam no rodapé" |
| Depoimentos de clientes executivos/empresariais | LP A, seção 9 — os dois da referência dela + pedido de mais dois |
| Padronizar CTA como "Solicitar cotação de voo" | LP A adota literalmente; B e C usam a variante do serviço |
| Rastreabilidade de forms, cliques em WhatsApp e ligações com UTM/GCLID | Notas de implementação das três LPs |
| Fotos reais das aeronaves | LP A seção 6 e LP B seção 7 — sem banco de imagens |
| Homologação antes de publicar + confirmação da URL final por campanha | Este documento, seção 5 |

**Um ponto de tensão resolvido, para ficar registrado:** a Ana pediu data de retorno e número de
passageiros; o briefing limita o formulário a 6 campos. A solução foi agrupar os três dados
(ida, volta opcional, passageiros) numa **única etapa**. Com a etapa de finalidade (seção 0), o
formulário da LP A fecha em **7 etapas** — uma de toque e seis de preenchimento. Se na homologação
a Ana quiser separar datas e passageiros, vira etapa 8, mas aí é preciso medir a queda: por isso o
evento por etapa é obrigatório.

---

## 2. Bloqueios — não publicar sem resposta

| # | Pendência | Quem responde | Trava o quê |
|---|---|---|---|
| 1 | **Prazo de retorno da cotação** ("em até X horas") | comercial (Ana/Dani) | Bloco de prazo da LP C; FAQ 2 da LP A; confirmações das três |
| 2 | **"Zero acidentes"** — pode ser mantido? | Dani/Ana | Bloco de confiança da LP A |
| 3 | **FlightSafety, SGSO, AVSEC** — redação e vigência | Dani/Ana | Checklist de confiança da LP A |
| 4 | **"desde 1997" vs "28 anos" vs "29 anos"** | Ana | Linha de prova das três LPs |
| 5 | **Plano de saúde / convênio / seguradora** | Dani | FAQ 8 da LP B, FAQ 5 da LP C |
| 6 | **Formas de pagamento** | Dani/Ana | FAQ 4 da LP C |
| 7 | **Itens inclusos na cotação** — todos entram em toda proposta? | comercial | Seção 5 da LP C (é a lista que o cliente usa para comparar propostas) |
| 8 | **Equipamento embarcado** — a lista reflete todas as aeronaves? | coordenação assistencial | Seção 7 da LP B |
| 9 | **Incubadora de transporte neonatal** — é própria e padrão? | coordenação assistencial | Seção 8.1 da LP B |
| 10 | **"Não intermediamos voos de terceiros"** — é verdade em qualquer demanda? | Dani/Ana | Seção 6 da LP A |
| 11 | **Vínculo com Sistema Unimed-RS** é atual? | Dani | Não usado em nenhuma LP até confirmar (há demanda de busca real) |
| 12 | **Lista das 47 cidades perdidas por GEO** | Ana/Dani | Não trava LP; trava o recorte de segmentação (briefing de tráfego, seção 8) |
| 13 | **E-mail ou canal de RH** para a tela de descarte de currículo | Ana | Telas 3.2-B das LPs A e B — sem isso a tela fecha sem destino |
| 14 | **"Passeio aéreo" é demanda aproveitável?** (8 conv. a R$ 30 de CPA na campanha de marca) | Ana/Dani | Opção de finalidade da LP A: descartar, contar como MQL ou manter só marcada |

Sem resposta em 1, 2, 3 e 4 as páginas ainda sobem — cada item tem redação alternativa segura
marcada nos arquivos. Os itens 5, 6, 7, 8, 9 e 10 **saem da página** se não houver confirmação;
nenhum deles é inventado ou arredondado.

---

## 3. Regras que valem para as três páginas

**Nunca escrever:**
- "jato" ou "jatinho" — a frota é turboélice e helicóptero, inclusive em `alt` de imagem
- qualquer preço, valor ou "a partir de"
- promessa de tempo operacional ("chegamos em X horas") — prazo de **cotação**, sim, quando confirmado
- convênio, plano de saúde, seguradora, operadora ou licitação sem validação da Dani
- "agendar voo" como CTA

**Sempre:**
- termo-cabeça literal no H1 (`táxi aéreo` / `transporte aeromédico` / `UTI aérea`)
- formulário visível no hero, em etapas, sem pop-up: **etapa 1 de finalidade (toque) + 6 etapas de
  preenchimento**
- conversão no Google Ads só para finalidade classificada como MQL
- um CTA principal por página, repetido — exceção: telefone em paralelo nas LPs B e C
- frota conforme a seção 6 do briefing: 2× AS350 B2 (5 pax), C90 SE (5), C90 GTI (6),
  B200GT (8), B260 (8)
- bases: Salgado Filho (POA/RS) e Governador José Richa (Londrina/PR)
- contatos: (51) 2121-1100 · WhatsApp (51) 99275-7845 · 0800 519 5190 · comercial@uniair.com.br

**Tom:** LP A é sóbria e corporativa, pode respirar. LPs B e C são institucionais e clínicas —
sem estética de campanha promocional, sem cor de urgência, sem escassez.

---

## 4. Mapa de destino das campanhas (Fase 3 do briefing de tráfego)

| Grupo de anúncios | LP | Conversão |
|---|---|---|
| `taxiaereo` | A — Táxi aéreo executivo | `LP_A_taxi_aereo_form` |
| `aeromedico_geral`, `ambulancia_resgate` | B — Transporte aeromédico | `LP_B_aeromedico_form` |
| `uti_aerea`, `uti_helicoptero` | C — UTI aérea | `LP_C_uti_aerea_form` |
| marca | A ou institucional, conforme o termo | — |

Palavras novas de preço e as B2B só entram **depois** das páginas no ar. Subir antes repete o erro
que criou o IQ 3,55.

---

## 5. Checklist antes de publicar

- [ ] H1 contém, literalmente, o termo-cabeça da LP
- [ ] CTA fala em cotação/orçamento, nunca em agendamento
- [ ] Formulário visível no hero, sem pop-up, em etapas com barra de progresso: finalidade + 6 campos
- [ ] Etapa 1 (finalidade) presente nas três LPs, com as opções de descarte e as telas da seção 3.2
- [ ] Descarte **não** dispara conversão no Google Ads; eventos internos de descarte registrados
- [ ] Roteamento no Kommo por finalidade (executivo / aeromédico / B2B / revisar) funcionando
- [ ] Objeção nº 1 respondida: preço em A e C, "isso serve pro meu caso?" em B
- [ ] Nenhuma menção a jato
- [ ] Nenhum valor ou "a partir de"
- [ ] Nada sobre convênio, seguradora ou licitação sem validação
- [ ] Dados de frota conferem com a seção 6 do briefing
- [ ] Vídeo com carregamento adiado (thumbnail + play), imagens em WebP
- [ ] LCP abaixo de 2,5s no mobile 4G
- [ ] Conversão própria por LP configurada
- [ ] UTMs (`source/medium/campaign/term/content`) e `gclid` preservados até o Kommo
- [ ] Eventos por etapa do formulário disparando
- [ ] Cliques em telefone, 0800 e WhatsApp rastreados
- [ ] Pendências bloqueantes da seção 2 respondidas ou removidas da página
- [ ] **Versão de homologação enviada para a Ana conferir, com a URL final de cada campanha**
      (pedido explícito dela em 31/07)

---

## 6. Como saberemos se funcionou

Não é opinião sobre layout. É o relatório de palavras-chave do Google Ads, coluna
**"Exp. na página de destino"**, 30 dias depois da publicação.

| indicador | hoje | alvo |
|---|---|---|
| Investimento em página "Abaixo da média"/"Não relevante" | 93,0% | abaixo de 50% |
| IQ ponderado do aeromédico | 3,55 | acima de 5 |
| CPA MQL do aeromédico | R$ 705 | abaixo de R$ 400 |
