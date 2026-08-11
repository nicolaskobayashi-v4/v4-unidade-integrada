# Governança de agentes — workspace integrado

## Escopo e precedência

O Codex é o agente operacional principal deste workspace.

Estas regras valem para todo o repositório. Instruções locais mais específicas podem complementar as regras da raiz dentro de seu próprio escopo, desde que não reduzam as proteções de dados, integridade e publicação definidas aqui.

O subtree `plugins/v4-estruturacao-ia/` preserva as instruções herdadas da matriz. Durante o piloto de landing pages, mudanças dentro desse plugin devem ser evitadas para reduzir divergências e conflitos com futuras atualizações da matriz.

## Fontes de informação do cliente

- `clientes/<slug>/client.json` é a fonte principal de informações estruturadas do cliente.
- A `base-de-conhecimento/` e os `outputs/` existentes devem ser consultados quando forem relevantes para a tarefa.
- Dados ausentes nunca podem ser inventados, inferidos como fatos ou preenchidos com placeholders que pareçam reais.
- Outputs existentes nunca podem ser modificados sem autorização explícita do usuário.
- Credenciais, tokens, secrets e arquivos `.env` nunca devem ser lidos, copiados, exibidos ou expostos.

## Camada operacional de landing pages

As skills operacionais de landing pages ficam em `.agents/skills/`:

- `client-knowledge-sync`;
- `lp-source-audit`;
- `lp-baseline-prepare`;
- `lp-design-adapter`;
- `lp-asset-pipeline`;
- `lp-quality-gate`;
- `lp-release`;
- `lp-orchestrator`.

Ao trabalhar com landing pages, o agente deve verificar se uma skill local é aplicável antes de improvisar procedimento equivalente. A matriz responde por estratégia, posicionamento, copy, CRO, identidade e outputs estruturados. A unidade responde por localizar a implementação, proteger a baseline, trabalhar código e aplicação visual, governar assets, executar QA, operar Git e preparar Preview. O subtree `plugins/v4-estruturacao-ia/` permanece somente leitura para essa camada.

Não recriar na unidade posicionamento, CRO, Manual de Marca, diagnóstico criativo ou geração estratégica de copy quando os outputs aprovados da matriz já existirem. Esses outputs são entradas; nunca devem ser modificados pelas skills locais.

Qualquer escrita exige escopo autorizado. Alterações de copy, links, claims e assets exigem autorização específica. Commit, push e Vercel Preview são autorizações independentes e não se autorizam mutuamente. Na V1, Production permanece desabilitada e `vercel --prod` é proibido. Ausência de informação crítica exige `STOP`.

## Segurança operacional

- Uma auditoria de branch, estado do repositório, arquivos-alvo e escopo deve ocorrer antes de qualquer escrita.
- Nenhuma automação pode publicar em produção durante o piloto.
- Nenhum arquivo, frame, código ou página existente do Figma, do cliente ou de qualquer destino alternativo pode ser sobrescrito.
- O agente deve trabalhar sempre em cópias, branches e ambientes de teste.
- Cada execução do piloto pode modificar somente uma seção de landing page.
- O agente deve parar quando houver risco de perda visual, alteração não autorizada de copy ou substituição de assets.
- Novos artefatos do piloto devem ficar isolados dos outputs atuais e ser identificados explicitamente como teste.

## Regras específicas do piloto de landing pages

- O fluxo principal é: Figma aprovado → Codex no VS Code → HTML, CSS e JavaScript versionados → testes locais → Git → Vercel Preview → revisão humana.
- O Figma original é somente leitura; qualquer trabalho deve ocorrer em arquivo duplicado.
- A implementação deve ocorrer em uma cópia isolada da landing page.
- Antes de editar Figma ou código, o agente deve apresentar um plano e confirmar que os originais permanecem protegidos.
- Qualquer escrita exige aprovação explícita, limitada aos arquivos, frames e operações descritos no plano.
- Testes locais devem ser concluídos antes de solicitar uma Vercel Preview.
- A criação de uma Vercel Preview exige aprovação explícita do usuário.
- Deployment em produção é proibido durante o piloto e só poderá ocorrer futuramente após aprovação explícita do usuário.
- GreatPages é apenas um possível adaptador ou destino alternativo futuro, ainda não implementado e fora do escopo do piloto atual.
- Se a fidelidade visual, a copy ou os assets não puderem ser preservados com segurança, a execução deve ser interrompida e submetida à revisão humana.

## Local dos artefatos do piloto

Todos os relatórios e registros do piloto devem ser criados exclusivamente em:

`clientes/instituto-salotti/outputs/landing-pages/piloto-figma-vercel/`

É proibido modificar:

- clientes/instituto-salotti/outputs/landing-page.html;
- clientes/instituto-salotti/outputs/landing-page/;
- clientes/instituto-salotti/outputs/deploy/;
- qualquer outro output existente do cliente.

Esses materiais podem ser consultados somente como referência. Nenhum arquivo existente pode ser sobrescrito, movido, renomeado ou reformatado.

## Auditoria e aprovação no Figma

- A auditoria inicial deve ser exclusivamente de leitura.
- Depois da auditoria, o agente deve apresentar um plano antes de editar Figma ou código.
- Nenhuma escrita no Figma ou no código pode ocorrer sem aprovação explícita do usuário.
- A aprovação vale somente para os arquivos, o frame e as operações descritas no plano.

## Fontes de verdade durante o piloto

- Conteúdo e dados do cliente:
  client.json, base-de-conhecimento e outputs aprovados.

- Referência visual:
  frame aprovado e preservado no Figma.

- Implementação operacional:
  arquivos HTML, CSS e JavaScript versionados no Git.

- Homologação:
  Vercel Preview.

- Produção:
  deployment da Vercel autorizado explicitamente pelo usuário.

- Histórico e decisões:
  repositório Git.

A Vercel não substitui o Figma como referência visual nem o Git como fonte da implementação.

## Controle de versão

- Commit e push só podem ocorrer após aprovação explícita do usuário.
- A aprovação para escrita no Figma não autoriza commit ou push no repositório.
