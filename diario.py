# diario.py com input, modo escrita "w"

with open("diario.txt", "w") as f:
    entrada = input("Digite algo para escrever no diário: ")
    f.write(entrada)

    