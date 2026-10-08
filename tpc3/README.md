# Manifesto: TPC3 - Analisador Léxico para Query Language

## Autor
- **Nome:** Gonçalo Miguel Abreu Pereira
- **Identificador:** A111016
- **Fotografia:**

<p align="center">
  <img src="https://github.com/user-attachments/assets/3b5dd59e-2b9f-412f-a572-7e6538925621" width="200" alt="Foto de perfil" />
</p>

## Resumo
Construção de um analisador léxico (lexer) em Python para uma linguagem de consulta do tipo SPARQL.

O lexer faz uso de expressões regulares com grupos nomeados e da função `re.finditer` para segmentar a cadeia de entrada nos seguintes componentes:
- **Comentários (`#`):** Descartados desde o cardinal até ao fim da linha.
- **Variáveis (`?`):** Capturam identificadores iniciados por `?` seguidos de caracteres alfanuméricos.
- **Identificadores de Língua (`@`):** Reconhecem tags de idioma no formato `@` seguido de dois caracteres alfabéticos.
- **Literais de Texto e Números:** Strings delimitadas por aspas e constantes numéricas inteiras.
- **Conceitos e Prefixo:** Reconhecimento de nomes simples ou qualificados por namespace (ex.: `dbo:MusicalArtist`, `foaf:name`).
- **Palavras Reservadas e Delimitadores:** Tratamento específico de `LIMIT`, `select`, `where` e símbolos pontuais `{`, `}`, `.`.

## Lista de resultados
- [Analisador Léxico (tpc3.py)](tpc3.py)
- [Bateria de Testes (teste3.py)](teste3.py)
