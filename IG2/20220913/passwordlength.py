# password check
import re

valid = False
while not valid:
    password = input("Enter new password: ")
    if len(password) < 8:
        print("Password must be at least 8 characters long")
    elif len(password) > 20:
        print("Password must be less than 20 characters long")
    # one lower case, one upper case, one digit, one special character
    if not re.search("[a-z]", password):
        print("Password must contain at least one lower case letter")
    if not re.search("[A-Z]", password):
        print("Password must contain at least one upper case letter")
    if not re.search("[0-9]", password):
        print("Password must contain at least one digit")
    if not re.search("[.,!@#$%^&*]", password):
        print("Password must contain at least one special character")
    else:
        print("Password changed.")
        valid = True
