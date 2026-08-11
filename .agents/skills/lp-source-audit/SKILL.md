---
name: lp-source-audit
description: Auditar somente em leitura as fontes disponíveis para uma landing page e determinar a implementação correta e seu grau de prontidão. Usar antes de baseline, design ou retomada de projeto; não usar para editar arquivos, produzir estratégia ou corrigir automaticamente lacunas.
---

# LP Source Audit

## 1. Propósito

Determinar, com evidência rastreável, qual implementação e quais fontes devem alimentar a landing page, identificando versões duplicadas, conflitos e lacunas antes de qualquer escrita.

## 2. Quando usar

- No início de uma produção ou retomada de landing page.
- Quando existirem múltiplas versões de HTML, CSS, JavaScript ou assets.
- Quando não estiver claro se copy, links, claims e referências visuais estão aprovados.

## 3. Quando NÃO usar

- Para editar, normalizar, mover ou excluir arquivos.
- Para executar diagnósticos que escrevam cache ou dados do cliente.
- Para inventar conteúdo ausente ou escolher silenciosamente entre fontes conflitantes.

## 4. Pré-condições

1. Ler as instruções de governança aplicáveis.
2. Confirmar branch, worktree, cliente e escopo da landing page.
3. Definir diretórios permitidos para leitura e excluir secrets.
4. Confirmar que plugin, Figma original e outputs existentes são somente leitura.

## 5. Entradas

- `client.json`, base de conhecimento e outputs estratégicos aprovados.
- Output estratégico de landing page, se existir.
- Implementações HTML, CSS e JavaScript candidatas.
- Assets, Manual de Marca, diagnóstico visual, posicionamento, CRO e diagnóstico de criativos.
- Copy, links, claims, dependências e fontes externas explicitamente indicadas.

## 6. Fontes permitidas

- Fontes internas aprovadas do cliente e histórico Git.
- Implementações e referências existentes em modo somente leitura.
- Resultados já aprovados da matriz.
- Referências externas apenas como repertório visual, nunca como fonte factual.

## 7. Precedência das fontes

- Fatos: confirmação explícita mais recente → `client.json` → base estratégica aprovada → outputs estratégicos aprovados → implementação existente.
- Visual: confirmação explícita mais recente → Manual de Marca aprovado mais recente → diagnóstico visual aprovado → assets oficiais → referências externas → implementação existente.
- Copy: copy explicitamente aprovada → output estratégico de landing page aprovado → implementação existente.
- Links: link explicitamente confirmado → implementação existente aprovada.

Documento especializado aprovado posteriormente pode prevalecer em seu domínio com conflito registrado. Não resolver divergências silenciosamente.

## 8. Procedimento

1. Inventariar todos os candidatos de implementação e registrar caminho, função e estado Git.
2. Localizar o output estratégico de landing page e verificar se é identificável e aprovado.
3. Mapear HTML, CSS, JavaScript, frameworks, dependências e instruções de execução.
4. Inventariar assets, variantes, formatos, dimensões conhecidas, origem e referências no código.
5. Localizar Manual de Marca, diagnóstico visual, posicionamento, CRO e diagnóstico de criativos.
6. Extrair, sem alterar, a copy, os links e os claims presentes na estratégia e na implementação.
7. Comparar as fontes segundo a precedência contextual e registrar cada conflito.
8. Avaliar estrutura responsiva, breakpoints, conteúdo oculto e diferenças relevantes entre versões.
9. Identificar duplicatas por caminho, conteúdo e hash; não eleger vencedor sem evidência.
10. Classificar cada requisito como disponível, ausente, conflitante ou dependente de validação humana.
11. Indicar a implementação recomendada apenas quando a evidência for suficiente; caso contrário, bloquear.

## 9. Saídas esperadas

- Mapa de fontes com caminho, papel, aprovação e precedência.
- Implementação candidata recomendada e justificativa, ou estado `BLOCKED`.
- Lista de lacunas, duplicatas, conflitos e dependências.
- Avaliação de prontidão para criar a baseline.

## 10. Critérios de parada

Parar se a implementação exata não puder ser determinada, se fontes críticas estiverem ausentes, se houver conflito factual, de copy, links ou claims, ou se a inspeção exigir acesso a secret. Toda lacuna crítica produz `STOP`; não criar placeholders plausíveis.

## 11. Checkpoints humanos

- Confirmar a implementação candidata e a versão estratégica correta.
- Resolver conflitos de copy, links, claims e assets.
- Aprovar a passagem para `lp-baseline-prepare`.

## 12. Proteções

O `AGENTS.md` raiz prevalece. Esta auditoria é estritamente somente leitura: não modificar plugin, matriz, cliente, output, Figma ou referência. Não ler `.env` ou credenciais. Não autoriza copy, assets, commit, push, Preview ou Production; Production permanece proibida.

## 13. Integração com a matriz

Consultar conceitualmente `ee-s3-landing-page`, Manual de Marca, posicionamento, diagnóstico CRO, diagnóstico de criativos, `revisor-qualidade`, `validate_output.py`, `page_audit.py` e `page_audit_deep.py`. Consumir apenas resultados aprovados; não executar rotinas incompatíveis que escrevam cache, cliente, deploy ou produção.

## 14. Ferramentas reutilizáveis

- Disponíveis: `rg`, `rg --files`, `Get-FileHash`, Git e inspeção estática de HTML/CSS/JS.
- Disponíveis para consulta: scripts de auditoria da matriz; sua execução não é pressuposta.
- Planejadas: inventário normalizado e detector genérico de links/assets, ainda não implementados.
- Humanas: confirmação de aprovação, leitura estética e validação de claims.
- Proibidas: crawlers ou diagnósticos que façam escrita não autorizada.

## 15. Ações proibidas

- Corrigir arquivos durante a auditoria.
- Executar deploy, instalar dependências ou criar outputs auxiliares.
- Tratar referência externa como fato ou copiar identidade, código, estrutura completa ou assets externos.
- Fazer commit ou push.

## 16. Definição de sucesso

Existe uma decisão auditável sobre qual implementação e quais fontes são válidas, com prontidão, conflitos e lacunas explícitos, sem qualquer mutação do workspace ou das fontes.
