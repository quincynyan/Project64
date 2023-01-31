"""
   /|
  / |
 /  |
/___|
"""

try:
    x = int(input("Enter an integer: "))
except(ValueError):
    print("Invalid input")
    quit()

# loop through the lines
for i in range(x):
    # print space
    print(" " * (x - i - 1), end="")
    # print slash
    print("/", end="")
    if (i != x - 1):
        print(" " * (i), end="")
    else:
        print("_" * (i), end="")
    # print |
    print("|", end="")
    # go to next line
    print()
