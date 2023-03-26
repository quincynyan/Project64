num = int(input("Enter the number of textbooks you want to buy: "))

if num < 6:
    total = num * 20.00
elif num < 10:
    total = num * 15.00
elif num > 9:
    total = num * 12.00
else:
    print("Invalid number of textbooks")

print("The total cost is", total)
