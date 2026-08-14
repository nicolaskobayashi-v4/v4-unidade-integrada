# Copy — LP C · UTI aérea (intenção de preço)

**Cliente:** Uniair · **Data:** 2026-08-07 · **Para:** design + implementação
**Base:** `briefings/2026-08-07-briefing-lps-copy-design.md` (seções 4-LP C, 5, 6, 7) +
`concorrencia-google-ads/2026-08-07-mapeamento-voeuniair.md`.

**Termo-cabeça:** `UTI aérea` — literal no H1, e o H1 endereça preço.
**Objeção nº 1:** preço, declarado na própria busca.
**CTA único:** `Solicitar cotação de UTI aérea`.

> ## Por que esta é a página mais importante do lote
> Gastamos R$ 2.052 no período em palavras de preço (`uti aérea preço`, `uti aérea valor`,
> `preço de uti aerea`, `valor de uti aerea`, `avião uti valor`) com **zero conversões** — porque
> todo esse tráfego caía numa página que não fala de preço em lugar nenhum. É também exatamente
> onde o segundo anunciante se posicionou em 18/07, com os anúncios "Cotação UTI Aérea", "Quanto
> Custa UTI Aérea" e "Preço Transporte Aeromédico".
>
> Quem chega aqui já decidiu que precisa de UTI aérea. É o lead mais quente do funil inteiro.

> ## A regra difícil desta página
> Ela **tem que falar de preço sem publicar preço.** Nada de tabela, nada de "a partir de", nada
> de faixa de valor. O que a página entrega é: **o que faz o valor variar**, **o que está incluso**
> e **em quanto tempo a cotação chega**. É isso que a página concorrente faz, e é por isso que ela
> ganha essa palavra.

> Mesmo tom institucional e clínico da LP B: sem gatilho comercial, sem escassez, sem exclamação.
> Itens `[CONFIRMAR: ...]` não vão ao ar sem resposta do cliente.

---

## 0. Metadados

**Title (59 car.):** UTI Aérea: Quanto Custa e Como Solicitar a Cotação — UniAir
**Meta description (154 car.):** Entenda o que define o valor de uma UTI aérea e o que está incluso na cotação. Informe os dados da remoção e receba o orçamento da UniAir. Atendimento 24h.
**URL sugerida:** `taxiaereo.uniair.com.br/uti-aerea`
**Nome da conversão (Google Ads):** `LP_C_uti_aerea_form`
**Grupos de anúncio que apontam para cá:** `uti_aerea`, `uti_helicoptero`

---

## 1. Barra superior (fixa, sem menu)

```
UniAir · UTI Aérea                    Atendimento 24 horas
                                      0800 519 5190 [clicável] · WhatsApp [clicável]
```

---

## 2. Hero (primeira dobra)

**Sobretítulo:**
> Remoção aeromédica com suporte intensivo · Operação 24 horas

**H1:**
> # UTI aérea: quanto custa e como solicitar sua cotação

**Subheadline:**
> O valor de uma UTI aérea depende da rota, da aeronave e do suporte clínico que o paciente
> precisa — por isso não existe tabela no setor. Informe os dados da remoção e a nossa equipe
> retorna com o orçamento fechado.

**Contato imediato:**
> **Prefere falar direto?** 📞 **0800 519 5190** · 💬 **WhatsApp (51) 99275-7845** — 24 horas.

**Linha de prova:**
> Desde 1997 · Frota própria · Equipe assistencial embarcada · Cotação sem compromisso
`[CONFIRMAR: padronizar "desde 1997" / "28 anos" / "29 anos"]`

**H1 alternativo para teste A/B** (mantém termo + preço):
- B: `UTI aérea: entenda o valor e receba a cotação da sua remoção`

---

## 3. Formulário do hero (visível, sem popup)

**Título:**
> ## Receba a cotação da sua UTI aérea

**Apoio:**
> São 7 perguntas. Com origem, destino e data a equipe já monta o orçamento.
> `[CONFIRMAR: acrescentar aqui o prazo de retorno, quando o comercial confirmar. Ex.: "Retorno em
> até X horas."]`

### Etapas (uma pergunta por tela, "1 de 7")

| # | Rótulo | Pergunta / placeholder | Tipo |
|---|---|---|---|
| **1** | **Finalidade** | **"Para qual situação você precisa da cotação?"** *(opções na seção 3.1)* | **seleção única, sem digitação** |
| 2 | Nome | "Para começar, como podemos te chamar?" · *Seu nome* | texto |
| 3 | WhatsApp | "{nome}, qual o WhatsApp para enviarmos a cotação?" · *(00) 00000-0000* | telefone |
| 4 | E-mail | "E o seu e-mail, para enviarmos o orçamento por escrito?" · *seu@email.com* | e-mail |
| 5 | Origem | "De qual cidade e estado o paciente sairá?" · *Cidade e estado · hospital, se souber* | texto |
| 6 | Destino | "Para qual cidade e estado ele precisa ser levado?" · *Cidade e estado · hospital de destino* | texto |
| 7 | Quando | "Quando o transporte precisa acontecer?" · *Hoje · Amanhã · Nos próximos dias · Ainda a definir* | seletor |

**Botão:**
> [ Solicitar cotação de UTI aérea ]

**Microcopy:**
> 🔒 Cotação sem compromisso. Seus dados são usados apenas para o retorno da equipe.

**Tela de confirmação:**
> ### Solicitação recebida, {nome}.
> Nossa equipe está montando o orçamento da remoção de **{origem}** para **{destino}** e retorna
> pelo WhatsApp **{whatsapp}**. `[CONFIRMAR: prazo]`
>
> **Se o caso for urgente, ligue: 0800 519 5190** — atendimento 24 horas.
>
> [ Continuar no WhatsApp ]

---

## 3.1 Etapa 1 — Finalidade (campo de qualificação)

> **Correção ao briefing** — mesma justificativa da LP A, seção 3.1. O campo "motivo do contato"
> não sai: é ele que sustenta a classificação de **MQL** enviada ao Google Ads. **Obrigatório e
> fora do teste A/B.**

Nesta página o campo tem um uso extra: separar **quem está cotando uma remoção real** de **quem
está pesquisando valor por curiosidade ou para comparação futura**. As duas são intenções
legítimas, mas só a primeira é lead de agora — e a segunda precisa de outro tratamento comercial.

**Pergunta:**
> ### Para qual situação você precisa da cotação?

**Opções (nesta ordem):**

| Opção exibida | Classificação | O que acontece |
|---|---|---|
| **Tenho uma remoção para fazer agora** | **MQL — quente** | segue para a etapa 2; prioridade no retorno |
| **Estou levantando valores para uma remoção provável** | **MQL** | segue o formulário |
| **Sou profissional de saúde ou represento um hospital** | **MQL — B2B** | segue o formulário; roteamento próprio no Kommo |
| Preciso de fretamento de voo executivo | **MQL — outro serviço** | segue o formulário, vocabulário de táxi aéreo |
| Traslado de corpo | **descarte** | tela 3.2-A da LP B (mesmo texto) |
| Trabalhar na UniAir, curso ou formação | **descarte** | tela 3.2-B da LP B (mesmo texto) |
| Outro assunto | **revisar** | segue o formulário, marcado `revisar`; não conta como MQL |

**Sobre a segunda opção:** não descartar quem está "só pesquisando". Esta LP recebe as palavras de
preço — pesquisa de valor é exatamente a intenção que estamos comprando, e o comercial pediu volume
nessa frente. O que muda é a prioridade da fila, não a existência do lead.

**Telas de descarte:** idênticas às da LP B (seção 3.2 daquele arquivo). Mesmos eventos:
`form_descarte_traslado`, `form_descarte_curriculo`. Nenhuma conversão enviada ao Google Ads.

---

## 4. "O que define o valor de uma UTI aérea" — o coração da página

Este bloco entra **imediatamente após o hero**. É a resposta literal à pergunta que a pessoa
digitou no Google. Se ela precisar rolar muito para chegar aqui, a página falhou.

**Sobretítulo:** A resposta direta
**H2:**
> ## O que define o valor de uma UTI aérea

**Abertura:**
> Duas remoções com a mesma distância podem custar valores diferentes. O orçamento é montado sobre
> seis variáveis — e é por isso que a cotação é rápida: são poucos dados para fechar a conta.

**As seis variáveis:**

1. **Distância e tempo de voo**
   A base do cálculo. Entra também o trecho de posicionamento da aeronave até a cidade de embarque,
   quando ela não está baseada lá.

2. **Aeronave necessária**
   Um helicóptero atende trajetos curtos e locais sem aeroporto; um King Air atende distâncias
   maiores, com mais autonomia e espaço para equipamento. A escolha depende da rota e do quadro do
   paciente — e muda o custo.

3. **Suporte clínico que o paciente exige**
   Um paciente estável em transferência programada e um paciente em ventilação mecânica com drogas
   vasoativas demandam equipe e equipamento diferentes. Isso pesa no orçamento.

4. **Ambulância em solo nas duas pontas**
   A remoção é porta a porta: do leito de origem até a aeronave, e da aeronave até o leito de
   destino. As duas ambulâncias fazem parte da operação e entram na composição do valor.

5. **Horário e prazo**
   Uma remoção programada com alguns dias de antecedência e uma remoção acionada de madrugada têm
   composições diferentes de tripulação e disponibilidade.

6. **Aeroportos envolvidos**
   Tarifas aeroportuárias, apoio em solo e a janela de operação do aeroporto de destino entram na
   conta final.

**Fecho do bloco:**
> Não publicamos tabela porque nenhuma tabela descreveria honestamente essas seis variáveis — e
> porque um número genérico levaria você a comparar coisas diferentes. O que fazemos é o oposto:
> a cotação chega com o valor fechado e a discriminação do que está incluído.
>
> [ Solicitar cotação de UTI aérea ]

---

## 5. "O que está incluso na cotação"

Este bloco existe para desmontar a comparação injusta: quem cota só a aeronave apresenta um número
menor e perde o resto no caminho. É argumento comercial legítimo e verificável.

**Sobretítulo:** Comparando propostas
**H2:**
> ## O que está incluso na cotação da UniAir

**Abertura:**
> Se você está comparando orçamentos, confira item a item o que cada um inclui. Propostas que
> parecem mais baratas às vezes cobrem só o voo — e o restante aparece depois.

**A nossa cotação inclui:**
- Aeronave própria, com tripulação (piloto e copiloto)
- Equipe assistencial embarcada — médico e enfermeiro com formação em transporte aeromédico
- Estrutura de UTI a bordo: ventilador de transporte, monitor multiparamétrico, bombas de infusão,
  oxigênio, desfibrilador e medicações de emergência
- Ambulância de apoio no hospital de origem e no hospital de destino
- Coordenação com os hospitais das duas pontas e autorizações de voo
- Combustível e tarifas aeroportuárias

`[CONFIRMAR com o comercial: todos estes itens entram em toda proposta, sem exceção? Qualquer item
que seja opcional ou cobrado à parte precisa sair desta lista ou ser marcado como opcional. Esta é
uma lista que o cliente vai usar para comparar propostas — não pode ter surpresa depois.]`

**Fecho:**
> Um acompanhante costuma poder viajar junto. A confirmação depende da aeronave, do peso total e do
> equipamento embarcado, e é feita na avaliação do caso.

---

## 6. Prazo de retorno da cotação

**H2:**
> ## Em quanto tempo a cotação chega

> `[BLOQUEADO ATÉ CONFIRMAÇÃO DO COMERCIAL. Este bloco só existe com um prazo real e sustentável —
> prometer prazo de cotação e não cumprir custa mais do que não prometer.]`
>
> **Redação para quando o prazo for confirmado:**
> "Solicitações recebidas pelo formulário são respondidas em até **[X] horas**. Casos urgentes
> acionados pelo 0800 519 5190 são avaliados na hora — o atendimento é 24 horas, todos os dias."
>
> **Redação provisória, se o prazo não for confirmado a tempo:**
> "Nosso atendimento funciona 24 horas. Assim que a solicitação chega, a equipe avalia a
> viabilidade da rota e retorna com o orçamento pelo WhatsApp informado. Se o caso for urgente,
> ligue no 0800 519 5190 — a avaliação é imediata."

> ⚠️ Este prazo é de **retorno da cotação**, nunca de execução da remoção. A página não pode conter
> nenhuma promessa de tempo operacional ("chegamos em X horas").

---

## 7. Seção helicóptero UTI

Existe demanda real de busca (`helicoptero uti`, `helicóptero uti preço`, `helicoptero uti movel`,
`helicóptero médico` — grupo `uti_helicoptero`, R$ 243 no período).

**Sobretítulo:** Quando o avião não é a melhor opção
**H2:**
> ## Helicóptero UTI: quando é indicado e como afeta o valor

> O helicóptero atende bem o que o avião não alcança: **trajetos curtos** e **locais sem
> aeroporto**. Ele pousa em heliponto ou em área autorizada, o que elimina os deslocamentos
> terrestres nas pontas e encurta o tempo total da remoção.
>
> **Como isso muda o orçamento:** em distâncias curtas, o helicóptero costuma ser a solução mais
> direta, porque tira duas ambulâncias da operação. Em distâncias maiores, o avião turboélice tem
> mais autonomia e velocidade, e acaba sendo a escolha adequada — inclusive em custo.
>
> A UniAir opera **dois helicópteros Airbus AS350 B2**, além da frota King Air. A definição da
> aeronave é feita na avaliação da rota e do quadro clínico — você não precisa escolher: informe os
> dados e a equipe indica a opção adequada.

---

## 8. Estrutura e equipe (versão curta)

**H2:**
> ## A UTI que embarca com o paciente

> A aeronave é configurada como uma unidade de terapia intensiva: maca com fixação aeronáutica,
> ventilador mecânico de transporte, monitor multiparamétrico, bombas de infusão, oxigênio,
> desfibrilador e medicações de emergência. O paciente segue monitorado do embarque ao desembarque,
> sem interrupção de suporte.
>
> A equipe tem formação em **fisiologia aeroespacial** — voo altera pressão e oxigenação, e isso
> muda o manejo do paciente em relação a um transporte terrestre.
>
> Frota própria: aviões turboélice **King Air** (B260 e B200GT, até 8 passageiros; C90 GTI, até 6;
> C90 SE, até 5) e helicópteros **Airbus AS350 B2**, até 5.
> Bases em **Porto Alegre (Salgado Filho)** e **Londrina (Governador José Richa)**.

> ⚠️ **Nunca escrever "jato" ou "jatinho".**

*Detalhamento completo da estrutura embarcada fica na LP B — link contextual: [Entenda como funciona
o transporte aeromédico].*

---

## 9. FAQ de preço

Este FAQ é o de maior valor de SEO/AEO da página: são as perguntas literais que as pessoas digitam.
Marcar com `FAQPage` schema.

**H2:**
> ## Perguntas frequentes sobre o valor da UTI aérea

**1. Quanto custa uma UTI aérea?**
> Não existe valor único. O orçamento é formado por distância, aeronave, suporte clínico
> necessário, ambulâncias nas duas pontas, horário e tarifas aeroportuárias. Com origem, destino e
> data em mãos, a nossa equipe monta a cotação com o valor fechado. É o que este formulário faz.

**2. Por que ninguém publica o preço de UTI aérea?**
> Porque um número publicado só seria honesto para uma rota específica, com uma aeronave
> específica e um quadro clínico específico. Qualquer valor genérico levaria você a comparar
> propostas que não são comparáveis. Preferimos explicar como o valor se forma e enviar o número
> real da sua remoção.

**3. O que está incluído no valor?**
> Aeronave e tripulação, equipe assistencial embarcada, estrutura de UTI, ambulância no hospital de
> origem e no de destino, coordenação com os dois hospitais, autorizações de voo, combustível e
> tarifas aeroportuárias. `[CONFIRMAR conforme seção 5.]`

**4. Como funciona o pagamento?**
> `[CONFIRMAR com Dani/Ana: formas de pagamento aceitas, se há parcelamento, se há adiantamento.
> Não publicar nada sobre pagamento antes dessa confirmação — sem isso o bloco sai da página.]`

**5. O plano de saúde cobre a UTI aérea?**
> `[BLOQUEADO — nada sobre convênio, plano ou seguradora antes da confirmação da Dani. Redação
> segura provisória, sujeita a aprovação: "A cobertura depende do contrato de cada paciente. A
> nossa equipe informa quais documentos costumam ser solicitados e orienta o processo."]`

**6. Qual a diferença entre UTI aérea e ambulância aérea?**
> Na prática, são o mesmo serviço com nomes diferentes. "UTI aérea" enfatiza a estrutura de terapia
> intensiva embarcada; "ambulância aérea" é o termo popular para a aeronave que faz a remoção. Nos
> dois casos, o que importa é o que vai a bordo: equipamento, equipe e suporte contínuo.

**7. Vale mais a pena que a UTI móvel terrestre?**
> Depende da distância e do quadro. Em trajetos curtos com paciente estável, a ambulância terrestre
> resolve bem e custa menos. Em distâncias longas ou com paciente que não tolera horas de estrada,
> o transporte aéreo reduz a exposição ao deslocamento. A nossa equipe diz com franqueza quando o
> aéreo não é necessário.

**8. Preciso pagar algo para receber a cotação?**
> Não. A cotação é gratuita e sem compromisso.

**9. Atendem qualquer cidade do Brasil?**
> A frota opera em todo o território nacional a partir das bases de Porto Alegre e Londrina.
> Cidades sem aeroporto são atendidas por helicóptero ou por ambulância de apoio até o aeroporto
> mais próximo, conforme a avaliação da rota.

---

## 10. Fechamento

**H2:**
> ## Receba a cotação da sua remoção

**Apoio:**
> Informe origem, destino e data. A equipe avalia a rota e retorna com o orçamento fechado.
> Sem compromisso.

> [ Solicitar cotação de UTI aérea ]
>
> 📞 **0800 519 5190** · 💬 **WhatsApp (51) 99275-7845**
> 📞 (51) 2121-1100 · ✉️ comercial@uniair.com.br
> Atendimento 24 horas, todos os dias.

**Rodapé:**
> UniAir Transporte Aeromédico · Bases: Aeroporto Salgado Filho (Porto Alegre/RS) e Aeroporto
> Governador José Richa (Londrina/PR)
> *(sem menu, sem rota de fuga; apenas política de privacidade)*

---

## 11. Notas de implementação

- O bloco "O que define o valor" é o segundo elemento da página. **Não empurrar para baixo** por
  causa de bloco institucional ou vídeo.
- Mesmo tratamento visual da LP B: institucional e clínico. Sem cor de urgência, sem selo, sem
  contagem regressiva.
- FAQ com marcação `FAQPage` — esta página tem chance real em busca orgânica e em resposta de IA
  para "quanto custa uti aérea".
- Considerar publicar `llms.txt` no domínio (o segundo anunciante já fez; é barato e essa página é
  a candidata natural).
- Formulário em etapas com teste A/B possível contra formulário único. **A etapa 1 (finalidade)
  fica fora do teste.**
- Eventos por etapa (`form_step_1` … `form_step_7`), eventos de descarte e cliques em telefone,
  0800 e WhatsApp.
- **Conversão enviada ao Google Ads apenas para finalidade classificada como MQL.**
- Conversão distinta (`LP_C_uti_aerea_form`). UTMs e `gclid` preservados até o Kommo.
- Palavras de preço só entram em correspondência exata **depois** desta página no ar — antes disso
  repetiríamos o erro que criou o IQ 3,55.
