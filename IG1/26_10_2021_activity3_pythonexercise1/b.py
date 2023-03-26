n = int(input("Enter n. "))
row = 0
while ( row <= n ):
	##print space
	for i in range(0, n-row):
		print(" ", end=" ")
	##print star
	for x in range (0, row):
		print("*", end=" ")
	print()
	row = row + 1