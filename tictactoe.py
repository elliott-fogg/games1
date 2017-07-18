import random
import math

bool_play = 1
while bool_play == 1:
	sq_num = ["1","2","3","4","5","6","7","8","9"]
	sq_blank = [" "," "," "," "," "," "," "," "," "]
	available_nums = [1,2,3,4,5,6,7,8,9]
	turns = 9
	winner = 'n'
	
	def print_sq_num():
		print("[{}][{}][{}]\n[{}][{}][{}]\n[{}][{}][{}]".format(\
		sq_num[0],sq_num[1],sq_num[2],\
		sq_num[3],sq_num[4],sq_num[5],\
		sq_num[6],sq_num[7],sq_num[8]))
	
	def print_sq_blank():
		print("[{}][{}][{}]\n[{}][{}][{}]\n[{}][{}][{}]".format(\
		sq_blank[0],sq_blank[1],sq_blank[2],\
		sq_blank[3],sq_blank[4],sq_blank[5],\
		sq_blank[6],sq_blank[7],sq_blank[8]))
	
	def check_winner():
		global winner
		if sq_num[0] == sq_num[1] and sq_num[0] == sq_num[2]:
			globalwinner = sq_num[0]
		elif sq_num[3] == sq_num[4] and sq_num[3] == sq_num[5]:
			winner = sq_num[3]
		elif sq_num[6] == sq_num[7] and sq_num[6] == sq_num[8]:
			winner = sq_num[6]
		elif sq_num[0] == sq_num[3] and sq_num[0] == sq_num[6]:
			winner = sq_num[0]
		elif sq_num[1] == sq_num[4] and sq_num[1] == sq_num[7]:
			winner = sq_num[1]
		elif sq_num[2] == sq_num[5] and sq_num[2] == sq_num[8]:
			winner = sq_num[2]
		elif sq_num[0] == sq_num[4] and sq_num[0] == sq_num[8]:
			winner = sq_num[0]
		elif sq_num[2] == sq_num[4] and sq_num[2] == sq_num[6]:
			winner = sq_num[2]
	
	print("Welcome to Tic Tac Toe!")
	print_sq_blank()
	char_start = input("Would you like to start? (y/n):  ")
	
	if char_start == 'y':
		bool_turn = 1
	else:
		bool_turn = 0
	
	while turns > 0:
		if bool_turn == 1:
			print_sq_num()
			player_input = input("You are X's.\nPick a number correlating to a square:  ")
			test = 0
			while test == 0:
				try:
					player_input = int(player_input)
					if player_input < 10 and player_input > 0:
						if player_input in available_nums:
							test = 1
						else:
							player_input = input("That square seems to have been chosen. \
Please pick another square:  ")
					else:
						player_input = input("Please pick an available integer from 1 to 9:  ")
				
				except ValueError:
					player_input = input("Please PIck an integer from 1 to 9:  ")
			
			sq_num[player_input - 1] = 'X'
			sq_blank[player_input - 1] = 'X'
			available_nums.remove(player_input)
			turns -= 1
			bool_turn = 0
		else:
			print("Computer turn:")
			pc_turn = available_nums[int(math.floor(random.random()*len(available_nums)))]
			sq_num[pc_turn - 1] = 'O'
			sq_blank[pc_turn - 1] = 'O'
			available_nums.remove(pc_turn)
			turns -= 1
			bool_turn = 1
		
		print_sq_blank()
		check_winner()
		if winner == 'X' or winner == 'O':
			turns = 0
		print("")
	
	if winner == 'X':
		print("Congratulations! You won!")
	elif winner == 'O':
		print("Bad luck! You lost!")
	else:
		print("It's a draw! Yay?")

	char_again = input("Play again? (y/n):  ")
	if char_again != "y":
		bool_play = 0

