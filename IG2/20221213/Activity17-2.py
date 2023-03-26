with open("marks.txt", "r") as file:
    marks = [[int(x) for x in line.split()] for line in file]

for set in marks:
    # highest mark
    print("Highest mark in set: " + str(max(set)))
    # lowest mark
    print("Lowest mark in set: " + str(min(set)))
    # average mark
    print("Average mark in set: " + str(sum(set)/len(set)))
    print("")
