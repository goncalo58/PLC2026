# Manifesto: TPC2 - Conversor de MarkDown para HTML

## Autor
- **Nome:** Gonçalo Miguel Abreu Pereira
- **Identificador:** A111016
- **Fotografia:**

<p align="center">
  <img src="https://github.com/user-attachments/assets/3b5dd59e-2b9f-412f-a572-7e6538925621" width="200" alt="Foto de perfil" />
</p>

## Resumo
Implementação em Python de um conversor de anotações MarkDown para linguagem HTML, contemplando os elementos nucleares da especificação "Basic Syntax".

O processamento das marcações apoia-se em expressões regulares com o módulo `re`:
- **Imagens e Hiperligações:** Substituição de `![alt](url)` por `<img .../>` antes de `[texto](url)`, garantindo que a sintaxe de imagem não é capturada previamente pelo padrão de link.
- **Tipografia:** Conversão de `**texto**` para `<b>texto</b>` executada prioritariamente em relação a `*texto*` para `<i>texto</i>`, prevenindo colisões no delimitador de asterisco.
- **Estruturas de Bloco:** Reconhecimento linha a linha de cabeçalhos (`#`, `##`, `###`) para as correspondentes tags `<h1>` a `<h3>`, bem como a identificação sequencial de listas numeradas (`^\d+\.\s+`), inserindo dinamicamente a abertura e encerramento de `<ol>` e as respetivas entradas `<li>`.

## Lista de resultados
- [Conversor Principal (tpc2.py)](tpc2.py)
- [Bateria de Testes Unitários (teste2.py)](teste2.py)
