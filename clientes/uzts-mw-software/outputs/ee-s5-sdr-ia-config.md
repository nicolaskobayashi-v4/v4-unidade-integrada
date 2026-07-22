# SDR IA — Configuração Patagon + Kommo — MW Software (UZTS Light)

**Versão:** 1
**Gerado em:** 2026-07-07

> ⚠️ Pula formalmente a dependência de `ee-s5-scripts-sdr` (que dependeria de `ee-s3-brandbook`, ainda pendente). O conteúdo abaixo é funcional — reaproveita a cadência e o tom que o Marcos já usa em outra conta — mas não é copy final de marca.
>
> **Timing:** documento pronto pra ativar, mas só entra em produção quando o Kommo for implantado (Horizonte 2, ver `ee-s3-crm-setup` v2). No Horizonte 1, o atendimento segue esses mesmos roteiros, só que manualmente pelo Marcos.

## Manchete

> Um agente, dois papéis: qualifica e ativa cliente orgânico; recebe relato de parceiro sem burocracia — os dois herdam a disciplina que o Marcos já usa em outra conta.

## Resumo

O SDR IA no Patagon cobre 2 fluxos distintos: um pro cliente final que chega organicamente (link na bio → qualificação → onboarding → ativação) e outro, mais enxuto, pro parceiro reportar handoffs sem nunca abrir o Kommo. Os dois fluxos reaproveitam a disciplina que o Marcos já demonstrou em outra conta (cadência D+24h/D+3/D+8, script de objeção, critério de desqualificação) — adaptada ao produto e ao ICP do UZTS Light.

## KPIs

| Indicador | Valor | Contexto |
|---|---|---|
| Fluxos configurados | 2 | Cliente orgânico (qualificação completa) + parceiro (auto-report leve) |
| Base de conteúdo | Reaproveitada | Cadência e objeções que o Marcos já usa no PS Institute |
| Ativação real | Kommo no H2 | Config pronta, mas só entra em produção quando o CRM pago existir |
| Escalonamento | 3 gatilhos | Sem resposta, sem instalar, sem ativar — todos com alerta automático |
| Testes simulados | 5 leads | Cobrindo as 3 personas + 2 objeções difíceis |

## Achados principais

- **[Contexto]** O agente cobre só o funil **orgânico** de ponta a ponta — no funil via parceiro, só recebe o relato de handoff, porque a qualificação já aconteceu na relação pessoal do parceiro.
- **[Vantagem]** A cadência D+24h/D+3/D+8 e os scripts de objeção reaproveitam quase 1:1 o que o Marcos já validou no PS Institute.
- **[Ameaça]** Sem o brandbook ainda, o tom usado é uma aproximação — pode precisar ajuste quando `ee-s3-brandbook` existir.
- **[Ação]** Configurar os 3 gatilhos de escalonamento antes de ligar o agente — são a rede de segurança contra o churn silencioso já visto no caso da distribuidora de bebidas.

## ⚠️ Alerta de honestidade

Este documento configura o **comportamento** do agente, mas não substitui o brandbook nem testa com leads reais — os "5 leads simulados" são cenários hipotéticos construídos a partir das personas já mapeadas. Validar com leads reais do Horizonte 1 antes de confiar 100% na automação.

## 💬 Ponto de alavancagem

**O agente não substitui o julgamento do Marcos — ele aplica a disciplina que ele já tem, em escala, nos momentos em que ele não pode estar presente.**

1. O critério de desqualificação precisa estar no agente, não só na cabeça do Marcos.
2. A cadência D+24h/D+3/D+8 já provou reativar lead frio (caso Dra. Marja) — reaplicar em vez de inventar do zero.
3. O agente precisa saber quando **não** insistir — mesma ética comercial que o Marcos já demonstrou.

**Ponto de discussão:** revisar os scripts com o Marcos antes de ativar — ele sabe se o tom soa natural pro público real.

---

## Fluxo 1 — Cliente orgânico

**Persona do agente:** direto, sem jargão, paciente com baixa maturidade digital. Nunca soa como robô lendo script.

| Etapa | Mensagem/ação | Lógica |
|---|---|---|
| Primeiro contato | "Oi! Vi que você quer parar de perder tempo com caderninho/calculadora... seu comércio é padaria, mercearia, conveniência ou outro?" | Confirma encaixe no ICP antes de gastar mensagens |
| Qualificação | 3 perguntas: já usa sistema? sabe da obrigatoriedade a partir de 01/08/2026? internet cai? | Se internet instável + sem sistema → reforça "funciona 100% offline" |
| Desqualificação | Se não for o tipo de negócio ou pedir "de graça" com insistência | Agradece e não segue — não força qualificação artificial |
| Onboarding D0 | Envia link + vídeo curto | Ligado ao ajuste de UX de `ee-s2-diagnostico-cro` |
| Checagem D+1 | "Conseguiu instalar?" | Sem resposta 24h → tenta 1x mais → sem resposta de novo → alerta humano |
| Checagem D+3 | "Já cadastrou os primeiros produtos?" | Perfil de baixa maturidade digital → oferece call de 10 min em vez de insistir só por texto |
| Ativação | "Parabéns, seu primeiro cupom saiu certinho! 🎉" | Gatilho automático via detecção real, não pergunta |
| Sem ativação em 7 dias | "Vi que ainda não rodou nenhuma venda — teve dificuldade?" | Resposta indicando dificuldade → alerta humano imediato (evita repetir o caso da distribuidora de bebidas) |

## Fluxo 2 — Auto-report do parceiro *(a partir do Horizonte 2)*

| Gatilho | Resposta do bot |
|---|---|
| Parceiro avisa "fechei com um cliente" | "Boa! Me passa: nome, contato, e já emitiu cupom ou só instalou?" |
| Parceiro responde com os dados | "Registrado! Se ainda não emitiu, vou acompanhar e te aviso se precisar de um empurrão." |
| 7 dias sem ativação do cliente reportado | "Lembra do [lojista] que você indicou? Ainda não rodou venda — vale checar com ele?" |

Cria registro direto na etapa "Recebido do parceiro" do pipeline Clientes-via-parceiro (`ee-s3-crm-setup`), com o campo "trazido por" preenchido automaticamente.

## Gatilhos de escalonamento humano

| Gatilho | Ação |
|---|---|
| Lead sem resposta após 2 tentativas | Marca como frio, não insiste mais |
| Cliente instalado sem ativar em 7 dias | Alerta humano |
| Parceiro reporta handoff, cliente não ativa em 7 dias | Avisa o parceiro primeiro; escala pro Gestor de Canais depois |

## Testes com leads simulados

| Persona/cenário | O que se espera do agente |
|---|---|
| Seu Geraldo — responde devagar, medo de errar | Oferece ligação em vez de insistir só por texto (D+3) |
| Dona Maria — pergunta sobre "cobrança surpresa" | Resposta objetiva sobre preço fixo, sem rodeio |
| Otávio — quer resolver tudo sozinho | Não empurra atendimento humano desnecessário |
| Lead fora do ICP (prestador de serviço) | Testa desqualificação — agradece e não segue |
| Lead pedindo sistema de graça com insistência | Reconhece o padrão da SWOT e recusa educadamente |

---

## Pendências para confirmação do operador

1. Validar o tom dos scripts com o Marcos antes de ativar.
2. Confirmar prazo exato de escalonamento (mesma pendência do `ee-s3-crm-setup`).
3. Revisar linguagem quando `ee-s3-brandbook` existir.
