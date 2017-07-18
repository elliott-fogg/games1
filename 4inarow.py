import random
import math

# Print the game grid
def print_grid(table):
	print()
	for num in range(7):
		print("  "+str(num)+"  ",end="")
	print("")
	for i in range(5,-1,-1):
		for j in range(7):
			print("["+table[j][i]+"]",end="")
		print("")
# Attempt to insert a specific token into the game grid.
# Returns a value of 1 if successful, and adds said token to the grid.
# Returns a value of 0 if unsuccessful.
def input_token(column,token):
	height_index = len(table_array[column])
	if height_index < 6:
		table_display[column][height_index] = " "+token+" "
		table_array[column].append(token)
		return 1
	else:
		return 0
# Check each possible combination for 4 in a row
def check_winner():
	#Check in vertical columns
	for i in range(7):
		for j in range(3):
			if table_display[i][j] == table_display[i][j+1] == table_display[i][j+2] == table_display[i][j+3]:
				if table_display[i][j][1] in (player_token,pc_token):
					winner = table_display[i][j][1]
					table_display[i][j] = "-"+winner+"-"
					table_display[i][j+1] = "-"+winner+"-"
					table_display[i][j+2] = "-"+winner+"-"
					table_display[i][j+3] = "-"+winner+"-"
					return winner
	# Check in horizontal rows
	for i in range(4):
		for j in range(6):
			if table_display[i][j] == table_display[i+1][j] == table_display[i+2][j] == table_display[i+3][j]:
				if table_display[i][j][1] in (player_token,pc_token):
					winner = table_display[i][j][1]
					table_display[i][j] = "-"+winner+"-"
					table_display[i+1][j] = "-"+winner+"-"
					table_display[i+2][j] = "-"+winner+"-"
					table_display[i+3][j] = "-"+winner+"-"
					return winner
	# Check in forward diagonals
	for i in range(4):
		for j in range(3):
			if table_display[i][j] == table_display[i+1][j+1] == table_display[i+2][j+2] == table_display[i+3][j+3]:
				if table_display[i][j][1] in (player_token,pc_token):
					winner = table_display[i][j][1]
					table_display[i][j] = "-"+winner+"-"
					table_display[i+1][j+1] = "-"+winner+"-"
					table_display[i+2][j+2] = "-"+winner+"-"
					table_display[i+3][j+3] = "-"+winner+"-"
					return winner
	# Check in backward diagonals
	for i in range (4):
		for j in range(3):
			if table_display[i][j+3] == table_display[i+1][j+2] == table_display[i+2][j+1] == table_display[i+3][j]:
				if table_display[i][j+3][1] in (player_token,pc_token):
					winner = table_display[i][j+3][1]
					table_display[i][j+3] = "-"+winner+"-"
					table_display[i+1][j+2] = "-"+winner+"-"
					table_display[i+2][j+1] = "-"+winner+"-"
					table_display[i+3][j] = "-"+winner+"-"
					return winner
# Check-sum the table_array to see if all spots are filled
def check_tie():
	total = 0
	for i in range(len(table_array)):
		if len(table_array[i]) is not 0:
			for j in range(len(table_array[i])):
				total += 1
	return total
# Get a valid yes/no answer to a question. Accepts yY/nN, returns 1/0.
def yesno(question):
	yn = input(question + "(y/n):  ")
	while yn not in ('y','Y','n','N'):
		print("\nThat is not a valid answer. Please reply with y or n.")
		yn = input(question + "(y/n)  ")
	if yn in ('y','Y'):
		return 1
	else:
		return 0

bool_repeat = 1
print("Welcome to 4-In-A-Row!")

while bool_repeat == 1:
	# Initialise game grid
	table_display = [["   ","   ","   ","   ","   ","   "] for i in range(7)]
	table_array = [[] for i in range(7)]
	bool_play = 1
	# Select token characters
	player_token = input("\nSelect a token for yourself:  ")
	while len(player_token) is not 1:
		player_token = input("Please select a single character for yourself:  ")
	pc_token = input("Select a token for the Computer:  ")
	while len(pc_token) is not 1 or pc_token is player_token:
		pc_token = input("Please select a different, single character for the Computer:  ")
	player_turn = yesno("Would you like to start?")
	print("\nYour symbol is '"+player_token+"'. The Computer's symbol is '"+pc_token+"'.")
	# Start play:
	while bool_play == 1:
		if player_turn == 1:
			# Player turn
			print_grid(table_display)
			column = input("Which column would you like to choose?  ")
			token_valid = 0
			while token_valid == 0:
				try:
					column = int(column)
					if 0 <= column <= 6:
						token_placed = input_token(column,player_token)
						if token_placed == 1:
							token_valid = 1
							player_turn = 0
						else:
							column = input("The column appears to be full. Please pick another:  ")
					else:
						column = input("That is not a valid column. Please try again:  ")
				except ValueError:
					column = input("That does not appear to be a valid input. Please try again:  ")
		else:
			# Computer turn
			print_grid(table_display)
			print("\nComputer's turn:")
			token_placed = 0
			while token_placed == 0:
				column = random.randint(0,6)
				token_placed = input_token(column,pc_token)
			player_turn = 1
		# Check for winner or tie
		if check_winner() in (player_token, pc_token):
			bool_play = 0
			print_grid(table_display)
			if check_winner() == player_token:
				print("Player Wins!")
			else:
				print("Computer Wins!")
		elif check_tie() == 42:
			bool_play = 0
			print_grid(table_display)
			print("\nIt's a tie!")
	# Play again?
	bool_repeat = yesno("Would you like to play again?")
