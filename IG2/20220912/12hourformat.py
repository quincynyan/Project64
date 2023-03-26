print("\n 12 Hour Format")
hour = int(input("Enter hour"))
minutes = int(input("Enter minutes"))
seconds = int(input("Enter seconds"))
if hour == 24 and minutes == 0 and seconds == 0:
    print("Midnight")
elif hour == 12 and minutes == 0 and seconds == 0:
    print("Noon")
else:
    if hour > 12:
        hour = hour - 12
        Convert = "P.M"
    else:
        Convert = "A.M"
    print("Convert Time=", hour, ":", minutes, ":", seconds, Convert)
