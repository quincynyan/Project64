storedLetter = "g"
letter = input("Input a letter: ")
# Letter converted to lower case
letter = letter.lower()
# Amend the code by completing the if statement
if letter == storedLetter:
    position = ""
elif letter > storedLetter:
    position = "higher than"
else:
    position = "lower than"

print("The letter is", position,
      "the letter stored in the variable in the alphabets. ")
