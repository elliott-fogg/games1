# Import the relevant modules
import random

# Initialise lives
bool_round = 1
bool_play = 1

while bool_play == 1:
	lives = 5
	rand_num = int(round(random.random()*20))
#	print(rand_num)
	guess = int(input("Guess the number between 1 and 20. You have "+str(lives)+" guesses left:  "))
	
	while bool_round == 1:
		if guess == rand_num:
			print("You guessed right!")
			bool_round = 0
		else:
			lives -= 1
			if lives == 0:
				print("You have failed. The number was "+str(rand_num)+".")
				bool_round = 0
			else:
				guess = int(input("Wrong. You have "+str(lives)+" guesses left. Try again:  "))

	char_yn = input("Would you like to play again? (y/n):  ")
	if char_yn != 'y':
		print("Thanks for playing!")
		bool_play = 0
	else:
		bool_round = 1
		print("")
