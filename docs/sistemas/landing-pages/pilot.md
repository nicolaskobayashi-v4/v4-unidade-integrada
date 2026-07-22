# Piloto — Hero do Instituto Salotti

## Escopo

- Cliente piloto: Instituto Salotti.
- Seção testada: somente a Hero.
- Variações: desktop e mobile.
- Objetivo: validar o fluxo Figma → Codex → preparação estrutural → GreatPages sem afetar materiais atuais do cliente.

## Proteção dos originais

- O arquivo Figma original será tratado como somente leitura.
- O trabalho ocorrerá em um arquivo Figma piloto duplicado.
- O frame usado como referência será preservado sem alterações.
- Um frame de exportação separado será criado na cópia de teste.
- A implementação no GreatPages ocorrerá em uma página nova e não publicada.
- Nenhum output atual em `clientes/instituto-salotti/` será alterado.
- A Hero será usada apenas como referência em uma cópia de teste.

Os outputs existentes abaixo são imutáveis durante o piloto:

- `clientes/instituto-salotti/outputs/landing-page.html`;
- `clientes/instituto-salotti/outputs/landing-page/`;
- `clientes/instituto-salotti/outputs/deploy/`.

Todos os novos relatórios e registros devem ficar exclusivamente em:

```text
clientes/instituto-salotti/outputs/landing-pages/piloto-figma-greatpages/
```

## Auditoria e autorização no Figma

- A auditoria inicial do Figma é exclusivamente de leitura.
- Depois da auditoria, o agente deve apresentar um plano antes de qualquer escrita.
- Nenhuma escrita pode ocorrer sem aprovação explícita do usuário.
- A aprovação é limitada ao frame e às operações descritas no plano; qualquer ampliação exige nova aprovação.

## Fontes de verdade

- Conteúdo: `client.json`, `base-de-conhecimento/` e outputs aprovados.
- Referência visual: frame de referência preservado na cópia do Figma.
- Estrutura preparada: frame de exportação.
- Implementação: página de teste não publicada no GreatPages.
- Histórico: repositório Git.

## Critérios de sucesso

- A copy da Hero permanece idêntica à referência aprovada, salvo autorização explícita.
- Assets não são substituídos, degradados ou publicados indevidamente.
- Desktop e mobile preservam hierarquia, espaçamento, tipografia, cores, imagem e CTA de forma verificável.
- A preparação estrutural permite reconstruir a seção no GreatPages sem alterar o original.
- A página permanece não publicada durante todo o teste.
- Outro membro da unidade consegue compreender o fluxo e repetir os passos documentados.
- Limitações, diferenças visuais e intervenções manuais ficam registradas.

## Critérios de interrupção

O teste deve parar imediatamente se houver:

- risco de sobrescrever o Figma original, uma página GreatPages existente ou outputs do cliente;
- necessidade de alterar copy sem autorização explícita;
- risco de perda visual relevante ou impossibilidade de comparar origem e destino;
- substituição, recompressão destrutiva ou perda de assets;
- dúvida sobre qual frame ou versão é a referência aprovada;
- tentativa de publicar a página;
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
- [ ] Criar um frame de exportação separado na cópia.
- [ ] Inventariar copy, fontes, cores, espaçamentos, imagens e CTA da Hero.
- [ ] Confirmar quais assets pertencem à Hero de referência e preservar seus arquivos, recortes, proporções e qualidade.
- [ ] Criar uma página nova e não publicada no GreatPages.
- [ ] Confirmar que nenhum output atual do Instituto Salotti será modificado.
- [ ] Definir evidências de comparação para desktop e mobile.

## Checklist depois do teste

- [ ] Confirmar que o Figma original permanece inalterado.
- [ ] Confirmar que o frame de referência da cópia permanece preservado.
- [ ] Confirmar que somente o frame de exportação foi usado para preparação.
- [ ] Confirmar que a página GreatPages continua não publicada.
- [ ] Comparar desktop e mobile com a referência.
- [ ] Verificar fidelidade de copy, tipografia, cores, espaçamentos, imagem e CTA.
- [ ] Verificar se nenhum asset foi substituído ou degradado.
- [ ] Registrar diferenças, limitações e passos manuais.
- [ ] Confirmar que nenhum output atual do cliente foi alterado.
- [ ] Confirmar que relatórios e registros novos estão somente no diretório exclusivo do piloto.
- [ ] Decidir em revisão humana se a fundação está aprovada para a criação da skill.

## Controle de versão

Commit e push só podem ocorrer após aprovação explícita do usuário. A aprovação de operações no Figma não autoriza operações no histórico Git.
