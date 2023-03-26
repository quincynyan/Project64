valid = True
validNum = False
while (not validNum):
	try:
		print("Please enter a number between 1 and 10:")
		number = int(input())
		if (number >= 1 and number <= 10):
			validNum = True
	except:
		print("That is not a number. ")
print("You have entered:", number)