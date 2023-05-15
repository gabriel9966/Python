import numpy as np

arr1 = np.arange(1,10)
print(arr1)

somado = np.sum(arr1)#soma dos elementos do array
print("soma total:",somado)

produto = np.prod(arr1)#faz a multiplicação dos valores
print("Produto:",produto)

soma_acumulada = np.cumsum(arr1)
print("Soma acumulada:",soma_acumulada)

arr2 = [1,2,3]
arr3 = [4,5,6]


soma_arrays = np.add(arr2,arr3)
print("Soma dos arrasy:",soma_arrays)

arr4 = np.array([[1,2],[4,5]])
arr5 = np.array([[4,5],[1,2]])
print(arr4.shape)
print(arr5.shape)

mult = np.dot(arr4,arr5)
print("mult:",mult)

#comparação de array 
arr5 = [1,2,3,4]
arr6 = [4,3,2,1]
 
print(arr5 == arr6)
 
comparacao_global = np.array_equal(arr5,arr6)
print(comparacao_global)