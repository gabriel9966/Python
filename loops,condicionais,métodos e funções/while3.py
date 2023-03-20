num = int(input("Digite quantos numeros vc quer imprimir :"))
x = 1
while x <=num:
    print(x)
    x+=1
else:
    print("loop concluido")


print("-----------------------------------------------")

valor =0 

while valor < 10:
    if valor == 4:
        break#quebra
    else:
        pass#passa/place holder/não faz nada
    print(valor)
    valor = valor+1

print("-------------------------------------")

for i in ("Python é zzz incrível"):
    if i == "z":
        continue#continua/pula para o próximo iteração
    print(i)