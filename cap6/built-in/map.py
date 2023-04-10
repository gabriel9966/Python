#função interna
#é uma função que aplica uma determinada função a cada elemento de uma estrutura de dados iterada
#retorna um objeto que pode ser transformado em outra estrutura de dados

def potencia (x):
    return x ** 2
numeros = [1,2,3,4,5,6]
#função map vai aplicar a função potência a cada item na lista de números , e converter em uma lista
novos_numeros = list(map(potencia,numeros))
print(novos_numeros)