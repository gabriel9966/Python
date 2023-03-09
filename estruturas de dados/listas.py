notas = [8,9,3,6]
print(notas[0])
notas.append(6)
print(notas)
#ordena a lista
notas.sort()
print(notas)

notas.sort(reverse=True)
print(notas)
# pop remove o último elemento
x = notas.pop()
print(notas)
print(x)
#insere um elemento (posição,elemento)
notas.insert(0,55)
print(notas)

notas.pop(2)
print(notas)


nomes = ["gabriel","luiz","julio","carol"]
print(nomes)

