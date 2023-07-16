def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

def calculadora():
    print("Calculadora")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    while True:
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado: ", soma(num1, num2))
        elif opcao == "2":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado: ", subtracao(num1, num2))
        elif opcao == "3":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado: ", multiplicacao(num1, num2))
        elif opcao == "4":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado: ", divisao(num1, num2))
        elif opcao == "5":
            print("Encerrando a calculadora...")
            break
        else:
            print("Opção inválida. Tente novamente.")

calculadora()
