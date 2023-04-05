import csv# = canpos separados por vírgula
#with = fecha o arquivo automaticamente
#W = modo de gravação                   arquivo = nome da váriavel
with open("cap6/numeros.csv", "w") as arquivo:
    #cria objeto de gravação
    writer = csv.writer(arquivo)
#gravar linha
    writer.writerow(("nota1","nota2","nota3"))
    writer.writerow((10,22,44,33))
    writer.writerow((13,15,22,12))

#leitura arquivo csv
#encoding = formato de caracteres
#\r volta o cursor para o ínicio da linha
with open("cap6/numeros.csv", "r", encoding="utf8", newline="\r\n") as arquivo:
    #acessa cada linha do arquivo
    #cria objeto de leitura
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)

#gerando uma lista com os dados do arquivo csv
with open("cap6/numeros.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
    print("print dados :",dados)
