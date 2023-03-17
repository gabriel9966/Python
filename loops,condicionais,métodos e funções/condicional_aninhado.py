# operador lógico or, and ,not(inverte o resultado)
idade = int(input("Digite sua idade :"))
acompanhado = input("Digite s se você está acompanhado e n se não :")

if idade >= 18 and acompanhado == "s":
    print("Pode entrar")
elif idade <18 and acompanhado == "s":
    print("Pode entrar")
elif idade >= 18 and acompanhado == "n":
    print("Pode entrar")
else:
    print("Não pode entrar")