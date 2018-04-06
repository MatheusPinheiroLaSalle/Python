from socket import *

s = socket ()

pega = "GET /rj/ HTTP/1.1\r\nHost:unilasalle.edu.br\r\n\r\n"

converte = str.encode(pega,"UTF-8")

servidor="unilasalle.edu.br"
porta=80

s.connect((servidor, porta))
s.send (converte)

while True:
	x = s.recv (4096)
	if not x:
		break
	print (x.decode("UTF-8"))

s.close ()

