# Quickstart

## 1. Abrir o cliente

Antes de trabalhar, confirmar:

- repositório correto;
- branch atual;
- working tree e arquivos já alterados;
- slug do cliente;
- projeto de landing page;
- escopo e operações autorizados.

Não ler `.env`, tokens ou credenciais.

## 2. Descobrir o estado atual

Usar `lp-orchestrator` para fluxos com histórico, múltiplos gates ou retomada. Em um caso simples, usar diretamente `lp-source-audit` para identificar fontes e implementação sem alterar arquivos.

Se faltarem dados críticos, emitir `STOP` informando exatamente o item ausente, o responsável e o próximo gate possível.

## 3. Preparar baseline

Usar `lp-baseline-prepare` quando ainda não existir referência imutável. Apresentar origem, caminhos e operações antes de criar:

```text
<projeto>/
├── reference/  # somente leitura
└── src/        # área de trabalho
```

Nunca sobrescrever uma baseline ou reorganizar outputs existentes.

## 4. Trabalhar o design

Usar `lp-design-adapter` somente na seção e nos arquivos autorizados. Preservar copy, links, claims, assets e estrutura comercial.

Redesign completo significa várias execuções por seção. Não significa editar a página inteira automaticamente; cada seção exige autorização e revisão humana próprias.

## 5. Assets

Usar `lp-asset-pipeline` somente quando houver assets a inventariar ou processar. Confirmar origem e direitos, preservar o original e aprovar derivados, crops e referências antes da escrita.

Não instalar processadores nem buscar stock automaticamente.

## 6. Revisão

Usar `lp-quality-gate` depois da implementação e dos assets revisados:

- `PASS`: todos os controles aplicáveis passaram.
- `PASS_WITH_WARNINGS`: somente warnings não factuais e não estruturais foram aceitos por humano.
- `BLOCKED`: existe falha crítica, evidência ausente ou alteração não autorizada.

O gate é read-only. Corrigir em execução separada e executar o gate novamente.

## 7. Preview

Usar `lp-release` somente com:

- quality gate válido;
- testes locais concluídos;
- diretório, branch e commit confirmados;
- projeto e equipe Vercel confirmados;
- aprovação humana específica.

Preview não autoriza Production.

## 8. O que nunca fazer

- Não modificar a matriz ou seus outputs.
- Não inventar dados, claims, depoimentos, links, preços ou métricas.
- Não alterar copy, links ou assets sem autorização específica.
- Não sobrescrever `reference/` ou outros originais.
- Não usar `vercel --prod`, promover Preview ou publicar Production.
- Não usar force push.
- Não acessar secrets ou arquivos `.env`.
- Não interpretar uma aprovação como autorização para as etapas seguintes.

## 9. Exemplos de prompts

> Use `lp-source-audit` para auditar a LP X do cliente Y. Não altere arquivos.

> Use `lp-design-adapter` somente na seção Hero já autorizada.

> Use `lp-asset-pipeline` para inventariar os assets desta seção e pare antes de criar derivados.

> Execute `lp-quality-gate` na implementação atual e pare se retornar `BLOCKED`.

> Use `lp-release` para preparar o checklist da Preview, sem executar deploy.
