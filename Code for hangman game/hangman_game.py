print "It's time to play Hangman game"

print "Start guessing the letters in the secret word..."
f = open("hangman_text")
lines = f.readlines()

print "Enter any integer number between 1 to 10"
num = int(raw_input())
line = lines[num]

word = ''
ct = 0

for c in line :
	word += c
	ct += 1
	if ct == (len(line) - 1):
		break

turns = 10
guesses = '0'
guess = ''
string = ''
cnt = 0
count = 0
	
for i in word :
	for j in word :
		if i == j :
			count += 1

#correction factor for the repetation of charectors.
r = (count - len(word)) / 2

while turns > 0:

	flag = 0
	guess = raw_input("guess a character:") 
	string += guess
	print "Input string : ", string

	for char in word :
		if char == guess :
			for ch in guesses :
				if char == ch :
					flag = 0
					break
				else :
					flag = 1
			if flag == 1 :
				print "char : ", char
				guesses += guess                    
				cnt += 1
	
	if guess not in word :
		turns -= 1
		print "Wrong guess"
		print "You have", turns, "more chance to guess"

	print "Correct guesses : ", guesses

	if (r + cnt) == len(word) :
		print "You own"
		print "The secret word is ", word
		exit(0)
	
	if turns == 0 :
		print "Sry you loosed the game"
		print "The secret word is ", word

