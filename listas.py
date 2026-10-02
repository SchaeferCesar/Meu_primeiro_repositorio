# manipulação de listas frutas = ["kiwi", "banana", "laranja", "uva"]
frutas = ["kiwi", "banana", "laranja", "uva"]
print("Frutas em estoque:", frutas)
frutas.append("abacaxi")
print(frutas)
frutas.remove("banana")
print(frutas)
frutas.sort()
print(frutas)
for fruta in frutas:
    print(fruta)    
    add = input("Nova fruta:  ")
    frutas.append(add)
    if add == "fim":
        break
print("Frutas atualizadas:", frutas)