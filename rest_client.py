import requests
import urllib.parse

nome=input("digite o nome do cliente: ")
sobrenome=input("digite o sobrenome do cliente: ")

api="http://127.0.0.1:5000/sd/"
#url1 = api+urllib.parse.urlencode({"nome":nome,"sobrenome":sobrenome})
url1 = api+urllib.parse.quote(nome)+"/"+urllib.parse.quote(sobrenome)

print (url1)

dados=requests.get(url1).json()
print (dados)
