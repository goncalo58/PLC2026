# Manifesto: TPC1 - Filtro de Sequências Binárias sem o Padrão "011"

## Autor
- **Nome:** Gonçalo Miguel Abreu Pereira
- **Identificador:** A111016
- **Fotografia:**

<img src="../foto.jpg" alt="Gonçalo Miguel Abreu Pereira" width="130"/>

## Resumo
Elaboração e verificação experimental de uma Expressão Regular destinada a filtrar linguagens binárias, rejeitando qualquer entrada onde ocorra a sequência contígua "011".

Para modelar este comportamento, utilizou-se a especificação `^1*(01?)*$`:
- `^1*`: Reconhece qualquer sucessão inicial composta exclusivamente pelo símbolo 1.
- `(01?)*$`: Controla o restante corpo da cadeia a partir do primeiro zero, impondo que cada símbolo 0 possa ser sucedido por no máximo um dígito 1 antes de terminar ou de iniciar outro bloco de zeros, inviabilizando a formação do par "11" após um "0".

## Lista de resultados
- [Script de Validação e Bateria de Testes (teste1.py)](teste1.py)
