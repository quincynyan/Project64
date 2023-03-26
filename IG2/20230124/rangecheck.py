validNum = False
number = 0
while validNum == False:
    print("Please enter a number between 1 and 10:")
    number = int(input())
    if number >= 1 and number <= 10:
        validNum = True
print("You have entered:", number)
