# Skills de produção de landing pages — V1

Este guia resume o uso operacional das skills em `.agents/skills/`. Os respectivos `SKILL.md` são os contratos normativos e devem ser lidos quando a skill for acionada.

## `client-knowledge-sync`

### Para que serve

Comparar uma origem autorizada com a base operacional do cliente e preparar uma sincronização mínima, rastreável e não destrutiva.

### Quando usar

Quando houver documentos novos, versões divergentes ou suspeita de base operacional desatualizada.

### Quando não usar

Para onboarding estratégico, revisão de estratégia, sincronização de outputs ou substituição de `ee-adicionar-base`.

### Entrada típica

Origem somente leitura, workspace do cliente, `client.json` quando existir e lista dos documentos em escopo.

### Saída típica

Inventário comparativo, conflitos, lacunas e plano de cópia arquivo a arquivo.

### Pode escrever?

Sim, mas somente depois de autorização explícita para cada cópia ou atualização. Nunca altera a origem nem apaga conteúdo exclusivo do destino.

### Checkpoint humano

Aprovar inventário, conflitos de precedência e operações de escrita propostas.

### Integração com matriz

Consulta `ee-adicionar-base`, `client.json` e outputs aprovados sem duplicar captação ou formulação estratégica.

### Exemplo de solicitação ao Codex

> Use `client-knowledge-sync` para comparar a pasta autorizada com a base do cliente X. Apresente o plano e pare antes de copiar.

## `lp-source-audit`

### Para que serve

Identificar a implementação correta, mapear fontes e avaliar a prontidão da landing page antes de qualquer edição.

### Quando usar

No início ou retomada do trabalho, especialmente quando houver múltiplas versões, assets ou fontes conflitantes.

### Quando não usar

Para corrigir arquivos, executar diagnóstico com efeitos colaterais ou escolher silenciosamente entre fontes conflitantes.

### Entrada típica

Implementações candidatas, `client.json`, outputs estratégicos, Manual de Marca, diagnósticos, copy, links e assets.

### Saída típica

Mapa de fontes, implementação recomendada, lacunas, duplicatas e decisão de prontidão ou `BLOCKED`.

### Pode escrever?

Não. A auditoria é estritamente read-only.

### Checkpoint humano

Confirmar a implementação candidata e resolver conflitos antes da baseline.

### Integração com matriz

Consome outputs de landing page, posicionamento, Manual de Marca, CRO, diagnóstico criativo e revisores como evidências somente leitura.

### Exemplo de solicitação ao Codex

> Use `lp-source-audit` para auditar a LP X do cliente Y. Não altere arquivos.

## `lp-baseline-prepare`

### Para que serve

Separar uma referência imutável da cópia de trabalho antes da primeira alteração.

### Quando usar

Depois da auditoria aprovada, quando ainda não existirem `reference/` e `src/` isolados.

### Quando não usar

Com fonte ambígua, destinos preexistentes, risco de sobrescrita ou ausência de autorização.

### Entrada típica

Implementação aprovada, caminhos novos, lista de arquivos, hashes e estado Git.

### Saída típica

`reference/` congelado, `src/` equivalente e manifesto humano de origem e hashes.

### Pode escrever?

Sim, somente nos caminhos novos e explicitamente autorizados. Não modifica código, origem, outputs existentes ou `reference/` depois de criado.

### Checkpoint humano

Aprovar caminhos e cópias; confirmar a imutabilidade da referência; autorizar separadamente a primeira seção.

### Integração com matriz

Usa a implementação indicada pela auditoria e outputs aprovados apenas como evidência.

### Exemplo de solicitação ao Codex

> Use `lp-baseline-prepare` para propor `reference/` e `src/` da LP X. Não copie antes da minha aprovação.

## `lp-design-adapter`

### Para que serve

Adaptar visualmente uma seção autorizada, preservando copy, links, claims, assets e estrutura comercial.

### Quando usar

Para adaptação por seção, aplicação de marca, correções visuais ou uma etapa de programa de redesign completo.

### Quando não usar

Para alterar a página inteira em uma execução, recriar estratégia, decidir copy ou inserir assets não autorizados.

### Entrada típica

Baseline, `src/`, seção autorizada, conteúdo congelado, Manual de Marca, diagnóstico visual e assets oficiais.

### Saída típica

Uma seção adaptada em `src/`, decisões visuais registradas e comparação com a baseline.

### Pode escrever?

Sim, somente na seção e nos arquivos autorizados em `src/`. Redesign completo significa várias execuções, uma seção por vez.

### Checkpoint humano

Aprovar o plano antes da escrita e revisar estética e responsividade antes da próxima seção.

### Integração com matriz

Aplica outputs aprovados de landing page, Manual de Marca, posicionamento e diagnósticos sem refazê-los.

### Exemplo de solicitação ao Codex

> Use `lp-design-adapter` somente na seção Hero já autorizada. Preserve copy, links e assets.

## `lp-asset-pipeline`

### Para que serve

Governar origem, direitos, original, derivados, crops, fallbacks e uso responsivo dos assets.

### Quando usar

Quando a seção possuir assets que precisem ser inventariados, derivados ou referenciados de forma responsiva.

### Quando não usar

Para selecionar stock arbitrariamente, presumir direitos, instalar processadores ou substituir imagens sem aprovação.

### Entrada típica

Assets oficiais, metadados, baseline, Manual de Marca, requisitos de crop e viewports.

### Saída típica

Inventário de assets, cadeia original-derivado-produção, variantes e plano de referências no código.

### Pode escrever?

Sim, depois de aprovação das transformações e destinos. Pode criar derivados e atualizar referências no código autorizado; nunca sobrescreve o original.

### Checkpoint humano

Confirmar direitos, seleção, transformações, crops, fallbacks e resultado visual.

### Integração com matriz

Consome Manual de Marca e diagnósticos visual/criativo sem duplicar suas decisões.

### Exemplo de solicitação ao Codex

> Use `lp-asset-pipeline` para inventariar os assets da Hero. Não processe nem substitua arquivos antes da aprovação.

## `lp-quality-gate`

### Para que serve

Auditar conteúdo, baseline, design, acessibilidade, responsividade, código, runtime, assets e Git antes do release.

### Quando usar

Depois da revisão da implementação e dos assets, e novamente após qualquer correção relevante.

### Quando não usar

Para corrigir silenciosamente problemas, aprovar fatos ou substituir revisão humana.

### Entrada típica

`reference/`, `src/`, escopo autorizado, fontes aprovadas, evidências locais e estado Git.

### Saída típica

Checklist com evidências, achados e decisão `PASS`, `PASS_WITH_WARNINGS` ou `BLOCKED`.

### Pode escrever?

Não. O gate identifica, classifica e bloqueia; não corrige código, copy, links ou assets.

### Checkpoint humano

Validar fidelidade visual e aceitar warnings não bloqueadores. Correções acontecem em execução separada e invalidam o gate anterior.

### Integração com matriz

Compõe conceitos do revisor e dos validadores matriciais, usando-os somente quando compatíveis e sem efeitos colaterais não autorizados.

### Exemplo de solicitação ao Codex

> Execute `lp-quality-gate` na implementação atual e pare se retornar `BLOCKED`.

## `lp-release`

### Para que serve

Validar artefato, destino e aprovações antes de uma eventual Vercel Preview.

### Quando usar

Somente depois de quality gate válido e testes locais concluídos.

### Quando não usar

Para assumir QA, corrigir a implementação, criar projeto Vercel, promover deploy ou executar Production.

### Entrada típica

Quality gate vigente, diretório, branch, commit, worktree, projeto/equipe confirmados e autorização humana.

### Saída típica

Checklist de release e, quando autorizada, URL de uma Preview isolada.

### Pode escrever?

Não altera código ou assets. É a única skill que pode executar Preview, exclusivamente depois de autorização explícita. Nunca executa Production.

### Checkpoint humano

Confirmar destino e autorizar Preview imediatamente antes da ação; depois, revisar a URL criada.

### Integração com matriz

Consome validações aprovadas, mas rejeita `vercel --prod`, mutações de cliente/cache e destinos presumidos.

### Exemplo de solicitação ao Codex

> Use `lp-release` para preparar o checklist da Preview. Não faça deploy até eu autorizar o destino apresentado.

## `lp-orchestrator`

### Para que serve

Coordenar estados, interrupções, retomadas e o próximo gate sem executar o trabalho especializado.

### Quando usar

Para iniciar ou retomar um fluxo, localizar o último estado válido e descobrir a próxima skill aplicável.

### Quando não usar

Para editar design/código, decidir conteúdo, alterar assets/links, fazer commit, push ou deploy.

### Entrada típica

Pedido atual, evidências das skills, aprovações, estado Git e outputs matriciais aprovados.

### Saída típica

Estado comprovado, bloqueio preciso, responsável, próximo gate e checkpoint humano pendente.

### Pode escrever?

Não executa mudanças especializadas nem persiste estado automaticamente na V1.

### Checkpoint humano

Cada transição depende do gate correspondente; silêncio ou aprovação anterior nunca autorizam a próxima etapa.

### Integração com matriz

Separa a estratégia produzida pela matriz da execução operacional da unidade e não modifica `client.json` automaticamente.

### Exemplo de solicitação ao Codex

> Use `lp-orchestrator` para identificar o último estado válido da LP X e informe somente o próximo gate.

## Matriz de permissões

| Skill | Read-only? | Pode alterar código? | Pode alterar assets? | Pode publicar Preview? | Exige aprovação? |
|---|---|---|---|---|---|
| `client-knowledge-sync` | Não | Não | Não | Não | Sim, antes de escrever |
| `lp-source-audit` | Sim | Não | Não | Não | Para avançar após a auditoria |
| `lp-baseline-prepare` | Não | Não; apenas prepara cópias | Não | Não | Sim |
| `lp-design-adapter` | Não | Sim, uma seção autorizada | Não | Não | Sim |
| `lp-asset-pipeline` | Não | Somente referências autorizadas | Sim, sem tocar o original | Não | Sim |
| `lp-quality-gate` | Sim | Não | Não | Não | Para aceitar warnings e avançar |
| `lp-release` | Read-only até a ação autorizada | Não | Não | Sim, somente Preview | Sim |
| `lp-orchestrator` | Sim quanto aos artefatos | Não | Não | Não | Em cada gate |

Nenhuma skill pode publicar Production. Commit, push e Preview são autorizações independentes.
