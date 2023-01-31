w = float(input("Enter weight in kg: "))
if(w < 2.5):
    t = w * 3.50
elif(2.5 <= w <= 5):
    t = w * 2.85
elif(w > 5):
    t = w * 2.45

print("The price is: $", t)
