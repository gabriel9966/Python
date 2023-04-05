#organizado em formato dicionario
import json
dict_guido = {
    "nome":"Guido Van Rossum",
    "linguagem":"python",
    "similar": ["c","Modula-3","lisp"],
    "users":789546
}
#converte dicionario para formando json
json.dumps(dict_guido)
#.items retorna uma lista de tuplas chave valor
for k,v in dict_guido.items():
    print(k,v)
#cria arquivo json
with open("cap6/dados.json", "w")as arquivo:
    arquivo.write(json.dumps(dict_guido))





#le arquivo json
with open("cap6/dados.json", "r") as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
    
print(dados)
