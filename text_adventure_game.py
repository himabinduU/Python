def blue_door_room() :
	print "We have treasure in treasure chest"
	print "Treasure chest has diamond, gold, silver and a guard is sleeping near the door"
	print "There are two choices to the player"
	print "Running towards_door orelse awayfrom_door"
	guard_moved = False

	while (1) :
		
		print "Enter your choice"
		player = raw_input()
		
		if player == "towards_door" and guard_moved == True :
			print "Game Over"
			return
		
		elif player == "wait" and guard_moved == True :
			guard_moved = False

		elif player == "wait" and guard_moved == False :
			print "Player got the treasure, enjoy....!"
			return

		elif player == "awayfrom_door" and guard_moved == True :
			print "Guard woke up from the sleep, player should be carefull"
	
		elif player == "awayfrom_door" and guard_moved == False :
			print "Guard is still sleeping, player can try to get the treasure"

		elif player == "towards_door" and guard_moved == False :
			print "Guard is stupidly looking at the other way"
			guard_moved = True
		
def red_door_room() :
	print "Great, a gaint dragan is sleeping"
	print "What r u going to do?"
	print "Choices available are wait and flee"
	dragon_moved = False

	while (1) :
		
		print "Enter your choice"
		player = raw_input()
		
		if player == "flee" and dragon_moved == True :
			player_died()
			return
		
		elif player == "wait" and dragon_moved == True :
			print "Dragon has woke up from the sleep"
			dragon_moved = False

		elif player == "flee" and dragon_moved == False :
			player_saved()
			return
		
		elif player == "wait" and dragon_moved == False :
			print "Dragon is still sleeping, player can try to escape"
			dragon_moved = True

def player_saved() :
	print "Ran away from danger\nplayer got saved"
	return

def player_died() :
	print "Player got died"
	print "Well, it was very tasty"
	return

print "Enter the player name"
player = raw_input()
print "player name is : %s" %player

print "player has two choices, i mean player can enter any of the two doors available"
print "1. blue door"
print "2. red door"
door_picked = raw_input()

if door_picked == "blue" :
	blue_door_room()

elif door_picked == "red" :
	red_door_room()

else :
	print "Please enter the valid choice"
