import random

leave_pgm  = 0
print "This is Dice rolling program"

while (leave_pgm != "q"):

	print "If u want to roll again press enter"
	raw_input()
	number = random.randint(1, 6)

	if number == 1 :
		print ("[-----------]")
		print ("[           ]")
		print ("[     o     ]")
		print ("[           ]")
		print ("[-----------]")
		print ("Type q to quit the program")
		leave_pgm = raw_input()
	
	if number == 2 :
		print ("[-----------]")
		print ("[           ]")
		print ("[    o  o   ]")
		print ("[           ]")
		print ("[-----------]")
		print ("Type q to quit the program")
		leave_pgm = raw_input()
	
	if number == 3 :
		print ("[-----------]")
		print ("[     o     ]")
		print ("[   o  o    ]")
		print ("[           ]")
		print ("[-----------]")
		print ("Type q to quit the program")
		leave_pgm = raw_input()
	
	if number == 4 :
		print ("[-----------]")
		print ("[   o  o    ]")
		print ("[           ]")
		print ("[   o  o    ]")
		print ("[-----------]")
		print ("Type q to quit the program")
		leave_pgm = raw_input()
	
	if number == 5 :
		print ("[-----------]")
		print ("[   o   o   ]")
		print ("[     o     ]")
		print ("[   o   o   ]")
		print ("[-----------]")
		print ("Type q to quit the program")
		leave_pgm = raw_input()
	
	if number == 6 :
		print ("[-----------]")
		print ("[   o   o   ]")
		print ("[   o   o   ]")
		print ("[   o   o   ]")
		print ("[-----------]")
		print ("Type q to quit the program")
		leave_pgm = raw_input()

	
