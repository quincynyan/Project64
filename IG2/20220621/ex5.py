def getinp(text):
    valid = False
    while not valid:
        try:
            inp = float(input(text))
            if inp < 0 or inp > 100:
                print("Please enter a number between 0 and 100")
            else:
                valid = True
        except ValueError:
            print("Please enter a valid number")
    return inp


def recordtocsv(record):
    with open("grades.csv", "a", encoding="utf8") as f:
        f.write(record)


def main():
    # vars
    grades = ["F", "E", "D", "C", "B", "A", "A*", "A++"]
    name = ""

    # inputs
    try:
        id = int(input("Enter your student ID: "))
    except ValueError:
        print("Please enter a valid ID")
        return
    # check if id already exists
    with open("grades.csv", "r") as f:
        for line in f:
            A = line.split(",")
            if A[0] == str(id):
                print("ID already exists")
                return
            # if str(id) in line:
            #     print("ID already exists")
            #     returns
    # get name from csv
    with open("names.csv", "r", encoding="utf8") as f:
        for line in f:
            A = line.split(",")
            if A[0] == str(id):
                name = A[1][1:-1]
                break
            # if str(id) in line:
            #     name = line.split(",")[1][1:-1]
            #     break
        if name == "":
            print("ID not found")
            return

    tut = getinp("Enter your tutorial mark: ")
    test = getinp("Enter your test mark: ")
    grade = ""
    exam = None
    final = None

    # check fail
    if ((float(tut)+float(test))/2) < 40:
        grade = grades[0]
        recordtocsv(str(id)+","+name+","+str(tut)+","+str(test)+"," +
                    str(exam)+","+str(final)+","+grade+"\n")
        print("Your grade is: "+grade)
        return

    exam = getinp("Enter your exam mark: ")
    final = (tut*0.25) + (test*0.25) + (exam*0.5)
    grade = grades[int((final // 10)-3)]
    recordtocsv(str(id)+","+name+","+str(tut)+","+str(test)+"," +
                str(exam)+","+str(final)+","+grade+"\n")
    print("Your grade is: "+grade)


if __name__ == "__main__":
    main()
