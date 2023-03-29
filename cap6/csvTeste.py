import csv

with open("cap6/numeros.csv", "w") as arquivo:
    #cria objeto de gravação
    writer = csv.writer(arquivo)
#gravar linha
    writer.writerow(("nota1","nota2","nota3"))
    writer.writerow((10,22,44,33))
    writer.writerow((13,15,22,12))

#leitura arquivo csv
with open("cap6/numeros.csv", "r", encoding="utf8", newline="\r\n") as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)
    