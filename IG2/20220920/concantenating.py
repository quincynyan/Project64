# Generate username

name = input("Enter your name: ")
first_name = name.split()[0]
last_name = name.split()[-1]

if len(last_name) < 4:
    last_name = last_name + "X" * (4 - len(last_name))
username = first_name[0] + last_name[:4]

print("Your username is: " + username)
