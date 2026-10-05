# diario.py com input, modo escrita "w"

contador = 1

with open("diario.txt", "w", encoding="utf-8") as arquivo:
    frase = input("Digite uma frase para adicionar ao diário: ")
    arquivo.write(frase + "\n")

#add frase modo "a"
with open("diario.txt", "a", encoding="utf-8") as arquivo:
    frase = input("Digite uma frase para adicionar ao diário: ")
    arquivo.write(frase + "\n") 
    contador += 1                            

#add frase:
with open("diario.txt", "r", encoding="utf-8") as arquivo:
    frase = input("Digite uma frase para adicionar ao diário: ")
    for linha in arquivo:
        print(contador,linha.strip())
        contador += 1

    

    