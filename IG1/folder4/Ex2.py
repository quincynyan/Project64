def myFunction2(name):
	myFile2 = open(name, "r")
	a = input("Enter an alphabet:").upper()
	n = 0
	for l in myFile2:
		if(l[0].upper() != a):
			n = n + 1
	print(n, " lines do not start with the alphabet ", a)
	myFile2.close()

myFunction2(input("File name of txt you want to open: "))