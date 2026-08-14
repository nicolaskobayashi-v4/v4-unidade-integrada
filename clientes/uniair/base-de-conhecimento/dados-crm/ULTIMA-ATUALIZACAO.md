# Última atualização das bases — dados-crm (Uniair)

Consulte esta tabela antes de usar qualquer base desta pasta para saber se os dados ainda estão atualizados.

| Arquivo | Última atualização | Origem |
|---|---|---|
| `contatos_vendas.csv` | 2026-08-03 | Export manual (telefones normalizados; correção manual do valor da Ana Dubiela para 81.900) |
| `GrowthPack _ Uniair - Base de Leads (4).csv` | 2026-08-03 | Export da planilha [GrowthPack \| Uniair](https://docs.google.com/spreadsheets/d/1Rmra7RGvh6Zh8bMJ61jse5bXtqIwBNZC-yqyOr19Zes/edit) |
| `contatos_vendas_enriquecido.csv` | 2026-08-03 | Gerado por `cruzar_growthpack.py` (cruzamento contatos_vendas × Growth Pack) |

> Ao subir uma nova versão de algum desses arquivos, atualize a data correspondente nesta tabela.

## Rotina mensal: cruzar contatos_vendas com o Growth Pack

Script: `cruzar_growthpack.py`. Casa telefones pelos últimos 8 dígitos (ignora o 9º dígito do WhatsApp, que varia conforme configuração do aparelho). Quando o mesmo telefone aparece em mais de um lead do Growth Pack, usa a conversão mais antiga. Sem match, preenche em branco.

Para rodar de novo (após subir uma nova versão do `contatos_vendas.csv` e/ou do CSV do Growth Pack):

```
cd dados-crm
python3 cruzar_growthpack.py
```

Gera/sobrescreve `contatos_vendas_enriquecido.csv`.
