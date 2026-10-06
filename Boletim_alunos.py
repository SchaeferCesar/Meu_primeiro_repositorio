import csv

with open("notas.csv", newline="", encoding="utf-8") as f:
          for aluno in csv.DictReader(f):
              media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
              if media >= 7:
                  status = "Aprovado"
              else:
                  status = "Reprovado"
              print(f"{aluno['aluno']}: {media:.2f} - {status}")

   


          