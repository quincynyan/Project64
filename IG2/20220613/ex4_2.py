A = [3.50, 2.85, 2.45]
w = float(input("Enter weight in kg: "))
print("The price is: $", w * (A[2] if w > 7.5 else A[int(w // 2.5)]))
