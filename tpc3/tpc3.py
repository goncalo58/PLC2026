import re
import sys


def tokenize(codigo: str):
    # Especificação das regras lexicais
    regras = [
        # Comentário: '#' até ao fim da linha (ignorado)
        ("COMMENT", r"#[^\n]*"),
        # String com tag de língua opcional ou apenas tag de língua
        ("STRING", r'"(?:[^"\\]|\\.)*"'),
        ("LANG", r"@[a-zA-Z]{2}"),
        # Variável: inicia com '?' seguido de alfanuméricos
        ("VAR", r"\?[a-zA-Z0-9_]+"),
        # Palavras Reservadas: select, where, LIMIT (case-insensitive ou conforme enunciado)
        ("LIMIT", r"\bLIMIT\b"),
        ("KEYWORD", r"\b(?:select|where)\b"),
        # Conceitos / Prefixos (ex: dbo:MusicalArtist, foaf:name, a)
        ("CONCEPT", r"[a-zA-Z_][a-zA-Z0-9_]*(?::[a-zA-Z_][a-zA-Z0-9_]*)?"),
        # Valores Numéricos
        ("NUMBER", r"\b\d+\b"),
        # Delimitadores individuais
        ("DELIM", r"[\{\}\.]"),
        # Espaços em branco e quebras de linha (ignorados)
        ("SKIP", r"[ \t\r\n]+"),
        # Erro léxico para qualquer outro caráter
        ("MISMATCH", r"."),
    ]

    regex_completa = "|".join(f"(?P<{nome}>{padrao})" for nome, padrao in regras)
    tokens = []

    for match in re.finditer(regex_completa, codigo):
        tipo = match.lastgroup
        valor = match.group()

        if tipo in ("COMMENT", "SKIP"):
            continue
        elif tipo == "MISMATCH":
            raise SyntaxError(f"Caráter inesperado encontrado: {valor!r}")
        else:
            tokens.append((tipo, valor))

    return tokens


def main():
    if not sys.stdin.isatty():
        conteudo = sys.stdin.read()
    else:
        conteudo = """# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000"""

    print("=== TOKENS ENCONTRADOS ===")
    tokens = tokenize(conteudo)
    for tipo, valor in tokens:
        print(f"{tipo:<12} -> {valor}")


if __name__ == "__main__":
    main()