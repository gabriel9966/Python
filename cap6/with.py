# com with o método close é chamado automaticamente
import os
with open("cap6/arquivo2.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(len(conteudo))
print(conteudo)