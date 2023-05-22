import pandas as pd

df  = pd.read_csv("cap10(pandas)\dataset.csv")

#print(df.ID_Pedido.head()) mesma coisa que o de baixo
#print(df["ID_Pedido"].head())

#split da coluna pelo caracter _ , split = dividir
print(df["ID_Pedido"].str.split("-").head())

print(df["ID_Pedido"].str.split("-").str[1].head())

df["Ano"] = df["ID_Pedido"].str.split("-").str[1]#criou a coluna ano

print(df)