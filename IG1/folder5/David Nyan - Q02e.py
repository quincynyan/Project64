#   Q02e

def sumOfNumbers(listNumbers):
    amount = 0
    for x in listNumbers:
        if (x > 22 and x <= 40):
            amount = amount + x
    return (amount)


numArray = [23, 22, 41, 26, 55, 27, 34, 45, 24, 40, 25, 29, 51, 28, 55]

message = "Sum of selected numbers is "
total = sumOfNumbers(numArray)
print (message,total)

