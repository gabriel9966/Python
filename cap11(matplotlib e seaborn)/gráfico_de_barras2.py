#x = categorias
#y = quantidades

#matplotlib.pyplot é uma interface gráfica para exibir os graficos dentro do pacote matplotlib, um módulo específico
import matplotlib.pyplot as plt

idades = [25, 32, 18, 42, 55, 29, 37, 41, 19, 63, 27, 35, 47, 52, 21,79]
bins = [10 * i for i in range(1,17)]# range faz uma lista de numeros em sequencia, new_list = [expression for item in sequence if condition]
#Em Python, o termo "bins" é frequentemente usado em análise de dados e visualização para se referir aos intervalos em que os dados são agrupados.

#histograma
plt.hist(idades,bins, histtype="bar" , rwidth=0.8)#largura entre das linhas, histype = tipo do stograma
plt.show()


