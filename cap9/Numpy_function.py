import numpy as np

arr1 = np.array([1,2,3,4,5])

print("Array original:",arr1)

print("Soma acumulada:",arr1.cumsum())

arr2 = np.arange(51)#igual o range ,so que para numpy (atart,atop,step), uma instância da classe arange
print(arr2)
print("tipo do array2:",type(arr2))
print("tipo do array2:",arr2.shape)
print(arr2.dtype)#tipo de dado nesse array

arr3 = np.zeros(10)
print(arr3)
arr3[5] = 6
print(arr3)

arr4 = np.eye(4)#retorna 1 em diagonal e 0 no resto
print("\n",arr4)#matriz diagonal

arr5 = np.diag(np.array([1,2,3,4]))#matriz diagonal
print("\n",arr5)