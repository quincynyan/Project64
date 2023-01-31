arrayForms = ["7AXB", "7PDB", "7ARL", "7JEH"]
form = input("Please enter a form number: ")
valid = False
index = 0
length = len(arrayForms)
while valid == False and index < length:
    if form == arrayForms[index]:
        valid = True
    index = index + 1
if valid == True:
    print("Valid form")
else:
    print("The form you entreed does not exist.")
