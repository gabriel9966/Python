#filtra elementos de uma estrutura de dados
 
def par (x):
    if x % 2 == 0:
        return True
    else:
        return False
        
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("O numero 35 é par ? :",par(4))

nova_lista = list(filter(par,numeros))
print("lista original :",numeros)
print("nova lista :",nova_lista)