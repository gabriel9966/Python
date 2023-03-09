nomes = ["gabriel","luiz","carol","julio"]
idade = [18,22,33,24]
total = 0
i = 0
qtd = len(idade)
while i < qtd:
    total = total + idade[i]
    i += 1

media = total / qtd
print("Essa e a media :",media) 
