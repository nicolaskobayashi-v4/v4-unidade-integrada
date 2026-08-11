# Sistema de landing pages

## 1. Objetivo do sistema

O sistema transforma estratégia e referências aprovadas em landing pages versionadas, testáveis e homologáveis sem alterar silenciosamente conteúdo, identidade ou materiais existentes. O fluxo primário é code-first: implementação local, testes, Git e, quando autorizada, Vercel Preview.

A V1 organiza o trabalho por skills operacionais em `.agents/skills/`. Ela não automatiza uma landing page inteira nem elimina revisão humana.

## 2. Arquitetura

```text
Matriz estratégica (somente leitura)
    ↓ outputs aprovados
Camada operacional da unidade (.agents/skills/)
    ↓ implementação e gates
Código local → testes → Git → Vercel Preview → revisão humana
```

- **Matriz:** estratégia, posicionamento, copy, CRO, identidade e outputs estruturados.
- **Unidade:** localização da implementação, baseline, código, aplicação visual, assets, QA, Git e Preview controlada.
- **Orquestração:** `lp-orchestrator` identifica o último estado válido e aponta somente o próximo gate.

O plugin `plugins/v4-estruturacao-ia/` e seus outputs permanecem somente leitura. Instruções matriciais de mutação de cliente, cache ou Production não são herdadas pela camada local.

## 3. Fontes de verdade

- Fatos: confirmação explícita mais recente, `client.json`, base estratégica e outputs aprovados.
- Referência visual: confirmação explícita, Manual de Marca aprovado mais recente, diagnóstico visual, assets oficiais e referências autorizadas.
- Copy: copy explicitamente aprovada, seguida do output estratégico de landing page aprovado.
- Links: confirmação explícita, seguida da implementação existente aprovada.
- Implementação: HTML, CSS e JavaScript versionados no Git.
- Baseline: conteúdo preservado em `reference/`.
- Homologação: Vercel Preview autorizada.
- Histórico: repositório Git e decisões registradas.

Conflitos devem ser registrados e submetidos ao checkpoint responsável. Referência externa nunca estabelece fatos do cliente.

## 4. Skills disponíveis

- `client-knowledge-sync`: compara e sincroniza conhecimento operacional quando necessário e autorizado.
- `lp-source-audit`: audita fontes e identifica a implementação correta, sem escrever.
- `lp-baseline-prepare`: cria a fronteira imutável entre referência e trabalho.
- `lp-design-adapter`: adapta uma seção autorizada sem recriar estratégia ou copy.
- `lp-asset-pipeline`: governa origem, direitos, derivados e uso responsivo de assets.
- `lp-quality-gate`: audita conteúdo, design, código, assets, Git e runtime, sem corrigir.
- `lp-release`: prepara e, quando autorizado, executa somente Vercel Preview.
- `lp-orchestrator`: coordena estados, bloqueios e próximos gates.

Uma skill só deve ser chamada quando for pertinente. Se não houver conhecimento novo ou divergente, por exemplo, não chamar `client-knowledge-sync`.

## 5. Fluxo oficial

```text
client-knowledge-sync (quando necessário)
→ lp-source-audit
→ lp-baseline-prepare
→ lp-design-adapter
→ lp-asset-pipeline (quando houver assets aplicáveis)
→ lp-quality-gate
→ lp-release
→ revisão humana
```

`lp-orchestrator` coordena os estados e indica o próximo gate. Nenhuma etapa autoriza automaticamente a seguinte. Cada execução de adaptação visual fica limitada a uma seção; redesign completo é um programa de sucessivas execuções por seção.

## 6. Checkpoints humanos

- Confirmar a implementação e as fontes corretas depois da auditoria.
- Aprovar caminhos e operações antes de criar a baseline.
- Autorizar uma seção e os arquivos exatos antes de qualquer edição.
- Revisar fidelidade visual e responsividade antes de avançar.
- Aprovar origem, direitos, recortes e derivados dos assets.
- Aceitar `PASS_WITH_WARNINGS` quando aplicável; `BLOCKED` impede release.
- Autorizar commit, push e Preview separadamente.
- Revisar a Preview sem interpretar homologação como autorização de Production.

Falta de pré-condição, evidência ou autorização gera `STOP`. Um gate que não pode ser aprovado retorna `BLOCKED`.

## 7. Estrutura recomendada por cliente

```text
clientes/<slug>/
├── base-de-conhecimento/
└── outputs/
    └── landing-pages/
        └── <projeto>/
            ├── reference/
            ├── src/
            └── reports/   # quando relatórios estruturados forem habilitados
```

`reference/` preserva a baseline e nunca deve ser editado. `src/` concentra a implementação autorizada. A V1 permite tanto HTML single-file quanto HTML, CSS e JavaScript separados; a separação entre referência e trabalho é o requisito central.

Outputs preexistentes não podem ser reorganizados ou sobrescritos para adotar essa estrutura.

## 8. Release

Testes locais e quality gate válido são obrigatórios antes de solicitar Preview. `lp-release` deve confirmar diretório, branch, commit, worktree, projeto e equipe Vercel, além da autorização humana específica.

Preview não é Production. Na V1:

- Production está desabilitada;
- `vercel --prod` é proibido;
- promoção, domínio e alias de produção são proibidos;
- criação automática de projeto Vercel é proibida;
- qualquer mudança posterior invalida o quality gate.

## 9. Limitações da V1

- Não há sincronização bidirecional com Figma ou outro destino.
- Figma não é o fluxo operacional principal da V1.
- GreatPages permanece fora do escopo.
- Processamento automático de imagens não está implementado.
- Playwright, axe, schemas, reports e testes automatizados não são obrigatórios nem estão garantidos.
- Não existem componentes visuais universais derivados dos pilotos.
- Production não faz parte do pipeline.

Os pilotos de Azul Viagens Bourbon Country, Mina Pizza e Instituto Salotti validaram decisões de processo; suas escolhas visuais não são regras universais.

## 10. Documentação detalhada

- [Guia completo das skills](skills-v1.md)
- [Quickstart](quickstart.md)
- [Decisões arquiteturais](decisions.md)
- [Histórico do piloto Salotti](pilot.md)
- Contratos executáveis: `.agents/skills/`

O histórico anterior à V1 permanece preservado em `pilot.md` e `decisions.md`.
