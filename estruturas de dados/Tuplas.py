# tuplas para armazenar valores diferentes, são imutaveis
x = (5,10)
print(x[0])
print(x[1])

pessoa = ("gabriel",18)

alunos = (
    ("nono ano",30),
    [10,30,20,44,12,6]
)
print(alunos)

nota1 = (5,7)
nota2 = [6,8]

pessoa1 = ("gabriel",17,True)
#desempacotamento
nome,idade,admin = pessoa1