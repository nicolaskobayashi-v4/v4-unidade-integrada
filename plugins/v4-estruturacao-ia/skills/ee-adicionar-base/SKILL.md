---
name: ee-adicionar-base
description: "Adiciona conteúdo à base de conhecimento de um cliente. O operador pode colar reuniões, docs, transcrições, emails — qualquer contexto sobre o cliente. Use quando o operador disser 'adicionar base', 'subir conteúdo', 'tenho uma reunião', 'colar informação do cliente'."
---

# Adicionar à Base de Conhecimento

O operador quer adicionar conteúdo à base de conhecimento de um cliente. Esse conteúdo será usado por TODAS as skills para evitar perguntas desnecessárias.

## Fluxo

### 1. Identificar o cliente

Se não está claro qual cliente:
- Leia `clientes/*/client.json (progress)` e pergunte qual
- Se só tem 1 cliente, use esse

### 2. Receber o conteúdo

Diga ao operador:
```
Cole aqui o conteúdo (reunião, doc, email, transcrição, anotação).
Pode ser em qualquer formato — eu organizo.
```

O operador vai colar texto bruto. Pode ser:
- Transcrição de reunião
- Email com briefing do cliente
- Documento de proposta comercial
- Anotações soltas
- Print/screenshot (multimodal)
- Link pra documento (fetch se possível)

### 3. Processar e salvar

Ao receber o conteúdo:

1. **Identifique o tipo:** reunião, documento, email, anotação, outro
2. **Extraia metadados:** data (se mencionada), participantes, assunto
3. **Salve como markdown** em `clientes/{slug}/base-de-conhecimento/`:

   Formato do nome: `{YYYY-MM-DD}-{tipo}-{assunto-slug}.md`
   
   Exemplo: `2026-04-06-reuniao-kickoff-cliente.md`

4. **Formato do arquivo:**
   ```markdown
   # {Tipo}: {Assunto}
   **Data:** {data ou "não informada"}
   **Fonte:** {reunião/email/doc/anotação}
   **Participantes:** {se mencionados}
   
   ---
   
   {conteúdo original do operador, preservado na íntegra}
   
   ---
   
   ## Dados extraídos automaticamente
   
   {lista de informações úteis que você identificou no texto}
   
   | Campo do briefing | Valor encontrado | Confiança |
   |-------------------|-----------------|-----------|
   | Segmento | {x} | alta/média/baixa |
   | Produto principal | {x} | alta/média/baixa |
   | ... | ... | ... |
   ```

5. **Mostre ao operador** o que extraiu:
   ```
   Salvo em: base-de-conhecimento/{filename}
   
   Encontrei essas informações relevantes:
   - Segmento: {x}
   - Produto: {y}
   - Concorrente mencionado: {z}
   - Objeção de venda: {w}
   
   Quer adicionar mais conteúdo ou seguir pro briefing?
   ```

### 4. Múltiplos conteúdos

O operador pode adicionar vários conteúdos em sequência. Para cada um:
- Salve separadamente
- Extraia dados
- Mostre o que encontrou

Quando o operador disser "pronto", "é isso", "pode seguir", retorne o controle.

## Regras

- NUNCA modifique o conteúdo original do operador. Preserve na íntegra.
- A seção "Dados extraídos automaticamente" é SUA análise — fica separada do conteúdo original.
- Se o conteúdo é grande (>5000 palavras), salve e diga: "Conteúdo salvo. É grande — vou processar em detalhe quando rodar o briefing."
- Se o operador colar algo que não faz sentido (código, spam), pergunte: "Isso é sobre o cliente? Pode me dar contexto?"
