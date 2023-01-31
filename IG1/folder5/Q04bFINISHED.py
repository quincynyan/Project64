#   Q04b

#	write subprogram for menu option 1 here

def menuOption1(pupilAttendance):
    message = ""
    for student in pupilAttendance:
        first = student[0]
        last = student[1]
        attendance = student[2]

        if (attendance < 75):
            message = message + first + " " + last + ", "
    return message

#	write subprogram for menu option 2 here

def menuOption2(pupilAttendance):
    n = 0
    for student in pupilAttendance:
        first = student[0]
        last = student[1]
        attendance = student[2]

        if (attendance >= 90):
            n = n + 1
    return n

#	menu program

pupilAttendance = [["Faroukh" , "Salah" , 70],
["Kelvin", "Glintode" , 85],
["Lara" , "Godfrey" , 90],
["Amara" , "Grzinski" , 70],
["Aaron" , "Grimshaw" , 90],
["Farihaa" , "Mohan" , 95],
["Taz" , "Grimstow" , 60],
["Ali" , "Aisha" , 95],
["Charlene" , "Hall" ,85],
["Asra" , "Ashiq" , 90],
["Sadia" , "Bhatti" , 65],
["Ria" , "Hall" , 90],
["Fernado" , "Askabat" , 60],
["Richard" , "Hawkins" , 80],
["Siyao" , "Wang" , 60],
["Marketta" , "Hosier" , 100]]

option = 0
print ("Attendance Menu Options")
print ("1 - Display names of low attendance")
print ("2 - Display number of high attendance")
option=int(input("Choose option: "))
print ('\n')

if option == 1:
    # complete the if statement
    print(menuOption1(pupilAttendance))

	
elif option == 2:
    # complete the else if statement
    print(menuOption2(pupilAttendance))

	
else:
    print("Program complete")
