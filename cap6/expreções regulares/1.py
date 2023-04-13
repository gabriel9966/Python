#As expressões regulares em Python são padrões que definem um conjunto de caracteres. Esses padrões são usados para pesquisar, localizar e manipular strings.

import re
texto = "Meu email é ganaan@gmail.com ,pode também tentar yofoa@hotmail.com"

resultado = len(re.findall("@",texto))#conta quantas vezer o arroba aparece no texto find =encontrar all =tudo
print("resultado :",resultado)

#achar a palavra depois da palavra pode 
                         #precissa do espaçoentre pode e (\w+)
resultado2 = re.findall(r"pode (\w+)", texto) #\w busca palavras, r para a linguagem interpretar certo
print("resultado :",resultado2[0])
