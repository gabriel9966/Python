from json import load
#importando o dataset
from sklearn.datasets import load_iris
datas = load_iris()
#importando o pandas para transformar rm data frame
import pandas as pd

df = pd.DataFrame(datas["data"], columns= datas["feature_names"])
df["species"] = datas["target"]
print(df.head())
#para criar um gráfico de linha com todas as variáveis
df.plot()

#importa um biblioteca para exibir graficos
import matplotlib.pyplot as plt
plt.show()


