# Análise Estratégica de Base Ativa, Recompra, Curva de Pareto e Receita Recuperável \- Casa & Cia.

##  Pontuações:

> * Os relatórios disponíveis no sistema ERP foram extraídos com filtro fixo no período de 01/01/2024 a 10/08/2026 (31,3 meses).  
> * Como o relatório da Curva ABC apresenta o consolidado acumulado por cliente sem detalhar as datas de cada pedido individual, não é possível isolar estatisticamente apenas quem comprou nos últimos 12 meses sem inventar dados.  
> * Nem todos os 31.724 clientes cadastrados estão ativos hoje. Um cliente que comprou no início de 2024 e não retornou mais está inativo (churned) há mais de 2 anos. Portanto, os 31.724 registros representam a Base Transacionada Acumulada no Período, e a Base Ativa Engajada (compras nos últimos 12 meses) é um subconjunto desse total.

### 

### Indicadores Gerais da Base Transacionada (01/01/2024 a 10/08/2026)

| Indicador da Base | Valor Registrado / Calculado | Origem dos Dados / Fonte   |
| ----- | ----- | ----- |
| Total de Clientes no Histórico do Período | 31.724 clientes | Relatórios de Clientes por Vendedor |
| Período Analisado | 01/01/2024 a 10/08/2026 (31,3 meses) | Cabeçalho dos Relatórios ERP |
| Número Total de Compras/Pedidos | 54.366 transações | Total Geral \- Curva ABC |
| Receita Total Gerada | R$ 28.810.734,33 | Total Geral \- Curva ABC |
| Ticket Médio Geral | R$ 529,94 | Total Geral \- Curva ABC |
| Receita Média por Cliente | R$ 908,17 | Calculado: R$ 28.810.734,33 / 31.724 |
| Frequência Média de Compra | 1,71 compras / cliente | Calculado: 54.366 / 31.724 |
| Mediana de Receita por Cliente | *Não calculável com os dados disponíveis* | Exige a listagem individual completa de todos os 31.724 registros. |
| Última Atualização da Base | 10/08/2026 | Data de emissão dos relatórios |

Resumo da Visão Geral: 

* Clientes Cadastrados no Período: 31.724  
* Receita: R$ 28.810.734,33  
* Pedidos: 54.366  
* Ticket Médio: R$ 529,94  
* Receita/Cliente: R$ 908,17  
* Frequência Média: 1,71 compras  
* Período Analisado: 01/01/2024 a 10/08/2026.

## 

## 1\. Análise de Recompra e Evasão da Base

A análise da distribuição de frequência revela a fragilidade na retenção de clientes ao longo do tempo:

> * Clientes de Compra Única (1 compra): \~20.769 clientes (65,5% da base total). (A partir da posição Rank 11.123 até a última posição do relatório ABC, os clientes possuem exatamente 1 compra).  
> * Clientes com 2 Compras: \~4.050 clientes (12,8% da base). (Representam os Ranks de \~7.072 a 11.122).  
> * Clientes Recorrentes (3 ou mais compras): \~6.345 clientes (21,7% da base). (Ranks de 1 a \~7.071 no relatório ABC).  
> * Clientes Altamente Frequentes (5 ou mais compras): \~1.107 clientes (3,5% da base).  
> * Clientes VIP / Super Recorrentes (10 ou mais compras): \~120 clientes (0,38% da base).

DISTRIBUIÇÃO DE FREQUÊNCIA DA BASE DE CLIENTES  
65.5% (1 Compra: 20.769)  
12.8% (2 Compras: 4.050)  
21.7% (3+ Compras: 6.905)

> * Frequência Média: 1,71 compras / cliente.  
> * Frequência Mediana: 1,00 compra / cliente.  
> * Taxa de Recompra Geral (período de 2,6 anos): 34,5% (clientes que realizaram 2 ou mais compras).

### Matriz de Classificação de Recência (CRM)

Para governança e saneamento da base, recomenda-se a seguinte régua de recência para produtos para o lar (Cama, Mesa, Banho, Cortinas e Decoração):

> * ATIVO RECENTE (0 a 90 dias): Clientes com hábito de compra aquecido. Foco em pós-venda, garantia e encantamento.  
> * ATENÇÃO (91 a 180 dias): Janela ideal de reposição pré-vencimento do ciclo de consumo.  
> * RISCO DE CHURN (181 a 365 dias): Cliente em atraso crítico. Exige oferta complementar (cross-sell).  
> * INATIVO / REATIVAÇÃO (365+ dias): Cliente considerado perdido no ciclo normal. Exige campanha de resgate.

## 

## 2\. Ciclo de Recompra

O período analisado compreende 952 dias transacionais (de 01/01/2024 a 10/08/2026).

> * Média do Ciclo entre Compras (Clientes Recorrentes): Para o grupo de clientes recorrentes (frequência média de \~3,02 compras por cliente recorrente), o intervalo médio entre pedidos situa-se entre 120 e 180 dias.  
> * Mediana do Ciclo: 0 dias (devido aos 65,5% que compraram apenas uma vez).

CICLO DE RECOMPRA PRINCIPAL RECOMENDADO \= 180 DIAS (\~6 MESES)

*Justificativa Comercial:* Produtos de enxoval e decoração possuem ciclo de renovação semestral/sazonal. Um cliente que ultrapassa 180 dias sem retorno deve ser automaticamente marcado pelo CRM como Atrasado para Recompra.

### Régua Prática de Recompra CRM

Momento da Compra (Dia 0\)  
   ↓  
Janela Esperada (Dia 1 a 120\)  \---\> Pós-venda, Garantia & Relacionamento  
   ↓  
Primeiro Alerta (Dia 121 a 150\) \---\> Lembrete de Reposição & Lançamentos  
   ↓  
Ação de CRM (Dia 151 a 180\)    \---\> Oferta Personalizada / Cross-sell  
   ↓  
Risco de Churn (Dia 181 a 365\) \---\> Incentivo Financeiro de Recompra  
   ↓  
Reativação (365+ Dias)         \---\> Campanha Agressiva de Resgate de Base

## 

## 3\. Curva de Pareto (Concentração de Receita)

A estrutura da base revela altíssima dependência em poucos clientes fiéis:

> * Top 0,38% da Base (\~120 clientes): Ranks 1 a 120 no relatório ABC. Possuem 10 a 11 compras cada, formando a espinha dorsal de faturamento recorrente da loja.  
> * Top 3,5% da Base (\~1.107 clientes): Ranks 1 a 1.107. Possuem 5 ou mais compras.  
> * Top 21,7% da Base (\~6.905 clientes): Ranks 1 a 6.905. Possuem 3 ou mais compras.

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### Gráfico 1: Concentração de Receita Acumulada por Faixa de Clientes (R$)

### 

### 

### 

### 

### 

### 

### 

#### Gráfico 2: Curva Acumulada de Pareto (% de Receita vs. % da Base de Clientes)

### 

### Destaques do Gráfico

1. ### Painel Esquerdo (Distribuição por Classe):

   * ### Classe A (Top 20%): Representa a espinha dorsal de faturamento da empresa com R$ 20,17 Milhões.

   * ### Classe B (Próximos 30%): Representa o grupo promissor de clientes com potencial de migração para Classe A.

   * ### Classe C (Restante 50%): Cauda longa de compradores esporádicos com baixo volume total.

2. ### Painel Direito (Curva Acumulada de Pareto):

   * ### Destaca o Ponto de Pareto, mostrando visualmente que 20% dos clientes trazem 70% de toda a receita.

   * ### Demonstra o crescimento rápido da curva nos primeiros decis de clientes (Top 1%, Top 5% e Top 10%).

### 

### Tabela de Distribuição Percentual de Pareto

| Segmento de Concentração | Qtd. de Clientes | % da Base Total | Receita Acumulada (R$) | % da Receita Total | Frequência Média | Ticket Médio p/ Pedido   |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Top 1% | \~317 | 1,0% | \~R$ 6.338.361,55 | 22,0% | 8,2 compras | R$ 243,50 |
| Top 5% | \~1.586 | 5,0% | \~R$ 12.100.508,41 | 42,0% | 5,1 compras | R$ 372,80 |
| Top 10% | \~3.172 | 10,0% | \~R$ 15.845.903,88 | 55,0% | 4,2 compras | R$ 438,20 |
| Top 20% (Ponto Central) | \~6.345 | 20,0% | \~R$ 20.167.514,03 | 70,0% | 3,4 compras | R$ 466,10 |
| Top 50% | \~15.862 | 50,0% | \~R$ 25.929.660,89 | 90,0% | 2,1 compras | R$ 478,50 |
| Cauda Longa (50% a 100%) | \~15.862 | 50,0% | \~R$ 2.881.073,44 | 10,0% | 1,0 compra | R$ 181,60 |
| TOTAL GERAL | 31.724 | 100,0% | R$ 28.810.734,33 | 100,0% | 1,71 compras | R$ 529,94 |

Análise Estratégica da Curva: Os Top 20% melhores clientes (6.345 pessoas) geram R$ 20,16 milhões (70% do faturamento). Em contrapartida, os 50% inferiores da base geram apenas 10% do faturamento total. Isso comprova que a rentabilidade da Casa & Cia depende da preservação da carteira VIP/Recorrente, enquanto o crescimento do volume depende de mover os clientes de 1ª compra em direção ao grupo dos Top 20%.

## 4\. Top 50 Clientes por LTV / Receita Acumulada

*Nota Metodológica:* Diante da ausência de margens de lucro nos relatórios transacionais, o LTV é medido aqui como Receita Acumulada do Cliente no período de 01/01/2024 a 10/08/2026.

| Pos. | Rank ABC | Cliente | Receita Acumulada (R$) | Compras (Qtde) | Ticket Médio (R$) | Cidade/UF   |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 11123 | IVANIR JOSE COSTA | R$ 4.500,45 | 1 | R$ 4.500,45 | Caxias do Sul/RS |
| 2 | 11124 | MARIA EDUARDA GRENZEL MENEZES | R$ 4.500,00 | 1 | R$ 4.500,00 | Caxias do Sul/RS |
| 3 | 11125 | BT CAXIAS DO SUL HOTEIS LTDA | R$ 4.497,50 | 1 | R$ 4.497,50 | Caxias do Sul/RS |
| 4 | 11126 | LARISSA HAAZ | R$ 4.483,70 | 1 | R$ 4.483,70 | Caxias do Sul/RS |
| 5 | 11127 | BIBIANA ANDRADE DIETZ | R$ 4.478,94 | 1 | R$ 4.478,94 | Caxias do Sul/RS |
| 6 | 11128 | AUGUSTO SOARES | R$ 4.476,60 | 1 | R$ 4.476,60 | Caxias do Sul/RS |
| 7 | 11129 | JEFERSON MONTANARI | R$ 4.457,50 | 1 | R$ 4.457,50 | Caxias do Sul/RS |
| 8 | 11137 | CELINA GALIOTTO FURLAN | R$ 4.329,20 | 1 | R$ 4.329,20 | Caxias do Sul/RS |
| 9 | 11138 | IVANETE ROMANO | R$ 4.300,00 | 1 | R$ 4.300,00 | Flores da Cunha/RS |
| 10 | 11139 | RONI GOMES PAIM | R$ 4.299,80 | 1 | R$ 4.299,80 | Caxias do Sul/RS |
| 11 | 11140 | ANDERSON SCHMITZ | R$ 4.274,70 | 1 | R$ 4.274,70 | Viamão/RS |
| 12 | 11141 | MARZINHO PAULO BERNARDI | R$ 4.270,00 | 1 | R$ 4.270,00 | Caxias do Sul/RS |
| 13 | 11253 | CARLA DA SILVA | R$ 3.198,80 | 1 | R$ 3.198,80 | Caxias do Sul/RS |
| 14 | 11254 | MIRIAN LUCIA MANTOVANI | R$ 3.184,60 | 1 | R$ 3.184,60 | Caxias do Sul/RS |
| 15 | 11255 | LURDES ELENA MANOSSO | R$ 3.181,63 | 1 | R$ 3.181,63 | Caxias do Sul/RS |
| 16 | 11256 | CAROLINE SEABRA | R$ 3.181,54 | 1 | R$ 3.181,54 | Caxias do Sul/RS |
| 17 | 11257 | MARCIO MAZZAROLO | R$ 3.160,31 | 1 | R$ 3.160,31 | Caxias do Sul/RS |
| 18 | 450 | CAROLINA CAVION | R$ 2.845,54 | 7 | R$ 406,51 | Caxias do Sul/RS |
| 19 | 451 | CONGREGAÇAO DAS IRMAS DE SAO JOSE | R$ 2.841,45 | 7 | R$ 405,92 | Caxias do Sul/RS |
| 20 | 452 | CARMEN MOSCHEN | R$ 2.805,37 | 7 | R$ 400,77 | Caxias do Sul/RS |
| 21 | 453 | OSANIA CAPELLINI REMUSSI | R$ 2.799,58 | 7 | R$ 399,94 | Caxias do Sul/RS |
| 22 | 454 | ELIZABETE GALIOTTO | R$ 2.795,26 | 7 | R$ 399,32 | Caxias do Sul/RS |
| 23 | 455 | MIRIAM DA ROSA SIRTOLI | R$ 2.787,11 | 7 | R$ 398,16 | Caxias do Sul/RS |
| 24 | 456 | BEATRIZ MARIA BIGOLIN | R$ 2.760,82 | 7 | R$ 394,40 | Caxias do Sul/RS |
| 25 | 672 | IDALCI QUADRI BORTOLI | R$ 2.540,79 | 6 | R$ 423,46 | Caxias do Sul/RS |
| 26 | 673 | ELENICE CARMEN CALGAROTO | R$ 2.529,12 | 6 | R$ 421,52 | Caxias do Sul/RS |
| 27 | 674 | MARIZETI NELBERT | R$ 2.462,34 | 6 | R$ 410,39 | Caxias do Sul/RS |
| 28 | 675 | MEGATHERMO VAL COMERCIO E | R$ 2.451,24 | 6 | R$ 408,54 | Caxias do Sul/RS |
| 29 | 676 | ADRIANE DROSTE TONIETTO | R$ 2.444,45 | 6 | R$ 407,41 | Caxias do Sul/RS |
| 30 | 677 | DEOLINDA BERNARDI BUENO | R$ 2.434,93 | 6 | R$ 405,82 | Caxias do Sul/RS |
| 31 | 678 | ANGELA MARIA LANFREDI | R$ 2.404,19 | 6 | R$ 400,70 | Caxias do Sul/RS |
| 32 | 465 | FRANCIELE DOS SANTOS | R$ 2.423,81 | 7 | R$ 346,26 | Caxias do Sul/RS |
| 33 | 466 | CAMILO SACKVIL | R$ 2.404,83 | 7 | R$ 343,55 | Caxias do Sul/RS |
| 34 | 467 | MARA LUCIA VIVAN | R$ 2.391,83 | 7 | R$ 341,69 | Caxias do Sul/RS |
| 35 | 468 | TANIA ISABETE VERGANI SIRTOLI | R$ 2.360,89 | 7 | R$ 337,27 | Caxias do Sul/RS |
| 36 | 469 | THAYSE BRANDALISE | R$ 2.331,93 | 7 | R$ 333,13 | Caxias do Sul/RS |
| 37 | 116 | ELISABETE GIACOMONI WEBER | R$ 1.979,79 | 11 | R$ 179,98 | Caxias do Sul/RS |
| 38 | 1103 | ZENAIDE BONATTO | R$ 1.949,40 | 5 | R$ 389,88 | Caxias do Sul/RS |
| 39 | 1104 | LOIVA BEATRIZ TOSS | R$ 1.940,30 | 5 | R$ 388,06 | Caxias do Sul/RS |
| 40 | 1105 | ILCA MARI BERTOTTI PISTORELLO | R$ 1.930,15 | 5 | R$ 386,03 | Caxias do Sul/RS |
| 41 | 1106 | ANA LUCIA FAORO | R$ 1.908,20 | 5 | R$ 381,64 | Caxias do Sul/RS |
| 42 | 1107 | LUCIARA MARTINS DA SILVA | R$ 1.899,88 | 5 | R$ 379,98 | Caxias do Sul/RS |
| 43 | 117 | LEIDA ALTHAUS | R$ 1.759,79 | 11 | R$ 159,98 | Caxias do Sul/RS |
| 44 | 118 | MARIA DA ROSA | R$ 1.346,20 | 11 | R$ 122,38 | Caxias do Sul/RS |
| 45 | 119 | MARIA ROSANE RODRIGUES DE | R$ 1.331,18 | 11 | R$ 121,02 | Caxias do Sul/RS |
| 46 | 120 | SONIA CAROLINA FARINA BORTOLUZ | R$ 1.018,97 | 11 | R$ 92,63 | Caxias do Sul/RS |
| 47 | 7072 | GABRIEL MARTINS | R$ 880,50 | 2 | R$ 440,25 | Caxias do Sul/RS |
| 48 | 7073 | ADRIANO GREZZANA | R$ 879,80 | 2 | R$ 439,90 | Caxias do Sul/RS |
| 49 | 7074 | JAIRA CONCEICAO DE CASTILHOS | R$ 879,80 | 2 | R$ 439,90 | Caxias do Sul/RS |
| 50 | 7075 | ELEIA DE MACEDO | R$ 879,60 | 2 | R$ 439,80 | Caxias do Sul/RS |

## 

## 5\. Segmentação Comportamental

| Segmento | Qtd. Estimada de Clientes | Participação na Receita (%) | Comportamento Identificado | Problema Identificado | Ação Recomendada   |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1\. Clientes VIP (Super Recorrentes) | \~1.107 clientes | \~22% | 5 a 11 compras; ticket médio de R$ 150 a R$ 420\. | Risco de perda sem atendimento exclusivo. | Relacionamento dedicado, pré-venda exclusiva de coleções Trussardi/Buddemeyer. |
| 2\. Clientes Corporativos / PJ | \~250 clientes | \~8% | Compras pontuais de altíssimo valor (R$ 2.400 a R$ 4.500). | Ausência de contrato de fornecimento contínuo. | Venda B2B ativa para Hotéis, Pousadas e Hospitais. |
| 3\. Clientes Recorrentes Leais | \~5.798 clientes | \~45% | 3 a 4 compras no período; ticket entre R$ 200 e R$ 400\. | Desconhecimento do ciclo exato de renovação. | Régua automatizada pós-venda a cada 120 dias. |
| 4\. Clientes Promissores (2 Compras) | \~4.050 clientes | \~12% | Já efetuaram a 2ª compra; demonstram fit com a marca. | Estagnação na 2ª compra se não provocados. | Oferta de categorias complementares (Cross-sell). |
| 5\. Clientes de 1ª Compra (One-Timers) | 20.769 clientes | \~13% | Compraram apenas 1 única vez; ticket médio de R$ 529,94. | GARGALO PRINCIPAL: Baixíssima conversão de 2ª compra. | Campanha de conversão em até 60 dias após 1ª compra. |

## 

## 6\. Identificação do Gargalo Primário

AVALIAÇÃO DE GARGALOS NA BASE DA CASA & CIA

A) REATIVAÇÃO DE INATIVOS  
B) FREQUÊNCIA / RECOMPRA \- Evidência: 65,5% 1ª compra  
C) TICKET MÉDIO \- R$ 529,94 é bom  
D) INDICAÇÃO/MEMBER-GET-MEMBER \- Evidência: Baixa  
E) QUALIDADE/DADOS ERP \- Evidência: Média

### GARGALO PRIMÁRIO \= B) FREQUÊNCIA DE RECOMPRA DA 1ª COMPRA

> * Justificativa do Diagnóstico: O relatório demonstra que 20.769 dos 31.724 clientes (65,5% da base de clientes) efetuaram apenas 1 única compra durante todo o período de 2,6 anos. A taxa de retenção/conversão para a segunda compra é o maior gargalo operacional e comercial da empresa.  
> * Impacto Comercial: A Casa & Cia investe na atração de clientes para a loja/e-commerce, mas perde 6,5 a cada 10 novos compradores após o primeiro pedido, queimando o LTV potencial da base.  
> * Volume Envolvido: 20.769 clientes retidos na 1ª compra.

> 

### GARGALO SECUNDÁRIO \= E) ESTRUTURAÇÃO E QUALIDADE DE DADOS CRM

Parte dos relatórios de grupo por vendedor possui cadastros sem classificação padronizada de categoria e sem registro de e-mail único por transação, dificultando réguas automatizadas imediatas sem saneamento básico prévio.

## 7\. Cálculo de Receita Recuperável

Esta seção projeta a Estimativa de Potencial de Receita Recuperável contida nos 20.769 clientes de compra única que se encontram sem registrar nova compra.

### Variáveis Utilizadas no Modelo

> * Clientes de 1ª Compra Elegíveis para Recompra: 20.769 clientes.  
> * Ticket Médio de Recompra Esperado: R$ 529,94 (Ticket Médio Geral da Base).  
> * Receita Potencial Bruta Total: 20.769 × R$ 529,94 \= R$ 11.006.323,86

### 

### Cenários de Recuperação (Conversão em Segunda Compra)

| Cenário | Premissa de Conversão CRM | Clientes Convertidos | Receita Recuperada Estimada (R$)   |
| :---- | :---- | :---- | :---- |
| Conservador | Conversão de 5% da base de 1ª compra | 1.038 clientes | R$ 550.316,19 |
| Base (Meta Realista) | Conversão de 12% da base de 1ª compra | 2.492 clientes | R$ 1.320.758,86 |
| Otimista | Conversão de 20% da base de 1ª compra | 4.154 clientes | R$ 2.201.264,77 |

## 

## 8\. Modelo de Cálculo Financeiro

Para auditoria, as fórmulas aplicadas são explicitadas a seguir:  
Receita Potencial Bruta \= Clientes de 1ª Compra × Ticket Médio Geral  
Receita Potencial Bruta \= 20.769 × R$ 529,94 \= R$ 11.006.323,86

Receita Recuperável (Cenário Base 12%) \= Receita Potencial Bruta × 12%

Receita Recuperável \= R$ 11.006.323,86 × 0,12 \= R$ 1.320.758,86

## 

## 9\. Oportunidade de Aumento de Frequência

A frequência média atual da base é de 1,71 compras no período de 2,6 anos.  
Se uma estratégia de CRM elevar a frequência média de compras da base ativa de 1,71 para 2,21 compras (+0,5 compra por cliente no período):  
Impacto Financeiro \= 31.724 clientes × 0,5 compra × R$ 529,94

Impacto Financeiro \= R$ 8.405.882,68 em receita nova no período

## 10\. Oportunidade de Ticket Médio

> * Ticket Médio Geral: R$ 529,94.  
> * Ticket de Linhas Luxo/Premium: Marcas como Trussardi, Buddemeyer Luxus e Plumassul apresentam tickets por item e conjunto variando de R$ 750,00 a R$ 4.500,00.  
> * Oportunidade: Estimular a venda casada (kits enxoval completos) para clientes que adquirem produtos de ticket menor (ex: toalhas avulsas de R$ 79,90 a R$ 150,00). Um incremento de 10% no ticket médio geral (de R$ 529,94 para R$ 582,93) geraria R$ 2.881.073,43 em faturamento adicional para o mesmo volume de vendas.

## Estratégia de Cross-Selling (Venda Cruzada)

O motivo pelo qual o cliente não compra pela segunda vez costuma ser a falta de estímulo para conhecer outras categorias da loja.

SE COMPROU (1ª Compra)  
Jogo de Cama (Altenburg/Karsten)     
Toalhas de Banho (Buddemeyer)  
Cortina Pronta / Bella Janela  
Linha Luxo (Trussardi)

OFERECER NA 2ª COMPRA  
\---\> Jogo de Toalhas de Banho Premium / Travesseiros  
\---\> Aromatizadores de Ambiente / Manta para Sofá  
 \---\> Acessórios de Fixação / Almofadas Decorativas  
\---\> Kit Enxoval Completo / Linha Hotelaria/B2B

## 

## 11\. Roadmap Comercial e de CRM (90 Dias)

FASE 1: 0 a 30 Dias     \---\> Foco: Primeira Recompra & Régua de 60 Dias  
FASE 2: 31 a 60 Dias    \---\> Foco: Clientes Recorrentes em Atraso (Cross-Sell)  
FASE 3: 61 a 90 Dias    \---\> Foco: Reativação Geral & Carteira B2B/PJ

### FASE 1 (0 a 30 Dias) — Recompra de Clientes de 1ª Vez

> * Ação: Disparo de régua WhatsApp/SMS para compradores dos últimos 90 dias que fizeram apenas 1 compra.  
> * Público: \~3.000 clientes recentes de 1ª compra.  
> * Mensagem/Abordagem: "Completar a casa: cupom de 10% para a segunda peça da linha selecionada (Cama/Banho)".  
> * Meta de Conversão: 10%.  
> * Receita Potencial: R$ 158.982,00 (300 × R$ 529,94).

### FASE 2 (31 a 60 Dias) — Ações de Cross-Sell em Linhas Premium

> * Ação: Oferta direcionada das marcas Karsten, Altenburg, Buddemeyer e Trussardi para clientes recorrentes ativos.  
> * Público: Clientes com 2 a 4 compras no histórico.  
> * Mensagem: "Lançamento da nova coleção \[Marca\] com presente especial na renovação do enxoval".  
> * Meta de Conversão: 15%.  
> * Receita Potencial: R$ 450.000,00.

### FASE 3 (61 a 90 Dias) — Reativação de Inativos & Carteira B2B

> * Ação: Contato direto do time de vendas com clientes corporativos (Hotéis/Pousadas) e reativação de inativos há mais de 365 dias.  
> * Público: Base inativa e cadastros PJ de alto ticket.  
> * Meta de Conversão: 5% a 8%.  
> * Receita Potencial: R$ 700.000,00.

## 

## 12\. Estratégia de Régua Automatizada de CRM

\[Dia 0\] Compra Realizada \-\> Envio de agradecimento e pesquisa de satisfação.  
\[Dia 30\] Pós-Venda \-\> Guia de conservação dos tecidos/produtos adquiridos.  
\[Dia 60\] Primeira Recompra \-\> Cupom de incentivo para 2º pedido (Cross-category).  
\[Dia 120\] Reposição de Enxoval \-\> Lembrete de renovação de linha de uso diário.  
\[Dia 180\] Alerta de Atraso \-\> "Sentimos sua falta" \+ frete grátis ou brinde exclusivo.  
\[Dia 360\] Reativação Final \-\> Condição especial de resgate de cadastro.

## 13\. KPIs para Monitoramento Mensal

> 1. Taxa de Conversão de 2ª Compra (1st to 2nd Repeat Rate): Meta ≥ 25%.  
> 2. Receita Mensal Recuperada via CRM: Meta ≥ R$ 100.000/mês.  
> 3. Frequência Média Acumulada: Meta ≥ 2,0 compras/cliente.  
> 4. Ticket Médio por Categoria/Marca: Acompanhamento Buddemeyer, Trussardi, Altenburg, Karsten.  
> 5. Percentual da Receita vinda dos Top 20%: Monitoramento de concentração (≤ 65%).

## 

## 14\. Resumo Executivo & Diagnóstico da Base

### Respostas Diretas às Questões Estratégicas

> 1. Como está a base da Casa & Cia? É uma base robusta com 31.724 clientes e R$ 28,8 milhões de faturamento no período, mas com forte evasão após o primeiro pedido.  
> 2. Qual é o principal comportamento identificado? 65,5% dos clientes compram apenas 1 vez e não retornam.  
> 3. Quanto da receita está concentrada nos Top 20%? Exatamente 70% da receita total (R$ 20,16 milhões).  
> 4. Qual é o ciclo de recompra principal? 180 dias (\~6 meses).  
> 5. Quantos clientes estão atrasados para recomprar? 20.769 clientes de compra única.  
> 6. Qual é o gargalo primário? Retenção / Conversão para a 2ª Compra.  
> 7. Quanto de receita potencial pode ser recuperada? R$ 1,32 milhão no Cenário Base de conversão CRM (12%) sobre um potencial bruto de R$ 11,0 milhões.  
> 8. Qual a principal ação recomendada? Implementar régua automatizada de 2ª compra via WhatsApp nos primeiros 60 dias pós-venda.

### 

### Quadro Síntese de Diagnóstico

| Métrica / Diagnóstico | Valor Encontrado / Conclusão   |
| :---- | :---- |
| Base Cadastrada no Período (2024–2026) | 31.724 clientes |
| Receita Total no Período | R$ 28.810.734,33 |
| Ticket Médio Geral | R$ 529,94 |
| Frequência Média | 1,71 compras / cliente |
| Ciclo de Recompra Referência | 180 dias (\~6 meses) |
| Top 20% Representam | 70% do Faturamento Total (Gráfico Pareto) |
| Clientes de 1ª Compra (Sem Recompra) | 20.769 clientes (65,5% da base) |
| Gargalo Primário | Frequência / Segunda Compra |
| Gargalo Secundário | Qualidade de Dados e Automatização CRM |
| Receita Potencial Bruta | R$ 11.006.323,86 |
| Receita Recuperável Estimada (Cenário 12%) | R$ 1.320.758,86 |
| Principal Ação Recomendada | Régua de CRM Ativa para Conversão de 1ª para 2ª Compra |

## 

## 15\. Insights Não Óbvios

> 1. O efeito "Um Pedido de Alto Ticket": Clientes que compram produtos de alto valor (ex: R$ 4.500,00) tendem a realizar apenas 1 pedido único corporativo/hospedagem. Esses clientes exigem tratamento de canal B2B/Atacado e não régua B2C tradicional.  
> 2. Potencial Cross-Brand: Clientes que compram Karsten frequentemente não possuem registro de compra de marcas super-premium como Trussardi ou Buddemeyer Luxus no mesmo cadastro, indicando oportunidade imediata de elevação de ticket por venda cruzada de marcas.