cidades = ["sorocaba","campinas","salvador","votorantim","boituva"]
a = cidades.index("campinas")
print(a)
#posição / valor
cidades.insert(2,"maringa")#inserir
print(cidades)

estados = ["sp","rj","bh","mg"]#adiciona uma lista na outra
cidades.extend(estados)
print(cidades)

cidades.remove("sp")
print(cidades)

cidades.reverse()
print(cidades)#inverte a ordem

numbers = [0,4,12,1,22,421,543,214,531,425,76,5,6,7,86,56,43,563,74]
numbers.sort()#ordena a lista
print(numbers)