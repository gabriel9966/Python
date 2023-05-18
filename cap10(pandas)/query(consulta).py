import pandas as pd
import numpy as np


df = pd.read_csv("cap10(pandas)\dataset.csv")

print(df.Valor_Venda.describe())#calculando resumo estatístico da coluna valor venda

df2 = df.query("229 < Valor_Venda < 10000")#gerando um novo dataFrame fazendo uma consulta nos valores e guardando aqueles que são maior que 229 e menor que 10000
print(df2.Valor_Venda.describe())

df3 = df2.query("Valor_Venda > 766")# query =  consulta
print(df3.head())

print(df.shape)