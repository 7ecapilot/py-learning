# Rock-paper-scissors-lizard-Spock template

import math
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
	# fill in your code below
	# convert number to a name using if/elif/else
	# don't forget to return the result!
	if number == 0:
		return 'rock'
	elif number == 1:
		return 'Spock'
	elif number == 2:
		return 'paper'
	elif number == 3:
		return 'lizard'
	else:
		return 'scissors'
	
	# convert name to number using if/elif/else
	# don't forget to return the result!
def name_to_number(name):
	# fill in your code below
	if name == 'rock':
		return 0
	elif name == 'Spock':
		return 1
	elif name == 'paper':
		return 2
	elif name == 'lizard':
		return 3
	else:
		return 4
		
		
def rpsls(name): 
# fill in your code below
# convert name to player_number using name_to_number
# compute random guess for comp_number using random.randrange()
# compute difference of player_number and comp_number modulo five
# use if/elif/else to determine winner
# convert comp_number to name using number_to_name
# print results
	you_push = 0
	you_win = 0
	outcome = ""
	winner = ""
	loser = ""
	computer_guess = random.randrange(0, 5)
	num = name_to_number(name)
	print("You chose",name,"|","Computer chose",number_to_name(computer_guess))
	moddiff = (num - computer_guess) % 5
	
	if moddiff != 0:
		if (moddiff < 3):
			you_win = 1
			winner = name
			loser = number_to_name(computer_guess)
		else:
			you_win = 0
			winner = number_to_name(computer_guess)
			loser = name
	else:
		you_push = 1

		
	if winner == "rock" and (loser == "scissors" or loser == "lizard"):
		outcome = "crushes"
	elif winner == "Spock" and loser == "rock":			
		outcome = "vaporizes"
	elif winner == "Spock" and loser == "scissors":
		outcome = "smashes"
	elif winner == "paper" and loser == "rock":
		outcome = "covers"
	elif winner == "paper" and loser == "Spock":
		outcome = "disproves"
	elif winner == "lizard" and loser =="paper":
		outcome = "eats"
	elif winner == "lizard" and loser == "Spock":
		outcome = "poisons"
	elif winner == "scissors" and loser == "paper":
		outcome = "cuts"
	elif winner == "scissors" and loser == "lizard":
		outcome = "decapitates"
	else:
		winner = name
		outcome = "ties"
		loser = number_to_name(computer_guess)
	print(winner, outcome, loser)
			
	if not you_push:
		if you_win == 1:
			print("You win!\n")
		else:
			print("You lose...\n")
	else:
		print("It's a tie.\n")

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

