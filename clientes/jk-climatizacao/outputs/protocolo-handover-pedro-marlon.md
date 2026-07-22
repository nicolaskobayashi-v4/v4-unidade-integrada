# Protocolo de Handover — Pedro → Marlon
**Gerado em:** 10/07/2026
**Fonte:** ee-s4-diagnostico-comercial + entrevistas comerciais (22/06) + drawflow-midia-e-captura.md

---

## Por que isso existe

Esse é o ponto mais citado como problema em TODAS as fontes comerciais: André descreve o processo hoje como *"nebuloso, conflituoso"*; no cliente oculto que a própria JK sofreu, o Marlon chegou a mandar um áudio que era pra outra pessoa — sinal claro de informação se perdendo na passagem entre Pedro e Marlon. André mesmo já disse o que precisa existir: *"esse processo tem que ter um handover muito claro, uma passagem de bastão muito clara ali de um pro outro."*

Este protocolo formaliza isso usando as ferramentas que a JK já tem HOJE (WhatsApp, grupo "agendamentos") — não depende do CRM estar pronto para começar a valer.

---

## Gatilho do handover

O handover acontece em **um momento exato**: assim que Pedro emite a Ordem de Serviço (o cliente aceitou o orçamento). É aí que a responsabilidade sai das mãos de Pedro (venda) e entra nas de Marlon (execução/onboarding).

**Antes desse momento:** o lead é 100% do Pedro. **Depois:** é 100% do Marlon. Não existe meio-termo — ambíguidade de "quem tá com isso agora" é exatamente o que gera o retrabalho hoje.

---

## O pacote de handover (checklist obrigatório)

Pedro **não pode** passar o cliente pro Marlon sem ter isso preenchido. Se faltar algo, o handover não está completo — Pedro continua responsável até completar.

| # | Campo | Por quê é obrigatório |
|---|---|---|
| 1 | Nome completo (pessoa ou empresa) | Básico, mas hoje se perde quando é só repassado de boca |
| 2 | Contato confirmado (telefone/WhatsApp) | Marlon precisa poder confirmar direto, sem voltar pro Pedro pra pegar número |
| 3 | Endereço/local exato do serviço | Alimenta a escolha do técnico pela tabela de prioridade (logística) |
| 4 | Tipo de cliente: **novo** ou **recorrente/contrato** | Muda o tratamento — recorrente já tem histórico, novo não |
| 5 | Score de qualificação (1-5⭐) | Já definido em `ee-s4-diagnostico-comercial` — Marlon prioriza pela mesma régua que Pedro usou |
| 6 | Tipo de serviço (avulso / recorrente / obra-instalação) | Define o critério de agendamento e o SLA |
| 7 | Detalhes técnicos levantados na qualificação | Nº de aparelhos, tipo (Split/VRF/Chiller), urgência, restrições de acesso (horário, portaria) — Marlon não pode ter que perguntar tudo de novo pro cliente |
| 8 | Valor acordado/provisionado | Já é prática hoje (Pedro posta a provisão no grupo) — só formaliza que é campo obrigatório, não opcional |
| 9 | Observações da conversa | Qualquer promessa feita, objeção levantada e como foi resolvida, prazo combinado |
| 10 | Data/hora já combinada (se houver) ou janela de disponibilidade do cliente | Evita Marlon agendar em horário que o cliente já disse que não pode |

---

## Template de mensagem (usar hoje, no grupo "agendamentos")

Em vez de texto livre, Pedro sempre preenche o mesmo modelo — reduz o risco de esquecer campo:

```
🔄 HANDOVER — [nome do cliente]
📞 Contato: [telefone]
📍 Local: [endereço]
🏷️ Tipo: [ ] Novo  [ ] Recorrente/contrato
⭐ Score: [1-5]
🔧 Serviço: [avulso / recorrente / obra]
🛠️ Detalhes técnicos: [nº aparelhos, tipo, urgência, restrições de acesso]
💰 Valor combinado: R$ [valor]
📝 Observações: [promessas feitas, objeções resolvidas, prazo combinado]
🗓️ Data/horário: [combinado ou janela de disponibilidade]

@Marlon — confirma recebido?
```

---

## Confirmação obrigatória

Marlon **precisa reagir** à mensagem (👍 ou "recebido, seguindo") antes de agir. Isso resolve dois problemas de uma vez:

1. **Evita o erro do áudio trocado** — Marlon só age depois de confirmar que leu e entendeu o cliente certo.
2. **Cria rastro** — se algo der errado depois, dá pra ver se o handover foi confirmado ou não.

**Se faltar informação:** Marlon pergunta pro Pedro **no grupo**, não liga direto pro cliente sem contexto. Ligar pro cliente perguntando algo que já devia estar no handover é o que gera a sensação de desorganização que o cliente oculto flagrou.

---

## Apresentação ao cliente (o momento visível)

Hoje a transição é muda pro cliente. Script sugerido pro Pedro usar sempre:

> *"Perfeito, [nome]! Vou te passar agora pro Marlon, que cuida do agendamento e da execução — já contei pra ele tudo que você me falou, então você não vai precisar repetir nada. Qualquer coisa, ele já tá com todos os detalhes."*

Isso faz duas coisas: tranquiliza o cliente (não vai ter que se repetir) e torna público — inclusive pro próprio cliente — que o handover aconteceu, o que indiretamente pressiona Pedro a ter feito o pacote completo antes de dizer isso.

---

## Casos especiais

- **Cliente recorrente com contrato:** hoje já vai direto pro Marlon, sem passar pelo Pedro. Isso continua — mas mesmo nesse caso, deveria existir um mini-registro (qual contrato, qual unidade, natureza da solicitação) pra não depender só da memória do Marlon quando o volume crescer.
- **Handover "de volta" (Marlon → Pedro):** se no meio do agendamento faltar uma informação, a regra é:
  - Pergunta **operacional simples** (ex.: confirmar disponibilidade de horário) → Marlon pode falar direto com o cliente.
  - Pergunta **comercial/sensível** (ex.: preço, objeção, condição especial) → sempre volta pro Pedro, nunca o Marlon decide isso sozinho no meio da execução.

---

## O que muda quando o CRM existir (`ee-s3-crm-setup`, pendente)

Este checklist vira **campos obrigatórios no card do CRM** antes de mudar de etapa (Proposta → Ganho → Onboarding) — o sistema simplesmente não deixa avançar se faltar campo. Até lá, é disciplina manual com o template acima. Nenhum destes 10 campos muda quando o CRM chegar — só migra de "mensagem de WhatsApp" pra "campo obrigatório do sistema".

---

## Como saber se está funcionando

Sem CRM, não dá pra medir isso automaticamente ainda. Sugestão simples até lá: **Sabrina ou André revisam 5 handovers por semana** (aleatórios, no grupo "agendamentos") e checam:
- O template foi usado por completo (todos os 10 campos)?
- Marlon confirmou recebimento?
- Houve alguma mensagem de "faltou informação" ou retrabalho depois do handover?

Se a resposta for "sim, faltou" mais de 1x por semana, o protocolo precisa de ajuste — não adianta só cobrar mais disciplina do Pedro.

---

**Alimenta:** `ee-s3-crm-setup` (define os campos obrigatórios do pipeline), `ee-s5-scripts-sdr` (já reflete o mesmo campo `handoff` no fluxo do agente de IA)
