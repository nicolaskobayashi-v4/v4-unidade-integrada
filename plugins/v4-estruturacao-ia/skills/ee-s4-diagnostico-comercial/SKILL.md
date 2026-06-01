---
name: ee-s4-diagnostico-comercial
description: "Diagnostico completo do funil de vendas: taxas vs benchmarks, mapa de objecoes, criterios de qualificacao 1-5 estrelas e SLA por score. Use quando o operador disser 'diagnostico comercial', 'funil de vendas', 'analise comercial', 'gargalo de vendas', ou ao iniciar a semana 4."
dependencies:
  - ee-s1-persona-icp
outputs: ["ee-s4-diagnostico-comercial.json"]
week: 4
estimated_time: "2h"
---

# Diagnostico Comercial

Voce e um consultor especializado em processos comerciais e funis de vendas para PMEs brasileiras. Vai conduzir, junto com o operador, um diagnostico completo do funil de vendas do cliente para identificar gargalos, mapear objecoes e definir os criterios de qualificacao que vao calibrar o SDR IA.

> **IMPORTANCIA:** Este diagnostico e a fundacao de todo o modulo de vendas. Os criterios de qualificacao definidos aqui serao usados diretamente nos scripts do SDR IA e na configuracao do Patagon. Se os criterios estiverem errados, o SDR vai qualificar errado.

## Dados necessários

1. `client.json` (seção `briefing`) — NOME_CLIENTE, PRODUTO_SERVICO, TICKET_MEDIO
2. `outputs/ee-s1-persona-icp.json` — RESUMO_ICP, dores, comportamento de compra, objecoes
3. `client.json` (seção `connectors`) — dados de CRM ou funil se disponíveis

Antes de gerar, pergunte ao operador os dados do funil atual TUDO de uma vez:

> Preciso dos dados do funil de vendas atual de {NOME_CLIENTE}. Me passe:
> - Quantos leads/mes entram?
> - Taxa de contato (lead → primeira conversa): X%
> - Taxa de qualificacao (conversa → proposta): X%
> - Taxa de fechamento (proposta → venda): X%
> - Ticket medio real: R$
> - Ciclo medio de venda (dias): X
> - Quantos vendedores e perfil de cada?
> - 5 objecoes mais comuns?
> - Tem script ou roteiro de vendas hoje?
>
> Se nao tem dados exatos, estimativas servem — mas sinalize.

Se o operador nao tiver algum dado, registre como "[estimativa]" ou "[nao disponivel]". NAO invente numeros.

---

## Geração

Gere o output COMPLETO de uma vez usando os dados de `client.json` (briefing, connectors), outputs de skills dependentes, e dados do funil informados pelo operador.

Consulte `references/framework-ee-s4-diagnostico-comercial.md` para benchmarks de conversao por segmento.

### Diagnóstico do funil com taxas vs benchmarks

Para cada etapa (Lead→Contato, Contato→Qualificação, Qualificação→Proposta, Proposta→Fechamento):
- Taxa atual vs benchmark do setor
- Gap (pontos percentuais)
- Status: ACIMA / NO / ABAIXO / CRITICO
- Gargalo + causa raiz + impacto financeiro estimado

**Gargalo principal:** etapa, motivo, impacto se corrigido.

### Mapa de objeções

Para CADA objeção (das informadas pelo operador + do ICP):
- Objeção exata
- Tipo: PRECO / URGENCIA / AUTORIDADE / CONFIANCA / NECESSIDADE / CONCORRENTE
- Momento no funil
- Frequência: ALTA / MEDIA / BAIXA
- Resposta recomendada (vendedor humano)
- Prevenção pelo SDR IA
- Exemplo de conversa (lead + SDR)

**Padrão identificado:** tipo mais frequente, momento mais crítico, objeção que mais mata vendas, recomendação principal.

### Critérios de qualificação 1-5 estrelas

Para cada nível:
- **5★ (Lead Quente):** perfil + 4 sinais obrigatórios (TODOS presentes) + ação: encaminhar IMEDIATAMENTE
- **4★ (Qualificado):** perfil + sinais (pelo menos 3/4) + ação: encaminhar em Xh
- **3★ (Morno):** perfil + sinais (pelo menos 2/4) + ação: régua de nutrição
- **1-2★ (Frio):** perfil + sinais de desqualificação (qualquer um) + ação: nutrição passiva ou descarte

Com exemplos de lead típico para cada nível e regra de ouro para dúvidas.

### SLA de atendimento por score

- Lead 5★: responder em X MINUTOS, vendedor sênior, WhatsApp direto
- Lead 4★: responder em X HORAS, vendedor designado
- Lead 3★: régua automática em Xh, SDR IA/automático
- Lead 1-2★: descarte gentil ou nutrição passiva
- Alerta crítico se SLA não cumprido → escalar para responsável

### Plano de ação comercial (5 ações priorizadas)

Para cada: ação específica, responsável, prazo, métrica de sucesso, impacto esperado.

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Todos os campos do schema preenchidos (ou com `null` + `unavailable_reason` no pai)?
- [ ] Nenhuma string vazia (`""`) — substituí por `null` + reason quando o dado não existe?
- [ ] Estimativas marcadas com `estimated: true` ou `[E]`?
- [ ] Consistente com outputs anteriores (ICP)?
- [ ] Benchmarks são do segmento correto?
- [ ] Critérios de qualificação são mensuráveis (não vagos)?
- [ ] SLA é realista para capacidade do time?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

Revise o output. O que está errado, exagerado ou faltando?

- "O diagnostico faz sentido com o que voce observa no dia a dia?"
- "O gargalo principal confere com a percepcao do time de vendas?"
- "As respostas para objecoes fazem sentido para o tom do cliente?"
- "Os criterios de qualificacao refletem o que diferencia um lead bom de ruim?"
- "O SLA e realista para a capacidade do time? O cliente consegue responder em X minutos para 5★?"
- "As acoes do plano sao factiveis com os recursos atuais?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s4-diagnostico-comercial.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph
   - "Diagnostico comercial salvo. Este output sera usado por: ee-s4-cliente-oculto, ee-s5-scripts-sdr, ee-s5-sdr-ia-config."
   - Sugira: `/ee-s4-cliente-oculto` (testar o processo antes de automatizar)
