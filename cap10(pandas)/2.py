import pandas as pd
import numpy as np
dados = {"Estado":["SP","RS","MG","BA","RJ","AM"],
         "Ano":[2000,2005,2010,2015,2012,2011],
         "Taxa de desemprego":[1.5,1.7,2.2,3.8,2.0,3.0]}

df = pd.DataFrame(dados,columns=["Estado","Ano","Taxa de Crescimento","Taxa de desemprego"],
                  index=["Estado1","Estado2","Estado3","Estado4","Estado5","Estado6",])

print(df)
print("\n ",df["Estado"])#imprimindo apenas uma coluna
print("Tipo de dados")
print("\n",df.dtypes,"\n")
print(df.values)

print("Colunas :",df.columns)#título de colunas

print(df[["Estado","Ano"]])

print(df.index)

#print(df.filter(items="Estado3",axis=0))

print(df.describe())


print(df.isna())#Tem valor nan (not a number)
print(df["Taxa de Crescimento"].isna())

df["Taxa de Crescimento"] = np.arange(6)#usando numpy com  pandas

print("\n\n",df)

