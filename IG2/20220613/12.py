# Convert 12 Hour format

time = input("Enter time in 24-hour format (hh:mm:ss): ")
h = int(time[0:2])
m = int(time[3:5])
s = int(time[6:8])
if h > 23 or m > 59 or s > 59:
    print("Invalid time")
else:
    if h > 12:
        h -= 12
        print("Time in 12-hour format:", h, ":", m, ":", s, "PM")
    else:
        if h == 0:
            h = 12
        print("Time in 12-hour format:", h, ":", m, ":", s, "AM")
