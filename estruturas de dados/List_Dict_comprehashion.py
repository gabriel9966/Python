#list comprehashion que imprimi até 10
#retorne x para cada valor de x na lista de elementos
lista_numeros = [x for x in range(10)]
print(lista_numeros)

lista_numeros2 = [x for x in range(10) if x < 5]
print(lista_numeros2)

lista_frutas = ['melancia','morango','uva','abacaxi','melao','pessego','manga']
nova_lista = []
#retorne x para cada x da lista se tiver m
nova_lista = [x for x in lista_frutas if 'm' in x]
print(lista_frutas)
print(nova_lista)

dict_aluno = {"Bob":68,"Clara":84,"Michel":57,"Roberto":93,"Luiz":77}
dict_status_aluno = {a:b for (a,b) in dict_aluno.items() }
print(dict_status_aluno)

dict_aluno2 = {"Bob":38,"Clara":27,"Michel":19,"Roberto":55,"Luiz":30}
dict_status_aluno2 = {a:("Aprovado" if v>70 else "Reprovado") for (a,v) in dict_aluno.items() }
print(dict_status_aluno2)
