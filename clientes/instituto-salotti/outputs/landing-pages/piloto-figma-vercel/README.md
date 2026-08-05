# Piloto HTML/Vercel — Instituto Salotti

## Identificação

- Cliente: Instituto Salotti.
- Piloto: Figma → Codex → HTML/CSS/JavaScript → Vercel Preview.
- Branch: `pilot/salotti-figma-vercel`.
- Data de criação: 2026-07-22.
- Commit documental de referência: `469b4d3`.

## Objetivo

Este diretório existe para testar exclusivamente a Hero desktop e mobile em uma cópia isolada. O piloto não modifica a landing page existente e não autoriza deployment em produção.

## Estrutura

- `reference/`: cópia binária imutável da versão de deploy.
- `preview/`: cópia de trabalho, inicialmente idêntica à referência.
- `README.md`: registro da origem, do inventário, da integridade e das regras do piloto.

## Fonte da cópia

Todos os arquivos copiados vieram exclusivamente de:

```text
clientes/instituto-salotti/outputs/deploy/
```

A origem permanece somente leitura.

## Escopo autorizado

- Somente a Hero desktop e mobile.
- A navbar está fora do escopo inicial.
- Todas as demais seções devem ser preservadas.
- Formulário, WhatsApp, links sociais e tracking estão fora do escopo.
- CSS e JavaScript permanecem inline no primeiro teste.

## Regras

- `reference/` nunca deve ser editada.
- `preview/` somente pode ser editada após auditoria e aprovação explícita.
- Somente uma seção pode ser modificada por execução.
- Nenhuma alteração pode atingir os outputs existentes do cliente.
- Nenhuma credencial, token, secret ou arquivo `.env` pode ser lido ou exposto.
- A criação de uma Vercel Preview exige aprovação explícita.
- Deployment em produção é proibido durante o piloto.
- Nenhuma skill será criada nesta etapa.

## Resultado do primeiro teste de escrita no Figma

- O servidor MCP oficial do Figma foi conectado e autenticado em uma conta com plano Pro e acesso Full.
- As ferramentas de escrita permaneceram bloqueadas até uma autorização específica.
- `use_figma` foi temporariamente liberado apenas para uma operação que tentaria criar uma página isolada, uma cópia da Hero desktop e um frame mobile vazio.
- A chamada falhou porque o ambiente MCP não conseguiu carregar a fonte personalizada `PF Marlet Display Light`.
- Nenhuma página, frame ou node foi criado; nenhum estado parcial precisou ser removido.
- O node original e o repositório permaneceram inalterados.
- Nenhuma segunda tentativa foi executada e `use_figma` voltou a ser bloqueado.

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

O Figma desktop continua sendo a referência visual aprovada. A primeira proposta mobile no código não será considerada design aprovado; o frame mobile somente se torna referência após revisão humana no Figma. `generate_figma_design` continuará bloqueado até a proposta local estar aprovada para captura, e a captura Code to Canvas será autorizada em execução separada. Nenhuma publicação ou Vercel Preview acontecerá antes da aprovação do frame mobile. A limitação de carregamento da fonte personalizada deverá ser considerada na futura criação da skill.

### Hipóteses controladas para a proposta mobile

Os parâmetros a seguir ainda são hipóteses e podem ser alterados após a revisão visual:

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

## Inventário e hashes SHA-256

| Arquivo | SHA-256 |
|---|---|
| `index.html` | `813EFD83385D376F5A32FAE7FD26AB0C8FCDE59864A0A89974F09787106AC69B` |
| `landing-page/assets-lp/especialidades-bg-2.png` | `0411FCEC3498BA92BF75B1103E454C5F64F5D8DEA20B6D0D1FD0924558EE0161` |
| `landing-page/assets-lp/especialista-bg.png` | `D42C44508A8B38A267C035AE1A2E179A40B8D7EFF500FFF71D3FB2BCE34223AD` |
| `landing-page/assets-lp/fabiana-volpe.png` | `FB80729F0385B4EFEEF7D19CD6A69AF30BCD9C93F54D9B206BD1E2FB59D3FA59` |
| `landing-page/assets-lp/faq-bg.png` | `3698E537DD00425C3406607D6B3845AD6E222815AF4D4B2C723149C88F6BE0CC` |
| `landing-page/assets-lp/foto-dr-salotti.png` | `F1B4B6DDCD7127D099B48F065D810B211FA5E2DE6A04EF82A8D758B6AAFFA626` |
| `landing-page/assets-lp/hero-background.png` | `6E23EBFB88A9D699B7D920827E78262F2BA421C553D43968A09A412192CC2169` |
| `landing-page/assets-lp/icon-ciclo.png` | `33F75B78555B416FA1673D346BD5441CBB5A4C975CFFA757C9FFC37A5C9B63CD` |
| `landing-page/assets-lp/icon-dente.png` | `D5292BA3E42C002DC735F46007706E1ACEB39F807902043EA994C30F07DE2A6D` |
| `landing-page/assets-lp/icon-diamond.png` | `22668E5046E4D151FECD44B743FFE1958A89DA7929B7A52EB8705F9230065EF1` |
| `landing-page/assets-lp/icon-microscopio.png` | `ACF4E544F7475F5FA6D365BD24D4D1BD9EF63B9B8C39A063E1C18137AFB4F1CD` |
| `landing-page/assets-lp/icon-monitor.png` | `64DC6A5D2C1959DB8A729F25F51954162E2711B58EAA125217D227E9B67796BF` |
| `landing-page/assets-lp/icon-odonto-digital.png` | `4367A0FC825CF2BDEBE18719848BB02A9F2D06CF01EC5B00BBDC3F70CC95EDBC` |
| `landing-page/assets-lp/icon-sineta.png` | `B63E7E42FDAF3B2BFFED7E3F4443A08E2DC2AB5617D4A3BCA411F44E92F77B99` |
| `landing-page/assets-lp/logo-instituto-salotti-branco.png` | `DA35332454AE2CBA4486EFEE3FE6D0BE7F9A24499F1B059FBDD5E6385E521CCD` |

## Integridade inicial

Na criação desta estrutura, os arquivos foram comparados por SHA-256 nas três vias:

- origem = `reference/`;
- origem = `preview/`;
- `reference/` = `preview/`.

O HTML não foi reformatado e as imagens não foram recomprimidas. O asset não utilizado `especialidades-bg.png` não foi copiado. Também não foram copiados `.gitignore`, `.vercel/`, `vercel.json`, arquivos `.env`, credenciais, caches ou logs.

## Recursos externos

Os dois HTMLs mantêm referências externas às folhas de estilo do Adobe Fonts e do Google Fonts. Nenhuma requisição externa foi realizada durante a criação desta estrutura.
