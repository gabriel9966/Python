import pandas as pd
import numpy as np


df = pd.read_csv("cap10(pandas)\dataset.csv")#le o csv


a = df[["Segmento","Regiao","Valor_Venda"]].groupby(["Segmento","Regiao"]).mean()#função de agrupamento grounpby, mean = média
print(a)

#agregassão multiplas

b = df[["Segmento","Regiao","Valor_Venda"]].groupby(["Segmento","Regiao"]).agg(["mean","std","count"])
print(b) # agg = para agregar dados