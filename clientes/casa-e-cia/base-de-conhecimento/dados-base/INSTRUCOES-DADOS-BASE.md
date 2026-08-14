# Instruções — `dados-base` (exportações do ERP Casa & Cia)

**Origem:** relatórios exportados do ERP da Casa & Cia (sistema versão 2.3.8.x, telas `CX0077T`, `CX0043C`, `CL1002V`).
**Exportado por:** Anderson Moreira · **Data da extração:** 10/08/2026
**Empresa no ERP:** `6 - CASA E CIA PREMIUM` · **Período coberto em todos os relatórios:** 01/01/2024 a 10/08/2026 (~31 meses)
**Formato original:** PDF paginado (não são planilhas).

> ✅ **Já convertidos.** Os 12 PDFs viraram tabelas em [`csv/`](csv/) — incluindo um `clientes-consolidado.csv` com uma linha por cliente juntando valor + vendedores + marcas + contato. Todos os totais foram validados contra os rodapés dos PDFs e batem exatamente. **Para qualquer análise, use os CSVs, não os PDFs.** Schema, colunas derivadas e ressalvas em [`csv/README-CSV.md`](csv/README-CSV.md).

---

## 1. O que é cada arquivo

### 1.1 `Curva ABC de Clientes por Quantidade com Ticket Médio.pdf` ⭐ **o mais valioso**

550 páginas · 31.891 clientes ranqueados.

| Coluna | Conteúdo |
|---|---|
| Rank | posição, ordenada por Qtde (decrescente) |
| Código | ID do cliente no ERP |
| Nome | nome completo |
| Cidade/UF | cidade (frequentemente truncada — ver limitações) |
| Telefone 1 / Telefone 2 / Celular | contatos |
| Qtde | quantidade no período (compras ou peças — **a confirmar**, ver §4) |
| Total | valor comprado no período (R$) |
| T.Médio | Total ÷ Qtde |

**Totais do relatório:** 54.366 unidades · **R$ 28.810.734,33** · ticket médio geral **R$ 529,94**.

É o **único arquivo com valor financeiro por cliente**. Tudo que envolva faturamento, concentração de receita, ticket, recência/frequência ou dimensionamento de base sai daqui.

**Habilita:** curva ABC real (quanto do faturamento vem de quantos clientes), distribuição de ticket médio, segmentação por valor, base endereçável para campanhas, sizing de LTV, cruzamento geográfico (cidade).

---

### 1.2 `Clientes com Compras no Periodo com Email eTelefones.pdf`

570 páginas · 31.729 clientes, agrupados por vendedor (24 vendedores identificados).
Colunas: Código · Nome · Telefone · Fax · Celular · E-Mail.

**Achado crítico já verificado:** apenas **~245 registros têm e-mail preenchido** — cerca de **0,8% da base**. Na prática, **a Casa & Cia não tem base de e-mail**. O ativo de contato da empresa é telefone/celular (WhatsApp).

> Atenção ao ler o PDF: o campo "Quantidade de Clientes do Vendedor" no rodapé de cada vendedor é um **total acumulado** (bug do relatório), não a contagem daquele vendedor. Para ter o número por vendedor é preciso calcular por diferença ou contar as linhas.

**Habilita:** dimensionar o gap de e-mail (argumento para captura de e-mail/CRM), mapear carteira por vendedor, atribuição de clientes a vendedores.

---

### 1.3 `Relacao de Clientes com Compras no Periodo por Grupo por Vendedor.pdf` (sem sufixo de marca)

790 páginas · 42.595 registros → **31.726 clientes únicos** (um mesmo cliente aparece uma vez para cada vendedor que o atendeu; média de 1,34 vendedores por cliente).
Filtro aplicado: `Grupo de: 1º piso loja até: 2º piso loja` — ou seja, recorte por **piso/setor da loja**, não por marca.
Colunas: Código · Nome · Telefone · Celular · Fone Emprego. **Sem valores.**

**Habilita:** carteira por vendedor, cruzamento de quantos clientes compram com mais de um vendedor. Como não tem valor, é um complemento — não uma fonte primária.

---

### 1.4 Os 9 arquivos `... por Grupo por Vendedor <MARCA>.pdf`

Mesmo relatório do item 1.3, mas filtrado por **fornecedor/marca** (`Grupo de: Fornecedor\<Marca>`). São listas de **quais clientes compraram de cada marca**, agrupadas por vendedor. **Sem valores, só contatos.**

| Marca (grupo no ERP) | Registros | Páginas |
|---|---:|---:|
| Altenburg | 12.990 | 242 |
| Niazitex | 6.719 | 126 |
| Buddemeyer | 6.343 | 119 |
| Kacyumara | 5.495 | 103 |
| Karsten | 5.270 | 99 |
| Bella Janela | 5.084 | 95 |
| Trussardi | 2.640 | 50 |
| Budd Luxus | 1.495 | 29 |
| Plumassul | 279 | 6 |
| **Soma** | **46.315** | |

**Habilita:** afinidade cliente↔marca, cross-sell (quem compra Altenburg mas nunca comprou Trussardi), segmentação de público para campanhas por marca, e — cruzando com a Curva ABC — **estimar o perfil de valor de quem compra cada marca** (ex.: o cliente Trussardi tem ticket maior que o cliente Altenburg?).

⚠️ **Não somar com o item 1.3.** São dimensões diferentes da árvore de grupos (piso da loja × fornecedor); os universos se sobrepõem, não se complementam. E os registros aqui também são duplicados por vendedor.

---

## 2. Como os arquivos se conectam

O **`Código` do cliente é a chave** presente em todos os relatórios. É por ele que se cruza tudo:

```
Curva ABC (valor, ticket, qtde, cidade)   ← fonte de VALOR
        │ Código
        ├── E-mails/Telefones  → vendedor + contatos + e-mail
        ├── Geral por piso     → vendedor(es) que atenderam
        └── 9 arquivos de marca → quais marcas o cliente compra
```

Cruzando os quatro conjuntos dá para montar **uma tabela única de cliente** com: valor, frequência, ticket, cidade, vendedor(es), marcas compradas e contato. É essa tabela que sustenta praticamente todas as análises da §5.

---

## 3. Limitações — o que estes dados **não** têm

Importante ter claro antes de prometer qualquer análise:

1. **Sem datas de compra individuais.** Tudo é agregado no período de 31 meses. **Não dá para calcular recência, sazonalidade, evolução mensal, coorte ou churn com precisão** — só "comprou alguma vez entre jan/24 e ago/26".
2. **Sem valor por marca e sem valor por vendedor.** A Curva ABC tem valor total do cliente; os relatórios de marca/vendedor não têm valor. Dá para estimar por cruzamento, não medir.
3. **Sem produto/SKU, sem margem, sem custo.** Só o grupo (marca/piso).
4. **Sem canal.** Não distingue venda em loja física de online/WhatsApp.
5. **Cidade truncada.** Vem cortada no PDF ("CAXIAS DO"), com grafias inconsistentes ("Caxias do Sul/RS", "CAXIAS DO SUL", "CAXIUAS DO"). Precisa de normalização; a análise geográfica sai em nível de cidade agrupada, com margem de erro.
6. **Telefones sujos.** Estimativa preliminar sobre a Curva ABC: **97,5% dos clientes têm algum telefone**, mas só **~72% têm celular em formato plausível** para WhatsApp (11 dígitos com 9, ou 9 dígitos). O resto são fixos antigos, 8 dígitos ou registros corrompidos (`9143,1096`, `054229,4171`, `(32)2118-03`). **A base acionável real é menor que os 31,9 mil.**
7. **E-mail é inexistente** (0,8%).
8. **Filtros de filial inconsistentes entre relatórios:** Curva ABC usa `Filial 1 a 6`; o geral usa `1 a 99999`; o de e-mails usa `1 a 999`. Provavelmente dá no mesmo, mas explica por que os totais não batem exatamente (31.891 vs 31.729 vs 31.726).
9. **São PDFs**, não planilhas — a extração introduz risco de erro de parsing em linhas com colunas coladas. Toda análise deve vir com validação contra os totais impressos no rodapé.

---

## 4. Pontos a confirmar com o cliente (Anderson) antes de fechar números

Estas quatro dúvidas mudam a leitura dos dados. Ideal resolver antes ou junto da primeira análise:

1. **O que é a coluna "Qtde" na Curva ABC** — número de compras (notas/atendimentos) ou número de peças? Isso define se o "ticket médio R$ 529,94" é ticket de compra ou preço médio por item, e muda toda a leitura de frequência.
2. **O recorte é só da loja Premium ou das duas lojas?** O cabeçalho diz `6 - CASA E CIA PREMIUM`, mas inclui filiais 1 a 6. No kick-off foi dito que o ticket médio é ~R$ 400 na loja do Centro e ~R$ 750 na Premium — o R$ 529,94 do relatório cai **entre** os dois, o que sugere base consolidada das duas lojas. Precisa ser confirmado: é a diferença entre analisar uma loja ou o negócio inteiro.
3. **A lista de 9 marcas é completa** ou existem outros fornecedores relevantes não exportados?
4. **Faturamento total do período** — os R$ 28,8 mi da Curva ABC cobrem 100% das vendas ou só as vendas com cliente identificado no caixa? Se houver venda anônima relevante, a base de 31,9 mil clientes subestima o alcance real da loja.

---

## 5. O que dá para produzir com esta base (proposta — aguardando aprovação)

Em ordem de valor estratégico:

**Bloco A — Diagnóstico da base de clientes**
- Curva ABC real por faturamento (hoje o relatório ordena por quantidade, não por valor) — % da receita concentrada em A/B/C.
- Quantos clientes compraram uma única vez vs recorrentes → tamanho concreto da oportunidade de recompra.
- Distribuição de ticket médio: existem de fato dois perfis (Centro ~R$400 / Premium ~R$750) ou é um contínuo?
- Concentração geográfica: quanto é Caxias do Sul vs entorno vs fora da região → define raio de mídia.

**Bloco B — Base acionável (insumo direto para mídia e CRM)**
- Quantificação da base realmente contatável: celulares válidos, deduplicados, prontos para WhatsApp/Custom Audience.
- Arquivos de público segmentado para Meta/Google (clientes A, compradores de marca X, inativos etc.).
- Dimensionamento do gap de e-mail e do que se perde por não capturar (argumento de CRM).

**Bloco C — Marca e cross-sell**
- Matriz cliente × marca: quem compra o quê, sobreposição entre marcas, quais marcas "puxam" cliente de maior valor.
- Oportunidades de cross-sell nomeadas e dimensionadas (ex.: "X mil clientes Altenburg nunca compraram Trussardi").

**Bloco D — Comercial**
- Carteira por vendedor: tamanho, e (por cruzamento com a ABC) valor médio da carteira.
- Clientes atendidos por múltiplos vendedores — indício de ausência de dono da conta.

---

## 6. Conversão para CSV — **feita**

Os PDFs foram convertidos em [`csv/`](csv/). Detalhe completo em [`csv/README-CSV.md`](csv/README-CSV.md); resumo:

| Arquivo | Linhas | Grão |
|---|---:|---|
| `clientes-consolidado.csv` ⭐ | 31.991 | 1 linha por **cliente** — valor + vendedores + marcas + contato |
| `curva-abc-clientes.csv` | 31.891 | 1 por cliente (fonte de valor) |
| `clientes-email-telefones.csv` | 31.729 | 1 por cliente |
| `clientes-por-vendedor.csv` | 42.595 | 1 por **cliente × vendedor** |
| `clientes-por-marca.csv` | 46.315 | 1 por **cliente × marca × vendedor** |
| `vendedores.csv` | 31 | 1 por vendedor (contagens recalculadas) |

**Validação:** todos os totais conferem com os rodapés dos PDFs, com zero linhas descartadas — inclusive R$ 28.810.734,33 e 54.366 unidades na Curva ABC.

Pontos que mudaram a leitura da §3 depois da conversão:

- **Telefone acionável é menor do que a estimativa inicial de 72%.** Com DDD explícito na origem: **15.976 clientes (49,9%)**. Outros 13.853 (43,3%) têm celular sem DDD, onde foi assumido o 54 — dá para usar, com bounce esperado. 2.162 não têm celular aproveitável.
- **Marcas cobrem 22.400 clientes únicos** dos 31.991 — ou seja, ~30% da base não comprou nenhuma das 9 marcas exportadas (reforça a pergunta 3 da §4).
- **100 clientes** aparecem nas listas de contato mas não na Curva ABC (diferença de filtro de filial). Ficam no consolidado com `na_curva_abc = 0`.

Scripts em [`scripts/`](scripts/), reprodutíveis (`python3 parse_abc.py && python3 parse_listas.py && python3 consolida.py`). Requerem `pdftotext`.

---

## 7. Dados sensíveis — LGPD

Estes arquivos contêm **dados pessoais de ~32 mil pessoas físicas identificadas** (nome completo, telefone, celular, cidade e histórico de compra). Consequências práticas:

- Não subir estes PDFs nem derivados nominais para ferramentas externas, apresentações ou drives compartilhados com terceiros.
- Entregáveis para o cliente devem usar **dados agregados e anonimizados** (faixas, percentuais, contagens) — nomes e telefones só em arquivos operacionais entregues diretamente à Casa & Cia.
- Para upload de público em Meta/Google, usar apenas arquivos com telefone **hasheado** pela própria plataforma, e registrar a base legal (relação contratual/legítimo interesse) com o cliente.

---

**Status:** materiais mapeados e compreendidos. Nenhuma análise executada ainda — aguardando confirmação do operador para iniciar (§5).
