from cProfile import label
from turtle import color
import matplotlib.pyplot as plt

fatias = [5,10,8,13]
atividades = ["dormir","comer","estudar","trabalhar"]
cores = ["olive","lime","violet","royalblue"]

plt.pie(fatias, labels=atividades, colors=cores , startangle=90, shadow=True,explode = (0,0.1,0,0))#shadow = sombra ,explode = (fatia1, 2,3,4)
plt.show()