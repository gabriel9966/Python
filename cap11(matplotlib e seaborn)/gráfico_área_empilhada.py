from matplotlib import colors
import matplotlib.pyplot as plt

dias = [1,2,3,4,5]#eixo x 
comer = [2,5,8,1,8]# y
dormir = [6,8,9,2,5]# y
trabalhar = [1,2,3,4,7]# y

plt.stackplot(dias,comer,dormir,trabalhar,labels=["comer","dormir","trabalhar"], colors= ["r","b","k"])
plt.legend()
plt.show()

# Dados de exemplo
anos = [2010, 2011, 2012, 2013, 2014, 2015]
serie1 = [5, 7, 3, 4, 6, 8]
serie2 = [2, 3, 4, 2, 2, 3]
serie3 = [1, 2, 1, 1, 2, 1]

# Criação do gráfico de áreas empilhadas
#plt.stackplot(anos, serie1, serie2, serie3, labels=['Série 1', 'Série 2', 'Série 3'])

# Configurações adicionais do gráfico
#plt.legend(loc='upper left')
#plt.xlabel('Ano')
#plt.ylabel('Valores')

# Exibição do gráfico
#plt.show()