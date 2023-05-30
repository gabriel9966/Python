
from matplotlib import pyplot as plt
import seaborn as sea# para gráficos estatísticos
#print(sea.__version__)

dados = sea.load_dataset("tips")
print(dados.head())

sea.jointplot(data=dados, x = "total_bill", y = "tip",kind="reg")
plt.show()