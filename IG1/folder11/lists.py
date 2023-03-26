Alist = ["BMW", "Toyota", "Audi", "Renault", "Rover"]
myFile = open("cars.txt", "w")
for index in range(len(Alist)):
	myFile.write((Alist[index]) + ",")
myFile.close()