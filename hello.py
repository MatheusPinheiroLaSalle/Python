import threading

total = 0
mutex = threading.Lock()

def Hello(tid):
	global total
	with mutex:
#	mutex.acquire()
		subtotal = total
		print("Sou Thread "+str(tid))
		subtotal+= tid
		total = subtotal
#	mutex.release()

threads=[]
for i in range(100):
	threads.append(threading.Thread(target=Hello, args=(i,)))
	threads[-1].start()

for i in range(100):
	threads[i].join()

print ("Total = "+str(total))
