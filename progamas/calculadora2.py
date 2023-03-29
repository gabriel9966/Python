#está dando erro
#variável global pode ser assesada em qualquer lugar
resultado = 0
conta = []
print("Operadores + , -, * ou /")

print("Resultado", resultado)

def soma (num):
    global resultado
    resultado += num 
    return resultado



def sub (num):
    global resultado
    resultado -= num
    return resultado


def mult (num):
    global resultado
    resultado *= num
    return resultado


def div (num):
    global resultado
    resultado /= num
    return resultado

tamanho_conta = len(conta)
while True:
    
    print(conta ," :", resultado)

    n1 = int(input("Digite o numero :"))
   

    
    if(tamanho_conta == 0):
        conta.append(n1)
        resultado += n1
        pass
    

    conta.append(n1)

    print(conta ," :", resultado)

    operador = input("Digite o operador :")

    conta.append(operador)

    
    if operador == '+':
        soma(n1)
    elif operador == "*":
        mult(n1)
    elif operador == "/":
        if n1 == 0:
            print("nao pode ser dividida por zero")
        else:
            div(n1)
    elif operador == "-":
        sub(n1)
    elif operador == "=":
        print("Resultado", resultado)
        break

    
    
             

