---
name: lp-asset-pipeline
description: Preparar e governar assets de landing pages com rastreabilidade de origem, direitos, original, derivados e uso responsivo. Usar quando assets aprovados precisarem ser selecionados ou preparados para produção; não usar para buscar stock automaticamente, instalar processadores ou substituir imagens sem aprovação.
---

# LP Asset Pipeline

## 1. Propósito

Definir o fluxo seguro de assets do original aprovado até o código, preservando origem e direitos e documentando todas as derivações usadas na landing page.

## 2. Quando usar

- Quando a seção autorizada usar imagens, logos, ícones, vídeos ou outros arquivos de mídia.
- Quando um asset exigir otimização, recorte, variantes responsivas ou fallback.
- Quando a implementação contiver base64 ou arquivos sem origem e direitos documentados.

## 3. Quando NÃO usar

- Para escolher fotografia de stock sem solicitação e aprovação humanas.
- Para alterar copy, layout, links ou identidade visual.
- Para instalar automaticamente bibliotecas, codecs ou processadores.
- Quando não houver autorização de uso ou origem verificável.

## 4. Pré-condições

1. Confirmar baseline, seção e arquivos autorizados.
2. Inventariar assets existentes sem modificar originals ou referência.
3. Confirmar origem, direito de uso e papel de cada asset.
4. Apresentar transformações e destinos propostos.
5. Obter aprovação explícita antes de criar derivados ou alterar referências no código.

## 5. Entradas

- Assets oficiais aprovados e seus metadados disponíveis.
- Baseline e cópia de trabalho.
- Manual de Marca e diagnóstico visual aprovados.
- Requisitos de exibição, recorte, densidade e viewports.
- Restrições técnicas da implementação.

## 6. Fontes permitidas

- Assets oficiais do cliente com uso autorizado.
- Derivados existentes cuja relação com o original seja comprovável.
- Ícones já aprovados e integrantes do sistema visual.
- Referências externas apenas para repertório, sem reutilização do arquivo.

## 7. Precedência das fontes

- Fatos: confirmação explícita mais recente → `client.json` → base estratégica aprovada → outputs estratégicos aprovados → implementação existente.
- Visual: confirmação explícita mais recente → Manual aprovado mais recente → diagnóstico visual aprovado → assets oficiais → referências externas → implementação existente.
- Copy: copy explicitamente aprovada → output estratégico de landing page aprovado → implementação existente.
- Links: confirmação explícita → implementação existente aprovada.

Em conflito de asset ou orientação visual, registrar e solicitar decisão. Documento especializado posterior prevalece apenas no seu domínio e com registro.

## 8. Procedimento

1. Inventariar arquivo, origem, proprietário/direito conhecido, função e ocorrências no código.
2. Identificar o original preservado e separar qualquer derivado existente.
3. Registrar para cada variante: dimensões, formato, peso, crop, densidade e fallback.
4. Classificar uso como decorativo, informativo, marca, ícone ou mídia funcional.
5. Propor a cadeia `original → derivado otimizado → asset de produção → referência no código`.
6. Preservar o original sem conversão, renomeação ou sobrescrita.
7. Preferir WebP quando compatível e manter fallback adequado ao projeto.
8. Para imagens responsivas, propor múltiplas larguras e uso coerente de `picture`, `srcset` e `sizes`.
9. Documentar recortes intencionais e comportamento por viewport.
10. Tratar base64 como tolerável em protótipo; para produção, registrar pendência até haver asset rastreável e aprovado.
11. Depois da autorização, criar somente derivados previstos e atualizar apenas código autorizado.
12. Verificar visualmente distorção, nitidez, crop e fallback.

## 9. Saídas esperadas

- Inventário de assets com origem e direito de uso conhecido.
- Mapa de original, derivados, dimensões, formato, peso, crop e fallback.
- Plano responsivo e referências de código propostas.
- Pendências explícitas para base64, direitos ausentes ou qualidade insuficiente.

## 10. Critérios de parada

Parar se origem ou direito de uso forem desconhecidos, se não houver original preservável, se a transformação comprometer identidade ou fidelidade, ou se a atualização exigir arquivo não autorizado. Ausência de foto não autoriza stock.

## 11. Checkpoints humanos

- Aprovar direito de uso e seleção dos assets.
- Aprovar transformações, crops, variantes e fallbacks.
- Aprovar mudança das referências no código.
- Revisar resultado visual antes do quality gate.

## 12. Proteções

O `AGENTS.md` raiz prevalece. Original, `reference/`, plugin e matriz são somente leitura. Não modificar asset, link ou copy sem aprovação. Não ler secrets. Commit/push e Preview exigem autorização separada; Production é proibida.

## 13. Integração com a matriz

Consumir Manual de Marca, diagnóstico visual, diagnóstico de criativos e output estratégico aprovados. Esta skill acrescenta rastreabilidade e preparação técnica de assets; não duplica diagnóstico, não altera os outputs da matriz e não herda mutações ou deploys.

## 14. Ferramentas reutilizáveis

- Disponíveis: metadados do filesystem, `Get-FileHash` e inspeção de referências com `rg`.
- Condicionais: recursos já instalados no projeto; descobrir e validar as ferramentas existentes antes de propor seu uso, sem instalar dependências automaticamente.
- Planejadas: processador de imagens, gerador de variantes e verificador de peso; nenhum está implementado nesta fase.
- Humanas: confirmação de direitos, crop, qualidade e adequação à marca.
- Proibidas: instalação automática de processador e busca automática de stock.

## 15. Ações proibidas

- Sobrescrever ou recomprimir o original.
- Baixar ou incorporar asset externo sem autorização e direitos confirmados.
- Alterar silenciosamente crop, formato, nome ou uso no código.
- Usar base64 como asset final de produção sem pendência documentada.
- Fazer commit, push ou deploy.

## 16. Definição de sucesso

Cada asset de produção é rastreável a um original autorizado, possui derivados documentados e comportamento responsivo validado, sem perda do original nem incorporação não autorizada.
