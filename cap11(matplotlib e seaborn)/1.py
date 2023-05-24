from cProfile import label
import matplotlib as mpl#permite criar gráficos

#plot = representação gráfica de dados

import matplotlib.pyplot as plt

#o método plot() define os eixos do gráfico

#plt.plot([1,3,5],[2,4,7])
x = [1,3,5]
y = [2,4,7]
#plt.plot(x,y)
plt.xlabel("Variável 1")
plt.ylabel("Variável 2")
plt.title("Teste plot")
#plt.show()

x2 = [1,2,3]
y2= [11,12,13]
plt.plot(x2,y2,label="Gráfico com matplot")
plt.legend()# faz do label uma legenda
plt.show()