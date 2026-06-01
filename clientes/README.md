# clientes/

Cada cliente vive em uma pasta própria aqui dentro, criada via `/novo-cliente`.

Estrutura padrão de um cliente:

```
clientes/<slug-do-cliente>/
├── client.json                  # metadados do cliente
├── base-de-conhecimento/        # briefings, calls, formulário V4MOS
├── kickoff/                     # perguntas e dúvidas de kickoff
├── outputs/                     # entregáveis das skills (.json)
├── assets/                      # criativos, identidade visual, logos
├── consolidated.md / .html      # consolidação dos diagnósticos
└── portal.html                  # portal do cliente
```

> Esta pasta vem **vazia** de propósito. Os dados de clientes não são versionados
> neste repositório compartilhado — rode `/onboarding` e `/novo-cliente` para
> começar a sua própria workspace.
