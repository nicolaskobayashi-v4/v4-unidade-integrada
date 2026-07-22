# Decisões — piloto de landing pages

## Decisões aprovadas para a fundação

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
- O GreatPages deve usar uma página nova e não publicada.
- A execução fica limitada a uma seção e às variantes desktop e mobile.
- Não haverá publicação em produção durante o piloto.
- Qualquer risco de alteração de copy, substituição de assets ou perda visual interrompe o processo para revisão humana.
- Os outputs existentes `landing-page.html`, `landing-page/` e `deploy/` não podem ser modificados.
