row = int(input("How many rows would you like to enter?"))
marks = [[0 for x in range(0)] for y in range(row)]
print(marks)

for i in range(0, row):
    s = input("Enter a set of marks: ")
    s = s.replace(" ", "")
    a = s.split(",")
    for j in range(0, len(a)):
        marks[i].append(int(a[j]))

print(marks)

# Record to marks.txt
f = open("marks.txt", "w")
# Clear the file
f.truncate()
# Write the marks to the file
for i in range(0, row):
    for j in range(0, len(marks[i])):
        f.write(str(marks[i][j]) + " ")
    f.write("\n")
f.close()
