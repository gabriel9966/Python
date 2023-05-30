from cProfile import label
from turtle import color
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [30000,28000,33000,28500,31250,38650]
label = ["hb20","gol","onix","palio","uno","celta"]
plt.bar(x,y)
plt.xticks(x,label)#(posiçães, rótulos), usado para personalizar os rótulos do eixo x
plt.legend()
plt.show()