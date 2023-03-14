print("Calculadora de media")
nota1 = float(input("Digite a nota1 :"))
nota2 = float(input("Digite a nota2 :"))
nota3 = float(input("Digite a nota3 :"))
nota4 = float(input("Digite a nota4 :"))
media_da_prova = float(input("Digite qual é a média :"))

def media(nota1,nota2,nota3,nota4):
    media_total = (nota1 + nota2 + nota3 + nota4)/4
    return media_total

valor_media = media(nota1,nota2,nota3,nota4)

if valor_media < media_da_prova:
    print("Reprovou")
elif valor_media == media_da_prova:
    print("Passou raspando")
else:
    print("Aprovado")