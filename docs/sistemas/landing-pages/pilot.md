# Piloto — Hero do Instituto Salotti

## Escopo

- Cliente piloto: Instituto Salotti.
- Seção testada: somente a Hero.
- Variações: desktop e mobile.
- Objetivo: validar o fluxo Figma → Codex → HTML/CSS/JavaScript → testes locais → Git → Vercel Preview sem afetar materiais atuais do cliente.

## Proteção dos originais

- O arquivo Figma original será tratado como somente leitura.
- O trabalho ocorrerá em um arquivo Figma piloto duplicado.
- O frame usado como referência será preservado sem alterações.
- A implementação ocorrerá em uma cópia isolada da landing page, sem alterar os outputs existentes.
- Nenhum output atual em `clientes/instituto-salotti/` será alterado.
- A Hero será usada apenas como referência em uma cópia de teste.

Os outputs existentes abaixo são imutáveis durante o piloto:

- `clientes/instituto-salotti/outputs/landing-page.html`;
- `clientes/instituto-salotti/outputs/landing-page/`;
- `clientes/instituto-salotti/outputs/deploy/`.

Eles podem ser consultados somente como referência. Nenhum arquivo existente pode ser sobrescrito, movido, renomeado ou reformatado.

Todos os novos relatórios e registros devem ficar exclusivamente em:

```text
clientes/instituto-salotti/outputs/landing-pages/piloto-figma-vercel/
```

Esse diretório ainda não deve ser criado durante a atualização documental.

## Auditoria e autorização no Figma

- A auditoria inicial do Figma é exclusivamente de leitura.
- Depois da auditoria, o agente deve apresentar um plano antes de editar Figma ou código.
- Nenhuma escrita no Figma ou no código pode ocorrer sem aprovação explícita do usuário.
- A aprovação é limitada aos arquivos, ao frame e às operações descritas no plano; qualquer ampliação exige nova aprovação.

## Primeiro teste de escrita no Figma

- O servidor MCP oficial do Figma foi conectado e autenticado.
- A conta utilizada possui plano Pro e acesso Full.
- As ferramentas de escrita permaneceram bloqueadas até uma autorização específica.
- `use_figma` foi temporariamente liberado apenas para uma operação.
- A operação autorizada tentaria criar uma página isolada, uma cópia da Hero desktop e um frame mobile vazio.
- A chamada falhou porque o ambiente MCP não conseguiu carregar a fonte personalizada `PF Marlet Display Light`.
- Nenhuma página, frame ou node foi criado e nenhum estado parcial precisou ser removido.
- O node original e o repositório permaneceram inalterados.
- Nenhuma segunda tentativa foi executada.
- `use_figma` voltou a ser bloqueado.

## Fluxo aprovado para criação do mobile

```text
Figma desktop aprovado
    ↓
Codex cria proposta mobile em HTML/CSS
    ↓
teste local em 360, 390 e 430 px
    ↓
Code to Canvas
    ↓
frame mobile editável na cópia piloto do Figma
    ↓
revisão e aprovação humana
    ↓
ajustes finais no código
    ↓
Vercel Preview
```

- O Figma desktop continua sendo a referência visual aprovada.
- A primeira proposta mobile no código não será considerada design aprovado.
- O frame mobile somente se torna referência após revisão humana no Figma.
- `generate_figma_design` continuará bloqueado até a proposta local estar aprovada para captura.
- A captura Code to Canvas será autorizada em execução separada.
- Nenhuma publicação ou Vercel Preview acontecerá antes da aprovação do frame mobile.
- A limitação encontrada deverá ser considerada na futura criação da skill.

### Hipóteses controladas para a proposta mobile

Os parâmetros abaixo são hipóteses iniciais e podem ser alterados após a revisão visual:

- viewport principal de 390 × 844 px;
- validações adicionais em 360 e 430 px;
- navbar mobile com logo e sem CTA lateral;
- eyebrow removido, acompanhando o Figma desktop;
- headline entre 44 e 48 px;
- subheadline entre 17 e 19 px;
- margens laterais de 24 px;
- CTA ocupando a largura disponível;
- preservação do mesmo background;
- reposicionamento do background para preservar parcialmente o rosto;
- overlay adicional somente quando necessário para legibilidade;
- nenhuma alteração de copy sem autorização;
- nenhuma alteração em formulário, WhatsApp, tracking, links sociais ou demais seções.

## Fontes de verdade

- Conteúdo: `client.json`, `base-de-conhecimento/` e outputs aprovados.
- Referência visual: frame aprovado e preservado no Figma.
- Implementação operacional: arquivos HTML, CSS e JavaScript versionados no Git.
- Histórico: repositório Git.
- Homologação: Vercel Preview.
- Produção: deployment da Vercel autorizado explicitamente pelo usuário.

A Vercel não substitui o Figma como referência visual nem o Git como fonte da implementação.

## Critérios de sucesso

- A copy da Hero permanece idêntica à referência aprovada, salvo autorização explícita.
- Assets não são substituídos, degradados ou publicados indevidamente.
- A Hero é implementada em HTML, CSS e JavaScript compreensíveis e editáveis.
- Desktop e mobile correspondem visualmente ao Figma e preservam hierarquia, espaçamento, tipografia, cores, imagem, CTA e responsividade.
- Nenhum output atual do cliente é alterado.
- Os testes locais são concluídos antes da homologação.
- A Vercel Preview permanece isolada da produção.
- Nenhum deployment em produção é realizado.
- Outro membro da unidade consegue compreender o fluxo e repetir os passos documentados.
- Limitações, diferenças visuais e intervenções manuais ficam registradas.

## Critérios de interrupção

O teste deve parar imediatamente se houver:

- tentativa de modificar qualquer output existente do cliente;
- necessidade de alterar copy sem autorização explícita;
- necessidade de alterar outra seção além da Hero;
- risco de perda visual, de responsividade ou impossibilidade de comparar Figma e código;
- substituição, recompressão destrutiva ou perda de assets;
- dependência ou tecnologia não aprovada;
- dúvida sobre qual frame ou versão é a referência aprovada;
- necessidade de credencial durante a auditoria;
- tentativa de deployment em produção;
- divergência não autorizada entre Figma e código;
- solicitação de credenciais, tokens, secrets ou leitura de arquivos `.env`;
- necessidade de ampliar o teste para mais de uma seção.

## Checklist antes do teste

- [ ] Confirmar a branch de trabalho e o estado limpo do repositório.
- [ ] Confirmar que o escopo continua restrito à Hero desktop e mobile.
- [ ] Confirmar que o arquivo Figma original está em modo somente leitura.
- [ ] Concluir a auditoria somente leitura e apresentar o plano ao usuário.
- [ ] Obter aprovação explícita limitada ao frame e às operações descritas antes de escrever no Figma.
- [ ] Duplicar o arquivo para o piloto sem alterar o original.
- [ ] Identificar e preservar o frame de referência.
- [ ] Inventariar copy, fontes, cores, espaçamentos, imagens e CTA da Hero.
- [ ] Confirmar quais assets pertencem à Hero de referência e preservar seus arquivos, recortes, proporções e qualidade.
- [ ] Planejar uma cópia isolada da LP para a implementação em HTML, CSS e JavaScript.
- [ ] Confirmar que nenhum output atual do Instituto Salotti será modificado.
- [ ] Definir evidências de comparação para desktop e mobile.
- [ ] Obter aprovação explícita antes de qualquer escrita em código.

## Checklist depois do teste

- [ ] Confirmar que o Figma original permanece inalterado.
- [ ] Confirmar que o frame de referência da cópia permanece preservado.
- [ ] Confirmar que a implementação está isolada dos outputs existentes.
- [ ] Concluir os testes locais.
- [ ] Obter aprovação explícita antes de criar a Vercel Preview.
- [ ] Confirmar que a Vercel Preview está isolada e que não houve deployment em produção.
- [ ] Comparar desktop e mobile com o Figma aprovado.
- [ ] Verificar que HTML, CSS e JavaScript estão compreensíveis, editáveis e versionados.
- [ ] Verificar fidelidade de copy, tipografia, cores, espaçamentos, imagem e CTA.
- [ ] Verificar se nenhum asset foi substituído ou degradado.
- [ ] Registrar diferenças, limitações e passos manuais.
- [ ] Confirmar que nenhum output atual do cliente foi alterado.
- [ ] Confirmar que relatórios e registros novos estão somente no diretório exclusivo do piloto.
- [ ] Decidir em revisão humana se a fundação está aprovada para a criação da skill.

## Controle de versão

Commit e push só podem ocorrer após aprovação explícita do usuário. A aprovação de operações no Figma não autoriza operações no histórico Git.
