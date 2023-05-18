#prenchendo valores ausentes
import pandas as pd
import numpy as np


df = pd.read_csv("cap10(pandas)\dataset.csv")#carregando o data set

print(df.head())

valor_alsente = df.isna().sum() # sum = soma os valores considerando 1 para true e 0 para false
print("\n",valor_alsente,"\n")

moda = df["Quantidade"].value_counts().index[0]
print("Moda =",moda)

#fillna = prencher valor ausente

df["Quantidade"].fillna(value = moda, inplace = True)# inplace para salvar o resultado no próprio dataFrame

print(df.isna().sum())