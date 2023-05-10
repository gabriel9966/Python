import numpy as np

arr1 = np.array([1,2,3,4,5])

print("Array original:",arr1)

print("Soma acumulada:",arr1.cumsum())

arr2 = np.arange(51)#igual o range ,so que para numpy (atart,atop,step), uma instância da classe arange
print(arr2)
print("tipo do array2:",type(arr2))
print("tipo do array2:",arr2.shape)
print(arr2.dtype)#tipo de dado nesse array