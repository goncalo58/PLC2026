import re


er = r"^1*(01?)*$"

testes = [
    # Válidas 
    "1111111",
    "0000000", 
    "1101010",  
    "0100101",
    "1110001",  
    "101010",  
    # Inválidas 
    "0110000",  # 011 logo no início
    "1110110",  # 011 a meio
    "1000011",  # 011 no fim
    "011011",  # 6 dígitos com duas ocorrências de 011
    "110111",  # 6 dígitos com sequência '0111'
    "101101",  # 011 no meio
]

print("=== RESULTADOS ===")
for t in testes:
    valido = bool(re.fullmatch(er, t))
    resultado = "ACEITE" if valido else "REJEITADO (Contém '011')"
    print(f"{t:<10} -> {resultado}")