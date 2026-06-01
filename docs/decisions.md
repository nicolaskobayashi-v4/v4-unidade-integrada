# Decisoes Arquiteturais — V4 Estruturacao IA

Data: 04-06/04/2026
Participantes: Gui (CPTO V4) + Claude

---

## Decisoes finais

| # | Tema | Decisao |
|---|------|---------|
| 1 | Operador | Analista interno (B), escalar pra franqueados depois |
| 2 | Dados | V4MOS API via Service Account como fonte primaria, gaps coletados on-the-fly durante operacao |
| 3 | Runtime | Claude Code (Claude Max do operador) via plugin marketplace |
| 4 | Entregaveis | HTML deployado na Vercel (link compartilhavel). Google Sheets via GOG pra planilhas |
| 5 | Determinismo | JSON Schema rigido → Template HTML. LLM nunca toca layout |
| 6 | Skills | SKILL.md lean + references/ pesadas. Se falta algo, cria skill |
| 7 | Human-in-the-loop | Checkpoints definidos com conversa livre dentro de cada um |
| 8 | Auth V4MOS | Service Account 1:1 por workspace, mapa local .credentials/clients.json |
| 9 | Agentes | Orquestrador (state + routing) + revisor qualidade (automatico) |
| 10 | Interface | Dashboard HTML local gerado do state.json |
| 11 | Feedback | /feedback → GitHub Issue (3 perguntas: oq rolou, como deveria, oq melhorar) |
| 12 | Onboarding | /onboarding skill com tutorial interativo |
| 13 | Distribuicao | Repo marketplace separado, `/plugin install` |
| 14 | State mgmt | state.json + decisions.jsonl + outputs .json por cliente, dentro de clientes/ |
| 15 | Dependencias | Grafo explicito em dependency_graph.json |
| 16 | Multi-operador | 1 operador por cliente (V1) |
| 17 | Multi-LLM | CLAUDE.md + AGENTS.md (Claude primeiro) |
| 18 | Custo | Operador usa Claude Max |
| 19 | Stack | Zero Python. HTML + bash + GOG + Vercel |
| 20 | Assets | Definir com Figueiredo. Templates a converter de Google Docs/Slides |

---

## Contexto: V4MOS (sistema existente)

O V4MOS (v4-marketing-backend) e o backend em producao da V4 Company (180 franquias, 8000+ clientes). Dados relevantes que o sistema de estruturacao consome:

### Integration Hub
- 100+ conectores OAuth (Meta Ads, Google Ads, Kommo, Shopify, etc.)
- Endpoint: `GET /workspaces/{id}/integrations/status`
- Auth: Service Account via headers `x-client-id` + `x-client-secret` + `x-workspace-id`

### Dados por workspace
- **Integracoes ativas** com status (active/warning/error)
- **MarketingProfile** (questionario preenchido, v4_form_data JSON)
- **WebsiteCollectedData** (scraping do site do cliente)
- **Diagnosis** (5 steps de maturidade digital processados por LLM)
- **MediaInvestment** (CPL, CPC, investimento por mes/segmento)

### Autenticacao
- Service Account e 1:1 por workspace (vinculado via metadata.workspaceId)
- Lambda Authorizer valida: `tokenWorkspaceId === requestWorkspaceId`
- NAO permite cross-workspace com mesmo Service Account

### API endpoints uteis
- `GET /workspaces/{id}/integrations/status` — status de integracoes
- `GET /workspaces/{id}/diagnoses` — diagnosticos existentes
- `GET /workspaces/{id}` — dados do workspace
- `POST /integrations/reconnect` — reconectar integracao
- Swagger em `/documentation` de cada servico

---

## Contexto: Repo do Figueiredo (fonte original)

O repo `v4-estruturacao-ia` do Figueiredo e um template manual de entrega em 5 semanas com 21 squads. Prompts para colar no ChatGPT, variaveis manuais, zero automacao. O conteudo dos prompts foi transformado em skills interativas neste marketplace.

### Mapeamento squad → skill
| Squad original | Skill no marketplace |
|---|---|
| s1-maturidade-digital | diagnostico-maturidade |
| s1-swot | swot |
| s1-persona-icp | persona-icp |
| s1-auditoria-comunicacao | auditoria-comunicacao |
| s2-pesquisa-mercado | pesquisa-mercado |
| s2-posicionamento | posicionamento |
| s2-diagnostico-midia | diagnostico-midia |
| s2-diagnostico-criativos | diagnostico-criativos |
| s2-diagnostico-cro | diagnostico-cro |
| s3-identidade-visual | identidade-visual |
| s3-brandbook | brandbook |
| s3-landing-page | landing-page |
| s3-copy-anuncios | copy-anuncios |
| s3-criativos-anuncios | criativos-anuncios |
| s3-crm-setup | crm-setup |
| s3-forecast-midia | forecast-midia |
| s3-google-meu-negocio | gmb-otimizacao |
| s4-diagnostico-comercial | diagnostico-comercial |
| s4-cliente-oculto | cliente-oculto |
| s5-scripts-qualificacao | scripts-sdr |
| s5-sdr-ia-config | sdr-ia-config |

### Skills novas (nao existiam no Figueiredo)
- onboarding, novo-cliente, continuar, feedback, duvida
- agents: orquestrador, revisor-qualidade
- scripts: v4mos_fetch, update_state, append_decision, render_dashboard

---

## Pendencias

1. **Templates HTML por entregavel** — Gui vai dar acesso aos Google Docs/Slides do Figueiredo. Converter cada um pra HTML que consome JSON do schema da skill.
2. **Assets visuais** — Definir com Figueiredo como os templates devem se parecer.
3. **Teste end-to-end** — Instalar plugin, /onboarding, cadastrar cliente ficticio, executar semana 1 completa.
4. **Transferir repo** — De guilhermelippert/ pra v4company/ quando tiver permissao na org.

---

## Como continuar o trabalho

1. Abra o Claude Code neste repo: `cd v4-estruturacao-marketplace && claude`
2. O CLAUDE.md na raiz do plugin tem todas as instrucoes operacionais
3. Cada skill em skills/ e autocontida (SKILL.md + schema.json + references/)
4. O dependency_graph.json mapeia todas as dependencias entre skills
5. Os agents em agents/ sao auto-descobertos pelo Claude Code
6. Para testar: rode /onboarding num diretorio de trabalho, depois /novo-cliente com dados ficticios
