---
name: ee-onboarding
description: "Setup inicial da workspace de estruturação IA. Configura diretórios e ensina o operador a usar o sistema. Use quando o operador disser /ee-onboarding ou 'configurar workspace' ou 'primeiro uso'."
---

# Onboarding — Setup da Workspace

Você está configurando a workspace de estruturação IA para um novo operador. Siga cada etapa em ordem.

**IMPORTANTE:** NÃO peça credenciais do V4MOS aqui. Cada cliente tem seu próprio workspace no V4MOS com seu próprio Service Account. Credenciais são coletadas por cliente, durante o /ee-novo-cliente.

## Pré-requisitos

Verifique se o operador tem as ferramentas necessárias:

| Ferramenta | Comando de verificação | Se não tiver |
|---|---|---|
| Claude Code | Já está rodando | — |
| GOG CLI | `gog --version` | `npm install -g @nicecode/gog` |
| Vercel CLI | `vercel --version` | `npm install -g vercel` |
| jq | `jq --version` | Mac: `brew install jq` / Linux: `apt install jq` / Windows: `choco install jq` |
| gh (GitHub CLI) | `gh --version` | Mac: `brew install gh` / Linux: `apt install gh` / Windows: `choco install gh` |

Se alguma ferramenta estiver faltando, instrua a instalação. Se o operador não precisar de Vercel ou GOG agora, registre como pendente e continue.

## Etapa 1: Criar estrutura de diretórios

No diretório atual do operador, crie:

```
.credentials/
  clients.json       ← inicializar com {}
clientes/            ← pasta raiz dos clientes
dashboard-geral.html ← arquivo vazio por enquanto
.gitignore
```

Conteúdo do `.gitignore`:
```
.credentials/
clientes/*/client.json (connectors)
dashboard-geral.html
*.tmp
```

Confirme ao operador:
```
Estrutura criada:
  .credentials/clients.json  ← credenciais V4MOS por cliente (privado)
  clientes/                  ← cada cliente terá sua subpasta aqui
  dashboard-geral.html       ← visão geral de todos os clientes
  .gitignore                 ← protege credenciais e caches
```

## Etapa 2: Tutorial rápido

Apresente ao operador:

```
COMO USAR O SISTEMA DE ESTRUTURAÇÃO IA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Comandos principais:
  /ee-novo-cliente      → Cadastrar novo cliente (coleta credenciais V4MOS + briefing)
  /ee-continuar         → Retomar trabalho (panorama de clientes + próximo passo)
  /ee-duvida [pergunta] → Tirar dúvida sobre o sistema
  /ee-feedback          → Reportar problema ou sugestão

Fluxo de trabalho:
  1. Cadastre o cliente com /ee-novo-cliente
     → O sistema pede o workspace_id do V4MOS
     → Puxa dados automaticamente (integrações, diagnóstico, métricas)
     → Faz briefing complementar interativo (só o que falta)
  2. O sistema guia semana a semana com checkpoints
  3. Você co-cria cada entregável — valida antes de avançar
  4. Entregáveis são HTML (deploy Vercel) ou Google Sheets (via GOG)

Sobre o V4MOS:
  Cada cliente tem um workspace no V4MOS (v4.marketing)
  O sistema puxa dados de lá automaticamente (Service Account)
  Credenciais são configuradas POR CLIENTE, não globalmente

Semanas do processo:
  S1 — Diagnóstico (maturidade, SWOT, ICP, auditoria)
  S2 — Pesquisa e Posicionamento (mercado, PUV, mídia, criativos, CRO)
  S3 — Produção (identidade, brandbook, LP, copy, CRM, forecast)
  S4-5 — Vendas (diagnóstico comercial, cliente oculto, scripts, SDR IA)
```

## Etapa 3: Verificação final

Confirme:
- [ ] Diretório `.credentials/` existe com `clients.json` vazio
- [ ] Diretório `clientes/` existe
- [ ] `.gitignore` protege credenciais

Apresente:
```
Workspace configurada!

Próximo passo: cadastre seu primeiro cliente com /ee-novo-cliente
O sistema vai pedir o workspace_id do V4MOS e configurar tudo automaticamente.

Dúvidas: /ee-duvida [pergunta]
```

Pergunte: "Quer cadastrar o primeiro cliente agora?"
Se sim, inicie `/ee-novo-cliente`.
