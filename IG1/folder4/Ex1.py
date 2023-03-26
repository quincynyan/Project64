import time

def myFunction1(name):
	myFile1 = open(name, "r")
	for l in myFile1:
		for c in l:
			print(c,end="",flush=True)
			time.sleep(0.05)
		time.sleep(1)
		print()
	myFile1.close()

myFunction1(input("File name of txt you want to open: "))