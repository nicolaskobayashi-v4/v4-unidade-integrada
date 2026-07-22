# Decisões — piloto de landing pages

## Registro histórico — decisões iniciais da fundação

As decisões abaixo preservam o histórico da fundação. As linhas relativas ao destino GreatPages e ao fluxo Figma → GreatPages foram substituídas pela decisão revisada registrada ao final deste documento.

| Tema | Decisão | Consequência inicial |
|---|---|---|
| Agente principal | O Codex no VS Code será a IA operacional principal. | A governança e a futura skill serão orientadas ao fluxo do Codex neste workspace. |
| Integração com Figma | Será utilizado o MCP oficial do Figma. | Não serão adotados conectores paralelos nesta fase. A configuração ocorrerá somente em etapa posterior. |
| Destino | O GreatPages será o destino de implementação. | O piloto avaliará sua capacidade real de reproduzir a Hero. |
| Direção do fluxo | Não haverá sincronização bidirecional. | Mudanças no GreatPages não retornarão automaticamente ao Figma. |
| Fluxo inicial | O fluxo será somente Figma → GreatPages, com auditoria e preparação pelo Codex. | A origem visual permanece protegida e o destino é tratado como derivado. |
| Plugin da matriz | `plugins/v4-estruturacao-ia/` permanecerá intacto durante o piloto. | A fundação da unidade não cria conflitos com atualizações da matriz. |
| Skill | Uma única skill será criada somente depois da aprovação desta fundação. | Nenhuma skill faz parte da primeira camada de governança. |
| Design system | O design system completo será adiado até existirem resultados reais do piloto. | Tokens, componentes e templates definitivos não serão antecipados sem evidência. |
| Referência do cliente | A Hero do Instituto Salotti será usada apenas como referência em uma cópia de teste. | O original e os outputs atuais do cliente não serão alterados. |
| Auditoria do Figma | A auditoria inicial será somente leitura; qualquer escrita exigirá plano e aprovação explícita, limitada ao frame e às operações descritas. | Aprovações não serão interpretadas como autorização geral para editar o arquivo. |
| Fontes de verdade | Conteúdo vem de `client.json`, `base-de-conhecimento/` e outputs aprovados; a referência visual é o frame preservado; a estrutura preparada é o frame de exportação; a implementação é a página de teste no GreatPages; o histórico é o Git. | Cada etapa possui uma referência canônica e verificável. |
| Registros do piloto | Novos relatórios e registros ficarão exclusivamente em `clientes/instituto-salotti/outputs/landing-pages/piloto-figma-greatpages/`. | `landing-page.html`, `landing-page/`, `deploy/` e demais outputs existentes permanecem imutáveis. |
| Controle de versão | Commit e push exigem aprovação explícita do usuário. | Autorizações para Figma ou GreatPages não autorizam operações Git. |

## Restrições decorrentes

- O arquivo Figma original é somente leitura.
- GreatPages não será implementado no piloto atual; permanece apenas como hipótese futura opcional.
- A execução fica limitada a uma seção e às variantes desktop e mobile.
- Não haverá publicação em produção durante o piloto.
- Qualquer risco de alteração de copy, substituição de assets ou perda visual interrompe o processo para revisão humana.
- Os outputs existentes `landing-page.html`, `landing-page/` e `deploy/` não podem ser modificados.

## Decisão revisada — HTML e Vercel

Data da revisão: 2026-07-22.

A decisão anterior de usar o fluxo Figma → GreatPages foi substituída após a identificação do fluxo HTML já existente no repositório e do acesso à Vercel.

O novo fluxo principal aprovado é:

```text
Figma aprovado
    ↓
Codex no VS Code
    ↓
HTML, CSS e JavaScript versionados
    ↓
Testes locais
    ↓
Git
    ↓
Vercel Preview
    ↓
Revisão humana
    ↓
Produção somente após aprovação explícita
```

Decisões decorrentes:

- HTML, CSS e JavaScript versionados no Git passam a ser a implementação operacional.
- A Vercel Preview passa a ser o ambiente de homologação.
- A Vercel não substitui o Figma como referência visual nem o Git como fonte da implementação.
- Produção exige autorização explícita e permanece proibida durante o piloto.
- GreatPages permanece como hipótese futura opcional de adaptador ou destino alternativo, ainda não implementada e fora do escopo atual.
- Nenhuma implementação da skill associada à decisão anterior chegou a ser criada.
- A governança, a auditoria somente leitura, a aprovação granular e as proteções dos materiais existentes continuam válidas.
- O diretório exclusivo passa a ser `clientes/instituto-salotti/outputs/landing-pages/piloto-figma-vercel/`, sem criação nesta etapa documental.
