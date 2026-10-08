import re
import sys


def markdown_to_html(texto_md: str) -> str:
    # 1. Imagens: ![alt](url) -> <img src="url" alt="alt"/>
    # Processar ANTES dos links, pois a sintaxe de imagem contém a de link
    texto = re.sub(
        r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', texto_md
    )

    # 2. Links: [texto](url) -> <a href="url">texto</a>
    texto = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', texto)

    # 3. Bold: **texto** -> <b>texto</b>
    # Processar ANTES do itálico para não confundir ** com *
    texto = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", texto)

    # 4. Itálico: *texto* -> <i>texto</i>
    texto = re.sub(r"\*(.*?)\*", r"<i>\1</i>", texto)

    # 5. Cabeçalhos (#, ##, ###) e Listas Numeradas (1. , 2. )
    linhas = texto.splitlines()
    linhas_finais = []
    em_lista = False

    padrao_item_lista = re.compile(r"^\d+\.\s+(.*)$")
    padrao_header = re.compile(r"^(#{1,3})\s+(.*)$")

    for linha in linhas:
        # Verifica se a linha é um item de lista numerada
        match_lista = padrao_item_lista.match(linha)
        if match_lista:
            if not em_lista:
                linhas_finais.append("<ol>")
                em_lista = True
            conteudo_item = match_lista.group(1)
            linhas_finais.append(f"<li>{conteudo_item}</li>")
            continue

        # Se não for item de lista mas estávamos numa lista, fechar a tag <ol>
        if em_lista:
            linhas_finais.append("</ol>")
            em_lista = False

        # Verifica cabeçalhos (# texto, ## texto, ### texto)
        match_header = padrao_header.match(linha)
        if match_header:
            nivel = len(match_header.group(1))
            conteudo = match_header.group(2)
            linhas_finais.append(f"<h{nivel}>{conteudo}</h{nivel}>")
        else:
            linhas_finais.append(linha)

    # Caso o texto termine ainda dentro de uma lista numerada
    if em_lista:
        linhas_finais.append("</ol>")

    return "\n".join(linhas_finais)


def main():
    # Lê do standard input (ou lê texto de demonstração se nada for passado)
    if not sys.stdin.isatty():
        conteudo = sys.stdin.read()
    else:
        # Exemplo com todos os requisitos do enunciado
        conteudo = """# Exemplo

Este é um **exemplo** com *itálico* misturado.

Como pode ser consultado em [página da UC](http://www.uc.pt).

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...

1. Primeiro item
2. Segundo item
3. Terceiro item"""

    resultado = markdown_to_html(conteudo)
    print(resultado)


if __name__ == "__main__":
    main()