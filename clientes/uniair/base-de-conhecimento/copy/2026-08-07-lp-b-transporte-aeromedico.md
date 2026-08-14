# Copy — LP B · Transporte aeromédico (página-mãe)

**Cliente:** Uniair · **Data:** 2026-08-07 · **Para:** design + implementação
**Base:** `briefings/2026-08-07-briefing-lps-copy-design.md` (seções 4-LP B, 5, 6, 7).

**Termo-cabeça:** `transporte aeromédico` — literal no H1, no title e no primeiro parágrafo.
**Objeção nº 1 a derrubar:** desconhecimento (31 perdas "DESCONHECIMENTO" + 35 "OUTRA FORMA DE
TRANSPORTE" no Kommo). A pessoa não sabe se o transporte aéreo se aplica ao caso dela e acaba de
ambulância terrestre. **A página responde "isso serve para o meu caso?" antes de pedir qualquer dado.**
**CTA único:** `Solicitar cotação de transporte` — com telefone em paralelo no hero.

> ## Regra de tom desta página — vale para cada linha
> Quem chega aqui está com medo, com pressa, ou é um profissional de saúde resolvendo um problema.
> **Nada de linguagem comercial.** Sem "aproveite", sem escassez, sem contagem regressiva, sem
> selo, sem exclamação. O registro é **institucional e clínico**: frases curtas, informação
> verificável, serenidade. Aqui a credibilidade é o produto — entusiasmo afasta.

> Tudo entre `[CONFIRMAR: ...]` não vai ao ar sem resposta do cliente. Lista consolidada em
> `2026-08-07-decisoes-e-pendencias.md`.

---

## 0. Metadados

**Title (58 car.):** Transporte Aeromédico com UTI Aérea 24h — UniAir
**Meta description (155 car.):** Transporte aeromédico com UTI aérea, equipe assistencial embarcada e operação 24 horas. Bases em Porto Alegre e Londrina. Fale com a equipe agora.
**URL sugerida:** `taxiaereo.uniair.com.br/transporte-aeromedico`
**Nome da conversão (Google Ads):** `LP_B_aeromedico_form`
**Grupos de anúncio que apontam para cá:** `aeromedico_geral`, `ambulancia_resgate`

---

## 1. Barra superior (fixa, sem menu)

```
UniAir · Transporte Aeromédico        Atendimento 24 horas
                                      0800 519 5190 [clicável]  ·  WhatsApp [clicável]
```

O telefone é o elemento mais visível da barra. Parte deste público está numa emergência e não vai
preencher formulário nenhum.

---

## 2. Hero (primeira dobra)

**Sobretítulo:**
> Remoção aeromédica entre cidades e estados · Operação 24 horas

**H1:**
> # Transporte aeromédico com UTI aérea e equipe especializada, 24 horas

**Subheadline:**
> Remoção de pacientes em aviões e helicópteros equipados com estrutura de UTI e equipe
> assistencial a bordo. Bases próprias em Porto Alegre e Londrina, com atendimento em todo o país.

**Contato imediato (acima do formulário, no mobile também):**
> **Precisa falar agora?**
> 📞 **0800 519 5190** · 💬 **WhatsApp (51) 99275-7845**
> Atendimento 24 horas, todos os dias.

**Linha de prova:**
> Desde 1997 · Frota própria · Equipe assistencial embarcada · Atendimento 24h
`[CONFIRMAR: padronizar "desde 1997" / "28 anos" / "29 anos" nas três LPs]`

---

## 3. Formulário do hero (visível, sem popup)

**Título:**
> ## Solicite a cotação da remoção

**Apoio:**
> São 7 perguntas. Com elas a equipe já consegue avaliar a viabilidade e montar o orçamento.
> Se preferir, ligue no 0800 519 5190 — o atendimento é 24 horas.

### Etapas (uma pergunta por tela, "1 de 7")

| # | Rótulo | Pergunta / placeholder | Tipo |
|---|---|---|---|
| **1** | **Finalidade** | **"Como podemos ajudar?"** *(opções na seção 3.1)* | **seleção única, sem digitação** |
| 2 | Nome | "Para começar, como podemos te chamar?" · *Seu nome* | texto |
| 3 | WhatsApp | "{nome}, qual o WhatsApp para o nosso retorno?" · *(00) 00000-0000* | telefone |
| 4 | E-mail | "E o seu e-mail, caso precisemos enviar documentos?" · *seu@email.com* | e-mail |
| 5 | Origem | "De qual cidade e estado o paciente sairá?" · *Cidade e estado · hospital, se já souber* | texto |
| 6 | Destino | "Para qual cidade e estado ele precisa ser levado?" · *Cidade e estado · hospital de destino* | texto |
| 7 | Quando | "Quando o transporte precisa acontecer?" · *Hoje · Amanhã · Nos próximos dias · Ainda a definir* | seletor |

**Campos que não existem mais** (estavam na LP atual e saem): "como podemos te ajudar" (texto
aberto) e a duplicidade origem/cidade de origem — três campos de atrito sem uso analítico.
**"Motivo do contato" fica** e vira a etapa 1: ver a seção 3.1, é o campo que sustenta a
classificação de MQL.

**Botão:**
> [ Solicitar cotação de transporte ]

**Microcopy:**
> 🔒 Seus dados são usados apenas para o retorno da equipe. Nenhuma informação clínica é solicitada
> neste formulário.

**Tela de confirmação:**
> ### Recebemos sua solicitação, {nome}.
> Nossa equipe está avaliando a remoção de **{origem}** para **{destino}** e entrará em contato
> pelo WhatsApp **{whatsapp}**.
> `[CONFIRMAR: prazo de retorno com o comercial]`
>
> **Se o caso for urgente, ligue agora: 0800 519 5190** — atendimento 24 horas.
>
> [ Continuar no WhatsApp ]

---

## 3.1 Etapa 1 — Finalidade (campo de qualificação)

> **Correção ao briefing** — mesma da LP A, ver seção 3.1 daquele arquivo. Resumo: o campo
> "motivo do contato" não é atrito descartável, é a origem da classificação de **MQL** enviada ao
> Google Ads. Sem ele a conversão vira lead bruto e o Smart Bidding aprende com currículo, curso
> de enfermagem aeromédica e traslado de corpo — as três maiores fontes de lixo desta campanha.
> **A etapa 1 é obrigatória e está fora do teste A/B do formulário.**

Nesta página o campo faz um segundo trabalho, além de filtrar: ele **separa os dois públicos**
(família e profissional de saúde) já na primeira interação, o que muda o roteamento no Kommo e o
vocabulário do retorno.

**Formato:** seleção única, sem digitação. Tom neutro e sem julgamento — a pessoa pode estar
numa emergência.

**Pergunta:**
> ### Como podemos ajudar?

**Opções (nesta ordem):**

| Opção exibida | Classificação | O que acontece |
|---|---|---|
| **Preciso remover um familiar ou paciente** | **MQL — família** | segue para a etapa 2 |
| **Sou profissional de saúde ou represento um hospital** | **MQL — B2B** | segue o formulário; roteamento próprio no Kommo |
| **Quero saber o valor de uma UTI aérea** | **MQL — preço** | segue o formulário; conteúdo de preço no retorno *(mesma intenção da LP C)* |
| Preciso de fretamento de voo executivo | **MQL — outro serviço** | segue o formulário, vocabulário de táxi aéreo, pipeline de executivo |
| Traslado de corpo | **descarte** | tela 3.2-A |
| Trabalhar na UniAir, curso ou formação | **descarte** | tela 3.2-B |
| Outro assunto | **revisar** | segue o formulário, marcado `revisar`; não conta como MQL |

**Por que essas duas opções de descarte e não outras:** vêm dos motivos de perda do Kommo, não de
suposição — 9 perdas por óbito/traslado e boa parte das 31 perdas por DESCONHECIMENTO são emprego,
curso e formação (`enfermagem aeromedica`, `médico aeronáutico`, `curso`, `salário`, `vaga`).
São exatamente as intenções que viram negativa na Fase 0 do briefing de tráfego. A negativa reduz
o clique; este campo protege a conversão de quem clicou mesmo assim.

**Não incluir opção de "SAMU/emergência em via pública"** — quem está nessa situação não preenche
formulário. Isso já é tratado em texto na seção 8.2.

---

## 3.2 Telas de descarte

O tom aqui é especialmente cuidadoso: a pessoa pode ter acabado de perder alguém.

**3.2-A · Traslado de corpo**
> ### A UniAir não realiza traslado de corpos.
> Nossa operação é de transporte de pacientes com suporte médico a bordo.
>
> O traslado é feito por funerárias, que cuidam da documentação e do transporte. Sentimos muito
> não poder ajudar neste momento.

**3.2-B · Trabalhar na UniAir, curso ou formação**
> ### Vagas e formação não são tratadas por este canal.
> Este formulário é da operação de transporte aeromédico.
>
> Para trabalhar conosco, envie seu currículo para `[CONFIRMAR: e-mail ou canal de RH da Uniair]`.
> A UniAir não oferece cursos de enfermagem ou medicina aeroespacial.

**Nas duas telas:** nenhum dado vai para o comercial e **nenhuma conversão é enviada ao Google
Ads**. Registrar evento interno (`form_descarte_traslado`, `form_descarte_curriculo`) — o volume
desses eventos é o termômetro de quanto lixo a campanha ainda está trazendo, e a correção é
negativa de palavra-chave, não página.

---

## 4. Bifurcação de público (logo abaixo do hero)

Dois públicos chegam nesta página e precisam se separar rápido, sem virar duas páginas.
São âncoras internas, não links externos.

**H2:**
> ## Como podemos ajudar?

| **Sou familiar ou responsável pelo paciente** | **Sou profissional de saúde ou represento um hospital** |
|---|---|
| Entenda em que situações o transporte aeromédico é indicado, como funciona a remoção e o que é preciso ter em mãos. → *(âncora: seção 5)* | Veja a estrutura embarcada, a equipe e como acionamos a operação para transferência inter-hospitalar. → *(âncora: seção 7)* |

`[Fase 2 — não escrever nada sobre convênio, seguradora, operadora ou licitação nesta página antes
da validação com a Dani. O ângulo B2B completo é a LP D, ainda não aprovada.]`

---

## 5. "Quando o transporte aeromédico é indicado" — o bloco que ataca a objeção nº 1

Este é o bloco mais importante da página. Ele existe porque 31 leads foram perdidos por
desconhecimento e 35 escolheram outra forma de transporte. A pessoa precisa reconhecer o próprio
caso aqui, antes de qualquer pedido de dado.

**Sobretítulo:** Antes de decidir
**H2:**
> ## Quando o transporte aeromédico é indicado

**Abertura:**
> Nem toda remoção precisa ser aérea, e nem toda remoção pode ser terrestre. A indicação é sempre
> da equipe médica que acompanha o paciente — o que segue são as situações em que o transporte
> aeromédico costuma ser considerado.

**Situações (lista, sem ícone de alarme):**

- **A distância é longa e o tempo importa.** Trajetos que levariam muitas horas de ambulância
  terrestre podem ser feitos em uma fração do tempo, reduzindo a exposição do paciente ao
  deslocamento.
- **O paciente precisa de suporte contínuo durante o trajeto.** Ventilação mecânica, monitorização,
  bombas de infusão e oxigênio permanecem em funcionamento durante todo o voo.
- **O hospital de origem não tem o recurso necessário.** Transferência para centro de referência,
  UTI especializada, cirurgia ou exame que não existe na cidade de origem.
- **A estrada é um risco em si.** Trechos longos, condições da via, clima ou instabilidade do
  quadro tornam o transporte terrestre menos indicado.
- **Retorno para a cidade de origem.** Paciente internado longe de casa que precisa voltar para
  perto da família ou para o hospital de convênio de origem.
- **Local de difícil acesso.** Quando não há aeroporto próximo, o helicóptero permite pouso em
  heliponto ou área autorizada.

**Fecho honesto (mantém a credibilidade e economiza tempo do comercial):**
> **Quando não é o caso:** deslocamentos curtos, pacientes estáveis sem necessidade de suporte e
> situações em que a ambulância terrestre atende com segurança. Se for o seu caso, a nossa equipe
> vai te dizer isso — não transportamos quem não precisa ser transportado por via aérea.

> A UniAir não realiza traslado de corpos. Para esse tipo de serviço, procure uma funerária.

*(Esta última linha resolve, na própria página, as 9 perdas do Kommo por óbito/traslado — a mesma
intenção que vira negativa no Google Ads.)*

---

## 6. "Como acionar" — passo a passo

**Sobretítulo:** O caminho
**H2:**
> ## Como acionar uma remoção aeromédica

| | |
|---|---|
| **01 · Fale com a equipe** | Pelo 0800 519 5190, pelo WhatsApp ou pelo formulário desta página. O atendimento é 24 horas. |
| **02 · Avaliação do caso** | Nossa equipe verifica o quadro do paciente com o médico assistente e define a aeronave, a equipe e os equipamentos necessários. |
| **03 · Cotação e autorização** | Você recebe a proposta da remoção. Com o aceite, iniciamos as autorizações de voo e o contato com os hospitais das duas pontas. |
| **04 · Remoção porta a porta** | Ambulância no hospital de origem, voo com equipe embarcada e ambulância até o hospital de destino. O acompanhamento é contínuo. |

**O que ter em mãos (acelera muito a avaliação):**
- Relatório médico atualizado do paciente
- Nome e cidade do hospital de origem
- Hospital de destino, se já houver definição
- Contato do médico assistente
- Se o paciente usa ventilação mecânica, bomba de infusão ou oxigênio

> Não tem tudo isso agora? Ligue mesmo assim. A equipe orienta o que buscar.

---

## 7. Estrutura embarcada e equipe

**Sobretítulo:** O que vai a bordo
**H2:**
> ## UTI aérea: estrutura e equipe

**Abertura:**
> A aeronave é configurada como uma UTI. O paciente é monitorado do embarque ao desembarque, sem
> interrupção de suporte.

**Estrutura:**
- Maca de transporte com fixação aeronáutica
- Ventilador mecânico de transporte
- Monitor multiparamétrico
- Bombas de infusão
- Oxigênio e aspiração
- Desfibrilador e material de via aérea avançada
- Medicações de emergência

`[CONFIRMAR com a coordenação: a lista precisa refletir exatamente o que está embarcado. Retirar
qualquer item que não seja padrão em todas as aeronaves.]`

**Equipe:**
> Médico e enfermeiro com formação em transporte aeromédico, além de piloto e copiloto em todas as
> operações. A tripulação técnica tem formação em **fisiologia aeroespacial** — o voo altera
> pressão e oxigenação, e isso muda o manejo do paciente em relação a um transporte terrestre.
> É essa diferença que justifica uma equipe treinada especificamente para o ambiente aéreo.

**Aeronaves:**
> Aviões turboélice **King Air** (B260, B200GT, C90 GTI e C90 SE) e helicópteros **Airbus AS350 B2**,
> todos próprios e operados por tripulação UniAir.

> ⚠️ **Nunca escrever "jato" ou "jatinho".** A frota é turboélice e helicóptero.

---

## 8. Sub-públicos (seções curtas, não viram páginas)

### 8.1 Transporte neonatal e pediátrico

> Recém-nascidos e crianças exigem equipamento e manejo próprios. A remoção neonatal é feita com
> incubadora de transporte e equipe habilitada para o cuidado dessa faixa etária, com atenção às
> particularidades do voo — temperatura, pressurização e ruído.
> `[CONFIRMAR: a Uniair opera com incubadora de transporte própria? Se não for padrão, reescrever
> sem afirmar o equipamento.]`

### 8.2 Ambulância aérea e resgate aeromédico

> Ambulância aérea é o nome popular do transporte aeromédico — a aeronave equipada que leva o
> paciente com suporte de UTI entre dois pontos. O helicóptero atende bem trajetos curtos e locais
> sem aeroporto; o avião, distâncias maiores entre cidades e estados.
>
> Para **emergência pública em via ou acidente**, o acionamento é do SAMU (192) ou do Corpo de
> Bombeiros (193). A UniAir opera **remoções e transferências programadas ou de urgência a partir
> de solicitação do paciente, da família ou do hospital.**

*(Este parágrafo é intencional: separa a nossa operação do serviço público e reduz o volume de lead
que chega buscando SAMU/bombeiros — a mesma intenção que vira negativa na campanha.)*

---

## 9. Cobertura

**Sobretítulo:** Onde estamos
**H2:**
> ## Bases próprias e alcance da operação

> **Aeroporto Salgado Filho — Porto Alegre/RS**
> **Aeroporto Governador José Richa — Londrina/PR**
>
> A partir dessas duas bases, a frota atende remoções em todo o território nacional. Cidades sem
> aeroporto podem ser atendidas por helicóptero ou por ambulância de apoio até o aeroporto mais
> próximo, conforme a avaliação da rota.

`[NÃO ESCREVER: qualquer promessa de tempo de chegada ("chegamos em X horas"). Prazo de retorno da
cotação, sim, quando confirmado. Tempo de operação, não.]`

---

## 10. FAQ

**H2:**
> ## Perguntas frequentes sobre transporte aeromédico

**1. O que é transporte aeromédico?**
> É a remoção de um paciente por via aérea, em aeronave equipada com estrutura de UTI e equipe
> assistencial a bordo. O suporte é contínuo: o paciente segue monitorado e assistido do hospital
> de origem até o hospital de destino.

**2. Qual a diferença entre transporte aeromédico e UTI aérea?**
> "UTI aérea" descreve a estrutura embarcada — os equipamentos e a equipe que transformam a
> aeronave em uma unidade de terapia intensiva. "Transporte aeromédico" é o serviço completo, que
> inclui a UTI aérea mais as ambulâncias nas duas pontas, as autorizações e a coordenação entre os
> hospitais.

**3. Quem decide se o paciente pode voar?**
> A indicação é do médico que acompanha o paciente. A nossa equipe avalia a viabilidade do
> transporte a partir do relatório médico e conversa diretamente com o médico assistente.

**4. Quanto custa?**
> O valor depende da distância, da aeronave, do suporte clínico necessário e das ambulâncias de
> apoio. Não há tabela — a cotação é montada caso a caso.
> → [Entenda o que define o valor de uma UTI aérea] *(link para a LP C)*

**5. Um acompanhante pode ir junto?**
> Na maior parte das remoções, sim — normalmente um acompanhante. A confirmação depende da
> aeronave, do peso total e do equipamento embarcado, e é feita na avaliação do caso.

**6. Vocês atendem 24 horas?**
> Sim. Atendimento e operação funcionam 24 horas, todos os dias.

**7. Atendem cidades sem aeroporto?**
> Sim, com helicóptero ou com ambulância de apoio até o aeroporto mais próximo. A solução é
> definida na avaliação da rota.

**8. O plano de saúde cobre?**
> `[BLOQUEADO — não publicar nada sobre convênio, plano ou seguradora antes da confirmação da
> Dani. Redação segura provisória, se a pergunta precisar existir: "A cobertura depende do contrato
> de cada paciente. A nossa equipe informa quais documentos costumam ser solicitados e orienta o
> processo." — mesmo essa versão só entra com aprovação.]`

---

## 11. Fechamento

**H2:**
> ## Fale com a equipe de transporte aeromédico

**Apoio:**
> Atendimento 24 horas, todos os dias. Se o caso for urgente, ligue — o telefone é o caminho mais
> rápido.

> 📞 **0800 519 5190**
> 💬 **WhatsApp (51) 99275-7845**
> 📞 (51) 2121-1100 · ✉️ comercial@uniair.com.br
>
> [ Solicitar cotação de transporte ]

**Rodapé:**
> UniAir Transporte Aeromédico · Bases: Aeroporto Salgado Filho (Porto Alegre/RS) e Aeroporto
> Governador José Richa (Londrina/PR) · Operação 24 horas
> *(sem menu, sem link para o site institucional; apenas política de privacidade)*

---

## 12. Notas de implementação

- **Sem estética de campanha promocional:** nada de vermelho de urgência, contagem regressiva,
  selo de desconto ou banner rotativo. Paleta institucional, tipografia legível, contraste alto.
  A referência visual é hospitalar, não de e-commerce.
- **Telefone sobe junto com o formulário** no hero — em mobile, botão de ligar fixo no rodapé da
  tela. Essa é a única exceção ao "um CTA por página": parte do público está em emergência.
- Sem pop-up, sem menu, sem rota de fuga.
- Vídeo, se houver: thumbnail estática com play, player só após o clique. LCP abaixo de 2,5s no 4G.
- Imagens em WebP, dimensionadas para o slot, `lazy` fora da primeira dobra. Fotos reais da frota,
  do hangar e da estrutura embarcada — sem banco de imagens.
- Formulário em etapas construído para permitir teste A/B contra formulário único. **A etapa 1
  (finalidade) fica fora do teste** — existe em qualquer variante.
- Evento por etapa concluída (`form_step_1` … `form_step_7`), eventos de descarte
  (`form_descarte_traslado`, `form_descarte_curriculo`) e eventos de clique em telefone, 0800 e
  WhatsApp.
- **Conversão enviada ao Google Ads apenas para finalidade classificada como MQL.** Descarte não
  converte.
- Conversão distinta (`LP_B_aeromedico_form`), separada de A e C. UTMs e `gclid` preservados até o
  Kommo.
