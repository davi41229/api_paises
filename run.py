from flask import Flask # importando o flask
app = Flask(__name__) #instanciando a variavel

# criando uma api REST de PAISES
# REGRAS DE IMPORT DE PACOTES 1º BUILT-IN ,2º PIP, 3º ARQUIVOS DO PROJETO
import sys

import json

import requests



URL_ALL = " https://restcountries.com/v2/all"
URL_NAME = " https://restcountries.com/v2/name"

def requisicao(url): #funcao para fazer requisicao
  try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
      return resposta.text
  except:
    print('Erro ao fazer requisicao em:', url)

def parsing(texto_da_resposta): #funcao para fazer o parsing de json para python
  try:
    return json.loads(texto_da_resposta)
  except:
    print('Erro ao fazer o parsing')

def contagem_de_paises():
  resposta = requisicao(URL_ALL)
  if resposta:
    lista_de_paises = parsing(resposta)
    if lista_de_paises:
    	return len(lista_de_paises)

def listar_paises(lista_de_paises):
  for pais in lista_de_paises:
    print(pais["name"])


def mostrar_populacao(nome_do_pais):
  resposta = requisicao("{}/{}".format(URL_NAME,nome_do_pais))
  if resposta:
    lista_de_paises = parsing(resposta)
    if lista_de_paises:
      for pais in lista_de_paises:
        print('Populacao do', pais['name'])
        print("{}: {} habitantes".format(pais["name"],pais['population']))
  else:
      print('Pais nao encontrado')
      
def mostrar_moedas(nome_do_pais):
  resposta = requisicao("{}/{}".format(URL_NAME,nome_do_pais))
  if resposta:
    lista_de_paises = parsing(resposta)
    if lista_de_paises:
      for pais in lista_de_paises:
        print('Moedas do', pais['name'])
        moedas = pais['currencies']
        for moeda in moedas:
          print("{} - {}".format(moeda['name'], moeda['code']))
  else:
      print('Pais nao encontrado')


def ler_nome_do_pais():
	try:
		nome_do_pais = sys.argv[2]
		return nome_do_pais
	except:
		print(	"E preciso passar o nome do pais")



if __name__ == "__main__":
  if len(sys.argv) == 1:
  	print("*" * 20)
  	print("ˆˆˆˆTˆˆˆˆBem vindo ao sistema de paisesˆˆˆˆTˆˆˆˆ")
  	print("*" * 20)
  	print("Como usar: python paises.py <ação> <nome do pais>")
  	print("*" * 20)
  	print("Ações disponiveis: contagem, moeda, polpulacao")
  	print("*" * 20)
  else:
  	argumento1 = sys.argv[1]
  	
  	if argumento1 =="contagem":
  		numero_de_paises = contagem_de_paises()
  		print("Existem {} paises no mundo todo.".format(numero_de_paises))
  	
  	elif argumento1 == "moeda":
  		pais = ler_nome_do_pais()
  		if pais:
  			mostrar_moedas(pais)
 
  	elif argumento1 == "populacao":
  		pais = ler_nome_do_pais()
  		if pais:
  			mostrar_populacao(pais)	  		
  	
  	else:
  		print("Argumento invalido!")
  
if __name__ == "__main__":
     app.run(debug=True, port="4300")  