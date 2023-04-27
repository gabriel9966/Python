class Carro():
    #construtor
    #self == this
    def __init__(self):
        
        self.marca = "vazio"
        self.modelo = "vazio"
        self.ano = "0"
        self.km = "0"
        
    def imprime(self):
        print("Foi criado o carro :",self.marca," modelo ",self.modelo, "ano ",self.ano,"km ",self.km)
        
        
carro1 = Carro()
carro1.imprime()
carro1.marca = "Ferrari"
carro1.modelo = "458"
carro1.ano = "2013"
carro1.km = "45875"
carro1.imprime()

carro2 = Carro()
carro2.imprime()
carro2.marca = "Ferrari"
carro2.modelo = "812"
carro2.ano = "2022"
carro2.km = "4569"
carro2.imprime()
        
         
        