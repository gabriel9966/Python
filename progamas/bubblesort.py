lista = [1,6,-4,65,-188,14,167,864,-1999]

def bublesort(arr):

    n = len(arr)
    
    for i in range(n):
        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return(arr)

print(bublesort(lista))