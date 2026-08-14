# Pendências para liberar as análises da base — pedido ao Anderson

Contexto: os 12 relatórios enviados em 10/08/2026 já foram convertidos e validados (ver [`csv/README-CSV.md`](csv/README-CSV.md)). O que segue é o que falta para destravar as análises que os dados atuais não sustentam.

**Prioridade:** 🔴 destrava muita coisa · 🟡 melhora bastante · ⚪ complementar

---

## Bloco 1 — Perguntas (resposta por texto, sem exportar nada)

| # | Pergunta | Por que importa |
|---|---|---|
| 1.1 🔴 | Na Curva ABC, a coluna **"Qtde" é número de compras (notas/atendimentos) ou número de peças?** | Define se o ticket médio de R$ 529,94 é ticket de compra ou preço médio por item. Muda toda a leitura de frequência e de recompra. |
| 1.2 🔴 | Esses dados são **só da loja Premium ou das duas lojas?** | O cabeçalho diz "CASA E CIA PREMIUM", mas o filtro inclui filiais 1 a 6. E o ticket de R$ 529,94 cai justamente **entre** os R$ 400 do Centro e os R$ 750 da Premium que vocês citaram no kick-off — o que sugere base consolidada. É a diferença entre analisar uma loja ou o negócio inteiro. |
| 1.3 🟡 | As **9 marcas** exportadas (Altenburg, Niazitex, Buddemeyer, Kacyumara, Karsten, Bella Janela, Trussardi, Budd Luxus, Plumassul) são todas as relevantes, ou ficou fornecedor de fora? | ~30% dos clientes da base não aparecem em nenhuma das 9. Ou falta marca, ou eles compram itens sem marca cadastrada. |
| 1.4 🟡 | Os **R$ 28,8 milhões** do período são 100% das vendas, ou só as vendas com cliente identificado no caixa? | Se houver muita venda anônima, a base de 31,9 mil clientes subestima o alcance real da loja. |
| 1.5 ⚪ | O que são os grupos **"1º piso loja" e "2º piso loja"**? Qual setor/categoria fica em cada piso? | Um dos relatórios foi filtrado por piso e não por marca — preciso saber o que esse recorte significa para usá-lo. |
| 1.6 🟡 | Aparecem **31 códigos de vendedor** no período. Quais ainda estão na equipe hoje? | Metade da base pode estar em carteira de gente que saiu — ou seja, cliente sem dono. Muda a recomendação comercial. |

---

## Bloco 2 — Exportações novas do ERP

### 2.1 🔴 Relatório de vendas **analítico, com data** — o mais importante da lista
Uma linha por venda, de 01/01/2024 até hoje, com pelo menos:
**data · nº da nota/cupom · código do cliente · loja/filial · vendedor · valor**
e, se o sistema permitir: **produto/grupo/marca · quantidade**.

> Destrava: recência e frequência de compra, RFM, quem está inativo há mais de X meses, sazonalidade mês a mês, curva de recompra, tempo médio entre compras, ticket por loja, evolução 2024 → 2025 → 2026.
>
> **Hoje isso é impossível.** Todos os relatórios enviados são agregados dos 31 meses inteiros — só dá para saber que o cliente comprou alguma vez entre jan/24 e ago/26, não quando. Sem isso, qualquer trabalho de reativação e de CRM fica no chute.
>
> Se o ERP não exportar tudo de uma vez, pode vir quebrado por ano ou por filial.

### 2.2 🔴 Os relatórios em **Excel/CSV**, não em PDF — custo zero
Os mesmos 12 relatórios já enviados, exportados em `.xls`, `.xlsx` ou `.csv`. E, daqui pra frente, sempre nesse formato.
> Destrava: elimina a etapa de conversão e o risco de erro de leitura. A conversão dos PDFs deu certo, mas é retrabalho evitável.

### 2.3 🔴 Vendas por **marca/fornecedor com valor**
Os 9 relatórios de marca vieram só com nome e telefone do cliente — **sem nenhum valor**. Preciso do faturamento por marca; ideal por cliente, mínimo o total de cada marca no período.
> Destrava: quais marcas puxam cliente de maior valor, mix de faturamento, e cross-sell dimensionado em dinheiro (hoje só dá para contar cabeças).

### 2.4 🔴 **Faturamento mensal por loja**, jan/2024 até hoje
Mês a mês, Centro e Premium separados.
> Destrava: sazonalidade real (vocês mencionaram o "serrote" no faturamento), base para meta e forecast de mídia, e confirma de quebra a pergunta 1.2.

### 2.5 🟡 Cadastro do cliente: **data de cadastro, data de nascimento, sexo, bairro/CEP**
> Destrava: quantos clientes novos por ano, faixa etária real da base (hoje a persona é hipótese nossa), e mapa de bairros para segmentar mídia por região.
> Obs.: o relatório enviado tem o filtro "Sexo: T", então esse campo existe no sistema.

### 2.6 🟡 **Categoria de produto**, se existir além de "Fornecedor\" e piso
Ex.: cama / mesa / banho / cortina / colchão / enxoval / decoração.
> Destrava: cross-sell por categoria, pauta de conteúdo e estrutura de campanha por linha de produto.

### 2.7 ⚪ **Vendas sem cliente identificado** no período (valor ou %)
> Destrava: resposta objetiva para a pergunta 1.4.

### 2.8 ⚪ Os valores enviados são **líquidos ou brutos** de devolução/troca?

---

## Bloco 3 — Fora do ERP

### 3.1 🔴 **Margem por marca / categoria** — nem que seja só o ranking, sem números
Quais marcas dão mais margem e quais dão menos, em ordem.
> Sem isso a gente otimiza para faturamento e pode empurrar justamente o que dá menos lucro. Se não puder abrir o número, um ranking relativo já resolve.

### 3.2 🔴 **Consentimento para WhatsApp** — base legal (LGPD)
- Existe opt-in no cadastro da loja? O cliente autoriza receber contato?
- Já houve disparo em massa antes? Qual foi o resultado?
- Os **10 grupos de WhatsApp com 1.800–2.000 pessoas** que você citou são gente que já está nessa base de 32 mil, ou é público separado?

> A base tem ~16 mil celulares confiáveis. Antes de usar isso em campanha ou subir como público no Meta, precisamos saber sob qual base legal.

### 3.3 🟡 **Lista completa das marcas trabalhadas hoje** e quais vocês querem crescer
Complementa a 1.3, e é insumo direto para posicionamento e para o plano de mídia.

---

## O que já dá para fazer sem esperar nada disso

Para o Anderson saber que não estamos parados:

- Curva ABC real por faturamento (concentração de receita em A/B/C)
- Distribuição de ticket médio — testar se existem mesmo dois perfis de cliente
- Compra única vs recorrente (sem a data, mas com a contagem)
- Concentração geográfica por cidade
- Matriz cliente × marca e sobreposição entre marcas
- Dimensionamento da base contatável para WhatsApp e públicos de mídia
- Tamanho de carteira por vendedor

O que **fica bloqueado** até vir o item 2.1: recência, inatividade, sazonalidade, coorte, churn e qualquer régua de CRM baseada em tempo.
