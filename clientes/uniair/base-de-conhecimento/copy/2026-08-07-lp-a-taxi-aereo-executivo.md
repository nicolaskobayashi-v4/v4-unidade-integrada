# Copy — LP A · Táxi aéreo executivo

**Cliente:** Uniair · **Data:** 2026-08-07 · **Para:** design + implementação (GreatPages/GPages)
**Base:** `briefings/2026-08-07-briefing-lps-copy-design.md` (seções 4-LP A, 5, 6, 7) +
análise da Ana no grupo UNIAIR + V4 em 31/07/2026 + referência visual enviada por ela no mesmo dia.

**Termo-cabeça:** `táxi aéreo` — aparece literalmente no H1, no title e no primeiro parágrafo.
**Objeção nº 1 a derrubar:** preço (28 perdas "PREÇO" + 25 "CONCORRENTE" no Kommo).
**CTA único da página:** `Solicitar cotação de voo` — padronizado conforme pedido da Ana. Nunca "Agendar voo".

> Tudo que estiver entre `[CONFIRMAR: ...]` **não vai ao ar** antes da resposta do cliente.
> A lista consolidada está em `2026-08-07-decisoes-e-pendencias.md`.

---

## 0. Metadados

**Title (57 car.):** Táxi Aéreo Executivo | Cotação da Sua Rota — UniAir
**Meta description (152 car.):** Táxi aéreo executivo sob demanda, com frota própria e operação 24h. Informe origem, destino e data e receba a cotação da sua rota com a UniAir.
**URL sugerida:** `taxiaereo.uniair.com.br/taxi-aereo-executivo`
**Nome da conversão (Google Ads):** `LP_A_taxi_aereo_form`

---

## 1. Barra superior (fixa, sem menu)

Sem menu de navegação, sem links para o site institucional, sem banner rotativo — a página tem
uma saída só, que é a cotação (pedido explícito da Ana em 31/07).

```
UniAir · Táxi Aéreo Executivo          Atendimento 24h · (51) 2121-1100 [clicável]
                                       [ Solicitar cotação de voo ]
```

---

## 2. Hero (primeira dobra)

**Sobretítulo:**
> Voos particulares sob demanda · Brasil e exterior

**H1:**
> # Táxi aéreo executivo: informe sua rota e receba a cotação

**Subheadline:**
> Frota própria de aviões e helicópteros, tripulação completa e operação 24 horas. Você informa
> origem, destino e data — a equipe avalia a aeronave adequada e retorna com a proposta da sua rota.

**Linha de prova (chips, uma linha no mobile):**
> Desde 1997 · Frota própria · Piloto e copiloto em todas as operações · Atendimento 24h

`[CONFIRMAR: "desde 1997" vs. "28 anos" vs. "29 anos" — padronizar uma única forma em todas as LPs]`

**Alternativas de H1 aprovadas no briefing** (para teste A/B, mesma regra do termo literal):
- B: `Táxi aéreo sob demanda — orçamento para a sua rota`
- C: `Táxi aéreo executivo com frota própria: receba a cotação da sua rota`

---

## 3. Formulário do hero (visível, sem popup)

Fica **ao lado do H1 no desktop e logo abaixo dele no mobile**. Sem clique intermediário.
O pop-up "Conheça o King Air" sai da página (pedido da Ana em 31/07).

**Título do bloco:**
> ## Solicite sua cotação de voo

**Apoio:**
> São 7 perguntas rápidas. A equipe avalia a melhor aeronave para a rota e retorna com a proposta.

**Página de origem (campo oculto, não conta como campo):** `LP_A_taxi_aereo_executivo`

### Etapas (uma pergunta por tela, barra de progresso "1 de 7")

| # | Rótulo | Pergunta / placeholder | Tipo |
|---|---|---|---|
| **1** | **Finalidade do voo** | **"Sobre qual serviço você precisa de cotação?"** *(opções na seção 3.1)* | **seleção única, sem digitação** |
| 2 | Nome | "Para começar, como podemos te chamar?" · *Seu nome* | texto |
| 3 | WhatsApp | "Prazer, {nome}! Qual o WhatsApp para o nosso retorno?" · *(00) 00000-0000* | telefone |
| 4 | E-mail | "E o seu e-mail, para enviarmos a cotação por escrito?" · *nome@empresa.com.br* | e-mail |
| 5 | Origem | "De qual cidade vocês vão partir?" · *Cidade de embarque* | texto |
| 6 | Destino | "E para qual cidade?" · *Cidade de destino* | texto |
| 7 | Datas e passageiros | "Por último: quando o voo precisa acontecer?" · *Data de ida* · *Data de retorno (opcional)* · *Passageiros* | data + data + seletor |

**Sobre a etapa 7:** o briefing pede no máximo 6 campos; a Ana pediu data de retorno e número de
passageiros. Resolvido agrupando os três dados numa **única etapa** — a cotação já sai com o que o
comercial precisa para dimensionar a aeronave. Data de retorno é opcional (voo só de ida é comum).

**Sobre a etapa 1 — por que ela existe apesar do briefing:** ver seção 3.1. Em resumo, é o campo
que separa lead de currículo e de passagem de linha aérea **antes** de virar conversão no Google
Ads. Sem ele, otimizamos lance em cima de lead bruto.

**Botão:**
> [ Solicitar cotação de voo ]

**Microcopy abaixo do botão:**
> 🔒 Cotação sem compromisso. Seus dados são usados apenas para o retorno da equipe.

**Tela de confirmação:**
> ### Recebemos sua solicitação, {nome}.
> Nossa equipe comercial está avaliando a rota **{origem} → {destino}** e retorna com a proposta
> pelo WhatsApp **{whatsapp}** `[CONFIRMAR: prazo de retorno da cotação com o comercial — ex.: "em até X horas úteis". Sem confirmação, publicar sem prazo.]`
>
> Prefere adiantar? [ Continuar no WhatsApp ] · Ou ligue: (51) 2121-1100
>
> *Prazo de retorno da cotação. Não é prazo de execução do voo.*

**Mensagens de erro (uma por campo, direta):**
- Nome: "Precisamos de um nome para o retorno."
- WhatsApp: "Confira o número — é por ele que a proposta chega."
- E-mail: "Esse e-mail parece incompleto."
- Origem/Destino: "Informe a cidade."
- Data: "Escolha a data prevista. Se ainda não sabe, marque 'Ainda a definir'."

---

## 3.1 Etapa 1 — Finalidade do voo (campo de qualificação)

> **Correção ao briefing.** A seção 5 do briefing manda eliminar "qual o motivo do seu contato",
> classificando-o como campo de atrito que "o comercial descobre na primeira ligação de qualquer
> jeito". **Está errado**, e a razão não é comercial, é de mídia:
>
> - É desta resposta que sai a classificação de **MQL** que o relatório usa e que é enviada ao
>   Google Ads como conversão. Sem ela, a conversão vira **lead bruto**, e o Smart Bidding passa a
>   otimizar para currículo e para quem procura passagem de linha aérea.
> - A automação de descarte já roda em cima desse campo desde 25/03/2026 (LP de aeromédico).
>   Removê-lo não simplifica o formulário: quebra a única classificação automática que existe.
> - Descobrir na ligação resolve para o comercial e **não resolve para a campanha** — o lance já
>   foi dado e o sinal já foi enviado errado.
>
> Portanto: **a etapa 1 é obrigatória e não é candidata a corte no teste A/B do formulário.**
> Se algum teste precisar reduzir etapas, o primeiro campo a sair é o e-mail, não este.

**Formato:** seleção única, **sem digitação**, um toque. É a etapa mais barata do formulário em
esforço e a mais cara em informação. Vem **primeiro** justamente para que quem não é lead pare
antes de gastar tempo — e antes de disparar conversão.

**Pergunta:**
> ### Sobre qual serviço você precisa de cotação?

**Opções (nesta ordem):**

| Opção exibida | Classificação | O que acontece |
|---|---|---|
| **Fretamento de voo executivo (táxi aéreo)** | **MQL** | segue para a etapa 2 |
| **Transporte aeromédico ou remoção de paciente** | **MQL — outro serviço** | segue o formulário, com vocabulário aeromédico; entra no Kommo na pipeline de aeromédico |
| Voo panorâmico ou passeio aéreo | a definir | segue o formulário, marcado `passeio` — ver nota abaixo |
| Compra de passagem de voo comercial | **descarte** | tela 3.2-A, não gera lead para o comercial |
| Trabalhar na UniAir / enviar currículo | **descarte** | tela 3.2-B, não gera lead para o comercial |
| Outro assunto | **revisar** | segue o formulário, marcado `revisar`; vai para o comercial sem contar como MQL |

**Sobre a pré-seleção que a Ana pediu:** a opção de fretamento executivo vem **primeiro e com
destaque visual**, mas exige o toque. Pré-selecionar com avanço automático anularia o filtro —
todo mundo passaria como executivo e voltaríamos ao lead bruto. Levar esse ponto para a
homologação com ela.

**Sobre "passeio aéreo":** `passeio aereo` gerou 8 conversões a R$ 30 de CPA na campanha de marca.
Não descartar antes de a Ana e a Dani confirmarem se é demanda aproveitável — mesma pendência que
está na seção 3 do briefing de tráfego. Enquanto não houver resposta, o lead vai para o comercial
marcado, mas **não conta como MQL**.

**Sobre "Transporte aeromédico" nesta página:** não é erro do usuário, é rotina — em 26/03 um lead
preencheu o formulário da LP de táxi aéreo pedindo aeromédico. Não jogar essa pessoa para outra
página (perderíamos o lead): o formulário continua igual, só muda o vocabulário das etapas 5 e 6
("de qual cidade o paciente sairá?") e o roteamento no Kommo.

---

## 3.2 Telas de descarte

Descarte não é porta na cara. As duas telas abaixo educam — parte de quem procura "passagem" na
verdade não sabe o que é táxi aéreo e pode virar lead ao entender.

**3.2-A · Compra de passagem de voo comercial**
> ### A UniAir não vende passagens de voo comercial.
> Nós operamos **voos particulares fretados**: a aeronave inteira é reservada para você e para o
> seu grupo, com origem, destino e horário definidos por você — inclusive em aeroportos onde não
> existe voo de linha.
>
> Se for isso que você procura, é só voltar e pedir a cotação.
> [ Voltar e solicitar cotação ]
>
> Se você busca passagem de uma companhia aérea, procure diretamente a companhia ou uma agência
> de viagens.

**3.2-B · Trabalhar na UniAir / currículo**
> ### Vagas não são tratadas por este canal.
> Este formulário é do comercial de voos. Para trabalhar conosco, envie seu currículo para
> `[CONFIRMAR: e-mail ou canal de RH da Uniair]`.
>
> Obrigado pelo interesse.

**Nas duas telas:** nenhum dado é enviado ao comercial, nenhuma conversão é disparada ao Google
Ads. Registrar apenas um evento interno (`form_descarte_passagem`, `form_descarte_curriculo`) —
esse número é diagnóstico de campanha: se crescer, há palavra-chave ou anúncio atraindo intenção
errada, e a correção é negativa, não página.

---

## 4. Bloco "Como funciona a cotação"

**Sobretítulo:** Jornada simples
**H2:**
> ## Da solicitação ao embarque

| | | |
|---|---|---|
| **01 · Informe a rota** | **02 · Receba a proposta** | **03 · Confirme e embarque** |
| Origem, destino, datas e número de passageiros. Leva menos de um minuto. | A equipe avalia a aeronave adequada e a viabilidade operacional da rota e envia a proposta. | Com a confirmação, a UniAir coordena tripulação, autorizações e apoio em solo nas duas pontas. |

---

## 5. Bloco "Como o preço é formado" — o coração da página

Este é o bloco que responde à objeção nº 1. Ele não publica valor e não usa "a partir de".
Ele explica a **formação** do preço: quem entende por que o número é aquele aceita melhor o
valor, e quem não tem orçamento se desqualifica sozinho — sem consumir tempo do comercial.

**Sobretítulo:** Transparência
**H2:**
> ## Por que não existe tabela de preço em táxi aéreo — e o que define o valor da sua rota

**Texto de abertura:**
> Cada voo é um voo. Duas rotas com a mesma distância podem ter custos diferentes conforme a
> aeronave, o tempo de permanência e a estrutura do aeroporto. Por isso a proposta é montada
> caso a caso — e por isso ela chega rápido: são poucos dados para fechar a conta.

**Seis fatores (cards ou lista com ícone):**

1. **Rota e distância**
   O tempo de voo é a base do cálculo, e ele inclui o trecho de posicionamento da aeronave até a
   cidade de embarque quando ela não está baseada lá.

2. **Aeronave escolhida**
   Um helicóptero atende bem trajetos curtos e pousos fora de aeroporto; um King Air é indicado
   para distâncias maiores e mais passageiros. A escolha muda o custo e a duração da viagem.

3. **Número de passageiros e bagagem**
   Define a capacidade necessária e, em alguns casos, o modelo da aeronave.

4. **Tempo de espera em destino**
   Voo de ida e volta no mesmo dia com a aeronave aguardando tem custo diferente de dois trechos
   independentes.

5. **Pernoite de tripulação**
   Quando a operação atravessa o dia, entram hospedagem e diária da tripulação.

6. **Aeroporto, horário e taxas**
   Tarifas aeroportuárias, apoio em solo e a janela de operação do aeroporto de destino entram
   na composição final.

**Encerramento do bloco:**
> Informe a rota e a data: a proposta chega com o valor fechado, sem custo escondido depois.
>
> [ Solicitar cotação de voo ]

---

## 6. Bloco Frota

**Sobretítulo:** Aeronaves para cada perfil de missão
**H2:**
> ## Frota executiva própria

**Apoio:**
> Aeronaves próprias e tripuladas pela UniAir — não intermediamos voos de terceiros.

`[CONFIRMAR: a frase "não intermediamos voos de terceiros" só entra se a operação for 100% com aeronave própria em qualquer demanda. Se houver parceria em picos, trocar por "Frota própria, operada por tripulação UniAir."]`

| Aeronave | Capacidade | Perfil |
|---|---|---|
| **King Air B260** | Até 8 passageiros | Conforto e desempenho para rotas executivas de maior distância |
| **King Air B200GT** | Até 8 passageiros | Versatilidade para operações nacionais e internacionais |
| **King Air C90 GTI** | Até 6 passageiros | Agilidade para rotas regionais |
| **King Air C90 SE** | Até 5 passageiros | Trechos curtos e médios com custo otimizado |
| **Airbus AS350 B2** (2 unidades) | Até 5 passageiros | Trajetos curtos, acesso a helipontos e áreas sem aeroporto |

> ⚠️ **Regra de escrita:** a frota é de **aviões turboélice e helicópteros**. A palavra "jato"
> (ou "jatinho") não pode aparecer em lugar nenhum da página, nem em texto alternativo de imagem.

**Imagens:** fotos reais das aeronaves e do hangar (pedido explícito da Ana: "colocar fotos reais
das aeronaves"). Sem banco de imagens. WebP, `lazy` fora da primeira dobra.

---

## 7. Bloco Rotas mais atendidas

**Sobretítulo:** Onde mais voamos
**H2:**
> ## Rotas executivas mais solicitadas

**Apoio:**
> Operamos em todo o território nacional e em voos internacionais, com bases próprias em
> **Porto Alegre (Aeroporto Salgado Filho)** e **Londrina (Aeroporto Governador José Richa)**.

**Lista (chips):**
Porto Alegre · São Paulo · Ribeirão Preto · Rio de Janeiro · Caxias do Sul · Florianópolis

**Fecho:**
> Sua rota não está na lista? A maior parte das solicitações que recebemos é de trechos sob
> demanda — informe origem e destino e avaliamos a viabilidade.

---

## 8. Bloco Confiança

**Sobretítulo:** Segurança que pode ser comprovada
**H2:**
> ## Os motivos para confiar não ficam no rodapé

**Texto:**
> Quem contrata um voo particular está decidindo sobre segurança antes de decidir sobre preço.
> Por isso estes dados aparecem aqui, antes do formulário — e não no fim da página.

**Checklist:**
- Operação 24 horas, desde 1997
- Frota própria e hangar próprio
- Piloto e copiloto em todas as operações
- Treinamento de tripulação em FlightSafety `[CONFIRMAR: redação e vigência]`
- Programas de SGSO e AVSEC `[CONFIRMAR: redação]`
- Histórico de zero acidentes `[CONFIRMAR com Dani/Ana antes de publicar]`

*Os quatro últimos itens vieram da referência que a Ana montou em 31/07. São afirmações da própria
Uniair, mas como envolvem segurança de voo, vão para confirmação formal antes do ar.*

**Sub-bloco pilotos:**
> ### Conheça quem voa com você
> Tripulação própria, treinada e escalada pela UniAir.
> *(fotos e nomes dos pilotos — ativo que o cliente já tem e valoriza)*

---

## 9. Bloco Depoimentos

**Sobretítulo:** Experiências reais
**H2:**
> ## Quem voa, recomenda

> "Tudo como combinado, programação antecipada, tudo no horário e agilidade na interação pelo
> WhatsApp. Voo impecável."
> — **Carlos Henrique Garla** · Cliente UniAir

> "A UniAir foi uma parceira essencial para mobilizar equipes e manter a continuidade da nossa
> operação."
> — **Case corporativo** · Identificação mediante autorização

`[PEDIR: mais 2 depoimentos de clientes executivos/empresariais, com autorização de uso do nome ou
da empresa. A Ana pediu especificamente depoimentos "de clientes executivos e empresariais" — os
dois acima vieram da referência dela e devem ser confirmados como autorizados.]`

---

## 10. FAQ

**H2:**
> ## Perguntas frequentes sobre táxi aéreo

**1. Quanto custa um táxi aéreo?**
> O valor depende da rota, da aeronave, do número de passageiros, do tempo de permanência em
> destino e das taxas do aeroporto envolvido. Por isso não trabalhamos com tabela: a cotação é
> montada para a sua rota específica e enviada com o valor fechado. Informe origem, destino e
> data no formulário desta página para receber a sua.

**2. Em quanto tempo recebo o orçamento?**
> `[CONFIRMAR: prazo com o comercial. Enquanto não houver confirmação, publicar: "Assim que
> recebemos a solicitação, a equipe comercial avalia a viabilidade da rota e retorna pelo WhatsApp
> informado. Nosso atendimento funciona 24 horas."]`

**3. A UniAir atende aeroportos menores?**
> Sim. Boa parte das rotas executivas usa aeródromos regionais, que costumam ficar mais perto do
> destino final do que os grandes aeroportos. Para locais sem pista, o helicóptero permite pouso
> em heliponto ou área autorizada. A viabilidade é confirmada na análise da rota.

**4. E se a data mudar depois?**
> Alterações de data e horário são comuns em voo executivo e são tratadas diretamente com a
> equipe. Remarcações dependem de disponibilidade de aeronave e tripulação na nova data e podem
> alterar a composição do valor — a equipe informa antes de qualquer confirmação.

**5. Quantas pessoas cabem?**
> De 5 a 8 passageiros, conforme a aeronave. Os helicópteros AS350 B2 levam até 5; os King Air,
> de 5 a 8. Grupos maiores podem ser atendidos com mais de uma aeronave.

**6. Vocês voam para fora do Brasil?**
> Sim, a frota King Air opera voos internacionais. A análise da rota considera autorizações,
> paradas para reabastecimento e documentação necessária.

**7. Preciso chegar com quanta antecedência?**
> O embarque em terminal executivo dispensa fila e check-in convencional. A equipe informa o
> horário de apresentação junto com a confirmação do voo.

**8. A UniAir opera 24 horas?**
> Sim. O atendimento e a operação funcionam 24 horas, todos os dias.

---

## 11. Fechamento

**H2:**
> ## Pronto para planejar seu próximo voo?

**Apoio:**
> Receba a cotação personalizada conforme a sua rota, as suas datas e o número de passageiros.

> [ Solicitar cotação de voo ]

**Contatos diretos (abaixo do CTA, discretos):**
- Telefone: **(51) 2121-1100**
- WhatsApp: **(51) 99275-7845**
- E-mail: **comercial@uniair.com.br**

**Rodapé:**
> UniAir Táxi Aéreo · Bases: Aeroporto Salgado Filho (Porto Alegre/RS) e Aeroporto Governador
> José Richa (Londrina/PR) · Operação 24 horas
> *(sem link para o site institucional — nenhuma rota de fuga; apenas política de privacidade)*

---

## 12. Notas de implementação

- **Um único CTA na página**, repetido: hero, fim do bloco de preço, fechamento. Sem botão
  concorrente no hero.
- **Zero pop-ups.** O "Conheça o King Air" sai.
- **Sem banner rotativo** — comunicação fixa (pedido da Ana).
- Vídeo do YouTube, se houver, entra por **thumbnail estática com play**; o player só carrega no
  clique. Alvo de LCP: abaixo de 2,5s no 4G.
- O formulário em etapas é **hipótese de conversão, não certeza**: construir de forma que dê para
  testar A/B contra o formulário único. Não hardcodar. **A etapa 1 (finalidade) está fora do teste**
  — ela existe em qualquer variante, inclusive na de formulário único.
- Disparar evento por etapa concluída (`form_step_1` … `form_step_7`) para sabermos onde a pessoa
  desiste, e os eventos de descarte (`form_descarte_passagem`, `form_descarte_curriculo`).
- **Só dispara a conversão do Google Ads quem chega ao envio com finalidade classificada como MQL.**
  Descarte não converte. É isso que impede o Smart Bidding de aprender com currículo e passagem.
- Preservar `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content` e `gclid` do
  clique até o Kommo. Hoje funciona — não pode quebrar.
- Conversão distinta desta LP (`LP_A_taxi_aereo_form`), separada das LPs B e C.
- Clique no telefone e no WhatsApp também são eventos rastreados (a Ana já apontou em 06/05 que
  muita gente prefere o WhatsApp ao formulário).
