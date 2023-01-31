n = int(input("Enter n. "))
row = 0
while ( row < n):
	i = 1
	##PRINT space
	while ( i <= ( n - ( row + 1 ) ) ):
		print(" ", end="")
		i = i + 1
	##PRINT star
	x = 1
	while ( x <= ( row + 1 ) ):
		print("* ", end="")
		x = x + 1
	#PRINT enter
	print()
	row = row + 1