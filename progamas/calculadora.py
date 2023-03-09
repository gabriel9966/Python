print("Bem vindo a calculadora")
a = float(input("Digite o primeiro numero :"))
operacao = input("Digite a operacao +,-,/ ou * :")
b = float(input("Digite o segundo numero :"))

if operacao == "+":
    print(a+b)
elif operacao == "-":
    print(a-b)
elif operacao == "/":
    print(a/b)
elif operacao == "*":
    print(a*b)
else:
    print("operacao invalida")