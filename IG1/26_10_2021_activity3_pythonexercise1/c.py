n = int(input("Enter n. "))
row = n
while ( row > 0 ):
	i = 0
	while ( i < row ):
		print("*", end="")
		i = i + 1
	row = row - 1
	print()
	