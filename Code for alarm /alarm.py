#  Title   :   Alarm program along with snooze and dismiss option, interfaced with webbrowser to play the video.

import time
import webbrowser
import random

#prints the current time.
print "Current time is", time.strftime("%H:%M:%S")

#Asks the user to set alarm time
print "At what time, you want me to wake you up?"
print "Enter the time in this format, Ex :- 06:30:00"

redo = 1
alarm = raw_input()
Time = time.strftime("%H:%M:%S")
u = time.mktime(time.strptime(alarm, "%H:%M:%S"))
s = time.mktime(time.strptime(Time, "%H:%M:%S"))

#Webbrowser links will be stored in YT.txt file.
with open("YT.txt") as f:
	content = f.readlines()

#If the alarm time is more than the current time than only loop will execute, otherwise it will ask the user to enter valid time
if (u < s):
	print "Please enter the time properly"
else :
	#If the current time is not equal to the alarm time, it will sleep
	while Time != alarm :
		Time = time.strftime("%H:%M:%S")
		time.sleep(1)

	#If the current time equals to the alarm time, it plays an video from the webbrowser 
	#and asks the user to choose either snooze or dismiss option
	if Time == alarm :
		while redo == 1:
			print "WAKE UP, It's time to wake up"
			print "Now the time is", time.strftime("%H:%M:%S")
			random_video = random.choice(content)
			fb = webbrowser.open(random_video)
			print "Choose any one of the options"
			print "1. Snooze\t2. Dismiss"
			op = int(raw_input())
			if op == 1:
				time.sleep(5)
			else:
				redo = 0
