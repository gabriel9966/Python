import os#manipulação de arquivo txt
texto = "Cientista de dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionaris precisam saber como programar python.\n"
texto += "E,claro ,devem ser proficientes em Data Science."

print(texto)


#crindo arquivo com pacote os
arquivo = open(os.path.join("/cap6/arquivo3s.txt", "w"))
# vai separar por espaço pq está vazio ()
for palavra in texto.split():
    arquivo.write(palavra + " ")

arquivo.close()

arquivo = open("/cap6/arquivo3.txt", "r")
conteudo = arquivo.read()

arquivo.close()
print(conteudo)