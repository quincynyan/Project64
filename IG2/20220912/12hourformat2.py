# Convert 12 Hour format

time = input("Enter time in 24-hour format (hh:mm:ss): ")
try:
    h = int(time[0:2])
    m = int(time[3:5])
    s = int(time[6:8])
except:
    print("Invalid time format")
    exit()

# check for midnight or noon
if h == 0 and m == 0 and s == 0:
    print("Midnight")
elif h == 12 and m == 0 and s == 0:
    print("Noon")
else:
    if h > 23 or m > 59 or s > 59:
        print("Invalid time")
    else:
        if h >= 12:
            if h > 12:
                h -= 12
            apm = "PM"
        else:
            if h == 0:
                h = 12
            apm = "AM"
        if h < 10:
            h = "0" + str(h)
        if m < 10:
            m = "0" + str(m)
        if s < 10:
            s = "0" + str(s)
        print("Time in 12-hour format:", h, ":", m, ":", s, apm)
