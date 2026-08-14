# Análise da base de clientes — Casa & Cia

Base: 31.891 clientes com valor · R$ 28.810.734,33 · 54.366 unidades · **01/01/2024 a 10/08/2026 (31 meses)**
Fonte: [`csv/clientes-consolidado.csv`](csv/clientes-consolidado.csv) · script: [`scripts/analise.py`](scripts/analise.py) · saída bruta: [`analise-saida-bruta.txt`](analise-saida-bruta.txt)
Executado em 11/08/2026, com os dados que temos hoje. As pendências enviadas ao Anderson estão em [`PENDENCIAS-ANDERSON.md`](PENDENCIAS-ANDERSON.md).

---

## ⚠️ Antes de ler: a ambiguidade que atravessa tudo

**Não sabemos se a coluna "Qtde" do ERP é número de compras ou número de peças** (pergunta 1.1 ao Anderson). As duas leituras mudam a conclusão de partes deste documento:

| | Se "Qtde" = **compras** | Se "Qtde" = **peças** |
|---|---|---|
| R$ 529,94 (média geral) | ticket médio de compra | preço médio por peça |
| 65,5% com qtde=1 | compraram **uma única vez** → problema de recompra | levaram **uma única peça** → problema de cesta |
| Seções afetadas | C (recompra) e B (ticket) | idem |

Onde a diferença importa, o texto aponta as duas leituras. **As seções A (concentração), D (geografia), E (marcas), F (contatabilidade) e G (vendedores) não dependem dessa resposta** — valem como estão.

Também vale lembrar: sem data de compra individual (pendência 2.1), **nada aqui é recência**. "Comprou" significa "comprou alguma vez nos 31 meses".

---

## Sumário executivo

1. **A base é mais rasa e mais diluída do que a percepção interna.** A mediana de ticket médio é **R$ 279,82** — metade dos clientes está abaixo disso. Os R$ 400 (Centro) e R$ 750 (Premium) citados no kick-off descrevem bem o topo da base, não o meio dela.
2. **A base é de volume, mas o topo é de carteira.** Os 20% maiores clientes fazem 67,7% da receita — abaixo da regra 80/20 — e são precisos **32,6% da base (10.386 clientes)** para chegar a 80%. Ninguém gerencia dez mil relacionamentos, então o grosso da receita só se move por campanha ampla. Mas **771 clientes gastaram R$ 5.000 ou mais e sozinhos fazem 25,6% do faturamento** — carteira gerenciável que hoje não existe. Ver §A.1.
3. **65,5% da base tem qtde = 1** e responde por 33,1% da receita. Sob qualquer das duas leituras, é o maior buraco identificado.
4. **Cross-sell entre marcas é a alavanca mais forte e mais mensurável.** Quem compra 1 marca gasta R$ 476; 4 marcas, R$ 2.739; 7 marcas, R$ 11.255. E não é só frequência — o ticket médio sobe junto (R$ 361 → R$ 1.189 → R$ 2.424).
5. **O negócio é hiperlocal: 94,4% dos clientes e 93,1% da receita em Caxias do Sul.** Mídia com raio amplo é desperdício. Mas quem vem de fora gasta 26% mais.
6. **O alvo prioritário existe e é nominal:** 3.570 clientes de alto valor que compraram uma única vez, gastaram R$ 1.514 em média, e 93,5% têm celular no cadastro.

---

## A. Concentração de receita

| Corte | Clientes | Receita | % da receita |
|---|---:|---:|---:|
| Top 1% | 318 | R$ 4.545.532 | 15,8% |
| Top 5% | 1.594 | R$ 10.654.324 | 37,0% |
| Top 10% | 3.189 | R$ 14.711.447 | 51,1% |
| Top 20% | 6.378 | R$ 19.514.297 | **67,7%** |
| Top 50% | 15.945 | R$ 25.916.073 | 90,0% |

Curva ABC por faturamento (não por quantidade, como vem no relatório do ERP):

| Faixa | Clientes | % base | Receita | Gasto médio | Ticket médio | Qtde média |
|---|---:|---:|---:|---:|---:|---:|
| **A** (até 80% da receita) | 10.386 | 32,6% | R$ 23.048.755 | R$ 2.219 | R$ 1.023 | 2,65 |
| **B** (80–95%) | 10.364 | 32,5% | R$ 4.321.561 | R$ 417 | R$ 339 | 1,42 |
| **C** (95–100%) | 11.141 | 34,9% | R$ 1.440.418 | R$ 129 | R$ 122 | 1,09 |

Corte da faixa A: **R$ 684,70** de gasto acumulado no período. Ou seja, "cliente A" na Casa & Cia é quem gastou mais de R$ 685 em dois anos e meio — uma régua baixa, que confirma o ponto 2 do sumário.

> **Leitura:** a empresa não tem um problema de dependência de poucos clientes (risco baixo), tem um problema de profundidade — um terço da base precisa ser mobilizado para mover o faturamento. Isso favorece campanha de base ampla (WhatsApp em massa, mídia local) e processo padronizado. **Mas não elimina a carteira** — ver §A.1.

### A.1 O topo tratável como carteira

*(Correção de 14/08. A leitura anterior — "é negócio de volume, não de carteira" — era absoluta demais.)*

| Gastou no período | Clientes | % da base | Receita | % da receita | Gasto médio |
|---|---:|---:|---:|---:|---:|
| ≥ R$ 20.000 | 42 | 0,1% | R$ 1.290.393 | 4,5% | R$ 30.724 |
| ≥ R$ 10.000 | 222 | 0,7% | R$ 3.695.212 | 12,8% | R$ 16.645 |
| **≥ R$ 5.000** | **771** | **2,4%** | **R$ 7.375.742** | **25,6%** | **R$ 9.566** |
| ≥ R$ 3.000 | 1.833 | 5,8% | R$ 11.404.558 | 39,6% | R$ 6.222 |
| ≥ R$ 2.000 | 3.253 | 10,2% | R$ 14.840.409 | 51,5% | R$ 4.562 |

**771 clientes fazem um quarto da receita.** Divididos entre as 8 vendedoras com carteira exclusiva relevante, dão **~96 clientes cada** — tamanho que uma pessoa consegue conhecer pelo nome. **94% têm celular** no cadastro e apenas **10% compraram uma única vez**: é gente que já volta sozinha.

Hoje esse grupo está diluído em territórios de 2.400 a 3.600 pessoas e não recebe nenhum tratamento diferenciado. Nada no processo atual sinaliza que são diferentes.

> **A recomendação correta é operar os dois modelos em paralelo:** volume e processo para a base ampla; acompanhamento nomeado para os 771. Lista em [`csv/publicos/publico_TOP-CARTEIRA.csv`](csv/publicos/publico_TOP-CARTEIRA.csv).
>
> ⚠️ O corte de R$ 5.000 é **operacional, não estatístico** — foi escolhido por dar ~96 clientes por vendedora. Outro corte é defensável. E o valor é acumulado em 31 meses, não anualizado: R$ 5.000 no período equivale a ~R$ 160/mês.

---

## B. Ticket médio — o número conflita com a percepção

- Média: **R$ 485,73** · Mediana: **R$ 279,82** · Média ponderada (receita ÷ qtde): **R$ 529,94**

| Percentil | Ticket médio |
|---|---:|
| P10 | R$ 79,90 |
| P25 | R$ 146,60 |
| **P50** | **R$ 279,82** |
| P75 | R$ 559,72 |
| P90 | R$ 1.053,65 |
| P95 | R$ 1.520,77 |
| P99 | R$ 3.218,55 |

Distribuição — a base se acumula na parte baixa:

| Faixa de ticket | Clientes | % base | % da receita |
|---|---:|---:|---:|
| Até R$ 200 | 12.001 | 37,6% | 7,1% |
| R$ 200–400 | 8.472 | 26,6% | 15,3% |
| R$ 400–750 | 6.056 | 19,0% | 22,6% |
| R$ 750–1.500 | 3.721 | 11,7% | 26,6% |
| R$ 1.500+ | 1.641 | 5,1% | **28,3%** |

**Não há dois picos.** Testei a hipótese dos dois perfis (Centro ~R$ 400 / Premium ~R$ 750): a distribuição é contínua e assimétrica, com pico único entre R$ 100 e R$ 300. Isso pode significar (a) que os dados são de uma loja só, (b) que os dois perfis existem mas se sobrepõem demais para aparecer aqui, ou (c) que a percepção interna reflete o cliente memorável, não o típico. **A pendência 1.2 resolve.**

> **Impacto no posicionamento:** o discurso de venda "elitizada" descreve 16,8% da base (os 5.362 clientes com ticket ≥ R$ 750, que fazem 54,9% da receita). É um segmento real e majoritário em receita — mas é minoria em gente. Vale decidir conscientemente se a comunicação fala com esses 17% ou com os 83%.

---

## C. Compra única vs. recorrente

| Qtde | Clientes | % base | Receita | % receita | Gasto médio |
|---|---:|---:|---:|---:|---:|
| **1** | 20.875 | **65,5%** | R$ 9.538.287 | 33,1% | R$ 457 |
| 2 | 6.130 | 19,2% | R$ 5.967.713 | 20,7% | R$ 974 |
| 3–5 | 4.087 | 12,8% | R$ 8.693.384 | 30,2% | R$ 2.127 |
| 6–10 | 679 | 2,1% | R$ 3.385.820 | 11,8% | R$ 4.986 |
| 11+ | 120 | 0,4% | R$ 1.225.530 | 4,3% | R$ 10.213 |

O ticket médio sobe com a recorrência (R$ 457 → R$ 487 → R$ 590 → R$ 694 → R$ 701): quem volta não só compra mais vezes, **compra mais caro por vez**.

> **Se "Qtde" = compras:** dois terços da base nunca voltou em 31 meses. Com um item de cama/mesa/banho, ciclo de recompra natural de 6 a 18 meses, isso é oportunidade e não fatalidade — mas confirma que não existe régua de retenção operando hoje.
>
> **Se "Qtde" = peças:** dois terços saem da loja com um item só. O problema muda de "recompra" para "cesta", e a alavanca vira treinamento de venda combinada e composição de kits — o que, aliás, casa com o achado de cross-sell da seção E.

Em qualquer dos casos, o número que interessa é o mesmo, e está na seção H.

---

## D. Geografia

| Cidade | Clientes | % base | Receita | % receita | Gasto médio |
|---|---:|---:|---:|---:|---:|
| **Caxias do Sul** | 30.119 | **94,4%** | R$ 26.822.098 | **93,1%** | R$ 891 |
| Flores da Cunha | 345 | 1,1% | R$ 406.797 | 1,4% | R$ 1.179 |
| Farroupilha | 187 | 0,6% | R$ 268.335 | 0,9% | R$ 1.435 |
| São Marcos | 192 | 0,6% | R$ 176.284 | 0,6% | R$ 918 |
| Bento Gonçalves | 105 | 0,3% | R$ 137.341 | 0,5% | R$ 1.308 |
| **Fora de Caxias (total)** | 1.772 | 5,6% | R$ 1.988.636 | 6,9% | **R$ 1.122** |

Quem vem de fora gasta **26% mais** que o cliente de Caxias (R$ 1.122 vs R$ 891) — faz sentido: deslocar-se até a loja pressupõe intenção maior. Farroupilha e Bento Gonçalves se destacam.

> **Duas conclusões operacionais:** (1) mídia paga deve ser hiperlocal — raio amplo queima verba; (2) existe um nicho de expansão regional pequeno em volume (6,9% da receita) mas de ticket alto, que hoje chega por conta própria e nunca foi trabalhado.
>
> ⚠️ A cidade vem truncada em ~20 caracteres no ERP ("CAXIAS DO"). Caxias é inequívoca, mas alguns truncamentos fora dela são ambíguos ("BENTO", "PORTO", "NOVA", "SANTA") e estão marcados com (?) na saída bruta. O detalhamento por bairro depende da pendência 2.5.

---

## E. Marcas e cross-sell — a alavanca mais clara da base

⚠️ Como os relatórios de marca vieram **sem valor** (pendência 2.3), o que segue é **afinidade**, não faturamento por marca: mede o valor do *cliente* que compra cada marca, não quanto a marca vendeu.

| Marca | Clientes | Gasto médio do cliente | Ticket médio | Mediana |
|---|---:|---:|---:|---:|
| Plumassul | 266 | R$ 4.962 | R$ 1.654 | R$ 903 |
| Trussardi | 2.357 | R$ 3.746 | R$ 1.376 | R$ 874 |
| Budd Luxus | 1.423 | R$ 3.539 | R$ 1.262 | R$ 730 |
| Kacyumara | 4.967 | R$ 2.467 | R$ 981 | R$ 626 |
| Buddemeyer | 5.599 | R$ 2.333 | R$ 922 | R$ 572 |
| Karsten | 4.850 | R$ 2.224 | R$ 860 | R$ 536 |
| Niazitex | 6.077 | R$ 2.148 | R$ 855 | R$ 548 |
| **Altenburg** | **11.436** | R$ 1.465 | R$ 639 | R$ 377 |
| Bella Janela | 4.732 | R$ 1.342 | R$ 542 | R$ 364 |
| *(nenhuma das 9)* | 9.555 | R$ 281 | R$ 240 | — |

Duas leituras claras:
- **Altenburg é a porta de entrada** — maior alcance (11.436 clientes, 36% da base) e o menor valor médio entre as marcas. É a marca que traz gente.
- **Trussardi, Budd Luxus e Plumassul são a cauda premium** — pouca gente, valor 2,5x maior. São marcas de segmentação, não de alcance.

### O número de marcas prevê valor melhor que qualquer outra variável

| Marcas | Clientes | % base | Gasto médio | Ticket médio | Qtde média |
|---|---:|---:|---:|---:|---:|
| 0 | 9.555 | 30,0% | R$ 281 | R$ 240 | 1,18 |
| 1 | 12.245 | 38,4% | R$ 476 | R$ 361 | 1,36 |
| 2 | 5.190 | 16,3% | R$ 1.006 | R$ 609 | 1,94 |
| 3 | 2.477 | 7,8% | R$ 1.722 | R$ 849 | 2,57 |
| 4 | 1.231 | 3,9% | R$ 2.739 | R$ 1.189 | 3,19 |
| 5 | 671 | 2,1% | R$ 4.342 | R$ 1.544 | 4,31 |
| 6 | 330 | 1,0% | R$ 6.498 | R$ 1.684 | 5,28 |
| 7 | 147 | 0,5% | R$ 11.255 | R$ 2.424 | 7,27 |
| 8 | 42 | 0,1% | R$ 16.616 | R$ 2.359 | 8,64 |

Parte disso é mecânico (quem compra mais vezes tende a encostar em mais marcas), mas **o ticket médio sobe junto com o número de marcas** — de R$ 361 para R$ 2.424. Ou seja: não é só que compram mais vezes; **compram mais caro**. Ampliar o repertório de marcas do cliente e aumentar o valor dele andam juntos.

### Lacunas de cross-sell dimensionadas

Dos 11.436 clientes Altenburg:
- 8.583 (75,1%) nunca compraram Niazitex
- 8.698 (76,1%) nunca compraram Buddemeyer
- 10.167 (88,9%) nunca compraram Trussardi
- 10.693 (93,5%) nunca compraram Budd Luxus

Dos 2.357 clientes Trussardi (o público de maior valor): 1.088 (46,2%) nunca compraram Altenburg, 1.415 (60,0%) nunca compraram Karsten.

> **Isso é lista pronta.** Cada uma dessas combinações é um público nominal e exportável do `clientes-consolidado.csv` — filtro de duas colunas. O que falta para priorizar entre elas é a margem por marca (pendência 3.1).

### Sobre os 30% sem nenhuma das 9 marcas

9.555 clientes, gasto médio R$ 281, **86,1% com qtde = 1**, e apenas 661 na faixa A. Não parecem ser um fornecedor faltando na exportação — parecem ser a cauda de compra avulsa de item barato. Isso **responde parcialmente a pendência 1.3**, mas ainda vale a confirmação do Anderson.

---

## F. Base contatável

| | Clientes | % |
|---|---:|---:|
| Total no consolidado | 31.991 | 100% |
| Com celular normalizado | 29.829 | 93,2% |
| **Com celular e DDD explícito na origem** | **15.976** | **49,9%** |
| Só com celular sem DDD (assumido 54) | 13.853 | 43,3% |
| Sem celular aproveitável | 2.162 | 6,8% |
| Com e-mail | 248 | 0,78% |

Cobertura nas faixas que importam:

| Faixa | Clientes | Com celular | Com DDD explícito |
|---|---:|---:|---:|
| A | 10.386 | 9.787 (94,2%) | 5.310 (51,1%) |
| B | 10.364 | 9.681 (93,4%) | 5.211 (50,3%) |

Só 173 cadastros compartilham celular com outro — duplicidade é irrelevante.

> **A base de e-mail não existe** (0,78%). Qualquer estratégia de CRM por e-mail parte do zero, e captura de e-mail precisa virar rotina de caixa. O ativo real é o telefone: **~16 mil contatos seguros**, mais ~14 mil que valem tentativa com bounce esperado.
>
> Antes de usar isso em campanha ou como público no Meta, falta a base legal (pendência 3.2).

---

## G. Vendedores

- **24.039 clientes (75,4%)** foram atendidos por um único vendedor; **7.852 (24,6%)** por dois ou mais.
- Quem passou por 2+ vendedores gasta R$ 1.805 em média, contra R$ 609 de quem tem um só. **Isso é mecânico** (mais compras → mais chance de vendedor diferente), não é prova de que rodízio aumenta venda.

Carteira exclusiva — clientes atendidos **só** por aquele vendedor (recorte limpo, sem dupla contagem):

| Vendedor | Clientes | Receita | Gasto médio |
|---|---:|---:|---:|
| 5 — Ritiane | 2.358 | R$ 2.359.969 | **R$ 1.001** |
| 10158 — Maria Paula Pinheiro | 2.018 | R$ 2.040.229 | **R$ 1.011** |
| 43 — Elena Mello | 1.969 | R$ 1.931.658 | **R$ 981** |
| 49 — Bernadete Maria Biagio | 3.209 | R$ 1.773.190 | R$ 553 |
| 5266 — Daiane Rodrigues | 3.202 | R$ 1.749.376 | R$ 546 |
| 44 — Neuza Sostisso Held | 3.202 | R$ 1.666.726 | R$ 521 |
| 120 — Tamires Lunardi | 3.622 | R$ 1.491.211 | R$ 412 |
| 10171 — Janaina Martins da Silva | 3.437 | R$ 1.293.358 | R$ 376 |

Oito vendedores concentram praticamente toda a base. E há **2,7x de diferença no valor médio do cliente** entre o topo (Maria Paula, R$ 1.011) e a base (Janaina, R$ 376) — com carteiras de tamanho parecido, ou até maiores nas de menor valor.

> Essa diferença pode ser skill de venda, mas também pode ser turno, loja, piso ou tipo de produto atendido. **Não dá para concluir com os dados atuais** — precisa da pendência 2.1 (vendas com loja e data) para separar. Se for skill, é a alavanca mais barata do projeto: replicar o que as três primeiras fazem.

---

## H. O alvo prioritário

Cruzando as seções, existe um segmento que é ao mesmo tempo grande, valioso, contatável e claramente mal aproveitado:

### 3.570 clientes de alta valor com uma compra só

- São **34,4% de toda a faixa A**
- Gastaram **R$ 5.405.189** — **18,8% da receita total** dos 31 meses — em uma única passagem
- Gasto médio de **R$ 1.514** cada
- **93,5% têm celular no cadastro**

Uma segunda compra desse grupo, ao mesmo valor médio, seriam **R$ 5,4 milhões**. Mesmo uma conversão de 10% representa R$ 540 mil — mais que qualquer ganho realista de mídia no mesmo período.

Esse é o público que eu recomendaria atacar primeiro, e ele já está isolável no CSV:
`na_curva_abc = 1` · `qtde = 1` · `total >= 684.70` · `whatsapp` preenchido.

Segundo alvo, por ordem de clareza: os **8.583 clientes Altenburg que nunca compraram Niazitex** (e as demais combinações da seção E).

⚠️ Os dois dependem de **base legal para contato** (pendência 3.2). E, sem a data da compra (2.1), não dá para saber se esses 3.570 compraram ontem ou em janeiro de 2024 — o que muda completamente a abordagem da mensagem.

---

## O que segue bloqueado

| Análise | Depende de |
|---|---|
| Recência, inatividade, "há quanto tempo não compra" | 2.1 — vendas com data |
| Sazonalidade, evolução 2024→2025→2026, efeito de campanhas | 2.1 / 2.4 |
| Coorte e churn real | 2.1 |
| Faturamento por marca (aqui só temos afinidade) | 2.3 |
| Comparação Centro vs Premium | 1.2 / 2.4 |
| Priorizar cross-sell por lucro, não por volume | 3.1 — margem |
| Faixa etária e perfil demográfico real da base | 2.5 |
| Mapa por bairro para geotargeting | 2.5 |
| Saber se "compra única" é recompra ou cesta | 1.1 |
