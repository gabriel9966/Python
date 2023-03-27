import random#numero aleatorio
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

special_character = ['!','@','#','%','$','&','*']

password = []


chances1 = int(input("Digite a quantidade de letras :"))
chances2 = int(input("Digite a quantidade de numeros :"))
chances3 = int(input("Digite quantos caracteres especiais :"))
totalChances = chances1 + chances2
zero1 = 0

print("chegou aqui")
while zero1 < chances1:
    for i in letters[random.randrange(0,len(letters) )]:

        password.append(i)
    zero1+=1
zero1 = 0
while zero1 < chances2:
    for l in numbers[random.randrange(0,len(numbers) )]:

        password.append(l)
    zero1+=1
zero1 = 0
while zero1 < chances3:
    for e in special_character[random.randrange(0,len(special_character) )]:

        password.append(e)
    zero1+=1

random.shuffle(password)#embaralha o array
print(password)
