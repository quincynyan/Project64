Blist = []
myFile = open("cars.txt", "r")
Blist = myFile.read().split(",")
myFile.close()
print(Blist)