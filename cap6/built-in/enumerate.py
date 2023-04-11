#A função enumerate retorna um objeto enumerado
seq = ["a","b","c","d"]

Enumerate = list(enumerate(seq))
print(Enumerate)

print("índice / valor")

for indice,valor in enumerate(seq):
    print(indice,valor)
    
print("-----------------------")

for indice,valor in enumerate(seq):
    if indice > 2:
        break
    else:
        print(indice,valor)
        
lista = ["administração","marketing","logística","vendas"]
print("-----------------------")
for num,valor in enumerate(lista):
    print(num,valor)
    
print("-----------------------")
for num,valor in enumerate("foda-se_cornos"):
    print(num,valor)