# r = só lê
arq1 = open("cap6/arquivo1.txt", "r")
print(arq1.read())
Numero_de_caracteres = arq1.tell()
print(Numero_de_caracteres)

#retorna o cursor para o ínicio
arq1.seek(0,0)

print(arq1.read(2))#imprime os dois primeiros caracteres

# escrever ou sobrescrever arquivo
# não podemos ler o arquivo se abrimos para escrever
arq2 = open("cap6/arquivo2.txt", "w")# w = write, perde o conteudo que já tem
arq2.write("OI FODA_SE 22")
arq2.close()#fechando arquivo

arq2 = open("cap6/arquivo2.txt", "r")
print(arq2.read())
arq2.close

arq2 = open("cap6/arquivo2.txt", "a")#append adiciona
arq2.write("jadasndnan kkkkk")
arq2.close

arq2 = open("cap6/arquivo2.txt", "r")
print(arq2.read())