from functools import reduce

#serve para reduzir uma sequencia a um único valor

#reduce(função , sequência)

lista = [1,2,3,4,5,6,7,8,9]

red = reduce(lambda x,y :x if (x > y) else y , lista)
print(lista)
print(red)#valor maior da lista