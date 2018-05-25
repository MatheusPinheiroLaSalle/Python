import json
import requests


nome = input ("nome?\n")
cli = requests.get("http://127.0.0.1:5000/cliente/"+nome)
list = json.loads(cli.text)
#for i in list:
print (list)
	
