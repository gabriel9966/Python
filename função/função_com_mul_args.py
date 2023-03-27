#é uma função com múltiplos argumentos
def var_info(arg1, *vartuple):
    
    print("O arg passado foi :",arg1)
    
    for i in vartuple:
        print("O arg passado foi :",i)
        
    #return;
    
    
var_info("amora","abacaxi","morango","uva")