import random
from os import system,name#para limpar a tela
#função para limpar tela
def limpa_tela():
    #windows
    if name == "nt":
        _ = system('cls')
    else:#outros so
        _ = system('clear')

def game():
    
    limpa_tela()
    
    print("Bem vindo a forca !!!")
    print("Adivinhe a palavra abaixo ")


    
    palavras = ["manga","abacaxi","uva","laranja","maracuja","morango","abacate"]
    
    
    #palavra_escolhida = palavras[random.randrange(0, len(palavras))]
    palavra_escolhida = random.choice(palavras)
    
    
    #list comprehenshion
    letras_descobertas = ["-" for letra in palavra_escolhida]

    chances = 6
    letras_erradas = []
    
    
    while chances > 0:
        print("".join(letras_descobertas))#join concatena uma lista de string em uma string só
        print("\nchances restantes:",chances)
        print("letras_erradas"," ".join(letras_erradas))
        
        tentativa = input("Digite uma letra :").lower()#minusculo
        
        if tentativa in palavra_escolhida:
            index = 0
            
            for letra in palavra_escolhida:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index +=1
                
        else:
            chances -=1
            letras_erradas.append(tentativa)
            
            
        if "-" not in letras_descobertas:
            print("Você venceu !!! a palavra era :",palavra_escolhida)
            break
        
    if "-" in letras_descobertas:
        print("inforcou !!!! a palavra era :",palavra_escolhida)
    
    
        
#bloco main 

if __name__ == "__main__":
    game()
        
        


