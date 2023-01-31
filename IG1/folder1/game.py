##Import libraries
import time
import random


##Assign variables
x = "Y"
choosen = ""
A = ["rock", "paper", "scissors"]
valid = False
choosen2 = ""
res = ""
###========###
score = 0
highscore = 0


##functions
def displayscore():
	print("")
	print("Your score: ", score)
	print("Highscore: ", highscore)
	print("")


##the actual game
while x == "Y":
	score = 0
	displayscore()
	time.sleep(2)
	n = int(input("How many rounds do you want to play? "))
	for i in range(1, n+1):
		time.sleep(2)
		print("Round ", i)
		time.sleep(2)
		while valid == False:
			choosen=input("Choose: ").lower().strip()
			if choosen in A:
				valid = True
				choosen2 = random.choice(A)
				if choosen == "rock" and choosen2 == "scissors":
					res = "You win!"
					score = score + 1
				elif choosen == "paper" and choosen2 == "rock":
					res = "You win!"
					score = score + 1
				elif choosen == "scissors" and choosen2 == "paper":
					res = "You win!"
					score = score + 1
				elif choosen == "rock" and choosen2 == "paper":
					res = "I win!"
					score = score - 1
				elif choosen == "paper" and choosen2 == "scissors":
					res = "I win!"
					score = score - 1
				elif choosen == "scissors" and choosen2 == "rock":
					res = "I win!"
					score = score - 1
				elif choosen == choosen2:
					res = "It's a draw!"
				print("You chose ", choosen, ", I chose ", choosen2, ". ", res)
				displayscore()
				time.sleep(2)
			else:
				print("Please choose a valid option, rock, paper, or scissors. ")
				time.sleep(2)
		valid = False
	if score > highscore:
		highscore = score
	time.sleep(2)
	x = input("Do you want to play another game? (Type \"Y\" if you want to. Type anything else to exit): ")