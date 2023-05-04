class veiculos():
    def __init__(self):
        print("veiculo criado")
        self.marca = "vazio"
        self.modelo = "vazio"
        self.ano = "0"
        self.km = "0"
        
        
class carro(veiculos):#herdou
    
    def __init__(self):
        
        super().__init__()#caso modifique o construtor precissa, se usar o construtor padrao não precissa
        print("Carro criado")
        self.portas = 0
        self.tetoSolar = "fechado"
        
    
    def abrirTetoSoçar(self):
        self.tetoSolar = "aberto"
        print("Teto solar :",self.tetoSolar)
    
    def fecharTetoSolar(self):
        self.tetoSolar = "fechado"
        print("Teto solar :",self.tetoSolar)
        
    
camaro = carro()
camaro.marca = "chevrolet"
camaro.modelo = "camaro"
camaro.abrirTetoSoçar()
print(camaro.marca)
print(camaro.modelo)    