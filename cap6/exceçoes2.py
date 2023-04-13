print("Somando numeros")
numeros = 0

while True:
    try:#tente executar
        scan = int(input("Digite o numero para ser somado ou 0 para terminar :"))
    except ValueError:#capture esse erro
        print("Por favor digite um numero")
        continue
    else:#se não teve erro ,faça isso
        print("Adicionado com sucesso!")
    finally:#executa de qualquer jeito
        print("Obrigado!")
    if scan == 0:
        break
    int(scan)
    numeros += scan
    
    
print("Total :",numeros)

    