AW = [": Zxask : Phone Pyae Aung", 
"Kyaw Zin Aung Win", 
"ahnt htoo", 
"Kelvin", 
"myat lwim", 
"Mary", 
"Ye Htet Myat Oo : Leonic", 
"Aung Naing Oo", 
"Yogita Naulakha", 
"Hnin Pwint", 
"T Shinn", 
"Xyris", 
"Su Shwe Yi Naing"]

myFileR = open("myFileR.txt", "r")
myFileW = open("myFileW.txt", "w")
myFileA = open("myFileA.txt", "a")

for l in (myFileR):
	print("l = ", l)
print()

AR = myFileR.readlines()
print("AR = ", AR)
print()

LR = myFileR.readline()
print("LR = ", LR)
print()

myFileW.writelines(AW)

myFileA.write("Eeeehh")

myFileR.close()
myFileW.close()
myFileA.close()