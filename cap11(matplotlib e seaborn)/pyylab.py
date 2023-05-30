import matplotlib.pylab as pylab

#from pylab import * # importa todas as funções do pylab, numpy com matplotlib
#O pylab é um módulo antigo do Matplotlib que combina as funcionalidades dos módulos pyplot e numpy
#gráfico de linha 
#dados
x = pylab.linspace(0,5,15)# gera uma sequencia de valores, (começo,final,quantidade)
y = x ** 2

#cria a figura

fig = pylab.figure()

#define as escalas dos eixos
axes = fig.add_axes([0,0,0.8,0.8])

#cria o plot
axes.plot(x,y,"r")
axes.set_ylabel("y")
axes.set_xlabel("x")
axes.set_title("Grafico de linha")

pylab.show()
