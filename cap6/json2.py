dict_guido = {
    "nome":"Guido Van Rossum",
    "linguagem":"python",
    "similar": ["c","Modula-3","lisp"],
    "users":789546
}

for k,v in dict_guido.items():
    print(k,v)
    
#importando o módulo json

import json

#convertendo dicionário em objeto json

json.dumps(dict_guido)

#criando arquivo json

with open("cap6/arqJson1.json", "w") as arquivo:
    arquivo.write(json.dumps(dict_guido))
    
#leitura arquivo json
print("-------------------------------------------")
with open("cap6/arqJson1.json", "r") as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
    
print(dados)
print(dados["nome"])