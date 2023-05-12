import numpy as np

arr1 = np.array([[1,2,3,4],[5,6,7,8]])#duas dimensões
print(type(arr1))
print(arr1.shape)
print(arr1)

arr2 = np.ones((2,3))#cria um array com duas dimensoes , com o numero 1
print("\n",arr2)

lista_de_listas = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

arr3 = np.matrix(lista_de_listas)#cria uma matrix, melhor para operação matematica
print("\n",arr3)
print(arr3.size)

#indexaão com duas dimensões

arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array de duas dimensoes:",arr4[2,2])

arr5 = [[1,2,3],[4,5,6],[7,8,9]]#array normal
print(arr5[2][2])#para acessar no array normal

print("array 4:",arr4[0:2,2])#[linha ate 1 ,2 é exclusivo, coluna 2]

arr5 = np.array([1,2,3,4,5,6],dtype=float)
print(arr5.dtype)
print(arr5)
print(arr5.itemsize)#tamanho ocupado na memória