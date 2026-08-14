# CSVs da base do ERP — Casa & Cia

Conversão dos 12 PDFs de `dados-base/` para tabelas. **Nenhum dado foi inventado, estimado ou filtrado** — os CSVs são transcrição fiel dos relatórios, mais colunas derivadas explicitamente marcadas.

Gerado em 11/08/2026 · fonte: exportação do ERP de 10/08/2026 · período 01/01/2024 a 10/08/2026.

## Convenções

- Encoding **UTF-8 com BOM** (abre direto no Excel/Sheets sem quebrar acento).
- Separador **vírgula**; decimais com **ponto** (`3529.9`), formato de máquina. No Excel pt-BR use *Dados → Obter dados → De arquivo de texto* e marque ponto como separador decimal; no Google Sheets abre correto.
- Campos vazios = ausentes no ERP (não são zero).
- `codigo` é a chave de junção entre todos os arquivos.

---

## Arquivos

### `clientes-consolidado.csv` ⭐ comece por aqui
**31.991 linhas — 1 linha por cliente.** Junta os quatro relatórios pelo `codigo`.

| Coluna | Descrição |
|---|---|
| `codigo` | ID do cliente no ERP (chave) |
| `nome` | nome do cliente (pode vir truncado pelo ERP na origem) |
| `cidade`, `uf` | cidade normalizada (maiúscula, sem acento) e UF quando identificável |
| `na_curva_abc` | 1 = tem dados de valor; 0 = aparece só nas listas de contato |
| `qtde`, `total`, `ticket_medio` | do relatório Curva ABC (vazio quando `na_curva_abc = 0`) |
| `rank_qtde` | posição no ranking por quantidade (do próprio relatório) |
| `email` | e-mail (preenchido em apenas 248 clientes) |
| `whatsapp` | **coluna derivada** — melhor celular normalizado, formato `55DDDNNNNNNNNN` |
| `whatsapp_ddd_assumido` | 1 = o número não tinha DDD na origem e foi assumido **54** |
| `telefones_brutos` | todos os telefones encontrados, separados por ` \| `, sem tratamento |
| `n_vendedores`, `vendedores` | quantos e quais vendedores atenderam (`id-NOME \| id-NOME`) |
| `n_marcas`, `marcas` | quantas e quais das 9 marcas o cliente comprou |
| `m_altenburg` … `m_plumassul` | 9 colunas 0/1, uma por marca (para filtro/pivot rápido) |

### `curva-abc-clientes.csv`
31.891 linhas. Transcrição literal da Curva ABC — a **única fonte de valor**.
`rank_qtde, codigo, nome, cidade_raw, cidade, uf, telefone1, telefone2, celular, qtde, total, ticket_medio`
`cidade_raw` preserva o texto original (truncado/sujo); `cidade` e `uf` são derivadas.

### `clientes-email-telefones.csv`
31.729 linhas (1 por cliente). `codigo, nome, telefone, fax, celular, email, vendedor_id, vendedor_nome`

### `clientes-por-vendedor.csv`
42.595 linhas — **formato longo, 1 linha por par cliente×vendedor** (31.901 clientes únicos). Recorte por piso da loja.
`codigo, nome, telefone, celular, fone_emprego, vendedor_id, vendedor_nome`
⚠️ Não conte linhas para contar clientes: deduplique por `codigo`.

### `clientes-por-marca.csv`
46.315 linhas — **formato longo, 1 linha por cliente×marca×vendedor** (22.400 clientes únicos).
`codigo, nome, marca, vendedor_id, vendedor_nome`
Marcas: ALTENBURG, NIAZITEX, BUDDEMEYER, KACYUMARA, KARSTEN, BELLA JANELA, TRUSSARDI, BUDD LUXUS, PLUMASSUL.

### `publicos/` — listas de cross-sell (geradas em 13/08)

11 arquivos, um por oportunidade de venda cruzada, produzidos por [`scripts/afinidade_marcas.py`](../scripts/afinidade_marcas.py).

**Regra de geração:** só entram pares com **lift ≥ 2,5** e público de **valor ≥ R$ 2 milhões**. O corte é deliberadamente restritivo — com lift ≥ 1,5 qualificariam 35 pares, o que devolveria quase toda a base em 35 arquivos de dado pessoal e anularia a priorização.

`publico_A_para_B.csv` = clientes que compram a marca A e **nunca** compraram a B, ordenados por valor gasto.
Colunas: `codigo, nome, cidade, whatsapp, total, ticket_medio, marcas_atuais`

`publico_SEM-MARCA.csv` = os 9.591 clientes que não aparecem em nenhuma das 9 marcas.

> ⚠️ **Não disparar ainda.** Os arquivos estão prontos, mas a base legal de contato (pendência 3.2 com o Anderson: existe opt-in no cadastro?) segue em aberto. Ver §7 de [`../INSTRUCOES-DADOS-BASE.md`](../INSTRUCOES-DADOS-BASE.md).

### `vendedores.csv`
31 vendedores. **Coluna derivada** — o rodapé do PDF traz um acumulado, inútil como contagem.
`vendedor_id, vendedor_nome, clientes_na_carteira, clientes_com_valor_na_abc, soma_total_clientes_abc`
⚠️ `soma_total_clientes_abc` **não é faturamento do vendedor**: o valor total de um cliente é somado a cada vendedor que o atendeu, então há dupla contagem. Serve para ordenar carteiras, não para medir venda individual.

---

## Validação

Todo parser confere seus totais contra o rodapé impresso no PDF. Resultado: **bate exatamente nos 12 arquivos, com zero linhas descartadas.**

| Checagem | Obtido | Esperado (rodapé do PDF) |
|---|---|---|
| Curva ABC — clientes | 31.891 | 31.891 |
| Curva ABC — soma Qtde | 54.366 | 54.366 |
| Curva ABC — soma Total | R$ 28.810.734,33 | R$ 28.810.734,33 |
| E-mails/telefones — clientes | 31.729 | 31.729 |
| Geral por piso — registros | 42.595 | 42.595 |
| 9 marcas — registros | 46.315 | 46.315 (soma) |
| Consolidado — soma Total | R$ 28.810.734,33 | idem ABC |

Os **100 clientes com `na_curva_abc = 0`** aparecem nas listas de contato mas não na Curva ABC — provavelmente diferença de filtro de filial entre os relatórios (a ABC usa filiais 1–6; as demais, 1–999/99999).

---

## O que é derivado (e portanto discutível)

Três colunas não vêm do ERP — foram calculadas aqui e podem ser refeitas com outro critério:

1. **`whatsapp`** — normalização de telefone. Regras: remove não-dígitos; tira zeros à esquerda e prefixo 55; 11 dígitos com 9 na 3ª posição = celular; 10 dígitos começando em 8/9 após o DDD = celular antigo, recebe o nono dígito; sem DDD, assume **54**. Resultado:
   - **15.976 clientes (49,9%)** com celular e **DDD explícito na origem** ← número conservador e confiável
   - **13.853 (43,3%)** só com celular **sem DDD**, onde o 54 foi assumido
   - **2.162 (6,8%)** sem nenhum celular aproveitável
   - Para campanha, a base segura é ~16 mil; os ~14 mil com DDD assumido valem tentar, mas com expectativa de bounce.
   - Há lixo evidente na origem: 73 números com DDD 99 (Maranhão) numa base de Caxias do Sul — quase certamente digitação de placeholder.
2. **`cidade` / `uf`** — normalização de `cidade_raw`, que vem truncado pelo ERP ("CAXIAS DO") e com grafias variadas. A UF só é extraída quando o campo trazia `/UF`.
3. **`vendedores.csv`** — contagens recalculadas do zero (ver ressalva acima).

Tudo o mais é transcrição.

---

## Reprodutibilidade

```bash
cd dados-base/scripts
python3 parse_abc.py        # Curva ABC
python3 parse_listas.py     # e-mails + geral + 9 marcas
python3 consolida.py        # consolidado + vendedores
```

Requer `pdftotext` (poppler: `brew install poppler`). Os scripts extraem o texto sozinhos para `.txt-cache/` na primeira execução — essa pasta é cache descartável (20 MB), pode apagar a qualquer momento.

Para ajustar uma regra (ex.: mudar o DDD padrão, tratar `(99)` como inválido), edite `consolida.py` e rode de novo — os CSVs são sobrescritos.

---

## LGPD

Estes CSVs contêm dados pessoais identificados de ~32 mil pessoas, agora em formato **muito mais fácil de vazar e de importar em qualquer lugar** do que os PDFs originais. Mesmas restrições da pasta-mãe: não subir para ferramentas externas, não anexar em apresentação, e usar só agregados nos entregáveis ao cliente. Ver §7 de `../INSTRUCOES-DADOS-BASE.md`.
