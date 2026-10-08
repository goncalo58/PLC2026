from tpc2 import markdown_to_html


def testar():
    casos = [
        ("# Exemplo", "<h1>Exemplo</h1>"),
        ("## Subtítulo", "<h2>Subtítulo</h2>"),
        ("### Secção", "<h3>Secção</h3>"),
        ("Este é um **exemplo** ...", "Este é um <b>exemplo</b> ..."),
        ("Este é um *exemplo* ...", "Este é um <i>exemplo</i> ..."),
        (
            "Como pode ser consultado em [página da UC](http://www.uc.pt)",
            'Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>',
        ),
        (
            "Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...",
            'Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...',
        ),
        (
            "1. Primeiro item\n2. Segundo item\n3. Terceiro item",
            "<ol>\n<li>Primeiro item</li>\n<li>Segundo item</li>\n<li>Terceiro item</li>\n</ol>",
        ),
    ]

    todos_passaram = True
    for entrada, esperado in casos:
        obtido = markdown_to_html(entrada)
        if obtido != esperado:
            print(f"FALHOU para:\n{entrada}\nEsperado:\n{esperado}\nObtido:\n{obtido}\n")
            todos_passaram = False

    if todos_passaram:
        print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    testar()