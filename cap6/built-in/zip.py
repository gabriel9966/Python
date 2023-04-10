#agrupa elementos de múltiplas estruturas de dados iteráveis
x = [1,2,3]
y = [4,5,6]
lista =list(zip(x,y))
print(lista)

zip_novo = list(zip("ABCD","XY"))
print(zip_novo)

d1 ={"a":1,"b":2}
d2 = {"c":3,"d":4}

zip_d1_d2 = list(zip(d1,d2))
print(zip_d1_d2)

zip_d1_d2_values = list(zip(d1.values(),d2.values()))
print(zip_d1_d2_values)