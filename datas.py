from datetime import datetime

texto = "25/12/2026"
data = datetime.strptime(texto, "%d/%m/%Y")

now = datetime.now()  

data_nasc = input("Digite a data de nascimento (dd/mm/aaaa): ")
data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")  

#calcula a idade em anos e a diferença de dias entre a data atual e a data informada
print ((now - data_nasc).days // 365)
print ((data - now).days)


