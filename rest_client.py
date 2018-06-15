import requests
import urllib.parse

nome=input("digite o nome do genero: ")


api="http://127.0.0.1:5000/cad/"
#url1 = api+urllib.parse.urlencode({"nome":nome,"sobrenome":sobrenome})
url1 = api+urllib.parse.quote(nome)

print (url1)

dados=requests.get(url1).json()
print (dados)
