# Sistema de landing pages

## Objetivo

Este sistema pretende estabelecer um fluxo seguro e repetível para transformar referências aprovadas no Figma em landing pages preparadas para implementação no GreatPages, com o Codex atuando como agente operacional e de validação.

O objetivo inicial não é automatizar uma landing page inteira. A primeira etapa deve descobrir, com um experimento pequeno, quais informações visuais e estruturais podem ser transferidas com fidelidade e quais decisões ainda exigem revisão humana.

## Fluxo proposto

```text
Figma original (somente leitura)
    ↓
Cópia de teste e frame de exportação
    ↓
Codex: auditoria e preparação estrutural
    ↓
GreatPages: página nova e não publicada
    ↓
Comparação visual e relatório do piloto
```

O fluxo desta fase é exclusivamente unidirecional. O GreatPages não atualiza o Figma, e alterações feitas no destino não retornam automaticamente à origem.

A auditoria inicial do Figma é somente leitura. Ao concluí-la, o Codex deve apresentar um plano. Qualquer escrita no Figma depende de aprovação explícita do usuário, restrita ao frame e às operações descritas nesse plano.

## Papel do repositório

O repositório registra a governança, as decisões, o escopo e os critérios de validação do processo. Ele também deverá, em fases posteriores, armazenar contratos estruturais, documentação, skills e ferramentas reutilizáveis.

Todos os novos relatórios e registros do piloto devem ficar exclusivamente em:

```text
clientes/instituto-salotti/outputs/landing-pages/piloto-figma-greatpages/
```

Os outputs existentes `landing-page.html`, `landing-page/` e `deploy/` não podem ser modificados. O repositório não substitui o Figma como referência visual nem o GreatPages como destino de implementação.

## Fontes de verdade

- Conteúdo: `client.json`, `base-de-conhecimento/` e outputs aprovados.
- Referência visual: frame de referência preservado na cópia do Figma.
- Estrutura preparada: frame de exportação.
- Implementação: página de teste não publicada no GreatPages.
- Histórico: repositório Git.

## Estado atual

O piloto está na camada inicial de governança. Nesta etapa existem apenas:

- regras operacionais para agentes;
- definição do fluxo de teste;
- decisões arquiteturais iniciais;
- critérios de sucesso, interrupção e validação.

Ainda não há skill do Codex, integração configurada, sincronização, contrato de componentes ou automação de importação.

## Limites da primeira fase

- Um único cliente: Instituto Salotti.
- Uma única seção: Hero.
- Duas variações responsivas: desktop e mobile.
- Figma original somente leitura.
- GreatPages em página nova, de teste e não publicada.
- Nenhuma alteração nos outputs atuais do cliente.
- Nenhuma publicação em produção.
- Nenhuma sincronização bidirecional.
- Commit e push somente após aprovação explícita do usuário.

O design system completo será definido somente depois da conclusão e avaliação do piloto, usando evidências reais sobre fidelidade, limitações das ferramentas e esforço operacional.
