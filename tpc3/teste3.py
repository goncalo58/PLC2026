from tpc3 import tokenize


def testar():
    query = """# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000"""

    tokens = tokenize(query)

    esperado = [
        ("KEYWORD", "select"),
        ("VAR", "?nome"),
        ("VAR", "?desc"),
        ("KEYWORD", "where"),
        ("DELIM", "{"),
        ("VAR", "?s"),
        ("CONCEPT", "a"),
        ("CONCEPT", "dbo:MusicalArtist"),
        ("DELIM", "."),
        ("VAR", "?s"),
        ("CONCEPT", "foaf:name"),
        ("STRING", '"Chuck Berry"'),
        ("LANG", "@en"),
        ("VAR", "?w"),
        ("CONCEPT", "dbo:artist"),
        ("VAR", "?s"),
        ("DELIM", "."),
        ("VAR", "?w"),
        ("CONCEPT", "foaf:name"),
        ("VAR", "?nome"),
        ("DELIM", "."),
        ("VAR", "?w"),
        ("CONCEPT", "dbo:abstract"),
        ("VAR", "?desc"),
        ("DELIM", "}"),
        ("LIMIT", "LIMIT"),
        ("NUMBER", "1000"),
    ]

    assert tokens == esperado, "Os tokens obtidos diferem dos esperados!"
    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    testar()