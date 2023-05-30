from matplotlib import markers
import matplotlib.pyplot as plt#pacote para gerar os gráficos

#gráfico de dispersão ou pontos
x = [7,1,4,9,5,4,7,3,7,5,4]#largura
y = [3,4,8,5,4,6,1,3,0.6,3,1]#altura

plt.scatter(x,y, label="Dispersão", color="black", marker = "o")
plt.legend()
plt.show()