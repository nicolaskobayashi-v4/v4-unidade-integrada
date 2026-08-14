# Briefing — reestruturação das campanhas Uniair (gestor de tráfego)

**Cliente:** Uniair Transporte Aeromédico e Táxi Aéreo
**Data:** 2026-08-07
**Para:** gestor de tráfego
**Base:** relatório de palavras-chave com índice de qualidade (jun/1 – ago/6 2026, R$ 21.210,53),
auction insights do mesmo período, leads do Kommo e da base GrowthPack.
**Documento irmão:** `briefings/2026-08-07-briefing-lps-copy-design.md` (LPs novas). As fases 3 e 4
deste plano dependem daquelas páginas ficarem prontas. As fases 0, 1 e 2 não dependem de nada.

---

## 1. Diagnóstico

**O problema não é lance nem verba. É índice de qualidade, e dentro dele um componente só.**

| componente | ponderado por investimento |
|---|---|
| Relevância do anúncio | 66,5% em "Acima da média" |
| CTR esperado | 43,0% em "Acima da média" / 26,9% abaixo |
| **Exp. na página de destino** | **93,0% em "Abaixo da média" ou "Não relevante"** |

Por grupo de anúncios:

| grupo | IQ ponderado | CPC | investimento | conv. (MQL) | CPA |
|---|---|---|---|---|---|
| táxi aéreo | 6,66 | R$ 2,04 | R$ 4.856,52 | 69 | R$ 70,38 |
| marca | 7,06 | R$ 1,37 | R$ 4.369,04 | 62 | R$ 70,47 |
| aeromédico | **3,55** | R$ 2,85 | R$ 11.984,97 | 17 | **R$ 705,00** |

### Uma ressalva importante antes de qualquer corte

O CPA de R$ 705 do aeromédico **não é prova de desperdício**, porque o ticket não é o mesmo. Nos
negócios ganhos do Kommo, UTI aérea/remoção fecha em torno de **R$ 67,7 mil** e fretamento em torno
de **R$ 22,6 mil** — amostras pequenas (3 e 2 negócios com finalidade preenchida; 30 ganhos com
valor no total, ticket médio R$ 61 mil, mediana R$ 40,5 mil), mas a ordem de grandeza é clara: o
aeromédico vale cerca de 3× por venda.

**Portanto: não reduzir a verba do aeromédico.** O desperdício existe e é grande, mas ele é
identificável palavra por palavra — não no nível da campanha. Este documento corta no nível da
palavra e mantém o investimento.

### Contexto competitivo

Um segundo anunciante (`voeuniair.com.br`, mesma razão social da Uniair, conta Google Ads
diferente) aparece em **34 dos 37 dias** do auction insights. Com **impression share abaixo de 10%**
— contra nossos 26–36% — ele fica **acima de nós em 71,8% das disputas** (1–6/ago), subindo de
64,5% na primeira quinzena de julho. Ele compra menos leilão e ganha posição. Isso é Ad Rank, e
Ad Rank é o que este plano ataca.

Ele entrou no aeromédico em **18/07**, com anúncios de "Cotação UTI Aérea", "Quanto Custa UTI
Aérea" e "Preço Transporte Aeromédico" — exatamente as palavras onde nosso IQ é 3.

---

## 2. Os quatro problemas estruturais

**1. Duplicação massiva entre campanhas.**
**65 palavras aparecem em mais de uma campanha, envolvendo R$ 16.825 — 79% de todo o investimento.**
Exemplos:

| palavra | campanhas | custo total |
|---|---|---|
| `taxi aereo` | 3 | R$ 5.720,10 |
| `aeromedico` | 3 | R$ 2.428,93 |
| `transporte aeromedico` | 2 | R$ 2.012,25 |
| `voo particular` | 3 | R$ 1.233,47 |
| `uti aerea` | 3 | R$ 895,62 |

Efeito: a mesma palavra recebe IQ diferente em cada campanha (`uti aerea` tem 5, 3 e 3), o
histórico de conversão fica picado em três lugares e o Smart Bidding não aprende em nenhum. Com
17 conversões de aeromédico em dois meses divididas por três campanhas, nenhuma delas sai da fase
de aprendizado.

**2. A campanha "institucional/brand" não é de marca.**
Custo total R$ 4.369,04. Termos com "uniair" somam **R$ 651,74 — 15%**. Os outros 85% são genéricos
(`taxi aereo` R$ 2.120,75, `táxi aéreo helicóptero` R$ 625,38, `voo particular` R$ 513,88,
`passeio aereo` R$ 241,04). O CPA bonito de R$ 70 dessa campanha vem de tráfego genérico, não de
marca — e ela está competindo com as campanhas de táxi aéreo pelas mesmas buscas.

**3. Um grupo de anúncios para 109 intenções diferentes.**
O grupo `aeromedico` tem 109 palavras apontando para uma página só: `uti aérea são paulo`,
`ambulância aérea`, `resgate aereo`, `transporte de enfermos`, `aeromédica londrina`,
`helicoptero uti preço`. É a causa direta da nota de página baixa.

**4. Palavra de concorrente dentro da campanha de aeromédico.**
`lider taxi aereo` (R$ 1.016,97), `abaeté taxi aéreo` (R$ 151,66), `lider aviação` (R$ 64,90),
`aerovida taxi aereo` (R$ 66,52). Intenção de marca de terceiro misturada com intenção de serviço.

---

## 3. Fase 0 — cortes imediatos (esta semana, independe das LPs)

Ordem de execução. Nada aqui precisa de página nova.

**Pausar:**

| palavra | grupo | custo | conv. | motivo |
|---|---|---|---|---|
| `transporte de enfermos` | aeromedico | R$ 1.727,50 | 1 | três componentes "Não relevante", 653 cliques |
| `aeromedico` (ampla) | aeromedico | R$ 2.393,24 | 2 | IQ 3, CTR esperado abaixo da média |
| `uti aérea` (ampla) | aeromedico | R$ 128,68 | 0 | 60 cliques, IQ 3 |
| `lider aviação` | aeromedico | R$ 64,90 | 0 | marca de terceiro, sem conversão |

Subtotal parado: **R$ 4.314,32 no período, 3 conversões.** Equivale a 89% do orçamento inteiro do
grupo de táxi aéreo, que entrega 4× mais MQL.

**Remover as 70 palavras com status "Limitado: baixa qualidade"** — R$ 738,99 e 4 conversões no
período. O Google já praticamente não as exibe; elas só poluem a leitura da conta. Guardar a lista
antes de remover: várias voltam depois, com as LPs novas e em grupo certo.
Exceção: `lider taxi aereo` (IQ 1, mas 3 conversões e R$ 1.016,97) — **não remover, mover** para a
campanha de concorrentes na Fase 1.

**Criar as negativas de intenção errada** (todas as campanhas, lista compartilhada). Vêm dos motivos
de perda do Kommo, não de suposição:

- *Óbito/traslado* — 9 perdas: `traslado de corpo`, `translado`, `transporte de corpo`, `urna`,
  `esquife`, `funerária`, `funerario`
- *Emprego, curso e formação* — origem de boa parte das 31 perdas por DESCONHECIMENTO:
  `enfermagem aeromedica`, `médico aeronáutico`, `curso`, `faculdade`, `salário`, `vaga`,
  `trabalhe conosco`, `piloto`, `anac`, `habilitação`
- *Transporte terrestre* — 35 perdas por OUTRA FORMA DE TRANSPORTE: `ambulância terrestre`,
  `uti móvel` (sem "aérea"), `remoção terrestre`
- *Serviço público* — `samu`, `bombeiros`, `resgate bombeiros`
- *Passeio e lazer* — `passeio de helicóptero`, `sobrevoo`, `voo panorâmico`, `aula de voo`.
  **Atenção:** `passeio aereo` gerou 8 conversões a R$ 30 de CPA na campanha de marca. Antes de
  negativar, confirmar com Ana e Dani se esse tipo de demanda é aproveitável ou não. Se for, ela
  merece grupo próprio, não negativa.

---

## 4. Fase 1 — desduplicar e reorganizar (semana 1–2, independe das LPs)

**4.1 Consolidar as três campanhas de aeromédico em uma.**
Hoje: `PR, RS, SC e SP` (R$ 8.199,39 / CPA 745), `Demais Estados` (R$ 2.061,66 / CPA 515), `SP`
(R$ 1.723,92 / CPA 862 — CPC de R$ 9,91, o mais caro da conta).

Vira uma campanha única com **ajuste de lance por localização**. Motivo: a separação geográfica
está duplicando palavra em vez de separar intenção, e fragmentando 17 conversões em três
aprendizados que nunca convergem. Geografia é ajuste de lance, não campanha — exceto quando o
orçamento precisa ser blindado por região, o que não é o caso aqui.

**4.2 Mesma consolidação no táxi aéreo.**
`taxi aereo` está em três campanhas somando R$ 5.720,10. Uma palavra, uma campanha.

**4.3 Transformar a campanha de marca em campanha de marca de verdade.**
- Ficam só os termos com "uniair" + `voeuniair`, em **correspondência exata**, orçamento pequeno,
  lance para segurar 1ª posição. Defesa de marca não é canal de aquisição.
- `taxi aereo`, `táxi aéreo helicóptero`, `voo particular`, `passeio aereo` saem para as campanhas
  de serviço correspondentes.
- Manter `voeuniair` ativo. Custou R$ 0,96 no período e é a palavra que nos coloca na frente de
  quem busca o outro site.

**4.4 Criar campanha de concorrentes, separada e com orçamento próprio.**
Recebe `lider taxi aereo`, `abaeté taxi aéreo`, `lider aviação`, `aerovida taxi aereo` — hoje
misturados no aeromédico.

Adicionar os que o auction insights mostra disputando de verdade, em ordem de impression share:
`flapper` / `flyflapper` (16,5%), `sete táxi aéreo` (16,0%), `fly revo` (14,9%), `brasil vida`
(14,4%), `upstar aviation` (12,6%), `rima aviação`, `avantto`, `helimarket`, `vistajet`, `voe mtx`,
`prime you`, `táxi aéreo hércules`.

Correspondência de frase ou exata, nunca ampla — ampla em marca de terceiro traz busca institucional
do concorrente e queima verba. Enquanto não houver LP comparativa, mandar para a LP de serviço
correspondente e **não esperar CPA de campanha normal**: essa campanha se avalia por volume
incremental, não por CPA.

---

## 5. Fase 2 — corrigir CTR esperado (semana 2, independe das LPs)

26,9% do investimento está em palavras com CTR esperado abaixo da média, concentradas no aeromédico.
Isso é anúncio, não página — dá para resolver antes das LPs ficarem prontas.

Quebrar o grupo `aeromedico` em quatro, com anúncios próprios. Por enquanto todos apontam para a
página atual; os destinos definitivos entram na Fase 3.

| novo grupo | palavras (o que já existe na conta) | custo no período |
|---|---|---|
| `aeromedico_geral` | transporte aeromédico, aeromédico, transporte aeromédico + geo | R$ 5.502,07 |
| `uti_aerea` | uti aérea, uti aérea preço/valor, avião uti, avião uti valor, uti aérea + cidade | R$ 1.809,41 |
| `uti_helicoptero` | helicoptero uti, helicóptero uti preço, helicoptero uti movel, helicóptero médico | R$ 243,00 |
| `ambulancia_resgate` | ambulância aérea, avião ambulância, helicóptero ambulância, resgate aéreo, resgate aeromédico | R$ 814,69 |

Regra do anúncio: **Título 1 contém o termo-cabeça do grupo, literalmente.** Grupo `uti_aerea` tem
"UTI Aérea" no título 1. É a mesma regra que está no briefing de copy, e é o que corrige tanto CTR
esperado quanto relevância.

Sitelinks obrigatórios por grupo, espelhando intenção de cotação — é o que o outro anunciante faz e
é barato de replicar: "Solicitar Cotação", "Quanto Custa", "Atendimento 24h", "Como Funciona".

---

## 6. Fase 3 — quando as LPs subirem

Cada grupo passa a apontar para a sua página:

| grupo | destino |
|---|---|
| `aeromedico_geral`, `ambulancia_resgate` | LP B — Transporte aeromédico |
| `uti_aerea`, `uti_helicoptero` | LP C — UTI aérea (intenção de preço) |
| `taxiaereo` | LP A — Táxi aéreo executivo |
| marca | LP A ou institucional, conforme o termo |

Só depois disso entram as palavras novas da lista de expansão — as de preço no aeromédico
(`quanto custa uti aérea`, `preço transporte aeromédico`, `orçamento remoção aeromédica`) e as B2B
(`transporte aeromédico para hospitais`, `remoção inter-hospitalar aérea`). **Adicionar essas
palavras antes das páginas existirem repete o erro que criou o IQ 3,55.**

Nas palavras de preço, usar **correspondência exata**. Hoje a exata representa R$ 191,62 de
R$ 21.210 — está praticamente sem uso, e é o tipo certo para intenção transacional específica.

---

## 7. Sobre tipo de correspondência — não faça o corte óbvio

| grupo | correspondência | custo | conv. | CPA |
|---|---|---|---|---|
| taxiaereo | ampla | R$ 4.856,52 | 69 | **R$ 70,38** |
| aeromedico | ampla | R$ 7.689,35 | 11 | R$ 699,03 |
| aeromedico | de frase | R$ 4.247,15 | 6 | R$ 707,86 |
| brand | ampla | R$ 4.019,03 | 57 | R$ 70,51 |

A leitura preguiçosa seria "ampla está queimando dinheiro". **Está errada.** Ampla no táxi aéreo
entrega CPA de R$ 70. E no aeromédico, ampla e frase têm CPA praticamente idêntico (R$ 699 e R$ 708)
— ou seja, **o problema não é o tipo de correspondência, é o destino.** Trocar tudo para exata no
aeromédico mataria volume sem tocar na causa.

Manter ampla onde funciona. Usar exata nas palavras transacionais novas. Revisar frase no aeromédico
só depois das LPs, com número novo na mão.

---

## 8. Geografia — o item de maior retorno pendente

**`NÃO ATENDE GEO` é o 3º maior motivo de perda do Kommo: 47 leads.** São leads pagos, entregues ao
comercial, e descartados porque a operação não alcança a região.

Isso não se resolve com palavra-chave nem com página. Resolve-se com recorte de segmentação — e
**não temos os dados para fazer o recorte**: o campo Origem está quase todo vazio no export do
Kommo.

**Ação bloqueante:** pedir para Ana ou Dani a lista de cidades/estados desses 47 leads perdidos por
GEO. Com ela: excluir as regiões sem alcance e revisar o ajuste de lance por localização,
principalmente na campanha "Demais Estados" do aeromédico (R$ 2.061,66, CPA R$ 515), que é a
suspeita natural.

---

## 9. O que não fazer

- **Não reduzir a verba do aeromédico.** Ticket ~3× maior. O corte é por palavra, não por campanha.
- **Não subir palavra nova antes das LPs.** Herda página ruim e nasce com IQ baixo.
- **Não trocar tudo para exata.** Ver seção 7.
- **Não subir Performance Max agora.** Com a página classificada abaixo da média em 93% do
  investimento, PMax só espalha o mesmo problema por mais inventário — e tira a visibilidade de
  palavra-chave que este plano depende para medir.
- **Não mexer em mais de uma variável por semana.** Fase 0 e Fase 1 juntas já mudam duplicação e
  negativas; se o resultado mudar, precisamos saber por causa de quê.
- **Não tratar `voeuniair` como concorrente hostil na comunicação com o cliente.** É a mesma razão
  social da Uniair, em outra conta. Assunto do Lucas com a Dani, não do relatório de mídia.

---

## 10. Cronograma e critérios de aceite

| quando | o quê | depende de |
|---|---|---|
| Semana 1 | Fase 0 — pausas, remoções, negativas | nada |
| Semana 1–2 | Fase 1 — consolidação, marca, campanha de concorrentes | nada |
| Semana 2 | Fase 2 — quebra em 4 grupos + anúncios novos + sitelinks | nada |
| Bloqueado | Recorte geográfico | lista das 47 perdas por GEO |
| Semana 4+ | Fase 3 — destinos novos e palavras de expansão | LPs publicadas |

**Aceite, medido 30 dias após cada fase:**

| indicador | hoje | alvo |
|---|---|---|
| Investimento em página "Abaixo da média"/"Não relevante" | 93,0% | abaixo de 50% |
| IQ ponderado do aeromédico | 3,55 | acima de 5 |
| CPA MQL do aeromédico | R$ 705,00 | abaixo de R$ 400 |
| Palavras duplicadas entre campanhas | 65 (R$ 16.825) | zero |
| Taxa de posição superior do `voeuniair.com.br` sobre nós | 71,8% | abaixo de 55% |

O último indicador é o que responde a pergunta original do cliente. Ele sai do relatório de auction
insights e deve ser puxado junto com o de palavras-chave em toda revisão.
