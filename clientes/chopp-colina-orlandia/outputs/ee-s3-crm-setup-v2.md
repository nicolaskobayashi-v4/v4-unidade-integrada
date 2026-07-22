# CRM Setup v2 — Chopp Colina Orlandia
**Skill:** ee-s3-crm-setup | **Gerado em:** 18/07/2026 | **Versão:** 2
**Plataforma:** Kommo
**Fonte principal:** Transcrição "Conectar Kommo Chopp Colina" (03/07/2026) — reunião real de conexão das 3 caixas de WhatsApp no Kommo, com Cláudio K. e Gustavo Argenta (INBEB)

> Esta v2 **não substitui** a v1 (21/06/2026). Ela complementa com o que a sessão real de conexão do Kommo revelou — principalmente que a **Choperia precisa de pipeline próprio**, separado do Delivery. Motivos de perda, tags de segmentação, mensagens rápidas e playbook comercial já documentados na v1 continuam valendo e não são repetidos aqui na íntegra.

---

## Manchete

> **O Kommo já está tecnicamente conectado nos 3 números (Delivery Orlândia, Choperia, Franca) — mas o que a reunião de 03/07 revelou é que a Choperia nunca teve pipeline próprio: ela estava rodando dentro da mesma lógica do delivery. Sem separar isso agora, o histórico de reserva de mesa — com valor médio real de R$200, não os R$500 estimados inicialmente — continua sem estrutura para virar prova de faturamento.**

---

## O que mudou desde a v1 (21/06 → 03/07)

| Mudança | Detalhe |
|---|---|
| **Choperia ganha pipeline próprio** | Na v1 só existiam 2 pipelines (Delivery B2C e Eventos&Revenda B2B). A conexão real do Kommo revelou que o número da choperia estava sendo usado "pros dois, Delivery e Choperia" — decisão tomada: separar definitivamente. Exige um 3º funil dedicado, detalhado abaixo. |
| **Régua de aniversário** | Não estava na v1. Surgiu na própria demonstração: campo de aniversário no contato + filtro de quem faz aniversário nos próximos 15 dias + abordagem automática. |
| **Fluxo de recuperação de vendas** | Citado como próximo passo pelo Lucas na reunião — mas **ainda não construído** dentro do Kommo. É pendência, não conquista. |
| **Valor médio por mesa corrigido** | Estimativa inicial de R$500/mesa foi corrigida pelo próprio Cláudio para **~R$200/mesa**, por causa do público jovem de baixo consumo — o mesmo problema já mapeado no SWOT, agora com número real do dono. |
| **Cronograma real, provavelmente ultrapassado** | Meta verbal: pronto 15/07, treinamento 16/07 (a confirmar — dia 15 "vai ter jogo"). Hoje é 18/07. Ver alerta abaixo. |

---

## ⚠️ Alerta de Cronograma

```
Meta definida em 03/07: 100% pronto em 15/07, treinamento em 16/07
Data atual: 18/07/2026
```

As duas datas já passaram sem registro de conclusão na base de conhecimento — não há transcrição de treinamento nem confirmação de que os pipelines foram de fato estruturados dentro do Kommo (a reunião de 03/07 tratou majoritariamente da **conexão dos números**, deixando "definir fase, pipeline, estrutura de criação, automações" como próximo passo verbal).

**Antes de prosseguir, confirme com o Cláudio:**
1. O treinamento aconteceu?
2. Os pipelines já foram estruturados no Kommo, ou ficou só a conexão dos números?

Esta v2 assume que a estruturação ainda está pendente.

---

## Setup Técnico do WhatsApp (pré-requisito)

Automação em cima de conexão instável não sustenta — este passo vem antes de qualquer régua.

| Número | Status | Observação |
|---|---|---|
| **Delivery Orlândia** | Conectado em 03/07 | Antes atendia Delivery + Choperia juntos; a partir de agora, dedicado só ao Delivery |
| **Choperia** | Conectado em 03/07 | Número novo e dedicado. Precisou reinstalar como **WhatsApp Business** (não o WhatsApp comum) para conectar sem falhas — atenção a esse detalhe em qualquer número novo |
| **Franca** | Cadastrado no Kommo, sem aparelho físico ainda | Estrutura pronta para quando a operação em Franca começar |

**Cuidados operacionais:**
- Usar o WhatsApp diariamente no celular físico — sem uso ativo, a sessão cai a cada ~14 dias (reconectar em Configurações > Central de Integrações)
- Múltiplos dispositivos acessando o mesmo Kommo geram só um aviso, não derrubam a sessão — pode ignorar
- Conector usado: **WhatsApp Light**, não o WhatsApp Business API oficial (que passa a cobrar por mensagem a partir de outubro/2026)
- Decisão consciente de **não integrar Instagram/TikTok DMs** no mesmo inbox — o próprio time avaliou que misturar canais bagunça a operação neste estágio

---

## Pipeline 1 — Delivery (Orlândia + Franca)

**Número:** Delivery Orlândia (dedicado) — Franca entra quando o número for ativado
**Ciclo esperado:** mesmo dia a 48h
**Tag obrigatória:** Cidade (Orlândia | Franca) — separa métricas por unidade dentro do mesmo funil

```
Lead novo → Diagnóstico (30L/50L, nº pessoas) → Orçamento enviado → Confirmar local de entrega* → Agendado → Entregue/instalado → Pós-venda
                                                                                                        ↓ (sem resposta)
                                                                                              Não fechou (motivo obrigatório)
```
*\*Etapa nova — cobre o gap real relatado pelo Cláudio: "a pessoa reserva o chopp, mas ainda não alugou o lugar".*

**Campos customizados:** Valor do negócio (R$) · Tipo de barril (30L/50L/Grauler) · Endereço de entrega · Cidade · Data agendada

**Uso do campo Nota:** registrar handoff entre quem atendeu primeiro (Cláudio) e quem executa a entrega (ex: Gustavo Barbosa) — fica interno, não aparece na conversa com o cliente.

---

## Pipeline 2 — Choperia (mesa/reserva) 🆕

**Número:** Choperia (dedicado, separado do Delivery a partir de 03/07)
**Ciclo esperado:** mesmo dia (reserva feita e consumida na mesma semana, geralmente quinta a domingo)

**Por que precisa de funil próprio:** a choperia não vende produto fechado — é reserva de mesa com consumo variável, e carrega um problema específico que o delivery não tem (público jovem de baixo consumo ocupando mesa). Rodar os dois no mesmo funil, como acontecia até 03/07, misturava dois processos de decisão diferentes.

```
Lead/mensagem recebida → Mesa reservada (nº pessoas + valor esperado) → Confirmado (chegou até horário-limite) → Atendido
                                                                                    ↓
                                                                    Não compareceu/cancelado (motivo)
```

**Campos customizados:** Nº de pessoas na mesa · Valor esperado de consumo (R$) · Horário da reserva

**Valor médio por mesa: R$200**
> Corrigido pelo próprio Cláudio durante a reunião — a estimativa inicial de R$500 foi considerada alta demais. Motivo dele: "vem muito figurante" (cliente jovem que ocupa mesa e consome pouco — água, refrigerante), problema já mapeado no SWOT e na entrevista comercial. Este valor é o multiplicador de forecast: **nº de reservas no fim de semana × R$200 = faturamento mínimo esperado.**

**Automação existente a manter:**
> *"Reserva de mesas chegada até às 20 horas. Aos domingos não reservamos mesas."*

Manter como está — não conflita com o diferencial "atende domingo" já comunicado no posicionamento. Aquele diferencial é do **Delivery** (atende domingo de manhã até 14h); este auto-reply é da **Choperia** (bar não recebe reserva de mesa aos domingos). São operações diferentes e podem manter comunicação separada por número.

---

## Pipeline 3 — Eventos & Ponto de Revenda B2B

Mantido sem alterações da v1 (ciclo de 7 a 60 dias) — não foi tema da reunião de conexão de 03/07. Ver `ee-s3-crm-setup.md` (v1) para etapas completas.

---

## Automações

### Novas nesta v2

**1. Régua de aniversário**
- **Gatilho:** campo de data de aniversário preenchido no contato + filtro "aniversário nos próximos 15 dias"
- **Mensagem:** *"Vai fazer uma festa aí do seu aniversário? Bora pedir um chopp — separo uma condição especial pra data."*
- Ideia surgida na própria demonstração do Kommo — custo zero, aplica-se a leads de Delivery e de Choperia
- **Pré-requisito:** popular o campo de aniversário nos contatos existentes (não é automático — depende de perguntar/registrar durante o atendimento)

**2. Tarefa automática de lembrete de follow-up**
- **Gatilho:** criada manualmente pelo atendente quando há condição futura a confirmar (ex: "ligar dia X para saber se ainda vai ter o jogo/evento")
- Recurso nativo do Kommo, usado ao vivo na reunião — evita depender da memória do Cláudio
- **Status:** disponível na ferramenta, ainda não formalizado como hábito de processo

### Pendente de construir — prioridade nº 1

**Fluxo de recuperação de vendas**
Pessoa que orçou e sumiu, ou que já comprou antes e não volta — como reabordar de forma sistemática.

- Citado pelo próprio Lucas como próximo passo na reunião de 03/07 ("já elaborar fluxo de recuperação de vendas") — **não estava configurado no Kommo até o fim da reunião**
- A v1 já continha a proposta "Resgate de orçamento parado" (48h sem resposta) — esta v2 confirma que ela ainda precisa ser efetivamente implementada, não é automação ativa hoje
- **Recomendação:** este é o item que mais aparece como pendência entre v1 e v2 — deve ser a prioridade da próxima sessão de trabalho com o Cláudio

### Mantidas da v1, sem alteração
- Boas-vindas / triagem inicial (delivery vs. choperia)
- Reativação — Anfitrião (30-45 dias sem pedido)
- Reativação — Organizador de evento (por data anual)
- Checagem de reposição — Ponto de Revenda (semanal)

---

## Ponto de Alavancagem

```
┌──────────────────────────────────────────────────────────────────────┐
│  ⚡ ALAVANCA PRIORITÁRIA                                              │
│                                                                      │
│  "Separar o pipeline da Choperia AGORA — antes de investir mais     │
│   tempo ajustando o Delivery. As reservas de mesa já estão sendo    │
│   registradas no Kommo desde 03/07, mas ainda sem campo de valor    │
│   esperado nem etapa de confirmação por horário. Cada fim de        │
│   semana sem essa estrutura é faturamento potencial da choperia     │
│   que se perde — o mesmo dado (R$200 real vs. R$500 estimado)       │
│   que confirma o problema do público jovem já mapeado no SWOT."     │
└──────────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Alerta Operacional

Mantido da v1: o CRM deve registrar e automatizar a logística (réguas, tags, motivos de perda, tarefas), nunca substituir o tom da conversa que já é validado como o melhor da praça. A separação em 3 números/pipelines reforça esse cuidado — cada operação (delivery, choperia, Franca) deve manter sua própria voz, sem forçar um script único que ignore o contexto de cada canal.

---

*Ver `ee-s3-crm-setup.md` (v1) para: motivos de perda padronizados, tags de segmentação, mensagens rápidas, playbook comercial mínimo, métricas de acompanhamento e plano de implementação por sprint.*
*Alimenta: ee-s5-scripts-sdr · ee-s5-sdr-ia-config · ee-revisao-semanal*
