# diario.py com input, modo escrita "w"

contador = 0

with open("diario.txt", "w", encoding="utf-8") as arquivo:
    frase = input("Digite uma frase para adicionar ao diário: ")
    arquivo.write(frase + "\n")
    frase = input("Digite uma frase para adicionar ao diário: ")
    arquivo.write(frase + "\n")
    frase = input("Digite uma frase para adicionar ao diário: ")
    arquivo.write(frase + "\n")
    
#add frase modo "a"
with open("diario.txt", "a", encoding="utf-8") as arquivo:
    frase = input("Digite uma frase para adicionar ao diário: ")
    arquivo.write(frase + "\n")
    contador += 1 
            

#printar o arquivo
with open("diario.txt", "r", encoding="utf-8") as arquivo:
        for numero, linha in enumerate(arquivo, start = 1):
        print (f"{numero}: {linha.strip()}")
