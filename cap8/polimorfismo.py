class veiculo():
    
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        
    def acelerar(self):
        pass
    
    def frear(self):
        pass
    
class carro(veiculo):
    
    
        
    def acelerar(self):
        print("Acelerando o carro")
        
    def frear(self):
        print("Freando o carro")
        
        
class moto(veiculo):
    
    
        
    def acelerar(self):
        print("Acelerando a moto")
        
    def frear(self):
        print("Freando a moto")
        
        
r3 = moto("yamaha","r3")#polimorfismo, usando o construtor da classe mae
r3.frear()
        
        