loop = []
primos = []

            #loop para percorre
for num in range(2,30):
    loop.append(num)
    
    #variável de controle
    eh_primo = True
    #loop while para verificar se é primo
    i=2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i = i +1
    
    if eh_primo:
        primos.append(num)

print(primos)
print(loop)
