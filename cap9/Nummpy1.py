#anaconda 3.10
import numpy as np # pacote para computação numerica, arrays
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1)
print(type(arr1))#nd = qualquer numero de dimenções
print(arr1.shape)#verifica o formato do array
#array numpy são mais eficientes
print(arr1[2:5])#[inclusivo:exclusivo]
indices = [1,2,3,4,5]
print(arr1[indices])#tem mais flexibilidade para devolver dados
par = (arr1 % 2 == 0)#uma mascara booleana para elementos pares, so seve para array numpy
print(arr1[par])
#não pode usar elementos de outros tipos no mesmo array
try:
    arr1[0] = "oi"
except:
    print("So pode ser usado numeros no array numpy")
    
arr2 = np.array(["oi","oi2"])

print(arr2)