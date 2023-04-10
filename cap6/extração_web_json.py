#imprimindo um arquivo json copiado da internet
# from serve para quando vamos importar partes especificas do módulo
import json
from urllib.request import urlopen
#urlopen para extrair um arquivo da web
response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]#so a primeira parte da resposta por isso o index 0

print(dados)

print("\n titulo :",dados["title"])

#copiando dados de um arquivo para o outro
arquivo_fonte = "cap6/dados.json"
arquivo_destino = "cap6/dados.txt"

#método 1

with open(arquivo_fonte, "r") as arquivo:
    text = arquivo.read()
    with open(arquivo_destino, "w") as arquivo2:
        arquivo2.write(text)
        
#método 2
open(arquivo_destino, "w").write(open(arquivo_fonte, "r").read())

#leitura de arquivo txt
with open("cap6/dados.txt", "r") as arquivo :
    # faz a leitura do arquivo
    texto9 = arquivo.read()
    #decodifica string json em objeto python
    dados = json.loads(texto9)
    print(dados)
    