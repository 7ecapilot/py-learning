# Insert random change here
# Rock-paper-scissors template
import random
import time

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors" to numbers
# as follows:
#
# 0 - rock
# 1 - paper
# 2 - scissors


# helper functions

def number_to_name(number):
	# fill in your code below
	# convert number to a name using if/elif/else
	# don't forget to return the result!
	if number == 0:
		return 'rock'
	elif number == 1:
		return 'scissors'
	else:
		return 'paper'
	
	
	# convert name to number using if/elif/else
	# don't forget to return the result!
def name_to_number(name):
	# fill in your code below
	if name == 'rock':
		return 0
	elif name == 'scissors':
		return 1
	else:
		return 2
		
def rpsls(name): 
# fill in your code below
# convert name to player_number using name_to_number
# compute random guess for comp_number using random.randrange()
# compute difference of player_number and comp_number modulo three
# use if/elif/else to determine winner
# convert comp_number to name using number_to_name
# print results
	computer_guess = random.randrange(0, 3, 1)
	print(computer_guess)
	cmptr_name = number_to_name(computer_guess)
	print(cmptr_name)
	
# test your code
print("Ready?")
time.sleep(2)
print('Go!')
print('1')
time.sleep(1)
print('2')
time.sleep(1)
print('3')
myGuess = input('Enter your guess: ')
rpsls(myGuess)

