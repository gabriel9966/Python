class Estudantes:
    
    estudantes = 0
    
    
    def __init__(self,nome,idade,nota):
        
        self.nome = nome
        self.idade = idade
        self.nota = nota
        Estudantes.estudantes += 1
         
       
        #self == this
    def imprimir (self):
        return("Nome :",self.nome,"idade :",self.idade," nota:",self.nota)
        
    def contarPessoas():
        return(Estudantes.estudantes)
        
        
        
enzo = Estudantes("Enzo",18,7.5)

print(enzo.imprimir())
print(Estudantes.contarPessoas())
        
        