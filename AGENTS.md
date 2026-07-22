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

## Segurança operacional

- Uma auditoria de branch, estado do repositório, arquivos-alvo e escopo deve ocorrer antes de qualquer escrita.
- Nenhuma automação pode publicar em produção durante o piloto.
- Nenhuma página existente do Figma, GreatPages ou de cliente pode ser sobrescrita.
- O agente deve trabalhar sempre em cópias, branches e ambientes de teste.
- Cada execução do piloto pode modificar somente uma seção de landing page.
- O agente deve parar quando houver risco de perda visual, alteração não autorizada de copy ou substituição de assets.
- Novos artefatos do piloto devem ficar isolados dos outputs atuais e ser identificados explicitamente como teste.

## Regras específicas do piloto de landing pages

- O fluxo inicial é unidirecional: Figma → Codex → preparação estrutural → GreatPages.
- O Figma original é somente leitura; qualquer trabalho deve ocorrer em arquivo duplicado.
- O GreatPages deve usar página nova, de teste e não publicada.
- Antes de qualquer escrita, o agente deve registrar o que pretende criar ou modificar e confirmar que os originais permanecem protegidos.
- Se a fidelidade visual, a copy ou os assets não puderem ser preservados com segurança, a execução deve ser interrompida e submetida à revisão humana.

## Local dos artefatos do piloto

Todos os relatórios e registros do piloto devem ser criados exclusivamente em:

`clientes/instituto-salotti/outputs/landing-pages/piloto-figma-greatpages/`

É proibido modificar:

- clientes/instituto-salotti/outputs/landing-page.html;
- clientes/instituto-salotti/outputs/landing-page/;
- clientes/instituto-salotti/outputs/deploy/;
- qualquer outro output existente do cliente.

## Auditoria e aprovação no Figma

- A auditoria inicial deve ser exclusivamente de leitura.
- Depois da auditoria, o agente deve apresentar um plano de alterações.
- Nenhuma escrita no Figma pode ocorrer sem aprovação explícita do usuário.
- A aprovação vale somente para o frame e para as operações descritas no plano.

## Fontes de verdade durante o piloto

- Conteúdo e dados do cliente:
  client.json, base-de-conhecimento e outputs aprovados.

- Referência visual:
  frame de referência preservado na cópia do Figma.

- Estrutura preparada:
  frame de exportação da cópia do Figma.

- Implementação de teste:
  página não publicada no GreatPages.

- Histórico e decisões:
  repositório Git.

## Controle de versão

- Commit e push só podem ocorrer após aprovação explícita do usuário.
- A aprovação para escrita no Figma não autoriza commit ou push no repositório.
