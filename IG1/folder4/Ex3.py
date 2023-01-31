def myFunction3(name):
	myFile3 = open(name, "r")
	A = myFile3.readlines()
	B = None
	n = 0
	for k in range(0, len(A)):
		B = [[None]] * len(A)
	for i in range(0, len(A)):
		A[i].strip()
		for j in range(0, len(A[i])):
			B[i] = A[i].split()
	for m in range(0, len(B)):
		n = n + len(B[m])
	print("Word count: ", n)
	myFile3.close()

myFunction3(input("File name of txt you want to open: "))


"""
One two three four
Five six seven
Eight
Nine Ten


A = ["One two three four", "Five six seven", "Eight", "Nine Ten"] 
len(A) = [4]
B = [["One", "two", "three", "four"], ["Five", "six", "seven"], ["Eight"], ["Nine", "Ten"]]
len(B) = [4, 4]
"""