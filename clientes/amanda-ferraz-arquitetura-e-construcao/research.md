# Deep Research — Amanda Ferraz Arquitetura e Construção
**Data:** 2026-07-19
**Fontes:** site (https://arqamandaferraz.com/), Instagram (@arqamandaferraz), Google, GMB, Facebook, Econodata/CNPJ, Glassdoor

---

## 1. Site — Análise Completa

Metodologia: fetch da home + páginas internas (`/projetos-e-obras`, `/blogescritorio`) via WebFetch, complementado por download de HTML bruto e parsing do payload de hidratação Vue/JSON embutido na página (SPA — grande parte do conteúdo só existe dentro de um blob JSON, não em HTML semântico simples).

### Textos extraídos

**Hero (headline):**
> "Construímos mais do que projetos. Entregamos tranquilidade."

**Hero (subtexto):**
> "Arquitetura, interiores e construção especializada em alto padrão com gestão completa, clareza total e um único foco: sua paz durante todo o processo."

**Sobre (seção "Quem somos"):**
> "Amanda nasceu nos Estados Unidos, mas foi no interior de Minas Gerais que aprendeu, desde cedo, o valor das relações diretas e das conversas olho no olho. Foi essa raiz mineira — de escuta, paciência e firmeza — que trouxe na bagagem quando se mudou para Campinas, ainda jovem, para cursar Arquitetura e Urbanismo. Já no 2° ano de faculdade, conquistava seu primeiro estágio em um escritório renomado da região — e foi ali que entendeu que projetar não era só sobre estética, e mais do que isso, aprendeu o que NÃO se deve fazer. Arquitetura é sobre lidar com expectativa, pressão, orçamento, prazos e, acima de tudo, com pessoas. Esse contato com o bastidor real moldou o que viria a ser seu maior diferencial. Em 2015, fundou o escritório Amanda Ferraz Arquitetura e Construção. Empresa onde a transparência se tornou mais do que um princípio: virou critério de permanência. Com clientes. Com fornecedores. Com a própria equipe. Hoje, o escritório segue crescendo com uma equipe que compartilha da mesma visão: criar espaços que funcionem, emocionem e respeitem o processo de quem vai habitá-los. Não desenhamos para tendências. Desenhamos para histórias. E toda boa história começa com confiança."

Reforço adicional: "Com mais de 14 anos de experiência no mercado, criamos um método único" / "Pensado 100% na individualidade de cada cliente e cada projeto."

Fundação: **2015** (CNPJ ativo desde 2016 — Amanda Ferraz & Cia Arquitetura Ltda). Tempo de mercado declarado: **14+ anos**. Origem pessoal: nasceu nos EUA, criada em Minas Gerais, formada em Arquitetura e Urbanismo em Campinas, hoje sediada em Jundiaí-SP.

**Serviços (seção "O que fazemos?"):**
1. **Projeto Arquitetônico** — "Projetos exclusivos sob medida, pensados para a rotina e seu estilo de vida."
2. **Design de Interiores** — "Criamos do zero o ambiente para estética, funcionalidade e conforto em cada detalhe. Execução completa, prazos definidos e acompanhamento de ponta a ponta."
3. **Gerenciamento de Obras** — "acompanhamento completo da execução."

Não há outros serviços listados (sem consultoria isolada, sem projeto comercial/corporativo explícito — tudo enquadrado como residencial de alto padrão).

**Depoimentos:** existe seção "O que nossos clientes falam..." mas o conteúdo é composto por **imagens** (prints de WhatsApp/Google, não texto). Não foi possível extrair texto literal — recomenda-se transcrição manual.

**FAQ:** não encontrado — não existe seção de perguntas frequentes em nenhuma página.

**Rodapé:**
- Endereço (do site): Rua Capitão Cassiano Ricardo de Toledo, 191, Sala 1310, Chácara Urbana, Jundiaí-SP, CEP 13201-840 — porém há endereço divergente citado pelo Waze/Google Maps (Rua Reinaldo Orsi, 260, Jundiaí). **Confirmar com a cliente.**
- CNPJ: não exibido no site, mas localizado via Econodata — Amanda Ferraz & Cia Arquitetura Ltda, CNPJ 24.162.666/0001-04, ativo desde 2016, nome fantasia "Amanda Ferraz Arq e Design".
- Horário: 9h às 17h
- Telefone/WhatsApp: +55 11 94076-1458
- Email: contato@arqamandaferraz.com
- Facebook linkado no site aponta para facebook.com genérico (não para a página real da empresa — provável erro de configuração do template, nunca editado).
- Menu real: Home, "Quem somos" (âncora), "Projetos e obras" (`/projetos-e-obras`), "Blog" (`/blogescritorio`, vazio), Contato (âncora/formulário na home).

**Portfólio (`/projetos-e-obras`):**
> "Conheça nossos projetos e obras por dentro. Cada projeto do Amanda Ferraz Arquitetura e Construção nasce da união entre estética, técnica e propósito. Atuamos em residências de alto padrão, desenvolvendo soluções personalizadas que valorizam a arquitetura contemporânea, o conforto e a identidade de cada cliente — do conceito à execução completa da obra."

Apenas 3 obras listadas, identificadas só por código, sem descrição/localização/metragem: OBRA 187, OBRA 207, OBRA 220.

**Blog:** página existe (`/blogescritorio`) mas sem nenhum post publicado (`postDate = null` no código-fonte) — infraestrutura criada, conteúdo zero.

### Dados técnicos
- SSL: sim, HTTPS funcionando com HSTS ativo, certificado válido.
- Mobile-friendly: sim, viewport configurado, breakpoints mobile/desktop distintos.
- Tecnologia: **Hostinger Website Builder** (antigo Zyro) — site 100% no-code/site builder, front-end Vue.js, servido via CDN Hostinger (`assets.zyrosite.com`). Não é código customizado.
- PageSpeed estimado: rápido para padrão de site builder (~0.43s, ~266KB, cache HIT via CDN) — mas conteúdo real é limitado (3 serviços, 3 projetos sem detalhe, blog vazio, sem depoimentos em texto, sem preços, sem CNPJ/endereço confiável no rodapé).

### Gaps identificados no site
- Sem preços/faixas de investimento publicados (CTA sempre "solicite orçamento" via WhatsApp).
- Depoimentos só em imagem, não indexáveis, não reaproveitáveis como texto.
- Sem FAQ.
- Blog criado mas vazio — oportunidade de SEO local desperdiçada.
- Portfólio raso: 3 projetos só com código numérico, sem case studies.
- Facebook linkado incorretamente.
- Endereço com divergência entre fontes; CNPJ ausente no site (mas existe formalmente).
- Site é site builder (Hostinger/Zyro) — qualquer entregável futuro (nova LP, brandbook aplicado) provavelmente exige trabalho dentro das limitações do builder ou migração.

---

## 2. Instagram — @arqamandaferraz

**Limitação metodológica:** Instagram bloqueia scraping direto; WebFetch retornou apenas tela de login. Dados abaixo vêm de snippets indexados pelo Google (meta description) e menções de terceiros — não há certeza de atualidade total; recomenda-se confirmação visual pelo operador.

### Bio
Fragmento capturado: *"Seu tempo vale mais do que qualquer metro quadrado…"* — com menção a escritório em Jundiaí-SP e atendimento também online. Bio completa (CTA, links) não encontrada.

### Números
~13 mil seguidores, 961 seguindo, 1.002 publicações (consistente em duas buscas — confiança alta na ordem de grandeza, pode estar levemente desatualizado).

### Conteúdo
- Tipo predominante: não confirmado por observação direta. Indício indireto de reels de acompanhamento de obra (vídeo espelhado no Facebook com hashtag #contrateumarquiteto, tema "obra condomínio Jundiaí").
- Frequência estimada: não encontrado.
- Tom de voz observado: não observado diretamente; por proxy do site, tom "profissional, mas próximo, emocional, sem jargão técnico".
- Temas recorrentes (inferência do site + matéria de terceiros não plenamente acessível): alto padrão residencial, gerenciamento de obra "sem transtornos", tranquilidade do cliente, transparência como valor central.
- Engajamento: não encontrado.
- Destaques: não encontrado (perfil inacessível via scraping).

---

## 3. Google Meu Negócio

**Atualizado em 2026-07-19 com screenshot fornecido pelo operador** (ver `base-de-conhecimento/2026-07-19-anotacao-gmb-google-maps.md`):

- Status: **ativo e confirmado.**
- Avaliações: **4,5 ★ (19 avaliações no Google)**. Web agregada: 1/5 no Facebook com apenas 1 voto (baixo volume, não indica padrão negativo).
- Categoria: **Escritório de arquitetura** (Jundiaí, São Paulo). Localizado em "Golden Office".
- Endereço: **confirmado — R. Cap. Cassiano Ricardo de Toledo, 191, Sl 1310, Chácara Urbana, Jundiaí-SP, 13201-840.** A divergência anterior (Rua Reinaldo Orsi, 260) está descartada.
- Horário: Abre seg. às 09:00 (consistente com "9h às 17h").
- Telefone: (11) 94076-1458 (mesmo número do WhatsApp do site).
- Google Ads: **conta ativa** — campanha "[Google] Projetos", qualidade "Bom", 95,8% impression share, alerta de saldo baixo no momento da captura.
- Instagram: atualizado para **12,7 mil+ seguidores** (consistente com estimativa anterior de ~13 mil).

---

## 4. Reputação Online

- Reclame Aqui: não encontrado (busca direta e restrita a `site:reclameaqui.com.br` não retornaram página da empresa — só homônimos não relacionados). Indício de que não há página cadastrada ou volume relevante de reclamações.
- Avaliações Google (texto): não encontrado.
- Facebook: página existe em facebook.com/arquiteturaamandaferraz, categoria "Arquitetura e Design de Interiores" confirmada — conteúdo de avaliações bloqueado por login.
- Menção de imprensa: artigo do site "Moda e Beleza Vale" ("Além da Arquitetura: Transformando Projetos em Experiências Memoráveis com Amanda Ferraz") — link retornou 404 no fetch direto, conteúdo só via snippet indexado (baixa confiança). Cita um cliente dizendo nunca ter imaginado "que uma reforma pudesse ser tão prazerosa" e reforça transparência como "critério de permanência".
- Glassdoor: vaga de estágio em arquitetura publicada pela empresa em Jundiaí, sem avaliações de funcionários agregadas encontradas.
- TikTok: tag "Amanda Ferraz Arquiteta" existe mas sem conteúdo específico identificado.

---

## 5. Mercado e Concorrentes

### Tamanho do mercado
- Construção civil Brasil: USD 156 bi (2025) → projeção USD 218,2 bi (2034), CAGR ~3,8% (2026-2034) — fonte IMARC Group.
- 2026: CBIC projeta +2,0%; SindusCon-SP/FGV IBRE estimam +2,7% — ambos acima do PIB nacional projetado (1,6%).
- Tendências: industrialização e BIM ganhando força (previsibilidade de prazo); sustentabilidade virando critério básico, não diferencial; escassez de mão de obra (90% das empresas do setor relatam dificuldade) — reforça valor de gerenciamento de obra integrado.

### Segmento e localização confirmados
- Segmento: arquitetura residencial de alto padrão, integrando projeto + interiores + gerenciamento/execução de obra ("chave na mão").
- Cidade: **Jundiaí, SP** (confirmado via CNPJ, Glassdoor, Waze, diretórios — não Campinas, que é onde Amanda estudou).
- Público-alvo implícito: famílias de alto poder aquisitivo em Jundiaí e região metropolitana (Campinas, Vinhedo, Valinhos, Alphaville).

### Concorrentes identificados (confirmados pela cliente em reunião de kickoff)

#### Eduardo Muzi — concorrente mais direto
- Site: https://www.eduardomuzi.com.br/
- Instagram: https://www.instagram.com/eduardo.muzi/
- Segundo Amanda Ferraz (reunião de kickoff, 2026-06-08): "fica numa briga mesmo, ele pega obras minhas e eu pego obras dele". Projetos com forte apelo estético ("muito bonitos"), mas projeto executivo tecnicamente fraco — Amanda já teve que redesenhar/corrigir vigas que apareciam no projeto estrutural dele mas não no arquitetônico, gerando retrabalho em obra.
- Segundo a análise de Natália Terciotti (designer V4, reunião de 2026-06-30): o site dele é o melhor em direção de arte/branding entre os concorrentes diretos — parece um editorial de arquitetura, muito espaço em branco, fotografia protagonista — mas sem nenhuma prova social (depoimentos, clientes). O Instagram dele mistura vida pessoal com projetos, tem capas de vídeo pixeladas e vídeos em formato horizontal (não otimizados para mobile), o que reduz a percepção de valor apesar do site forte.

#### Ricardo Gaspari — referência consolidada em condomínio específico
- Site: https://ricardogaspari.com.br/
- Instagram: https://www.instagram.com/ricardogaspariarquiteto
- Segundo Amanda: nome consolidado no condomínio Atenas (Jundiaí), onde ela ainda não tem presença — mas ele faz pouca publicidade/Instagram. Atua do projeto à execução final (modelo similar ao dela). Não é o concorrente que mais "dói".
- Segundo Natália: site com modelo "institucional" datado (estilo 2015-2018), sem personalidade — "se tirar as fotos de fundo, não dá para saber o que ele faz". Comunica competência mas não constrói marca memorável — recomendação explícita da V4: não seguir esse caminho de posicionamento.

#### Guedes e Bisoli
- Boa visibilidade/qualidade de marketing dos projetos — Amanda já ouviu críticas técnicas de terceiros ("itens a desejar"), sem confirmação direta.
- Segundo Natália: transmite sensação "premium", usa bem provas sociais (depoimentos, parceiros, clientes) e tem boa organização — ponto forte que falta aos outros dois concorrentes diretos. Tipografia/direção de arte "no meio-termo": nem tão popular quanto o Ricardo Gaspari, nem tão refinado quanto o Eduardo Muzi.

#### Marília Zima — referência admirada (não concorrente direta)
- Combina qualidade técnica e estética; conteúdo de Instagram "profundo", não raso — citada por Amanda como quem ela mais admira no segmento.

---

### Concorrentes adicionais identificados na pesquisa automática (menor confiança — confirmar relevância)

#### 1. Vitor Dias Arquitetura (vdarquitetura.com)
- Proposta de valor: "Arquitetura que transforma espaços em experiências de viver."
- Diferencial percebido: tradução da personalidade do cliente no traço arquitetônico; presença multi-praça (Jundiaí, Alphaville, Campinas) e atuação nacional — escala maior que a Amanda Ferraz.
- Preço: não divulgado.

#### 2. Adriana Consulin Arquitetura (adrianaconsulin.com.br)
- Proposta de valor: "Transforma ambientes em experiências memoráveis."
- Diferencial percebido: forte prova social — 20+ anos, portfólio internacional (Espanha, EUA), premiada em CasaCor SP e Campinas Decor, aparições em TV (Bora Decorar/Band). Maior capital de mídia do grupo.
- Preço: não divulgado. Base em Campinas, atende Jundiaí/interior.

#### 3. L&L Arquitetura (lelarquitetura.com.br)
- Proposta de valor: "Transformando Espaços em Lares Únicos e Sofisticados."
- Diferencial percebido: "previsibilidade total" (orçamento fechado sem surpresas), execução fiel ao projeto 3D — discurso mais próximo ao da Amanda Ferraz (ambas apostam em transparência/previsibilidade). Território quase idêntico (Jundiaí + RMC). Ativa desde 2018 (menos tempo de mercado que os 14+ anos da Amanda Ferraz).
- Preço: não divulgado.

#### 4. E2C Arquitetura (e2carquitetura.com.br)
- Proposta de valor: "Arquitetura que Transforma Sonhos em Realidade."
- Diferencial percebido: equipe multidisciplinar e rede de parceiros; sede em Franco da Rocha, atua em Jundiaí como praça secundária — concorrente mais periférico.
- Preço: não divulgado.

#### 5. Daniel Santana Arquitetos (arquitetosdanielsantana.com)
- Proposta de valor: espaços que "desaceleram o ritmo", integração com natureza, rigor técnico.
- Diferencial percebido: interpretação autoral, atuação ampla (SP, Jundiaí, Campinas, capitais do Nordeste) — operação maior/mais pulverizada, menos "boutique local".
- Preço: não divulgado.

### Posicionamento comparativo
Todo o setor usa discurso muito parecido ("transformar sonhos/espaços em experiências", "alto padrão", "exclusividade") — pouco diferenciador isoladamente. O ponto de maior diferenciação real e verificável da Amanda Ferraz é operacional: "método único" em 14+ anos, gestão completa sem repassar decisões técnicas ao cliente, prazos definidos. Esse território é o mesmo ocupado pela **L&L Arquitetura** (concorrente mais próxima em discurso e geografia, porém com menos tempo de mercado). Frente à **Adriana Consulin**, a Amanda Ferraz está em desvantagem de prova social pública (sem prêmios/mídia equivalentes documentados). Frente a **Vitor Dias** e **Daniel Santana**, que operam multi-praça, a Amanda Ferraz aparenta mais boutique/local — pode ser lido como força (proximidade) ou limitação de escala, dependendo de como for comunicado.

**Gap identificado:** nenhum concorrente reivindica de forma explícita e sistemática "gestão completa da obra sem decisões técnicas repassadas ao cliente" — território de diferenciação a explorar com mais força, hoje concorrendo sem se diferenciar suficientemente da promessa de previsibilidade da L&L.

---

## 6. Dados inferidos (a confirmar com operador)

| Campo | Valor inferido | Confiança | Fonte |
|-------|---------------|-----------|-------|
| Segmento | Arquitetura residencial de alto padrão (projeto + interiores + gerenciamento de obra) | alta | site |
| Localização | Jundiaí, SP | alta | CNPJ/Econodata, Glassdoor, Waze |
| Tempo de mercado | 14+ anos (fundada em 2015) | alta | site |
| Produto principal | Projeto arquitetônico + design de interiores + gerenciamento de obras (pacote integrado) | alta | site |
| Ticket médio | não divulgado — nenhum concorrente publica preço (venda consultiva) | baixa | inferência de mercado |
| Endereço exato | Rua Capitão Cassiano Ricardo de Toledo, 191, Sala 1310, Jundiaí-SP (divergência com Rua Reinaldo Orsi, 260 no Waze) | média — precisa confirmação | site vs. Waze/Google Maps |
| CNPJ | 24.162.666/0001-04 (Amanda Ferraz & Cia Arquitetura Ltda) | alta | Econodata |
| Seguidores Instagram | ~13 mil | média | snippet indexado Google |

**Fontes consultadas:** arqamandaferraz.com (home, /projetos-e-obras, /blogescritorio), instagram.com/arqamandaferraz, facebook.com/arquiteturaamandaferraz, Econodata (CNPJ), Glassdoor (vaga), IMARC Group (mercado construção Brasil), ConstruConnect (panorama 2026), vdarquitetura.com, adrianaconsulin.com.br, lelarquitetura.com.br, e2carquitetura.com.br, arquitetosdanielsantana.com.
