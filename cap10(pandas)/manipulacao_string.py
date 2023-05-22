import pandas as pd

df  = pd.read_csv("cap10(pandas)\dataset.csv")#lendo o arquivo e transformando em data frame
#print(df.head())

#filatrando a coluna segmento pela as palavras que começam "con"

df[df.Segmento.str.startswith('con')].head()

#filatrando a coluna segmento pela as palavras que terminam "mer"
df[df.Segmento.str.endswith('mer')].head()

print(df)
