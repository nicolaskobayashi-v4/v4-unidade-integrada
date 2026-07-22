# CRM Setup — MW Software (UZTS Light)

**Versão:** 3 — completed (como pipeline conceitual, não como setup de ferramenta paga)
**Gerado em:** 2026-07-16

> v3: reversão da recomendação de ferramenta (Kommo), a pedido do operador. Mantida a estrutura de pipeline porque ela é tool-agnostic e continua fazendo sentido — na reunião real de 07/07/2026, o próprio Lucas Calefi confirmou ao vivo que o CRM do Horizonte 1 "não precisa ser robusto", podendo ser uma planilha ou um projeto open-source básico do GitHub. Este documento entrega a **lógica** (o que rastrear, em que ordem, com qual rede de segurança), não um guia de configuração de uma ferramenta específica.

## Manchete

> O que importa aqui não é a ferramenta — é a etapa de rede de segurança que impede repetir o churn da distribuidora de bebidas. Isso roda numa planilha tão bem quanto num CRM pago.

## Resumo

O valor real deste documento é a estrutura de **2 pipelines paralelos**: um para gerenciar o **parceiro** (recrutamento, comissão, performance) e outro, bem mais enxuto, para o **cliente que vem via parceiro** — que entra no controle já perto do fim do funil, porque quem prospecta, fecha e onboarda é o próprio parceiro. Essa lógica funciona numa planilha simples tanto quanto num CRM pago; o que não pode faltar, em qualquer meio escolhido, é a etapa de rede de segurança contra o padrão de churn já conhecido.

## KPIs

| Indicador | Valor | Contexto |
|---|---|---|
| Ferramenta | Planilha ou CRM básico gratuito | Confirmado ao vivo na reunião real — "não precisa ser robusto" |
| CRM hoje | 0 — manual | "Clone de WhatsApp" + planilha, visível só pra 1-2 pessoas |
| Estrutura | 2 pipelines | Parceiros (gestão de canal) + Clientes (2 variantes) |
| Ponto de falha conhecido | Instalado ≠ Ativado | Caso real de churn (distribuidora de bebidas) por isso |
| Acesso do parceiro à ferramenta | Nenhum (H1) / Auto-report leve (H2) | Parceiro nunca precisa abrir a ferramenta interna |

## Achados principais

- **[Contexto]** O parceiro prospecta, fecha **e** faz o onboarding — a MW só recebe o cliente depois de implementado, idealmente já ativado.
- **[Ameaça]** O cenário "ideal" não é garantido — o mínimo aceitável é "no máximo o onboarding do parceiro", podendo chegar só instalado. Mesmo padrão do churn da distribuidora de bebidas.
- **[Vantagem]** A reunião real confirmou ao vivo: "não precisa ser um CRM robusto — se vocês conseguirem resolver com uma planilha, tá ótimo", incluindo sugestão de projeto open-source básico do GitHub.
- **[Ação]** Manter a estrutura de pipeline independente da ferramenta escolhida — é essa lógica que evita repetir o churn, não a marca do software.
- **[Ação]** No Horizonte 2, se o volume justificar ferramenta mais robusta, priorizar WhatsApp nativo — RD Station já foi descartado em outra conta por não ser chat-first.

## ⚠️ Alerta de honestidade

Esta estrutura de pipeline não resolve, sozinha, o padrão histórico de "frear" o crescimento por medo operacional — ela só dá visibilidade pra decisão ser tomada com dado. Se a MW não usar essa visibilidade pra realmente agir, a planilha (ou qualquer ferramenta escolhida) vira só mais um registro bonito e inútil, do mesmo jeito que o RD Station virou inútil na outra conta do Marcos.

## 💬 Ponto de alavancagem

**A etapa de "confirmação de ativação" é a única rede de segurança entre o modelo de parceria e o padrão de churn que a MW já viveu — e isso vale em qualquer ferramenta.**

1. O mínimo aceitável do parceiro é entregar "no máximo o onboarding" — ativação não é garantida no handoff.
2. O caso da distribuidora de bebidas prova que "instalado" e "sendo usado" são estados diferentes.
3. Comissão recorrente só faz sentido sobre cliente realmente ativo.

**Ponto de discussão:** quem monitora e age quando um cliente trava em "aguardando confirmação de ativação" — o parceiro (1ª linha) ou o Gestor de Canais (2ª linha)?

---

## Ferramenta

**Recomendação:** planilha compartilhada (Google Sheets) ou CRM gratuito/open-source básico — a escolha específica é operacional, não estratégica. O que importa é implementar a estrutura de pipeline abaixo.

> **Confirmado em reunião real (07/07/2026):** *"Não precisa ser um CRM robusto. Se vocês conseguirem se resolver com uma planilha, tá ótimo (...) dá até pra pegar no GitHub uns projetos de graça, um CRM basicão open source que funciona muito bem."* — Lucas Calefi

**Se o volume crescer (Horizonte 2):** se 10-15+ parceiros externos justificarem uma ferramenta mais robusta, priorizar WhatsApp como canal nativo — RD Station já foi testado e descartado em outra conta do Marcos por ser orientado a e-mail/lead scoring B2B.

## Estrutura de pipelines

### 1. Pipeline Parceiros

**Etapas:** Aplicação recebida → Em análise → Aprovado/ativo → Aprovado com ressalva → Inativo/reavaliar

**Campos:** % comissão (10%, confirmado), região, nº de clientes trazidos, data da última indicação, perfil

### 2. Pipeline Clientes — via parceiro

| Etapa | Descrição |
|---|---|
| Recebido do parceiro | Pode chegar já ativado (ideal) ou só instalado (mínimo aceitável) |
| Aguardando confirmação de ativação | Só existe se não chegou já ativado — rede de segurança |
| Ativo | 1º cupom fiscal emitido — inicia contagem de comissão |
| Em risco / Cancelado | Sem emissão recente ou sinalização de cancelamento |

**Campo obrigatório:** "Trazido por: [parceiro]".
**Regra de segurança:** se travar em "aguardando ativação" sem emitir o 1º cupom em N dias, alerta — parceiro primeiro, Gestor de Canais depois.

### 3. Pipeline Clientes — orgânico

**Etapas:** Lead → Qualificado → Instalado → Ativado (1º cupom emitido) → Retido/Em risco

Único funil onde a MW opera prospecção, qualificação e onboarding de fato — pode começar manual (Marcos) e evoluir pra automação só quando o volume justificar.

## Acesso do parceiro à ferramenta, por horizonte

- **Horizonte 1:** nenhum acesso direto. Parceiros-piloto reportam por WhatsApp; Marcos/Gestor de Canais registra manualmente na planilha.
- **Horizonte 2:** ainda sem acesso completo — fluxo leve de auto-report (se/quando a MW automatizar), sem o parceiro nunca abrir a ferramenta.

---

## Pendências para confirmação do operador

1. Prazo N de dias para a regra de segurança da etapa "aguardando confirmação de ativação".
2. Quem recebe primeiro o alerta de estagnação — parceiro ou Gestor de Canais.
3. Qual planilha/ferramenta específica será usada no Horizonte 1.
