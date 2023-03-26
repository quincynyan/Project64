subjects = ["English", "FPM", "MathB",
            "Physics", "Chemistry"]
num = int(input("Please enter the number of students in the class: "))

for student in range(num):
    sum = 0
    print("Student", student + 1)
    for subject in subjects:
        mark = int(input("Please enter the mark for " + subject + ": "))
        sum = sum + mark
    average = sum / len(subjects)
    print("The average mark for student", student + 1, "is", average)
