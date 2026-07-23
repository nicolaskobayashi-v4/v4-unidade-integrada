# Direção de design

## Princípio central

A landing page deve parecer uma experiência editorial e comercial da Azul Viagens, com presença local e acabamento humano. A direção combina azul-marinho, azul-claro, branco, espaços generosos, hierarquia tipográfica forte e fotografia espontânea. A referência de Itabirito orienta ritmo e organização, não identidade local nem implementação.

## Aplicação da paleta

As três cores diretamente verificadas nos logos recebidos são:

- Azul-marinho `#041E42`.
- Azul-claro `#35A7D6`.
- Branco `#FFFFFF`.

Uso recomendado:

- **Azul-marinho:** texto principal, footer, seção de autoridade, CTA principal e ícones sobre fundos claros.
- **Azul-claro:** detalhes, linhas, badges discretos, estados de foco, destaques curtos e superfícies de apoio. Não usar texto branco pequeno sobre esse azul sem teste de contraste.
- **Branco:** superfícies principais, cards e conteúdo sobre fundos escuros.
- **Neutros azulados claros:** fundos alternados e separação de seções; os valores exatos deverão ser definidos e testados na implementação.

CTAs devem permanecer na família Azul. A opção mais segura é fundo azul-marinho com texto branco; uma variação secundária pode usar fundo claro com texto azul-marinho e borda Azul.

O ícone do WhatsApp pode aparecer em branco dentro do botão, sem transferir o verde do aplicativo para a interface. Não criar dois botões de mesma prioridade apontando para o mesmo destino. Na Hero:

- CTA principal **Planejar minha viagem** em azul-marinho → WhatsApp.
- CTA secundário **Conhecer destinos** em estilo de menor ênfase → `#destinos`.

Não usar:

- verde de WhatsApp como cor de botão, ícone, estado ou destaque;
- amarelo ou dourado;
- laranja, vermelho ou roxo como cores dominantes, em linha com o manual;
- gradientes multicoloridos ou cores decorativas fora da paleta.

## Usos das versões de logo

### Versão positiva

`logo-azul-poa-2.png`, em azul-marinho, sobre branco ou neutro muito claro. É a aplicação preferencial no header.

### Versão negativa

`logo-azul-poa.png`, em branco, sobre azul-marinho ou fotografia com overlay escuro uniforme. É a aplicação preferencial no footer e pode ser usada na seção de autoridade.

### Ativo adicional

`logo-azul-poa-3.png`, em azul-claro, foi recebido, mas deve ficar reservado até confirmação de contexto de uso. Não misturar as versões na mesma área nem recolorir, distorcer, recortar ou reconstruir a assinatura.

Em todas as aplicações:

- preservar proporção e área de respiro;
- não aplicar sobre fundo ruidoso ou de baixo contraste;
- não animar partes isoladas;
- usar o texto alternativo com o nome oficial da unidade, depois de validado.

## Tipografia

Helvetica Neue é a tipografia oficial confirmada do projeto e deve ser usada em toda a landing page. Não introduzir outras famílias tipográficas.

Enquanto os arquivos licenciados para web não forem fornecidos, usar exclusivamente:

```css
font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
```

O mecanismo definitivo de carregamento web permanece pendente. Não baixar, incorporar nem distribuir arquivos de fonte nesta execução.

A implementação deve:

- usar Bold em títulos e Regular em textos;
- evitar excesso de pesos;
- manter corpo confortável, entrelinha aberta e largura de leitura controlada;
- preferir caixa normal em textos e caixa alta apenas em kickers curtos;
- não usar fonte display genérica, manuscrita, “futurista” ou qualquer família adicional.

## Contraste e acessibilidade visual

- Almejar WCAG 2.2 AA: contraste mínimo de 4,5:1 para texto normal e 3:1 para texto grande e componentes gráficos essenciais.
- Não depender apenas de cor para indicar estado, clique ou foco.
- Manter foco visível em todos os elementos interativos.
- Aplicar overlay apenas quando necessário para proteger a legibilidade sobre fotografia.
- Evitar texto longo sobre imagem.
- Não usar transparência ou glassmorphism se o resultado reduzir contraste.
- Validar logos, badges, cards e CTAs nos fundos reais, em desktop e mobile.

## Fotografia

A fotografia final deve ser:

- natural, espontânea e humanizada;
- relacionada aos serviços e destinos oferecidos;
- predominantemente azul ou compatível com a paleta;
- livre de poses artificiais, saturação excessiva e aparência de banco genérico;
- licenciada e, quando houver clientes, colaboradores ou crianças, acompanhada das autorizações necessárias.

Necessidades previstas:

1. Hero: cena humana de viagem, com área de respiro para a composição; eventual uso de aeronave depende de ativo autorizado.
2. Destinos: Disney/Orlando, Nordeste/Caribe e cruzeiros, com seleção aprovada e coerência de tratamento.
3. Atendimento: fachada ou interior real da loja no Shopping Bourbon Country.

Não reutilizar fotografias de Itabirito e não buscar imagens aleatórias na internet.

## Iconografia

- Usar uma única família de ícones lineares.
- Manter espessura visual equivalente a 2 pt, conforme o manual.
- Aplicar sobre fundos neutros e com contraste claro.
- Evitar emojis como solução final, misturas de estilos, ícones preenchidos sem necessidade e excesso de símbolos.
- Não colocar ícones sobre áreas visualmente ruidosas das fotos.
- Usar ícones apenas quando ajudarem a reconhecer informação: localização, documentação, pacote, atendimento e navegação.

## Composição

- Container central consistente e grid responsivo.
- Alternância controlada entre superfícies claras e uma seção de autoridade azul-marinho.
- Hero em duas colunas no desktop: copy e ações à esquerda; placeholder fotográfico com painel de pacote à direita.
- Diferenciais em quatro cards numerados, com números em segundo plano de baixa ênfase.
- Destinos em três cards de imagem com proporção uniforme, título protegido por overlay e tags discretas.
- Autoridade em composição assimétrica: narrativa/credencial de um lado; métricas e prova social do outro.
- Atendimento em duas colunas: checklist e imagem real da loja com card de localização.
- CTA final centralizado, curto e com um único foco principal.
- Footer em três colunas no desktop, sem botão flutuante de WhatsApp nesta fase.

Usar espaço em branco, alinhamentos precisos e variação de escala para criar ritmo. Evitar excesso de sombras, bordas e caixas em todas as seções.

## Responsividade

- Projetar mobile-first e validar pontos de quebra pelo conteúdo, não por aparelhos específicos.
- Header deve reduzir para navegação compacta sem ocultar o caminho principal de conversão.
- Hero passa para uma coluna; copy e CTA vêm antes da imagem.
- CTAs ficam com largura confortável no mobile, sem dois botões apertados lado a lado.
- Cards passam de quatro/três colunas para uma coluna ou trilho acessível; não depender de hover.
- Métricas devem quebrar sem perder rótulo e unidade.
- Endereço e demais textos longos devem quebrar naturalmente, sem abreviações ambíguas.
- Alvos de toque devem ter pelo menos 44 × 44 px.
- Não ocultar informação essencial em mobile.
- Respeitar preferência por redução de movimento em qualquer animação futura.

## Regras contra visual genérico de IA

- Não usar ilustrações abstratas de “tecnologia”, globos 3D, brilhos gratuitos ou mosaicos sem função.
- Não usar gradientes roxo/azul, glow neon, glassmorphism generalizado ou cards idênticos em toda a página.
- Não preencher espaço com textos decorativos, selos inventados ou métricas sem evidência.
- Não usar imagens com pessoas excessivamente posadas, anatomia estranha ou cenários artificiais.
- Não misturar famílias de ícones nem usar emojis como iconografia final.
- Não criar aeronaves, parques, logos ou fachadas por IA.
- Não repetir o mesmo padrão “badge + título + três cards” sem variação de ritmo e propósito.
- Basear detalhes visuais na marca, no conteúdo e na loja real, não em tendências genéricas.

## Elementos aproveitados da referência

Somente como princípios visuais e estruturais:

- header compacto e navegação por âncoras;
- hero em duas colunas com painel informativo associado à imagem;
- títulos com contraste entre azul-marinho e azul-claro;
- cards numerados para diferenciais;
- cards de destino com overlay inferior para legibilidade;
- seção escura de autoridade com métricas;
- seção de atendimento com checklist e imagem da loja;
- CTA final concentrado;
- footer em colunas;
- alternância de fundos e uso generoso de espaço.

Nenhum código, script, tracking, metadata, dado local, imagem, link ou integração da referência será reaproveitado.

## Elementos corrigidos da referência

- Remover verde de WhatsApp e converter todos os CTAs para a paleta Azul.
- Remover amarelo/dourado dos badges e detalhes.
- Não usar botão flutuante de WhatsApp nesta primeira versão; o canal está validado, mas esse componente não faz parte do escopo atual.
- Reduzir o número de CTAs concorrentes no hero e no fechamento.
- Evitar números animados que apareçam como “0” sem JavaScript ou prejudiquem leitura.
- Não depender de hover para revelar informações de destinos.
- Reduzir glassmorphism e transparências onde afetarem contraste.
- Não copiar dados estruturados, canonical, metatags, trackers ou URLs da loja de Itabirito.
- Substituir conteúdo local e fotos da referência por dados validados e ativos próprios.
- Manter tags de destinos discretas e somente quando seus claims forem confirmados.

## Estratégia dos placeholders

Os placeholders serão criados apenas na futura implementação, como componentes locais sem dependência externa.

Cada placeholder deve:

- indicar claramente sua finalidade no ambiente de desenvolvimento, por exemplo `Hero — foto de viagem aprovada`, `Destino — Disney/Orlando` e `Loja — fachada Bourbon Country`;
- reservar a proporção e o enquadramento esperados para evitar mudança brusca de layout;
- usar fundo neutro azulado, borda discreta e ícone linear simples;
- conter texto curto, que não se confunda com conteúdo final;
- oferecer `aspect-ratio` coerente com o uso futuro;
- prever posição segura para pessoas, títulos e overlays;
- ser facilmente substituível por arquivo local aprovado;
- nunca apontar para uma imagem remota.

Proporções iniciais para planejamento:

- Hero: aproximadamente 4:3 no desktop e 16:10 no mobile.
- Destinos: aproximadamente 4:5.
- Loja/atendimento: aproximadamente 4:3.

As proporções finais devem ser ajustadas ao material fotográfico aprovado, sem recortes que prejudiquem pessoas, marcas ou arquitetura.
