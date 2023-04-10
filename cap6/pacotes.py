#import numpy #importando pacote
# em python o ,módulo é um arquivo script que contém código python e pode ser importado em outros arquivos python. Ele é usado para compartilhar funções classes e variáveis entre arquivos

#já o pacote é uma coleção de módulos organizados em uma estrutura de diretório.Ele permite a divisão de um aplicativo em múltiplos módulos , o que facilita a manutenção e desenovolvimento

#verificando todos os métodos e atributos do pacote
#dir(numpy)

#numpy.sqrt(25)

#importando apenas um dos métodos do pacote numpy
#from numpy import sqrt

#usando método
#sqrt(50)

import random#gera números aleatórios
# escolhe um aletório
palavra_escolhida = random.choice(["abacaxi","morango","uva","melao"])
print(palavra_escolhida)
#range = sequencia de numeros
#sample amostra (números possíveis , quantidade de números)
amostra_aleatoria = random.sample(range(101),10)
print(amostra_aleatoria)

import statistics

dados = [1.89,7.98,4.65,33.8,4.68,6.52,5.79]
print("\n",dados)
media_conjunto_dados = statistics.mean(dados)#mean = média
print("media :",media_conjunto_dados)

mediana = statistics.median(dados)
print("mediana :",mediana)

import os
print("\ndir\n",dir(os))

#podemos trabalhar com módulos dos pacotes

import urllib.request#usado para trazer urls

resposta = urllib.request.urlopen("http://python.org")#objeto de conexão da url
print(resposta)

html = resposta.read()#retorna código html
print(html)