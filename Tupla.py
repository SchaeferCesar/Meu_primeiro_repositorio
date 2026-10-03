# Convert entre tupla e lista
dias_top10 = ("sexta", "sábado", "domingo")
print("Tupla inicial:", dias_top10)

dias_lindos = list(dias_top10)
print("Convertida em lista:", dias_lindos)

dias_lindos.append("feriado")
print("Lista após adicionar:", dias_lindos)

dias_favoritos = tuple(dias_lindos)
print("Tupla final:", dias_favoritos)
