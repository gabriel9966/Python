import pandas as pd

df  = pd.read_csv("cap10(pandas)\dataset.csv")

#strip remove caracteres da string, split dividi a string

a = df["Data_Pedido"].head()
print(a)

#removendo o numero 20 a esquerda

a = df["Data_Pedido"].str.lstrip("20")#l por que é left = esquerda
print(a)