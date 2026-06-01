# V4 Estruturação IA — Marketplace

Sistema de estruturação estratégica com IA para operadores V4.

## Setup (cada operador roda uma vez)

### 1. Adicionar o marketplace

No Claude Code:
```
/plugin marketplace add guilhermelippert/v4-estruturacao-marketplace
```

### 2. Instalar o plugin

```
/plugin install v4-estruturacao-ia@v4-estruturacao-marketplace
```

### 3. Criar workspace de trabalho

```bash
mkdir ~/estruturacao-ia && cd ~/estruturacao-ia
claude
```

Dentro do Claude Code:
```
/onboarding
```

### 4. Verificar instalação

Rode `/plugin` e vá na aba Installed. Você deve ver `v4-estruturacao-ia`.
Digite `/` no Claude Code e veja as skills no autocomplete.

## Uso diário

```bash
cd ~/estruturacao-ia
claude
> "continuar"
```

O sistema mostra o panorama de todos os clientes e propõe o próximo passo.

## Skills disponíveis

### Utilidade
- `/onboarding` — Setup inicial da workspace
- `/novo-cliente` — Cadastrar novo cliente
- `/continuar` — Retomar trabalho (mostra panorama + próximo passo)
- `/feedback` — Reportar problema numa skill (cria GitHub Issue)
- `/duvida` — Tirar dúvida sobre o sistema

### Semana 1 — Diagnóstico
- `diagnostico-maturidade` — Análise de maturidade digital (dados V4MOS)
- `swot` — Matriz SWOT acionável
- `persona-icp` — ICP + Persona com Jobs-to-be-Done
- `auditoria-comunicacao` — Auditoria de touchpoints digitais

### Semana 2 — Pesquisa e Posicionamento
- `pesquisa-mercado` — TAM/SAM/SOM + concorrentes + tendências
- `posicionamento` — PUV + Canvas 4P + território de marca
- `diagnostico-midia` — Análise de mídia paga (dados V4MOS)
- `diagnostico-criativos` — Avaliação de criativos (multimodal)
- `diagnostico-cro` — Análise de conversão + wireframe

### Semana 3 — Produção e Implementação
- `identidade-visual` — Conceito + paleta + tipografia + logo
- `brandbook` — Manual de copy + tom de voz + narrativa
- `landing-page` — Copy + código + deploy Vercel
- `copy-anuncios` — 30+ variações por funil (Google Sheets)
- `criativos-anuncios` — Briefing criativo + prompts Midjourney
- `crm-setup` — Pipeline Kommo + réguas de automação
- `forecast-midia` — Modelagem 3 meses (Google Sheets)
- `gmb-otimizacao` — Google Meu Negócio otimizado

### Semana 4-5 — Vendas (opcional)
- `diagnostico-comercial` — Análise do funil + critérios de qualificação
- `cliente-oculto` — Simulação + relatório
- `scripts-sdr` — Scripts de qualificação WhatsApp
- `sdr-ia-config` — Configuração Patagon + integração Kommo
