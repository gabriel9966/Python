#Pandas é uma biblioteca construída sobre o NumPy, que fornece estruturas de dados de alto nível, como o DataFrame. O Pandas é voltado para a análise de dados tabulares e oferece recursos poderosos para manipulação, limpeza, agregação e visualização de dados. Ele permite carregar dados de diferentes fontes, como arquivos CSV ou bancos de dados, e realizar operações complexas em dados estruturados.
import pandas as pd # para manipular dados tabular(linhas e colunas)
a = pd.__version__
print(a)

dados = {"Estado":["SP","RS","MG","BA","RJ","AM"],
         "Ano":[2000,2005,2010,2015,2012,2011],
         "Taxa de desemprego":[1.5,1.7,2.2,3.8,2.0,3.0]}

print("Esse são os dados :",dados)

df = pd.DataFrame(dados)
print("\n Data Frame \n",df)
print(type(df))
print(df.head(2))#as primeiras linhas

print("\n\n")
#alterando as colunas do data frame
print(pd.DataFrame(dados, columns=["Estado","Taxa de desemprego","Ano"]))