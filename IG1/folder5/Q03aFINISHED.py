#   Q3a

#   Initialise variables

base = 50
heightChk = True

#   Print prompt and take input from user

while(heightChk):
	print("Enter the height (between 1 and 100): ")
	height = int(input())
	if(height >= 1 and height <= 100):
		heightChk = False

#   Calculate area and print out values

area = 0.5 * base * height

print("Base of triangle is: ", base)
print("Height of triangle is: ", height)
print("Area of triangle is: ", area)