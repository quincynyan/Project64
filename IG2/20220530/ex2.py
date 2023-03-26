first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))
temp = first
first = second
second = temp
print("After Swapping: ", first, second)

print("\n\n")

first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))
first, second = second, first
print("After Swapping: ", first, second)
