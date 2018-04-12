from socket import *

s = socket ()

pega = "Oi, Tudo bem?"

converte = str.encode(pega,"UTF-8")

servidor="10.10.13.1"
porta=8752

s.connect((servidor, porta))


while True:
	s.send (converte)
	while True:
		x = s.recv (4096)
		if not x:
			break
		print (x.decode("UTF-8"))
		resposta = input ()
		c = str.encode(resposta,"UTF-8")
		s.send(c)
s.close ()
