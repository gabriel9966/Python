import pandas as pd

df  = pd.read_csv("cap10(pandas)\dataset.csv")

df["Pedido_Segmento"] = df["ID_Pedido"].str.cat(df["Segmento"], sep="-")#str para transformar em string

print(df.head())