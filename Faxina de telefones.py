import csv as txt
import re

with open("telefones.txt", newline="", encoding="utf-8") as f:
    for contato in  csv.DictReader(f):
        numero = contato["telefone"]
        numeros = re.sub(r"\D", "", numero)
        if re.fullmatch(r"\d{11}", numeros):
            print(f"Telefone válido: {numeros}")
        else: print(f"Telefone inválido: {numeros}")