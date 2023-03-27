def BoasVindas():
    print("Boas vindas")

def somar(a,b):
    print(a+b)

BoasVindas()
somar(5,8)

def Bem_vindo(nome,sobreNome,curso):
    print("Bem vindo ",nome,sobreNome)
    print("Seu curso e :",curso)
#argumento nomeado
Bem_vindo(nome="Sergio",curso="T.i",sobreNome="Marinho")


def imprimi_nome(nome):
    print('meu nome e %s'%(nome))

imprimi_nome("gabriel")
#função com número variável de argumentos
def imprime_var (arg1, *vartuple):
    print("o parametro passado foi ",arg1)

    for i in vartuple:
        print("o parametro passado foi ",i)
    return;

imprime_var ("morango","uva","abacaxi")