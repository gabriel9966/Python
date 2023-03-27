#expressões lambda

def potencia01 (num):
    resultado = num**2
    print(resultado)

def potencia2 (num):
    return num**2
# função de uma linha
def potencia3(num) : return num**2

#expressão lambda (Função anônima) não precissa dar nome a função, gravada na variável potência

potencia = lambda num: num**2

print(potencia(2))

par = lambda num :num % 2 == 0
print(par(2))
print(par(3))

primeiro_caracter = lambda s : s[0]
print(primeiro_caracter("Ronaldo"))

reverso = lambda s : s[::-1]
print(reverso("Irinelsom"))