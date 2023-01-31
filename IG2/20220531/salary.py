regularhours = int(input("Enter the number of regular hours: "))
overtimehours = int(input("Enter the number of overtime hours: "))
wagerate = float(input("Enter the wage rate: "))

Regularpay = regularhours * wagerate
overtimepay = overtimehours * wagerate * 1.5
weeklypay = Regularpay + overtimepay

print("The regular pay is: ", Regularpay)
print("The overtime pay is: ", overtimepay)
print("The weekly pay is: ", weeklypay)
