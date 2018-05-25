import json
import requests


nome = input ("nome?\n")
user = requests.get("https://jsonplaceholder.typicode.com/users")
req = requests.get("https://jsonplaceholder.typicode.com/posts")
list = json.loads(req.text)
listnome = json.loads(user.text)
for x in listnome:
	if (nome == x['username']):
		id = x['id']
		for i in list:
			if (id == i['userId']):
				print ("\nTitle:"+"\n"+i['title']+"\n")
				print ("Body:"+"\n"+i['body'])
				print ("\n")
		break
	else: 
		print("Tem não")
break
