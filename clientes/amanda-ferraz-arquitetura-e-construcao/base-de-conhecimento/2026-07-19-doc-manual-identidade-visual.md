# Manual de Identidade Visual — Amanda Ferraz Arquitetura e Construção
**Tipo:** Documento estratégico (Projeto de Marca, já produzido — "V4 SCN&CO")
**Data de upload:** 2026-07-19
**Fonte:** PDF enviado pelo operador (`Amanda_Ferraz_-_Manual_.pdf`)

> Nota de proveniência: documento assinado "V4 SCN&CO" — indica que já houve um projeto de identidade visual formal produzido para esta cliente antes da entrada dela no sistema atual. Este material deve ser tratado como insumo validado para `ee-s3-identidade-visual` (não recriar do zero) e para qualquer peça de direção de arte.

## Paleta de cores

| Cor | Hex | Uso |
|---|---|---|
| Cor primária (preto) | `#030208` | Base/fundo |
| Off-white | `#D4D1D4` | Texto/fundo claro |
| Taupe | `#8B8077` | Secundária |
| Marrom escuro | `#453B35` | Secundária |
| Vermelho (destaque) | `#91211E` | **Utilizar apenas para destaque** — nunca como cor dominante |

## Tipografia

- **H1 (títulos principais):** Season Light, Season Light Italic. Para destacar texto dentro da fonte Season, usar **itálico** (não bold) — alternativa é mudar a cor para vermelho, só se o contraste fizer sentido.
- **H2 e H3 (subtítulos e texto corrido):** Josefin — pesos Extralight, Light, Regular e Medium. **Evitar Semibold, Bold e Black** na Josefin. No texto corrido, destaque = Josefin Extralight com o trecho destacado em Medium.

## Especificações de formato (redes sociais)

- **Posts para ads:** 1080×1350px. Margem superior/inferior de 126px. H1 (títulos): 50-120pt (até 170pt para palavra de destaque). H2 (subtítulos): 42-50pt. H3 (texto corrido): 35-42pt. Logo: largura mínima 316px, altura 59px.
- **Posts para stories:** 1080×1920px. Margem superior 358px, margem lateral 122px, margem inferior 458px. H1: 50-120pt. H2: 42-50pt. H3: 35-42pt. CTAs: altura 80-100px, largura 400-600px.

## Diretrizes de direção de arte

**A identidade visual deve comunicar, em todos os pontos de contato, altíssimo padrão — não através do excesso, mas por simplicidade, precisão e qualidade dos detalhes.** Cada peça deve reforçar que o escritório desenvolve projetos únicos, sofisticados e atemporais.

### A marca DEVE transmitir:
1. **Exclusividade** — comunicação para público seleto; evitar elementos genéricos ou populares; projeto percebido como único e personalizado.
2. **Sofisticação** — na qualidade da composição, escolha de materiais visuais, tipografia, fotografia e equilíbrio entre elementos. O luxo não depende de quantidade de recursos gráficos, mas de como são usados.
3. **Silêncio visual** — toda composição deve respirar; espaço em branco é elemento de design tão importante quanto texto/imagem; evitar excesso de informação ou layouts carregados.
4. **Arquitetura como protagonista** — as fotografias da arquitetura ocupam o papel principal; elementos gráficos existem para valorizar os projetos, nunca para competir com eles.
5. **Elegância discreta** — comunicação contida e refinada; desperta interesse pela qualidade estética, não pelo impacto visual. A percepção de luxo nasce da discrição.
6. **Atemporalidade** — peças devem permanecer relevantes ao longo do tempo; evitar tendências passageiras de design, redes sociais ou linguagem.

### A marca NÃO deve transmitir:
1. **Conteúdo popular** — evitar emojis, efeitos chamativos, textos exagerados, linguagem informal em excesso.
2. **Excesso de informação** — simplificar sempre; menos informação = mais clareza e sofisticação percebida.
3. **Sensação promocional** — nada de campanhas de varejo/marketing agressivo, urgência exagerada, ofertas, excesso de CTAs.
4. **Estética de TikTok genérico** — vídeos curtos/tendências só quando fizerem sentido, sem linguagem acelerada/editada típica de entretenimento; preservar ritmo, contemplação, qualidade cinematográfica.
5. **Marketing chamativo** — evitar títulos sensacionalistas, cores excessivamente vibrantes, elementos gráficos em excesso, composições competindo por atenção.

### Checklist de validação (toda peça deve responder "sim" a todas):
- A arquitetura é protagonista?
- Existe espaço para respirar?
- O vermelho está sendo usado apenas como detalhe?
- A fotografia parece editorial?
- O texto é realmente necessário?
- A composição transmite calma?
- O luxo está sendo sugerido, e não gritado?
- A peça poderia estar em uma revista como Casa Vogue?

*Se a resposta for "não" para qualquer uma, a peça precisa ser revisada.*

## Exemplos de entregáveis já produzidos/mockados neste manual
- **Landing Page:** mockup mostrando "Projeto arquitetônico residencial, comercial, design de interiores e gerenciamento de obras" — **nota: este mockup expande o escopo para incluir "comercial"**, enquanto o site atual (arqamandaferraz.com) só menciona "residências de alto padrão". Confirmar com o operador/cliente se comercial é realmente um serviço oferecido ou se é só um placeholder do mockup.
- **Vídeo, Carrossel:** exemplos de aplicação da paleta/tipografia em peças de mídia social, com fotografia de interiores como protagonista, uso do vermelho só em detalhes/CTA, tipografia serifada fina.

## Implicação para o briefing
- `brand.current_colors` = paleta acima (5 cores, já formalizada)
- `brand.has_logo` = true (logo já existe, com specs de tamanho mínimo documentadas)
- `brand.voice_tone` = alinhado com o Manual de Copywriting: "quiet luxury", contido, editorial, sem emojis
- `brand.restrictions` = ver lista "NÃO deve transmitir" acima — já formalizada, não precisa perguntar de novo ao operador
- Já existe brand book emocional (Manual de Copywriting) + brand book visual (este documento) — ambos devem ser tratados como insumo pronto para `ee-s3-brandbook` e `ee-s3-identidade-visual`, e não recriados do zero quando essas skills rodarem.
