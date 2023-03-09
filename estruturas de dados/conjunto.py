#conjuntos usa chaves ou set, não pode ter elementos repetidos, não possuem ordem
usuarios = {"alice","bob"}
usuarios2 = set(["alice","bob"])
usuarios3 = {"alice","bob","alice"}
resultado = usuarios == usuarios2
print(resultado)

usuarios.add("ronaldo")

print(usuarios)
print("---//---")
print(usuarios2)
print("---//---")
usuarios_unicos = set(usuarios3)
print(usuarios_unicos)

conjunto1 = {"alice","bob"}
conjunto2 = set(["alice","bob","carlos"])

print("---//---")

print(conjunto1.union(conjunto2))