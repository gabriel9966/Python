import pandas as pd
import numpy as np
#operadores lógicos no pacote pandas

df = pd.read_csv("cap10(pandas)\dataset.csv")

df2 = df[ (df.Segmento == "Home Office") & (df.Regiao == "South")].head()#Filtrando
print(df2)

df3 = df[ (df.Segmento == "Home Office") | (df.Regiao == "South")].tail()#últimos registros , | = ou
print(df3)
df4 = df[ (df.Segmento != "Home Office") | (df.Regiao != "South")].sample()# != diferente, sample = traz os registros de forma aleátoria
print(df4)