row = int(input("How many sets would you like to enter?"))
col = int(input("How many marks are in each set?"))
marks = [[0 for x in range(col)] for y in range(row)]

print(marks)

for i in range(0, row):
    print("Enter " + str(col) + " marks for set " + str(i+1) + ":")
    for j in range(0, col):
        marks[i][j] = int(input("Enter mark " + str(j + 1) + ":"))

print(marks)

# Record to marks.txt
f = open("marks.txt", "w")
# Clear the file
f.truncate()
# Write the marks to the file
for i in range(0, row):
    for j in range(0, col):
        f.write(str(marks[i][j]) + " ")
    f.write("\n")
f.close()
