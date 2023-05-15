import numpy as np

#criando array de 3D

arr1 = np.array([
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ],
    [
        [13,14,15,16],
        [17,18,19,20],
        [21,22,23,24]
    ]
])
print(arr1[0,0,0])
print(arr1.shape)
print(arr1,"\n")
print("Numero de dimensões:",arr1.ndim)
arr2 = np.ones(10)
print("\n",arr2,"\n")
print("\n Array de 3 dimensões usando ones\n")
arr3 = np.ones((2,3,4))
print(arr3)

arr4 = np.ones((3,3,3,3))
print("Numero de dimensões:",arr4.ndim)
print("\n Array de 4D \n")
print("\n",arr4)
print(arr4.shape)#formato do array

