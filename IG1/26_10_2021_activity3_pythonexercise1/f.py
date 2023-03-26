n = int(input("Enter n. "))
##uppper row
for x in range(1, int(((n+1)/2)+1)): 	##for( x <- 1; x <= ( ( n + 1 ) / 2 ); x <- x + 1; )
	##space
	for	y in range(int(((n+1)-(x*2))/2), 0, -1): 	##for( y <- ((n+1)-(x*2))/2; y > 0; y <- y - 1; ) 
		print(" ", end="")
	##star
	for z in range(1, (x*2)):	##for( z <- 1; z <= (x*2)-1; z <- z + 1; ) 
		print("*", end="")
	print()
##lower row
for a in range(1, int((n-1)/2)+1): 	##for( a <- 1; a < ( ( n - 1 ) / 2 ); a <- a + 1; )
	##space
	for b in range(0, a): 	##for( b <- 0; b < a; b <- b + 1; )
		print(" ", end="")
	##star
	for c in range(1, int(((((n+1)-(a*2)))))): 	##for(c <- 1; c <= ( ( ( ( n + 1 ) - ( a * 2 ) ) / 2 ) * 2 ) - 1; c <- c + 1; )
		print("*", end="")
	print()