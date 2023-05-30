import pylab

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Cria o gráfico de linha
pylab.plot(x, y)

# Personaliza o gráfico
pylab.xlabel("Eixo x")
pylab.ylabel("Eixo y")
pylab.title("Gráfico de Linha")

# Exibe o gráfico
pylab.show()
