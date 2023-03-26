w = float(input("Enter weight in kg: "))
c = 0
if w > 0:
    c += 3
    if w > 2:
        if w <= 10:
            c += 2*(w-2)
        else:
            c += 16+(3*(w-10))
print("Cost: ", c)
