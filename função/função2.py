def Calcular_conta(consumo,Taxa_Serviço = 0.1,Desconto_fidelidade=0):
    if Taxa_Serviço == 0 and Desconto_fidelidade == 0:
        return consumo
    serviço = consumo * Taxa_Serviço
    desconto = consumo * Desconto_fidelidade
    valor = (consumo + serviço) - desconto
    return print("A conta deu : ",valor)

a = Calcular_conta(consumo=100,Taxa_Serviço=0.15,Desconto_fidelidade=0.1)
print(a)