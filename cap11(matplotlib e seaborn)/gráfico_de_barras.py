#x = categorias
#y = quantidades
from cProfile import label
from turtle import color
#matplotlib.pyplot é uma interface gráfica para exibir os graficos dentro do pacote matplotlib, um módulo específico
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,12,17]
# bar = barra 
plt.bar(x,y,label = "Barras",color="red")
plt.legend()
plt.show()

