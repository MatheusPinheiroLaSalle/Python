from socket import  *
import threading
import sys


nome = input ("Qual é o nome do arquivo?")

s = socket ()

servidor="10.10.13.3"
porta=8752

s.connect((servidor, porta))

s.send (str.encode (nome, "UTF-8"))

f = open(nome,'r')
for line in f:
     s.send (str.encode( line , "UTF-8"))



s.close ()

