import numpy as np

arr1 = np.arange(1,10)
print(arr1)

somado = np.sum(arr1)#soma dos elementos do array
print("soma total:",somado)

produto = np.prod(arr1)#faz a multiplicação dos valores
print("Produto:",produto)

soma_acumulada = np.cumsum(arr1)
print("Soma acumulada:",soma_acumulada)