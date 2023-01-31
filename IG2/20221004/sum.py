start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
sum = 0
for i in range(start, end + 1):
    sum += i
print("Sum of numbers from {} to {} is {}".format(start, end, sum))
0