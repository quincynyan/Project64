import sys
import time

x = 9 					# initialize x
while x >= 0: 						# iteration
    if x > 0: 						# selection
        sys.stdout.write(str(x)) 	# output
        time.sleep(.75) 			# delay
        sys.stdout.write("\b") 		# backspace
        sys.stdout.flush() 			# flush
    else:
        print("Blast Off")
    x = x - 1 					# update
