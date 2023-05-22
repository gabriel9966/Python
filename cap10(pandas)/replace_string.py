import pandas as pd
#replace = substituir
df  = pd.read_csv("cap10(pandas)\dataset.csv")

df["ID_Cliente"] = df["ID_Cliente"].str.replace("CG","AX")

print(df["ID_Cliente"].head())