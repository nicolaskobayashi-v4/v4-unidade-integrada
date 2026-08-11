---
name: client-knowledge-sync
description: Sincronizar, de forma controlada e auditável, conhecimento operacional do cliente entre uma origem autorizada e o workspace. Usar quando houver material novo ou divergente a comparar; não usar para reescrever estratégia, duplicar a skill ee-adicionar-base ou copiar arquivos sem aprovação.
---

# Client Knowledge Sync

## 1. Propósito

Preparar a base operacional necessária a uma landing page sem alterar a estratégia aprovada. Comparar origem e destino, classificar diferenças e propor uma sincronização mínima, reversível e autorizada.

## 2. Quando usar

- Quando uma origem autorizada contiver documentos de cliente ainda não presentes no workspace.
- Quando houver suspeita de divergência entre arquivos homônimos ou versões da base.
- Antes da auditoria de fontes, se a base operacional puder estar desatualizada.

## 3. Quando NÃO usar

- Para captar, formular ou revisar estratégia; encaminhar esse trabalho à matriz.
- Para substituir `ee-adicionar-base`, cujo escopo é adicionar conteúdo estratégico à base.
- Para sincronizar `outputs/`, caches, temporários, credenciais, tokens ou arquivos `.env`.
- Quando a origem, o destino ou a autorização não estiverem inequívocos.

## 4. Pré-condições

1. Ler o `AGENTS.md` raiz e qualquer instrução local aplicável.
2. Auditar branch, worktree, origem, destino e arquivos-alvo sem escrever.
3. Confirmar que o repositório-fonte será somente leitura.
4. Confirmar que a operação não tocará o plugin da matriz nem outputs existentes.
5. Obter autorização explícita para cada futura cópia ou atualização.

## 5. Entradas

- Caminho absoluto da origem autorizada, somente leitura.
- Caminho do workspace do cliente.
- `clientes/<slug>/client.json`, quando existir.
- Lista de documentos solicitados e limites da sincronização.
- Confirmações humanas recentes sobre fatos ou versões.

## 6. Fontes permitidas

- Arquivos indicados explicitamente pelo responsável.
- `client.json`, base de conhecimento e outputs estratégicos aprovados.
- Histórico Git para identificar origem e divergência.
- Metadados de arquivo, hashes e comparação textual.

Referências externas servem apenas como repertório; nunca estabelecem fatos do cliente.

## 7. Precedência das fontes

Aplicar a precedência por contexto e registrar conflitos:

- Fatos: confirmação explícita mais recente → `client.json` → base estratégica aprovada → outputs estratégicos aprovados → implementação existente.
- Visual: confirmação explícita mais recente → Manual de Marca aprovado mais recente → diagnóstico visual aprovado → assets oficiais → referências externas → implementação existente.
- Copy: copy explicitamente aprovada → output estratégico de landing page aprovado → implementação existente.
- Links: link explicitamente confirmado → implementação existente aprovada.

Um documento especializado aprovado posteriormente pode prevalecer em seu domínio, desde que a divergência seja registrada. Nunca resolver conflito silenciosamente.

## 8. Procedimento

1. Inventariar origem e destino sem ler secrets e sem percorrer diretórios excluídos.
2. Excluir `outputs/`, caches, temporários, dependências, `.env` e arquivos de credenciais.
3. Comparar caminhos relativos, tamanho, data e hash com `Get-FileHash`.
4. Para arquivos textuais divergentes, comparar conteúdo com Git ou `Compare-Object`.
5. Classificar cada item como novo, idêntico, divergente ou exclusivo do destino.
6. Preservar todo item exclusivo do destino; nunca apagá-lo nem substituí-lo por conveniência.
7. Identificar conflitos de fatos, visual, copy e links pela precedência contextual.
8. Apresentar plano de cópia arquivo a arquivo, com origem, destino, ação e risco.
9. Parar e solicitar autorização explícita antes de qualquer escrita.
10. Em execução futura autorizada, copiar somente os itens aprovados e validar hashes/conteúdo depois da operação.

## 9. Saídas esperadas

- Inventário comparativo de origem e destino.
- Relação de itens novos, idênticos, divergentes e exclusivos do destino.
- Registro de conflitos de precedência e lacunas críticas.
- Plano de sincronização proposto; cópia somente em execução futura autorizada.

## 10. Critérios de parada

Parar com estado `BLOCKED` se faltar origem confiável, destino inequívoco, autorização, dado crítico ou se houver risco de sobrescrita, exposição de secret ou perda de material. Não preencher lacunas com fatos, claims, depoimentos, links, preços ou métricas inventados.

## 11. Checkpoints humanos

- Aprovar o inventário e os diretórios excluídos.
- Resolver conflitos de precedência.
- Aprovar explicitamente cada escrita proposta.
- Revisar o resultado antes de qualquer commit ou push, que exigem autorização separada.

## 12. Proteções

O `AGENTS.md` raiz é superior e nenhuma regra local pode enfraquecê-lo. Tratar o plugin da matriz como somente leitura e seus outputs apenas como entradas. Não alterar fonte, destino exclusivo, copy, link ou asset sem aprovação. Não ler secrets. Vercel Preview requer aprovação explícita; Production permanece proibida.

## 13. Integração com a matriz

Consumir, sem modificar, `ee-adicionar-base`, outputs estratégicos e a convenção `client.json`. Esta skill estende a matriz com comparação operacional entre repositórios; não cria estratégia, não executa mutações da matriz e não replica suas instruções integrais.

## 14. Ferramentas reutilizáveis

- Disponíveis: `Get-FileHash`, `Compare-Object`, `git status`, `git diff --no-index` e `git log`.
- Planejadas: relatório persistido e manifesto de sincronização, somente após desenho e aprovação próprios.
- Humanas: validação de domínio, versão aprovada e resolução de conflito.
- Proibidas: automações de cópia em massa, leitura de secrets e sincronização destrutiva.

## 15. Ações proibidas

- Modificar o repositório-fonte, o plugin, outputs existentes ou arquivos não autorizados.
- Apagar, mover, renomear ou sobrescrever itens exclusivos do destino.
- Copiar caches, temporários, outputs, dependências ou credenciais.
- Fazer commit, push, Preview ou Production como efeito colateral.

## 16. Definição de sucesso

A base operacional fica comparada de forma rastreável, conflitos e lacunas ficam explícitos, e qualquer sincronização futura possui plano mínimo e autorização específica sem perda de dados nem alteração estratégica.
