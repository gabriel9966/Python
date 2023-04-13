def div (num,num2):
    res = num/ num2
    return(res)

print(div(5,2))
#print(div(5,0))# erro

#tratamento de exceções]

try:
    print(div(5,2))
except ZeroDivisionError:
    print("Não pode ser dividido por 0")
else:
    print("não ouve erro")

try:
    print(div(5,0))
except ZeroDivisionError:
    print("Não pode ser dividido por 0")
else:
    print("não ouve erro")