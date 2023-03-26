n = int(input("Enter n. "))
row = 0
while ( row < n ):
	i = 0
	##PRINT "*" * ( row + 1 )
	while ( i <= row ):
		print("*", end="")
		i = i + 1
	row = row + 1
	##go next row
	print("\n")