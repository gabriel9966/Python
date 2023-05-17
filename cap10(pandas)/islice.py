import pandas as pd
import numpy as np
dados = {"Estado":["SP","RS","MG","BA","RJ","AM"],
         "Ano":[2000,2005,2010,2015,2012,2011],
         "Taxa de desemprego":[1.5,1.7,2.2,3.8,2.0,3.0]}

df = pd.DataFrame(dados,columns=["Estado","Ano","Taxa de Crescimento","Taxa de desemprego"],
                  index=["Estado1","Estado2","Estado3","Estado4","Estado5","Estado6",])

print(df["Estado2":"Estado4"])

print(df[df["Taxa de desemprego"] < 2])

#se for só uma coluna [], se for mais [[]]
print(df["Estado"])