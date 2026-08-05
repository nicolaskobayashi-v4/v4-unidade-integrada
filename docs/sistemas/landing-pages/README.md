# Sistema de landing pages

## Objetivo

Este sistema pretende estabelecer um fluxo seguro e repetível para transformar referências aprovadas no Figma em landing pages implementadas como HTML, CSS e JavaScript versionados, com homologação por Vercel Preview. O Codex no VS Code atua como agente operacional, de preparação e validação.

O objetivo inicial não é automatizar uma landing page inteira. A primeira etapa deve descobrir, com um experimento pequeno, quais informações visuais e estruturais podem ser transferidas com fidelidade e quais decisões ainda exigem revisão humana.

## Fluxo proposto

```text
Figma aprovado
    ↓
Codex no VS Code
    ↓
HTML, CSS e JavaScript versionados
    ↓
Testes locais
    ↓
Git
    ↓
Vercel Preview
    ↓
Revisão humana
    ↓
Produção somente após aprovação explícita
```

O Figma define a referência visual aprovada. O Codex prepara e edita a implementação dentro do escopo autorizado. HTML, CSS e JavaScript constituem a implementação operacional; o Git preserva seu histórico; e a Vercel Preview fornece um ambiente isolado de homologação.

Preview e produção são etapas diferentes. A Preview serve para testes e revisão humana, exige aprovação explícita e não autoriza deployment em produção. Produção é proibida durante o piloto e só poderá ocorrer futuramente mediante autorização explícita do usuário.

A auditoria inicial do Figma é somente leitura. Ao concluí-la, o Codex deve apresentar um plano. Qualquer escrita no Figma depende de aprovação explícita do usuário, restrita ao frame e às operações descritas nesse plano.

## Papel do repositório

O repositório registra a governança, as decisões, o escopo e os critérios de validação do processo. Ele também deverá, em fases posteriores, armazenar contratos estruturais, documentação, skills e ferramentas reutilizáveis.

Todos os novos relatórios e registros do piloto devem ficar exclusivamente em:

```text
clientes/instituto-salotti/outputs/landing-pages/piloto-figma-vercel/
```

Os outputs existentes `landing-page.html`, `landing-page/` e `deploy/` podem ser consultados somente como referência e não podem ser sobrescritos, movidos, renomeados, reformatados ou modificados. O novo diretório não existe ainda e não deve ser criado nesta fase documental.

## Fontes de verdade

- Conteúdo: `client.json`, `base-de-conhecimento/` e outputs aprovados.
- Referência visual: frame aprovado e preservado no Figma.
- Implementação operacional: arquivos HTML, CSS e JavaScript versionados no Git.
- Histórico: repositório Git.
- Homologação: Vercel Preview.
- Produção: deployment da Vercel autorizado explicitamente pelo usuário.

A Vercel não substitui o Figma como referência visual e não substitui o Git como fonte da implementação.

## Estado atual

O piloto está na camada inicial de governança. Nesta etapa existem apenas:

- regras operacionais para agentes;
- definição do fluxo de teste;
- decisões arquiteturais iniciais;
- critérios de sucesso, interrupção e validação.

Ainda não há skill do Codex, integração configurada, código do piloto, Preview ou automação de deployment.

## Limites da primeira fase

- Um único cliente: Instituto Salotti.
- Uma única seção: Hero.
- Duas variações responsivas: desktop e mobile.
- Figma original somente leitura.
- Implementação em uma cópia isolada da LP.
- Testes locais antes da Vercel Preview.
- Vercel Preview somente após aprovação explícita.
- Nenhuma alteração nos outputs atuais do cliente.
- Nenhuma publicação em produção.
- Commit e push somente após aprovação explícita do usuário.

O design system completo será definido somente depois da conclusão e avaliação do piloto, usando evidências reais sobre fidelidade, limitações das ferramentas e esforço operacional.

## GreatPages

GreatPages deixou de ser o destino principal. Permanece registrado apenas como possível adaptador ou destino alternativo futuro, ainda não implementado e fora do escopo do piloto atual.
