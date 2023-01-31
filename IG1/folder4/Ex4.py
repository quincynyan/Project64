num1 = int(input("Enter past meter reading: "))
num2 = int(input("Enter current meter reading: "))
n = num2 - num1
if (n <= 100):
	c = 0.50 * n
elif (n <= 200):
	c = 50 + (1 * (n - 100))
elif (n <= 300):
	c = 150 + (1.5 * (n - 200))
else:
	c = 300 + (2 * (n - 300))
print("Past meter reading: ", num1)
print("Current meter reading: ", num2)
print("Units consumed: ", n)
print("Bill: ", c)