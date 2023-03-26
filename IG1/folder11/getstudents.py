myFile = open("studentlist.txt", "r")
rawS = myFile.read()
rows= rawS.split("\n")
A = [[]]*len(rows)
for i in range(0, len(rows)):
	A[i] = rows[i].split(",")
print(A)
myFile.close()
A.append(["StudentY", 34])
A.append(["StudentB", 42])
myFile = open("studentlist.txt", "w")
for j in range(0, len(A)):
	myFile.write(A[j][0]+ ","+ str(A[j][1])+ "\n")