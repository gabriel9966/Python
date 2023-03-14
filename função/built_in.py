#funções built-in são funções que não precisam importar pacotes
s = "oi tudo bem com vc, td "
a = s.upper()
print(a)
b = a.split()#quebra por espaços
print(b)
c = s.split("t")# quebra quando acha "t"
print(c)

#Função String

d = s.capitalize()
print(d)#deixa a primeira letra maiscula

e = s.count("t")#conta quantas letras # tem
print(e)
f = s.isalnum()# é toda de numeros
print(f)
# endSwith = termina com a letra ()

g = "78172"
print(g.isalnum())
#built-in
numeros = [10,9,8,7,6,5,4,3,2,1,0,10]
print(len(numeros))
print(max(numeros))
print(min(numeros))
numeros.append(15)
print(numeros)
print(numeros.count(10))#conta a quantidade de elementos desse no array
