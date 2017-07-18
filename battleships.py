import random
import math

#GLOBAL VARIABLES
global cardinals
global dir_text
global directions

global blanks
blanks = ("·","?")
global YES
YES = ('y','Y')
global NO
NO = ('n','N')
#DICTIONARIES
numpad = {
	'dir_text' : {
		8 : "Up (8)",
		6 : "Right (6)",
		2 : "Down (2)",
		4 : "Left (4)"
	},
	'cardinals' : {
		8 : (0,-1),
		6 : (1,0),
		2 : (0,1),
		4 : (-1,0)
	},
	'directions' : [8,6,2,4]
}
no_numpad = {
	'dir_text' : {
		0 : "Up (0)",
		1 : "Right (1)",
		2 : "Down (2)",
		3 : "Left (3)"
	},
	'cardinals' : {
		0 : (0,-1),
		1 : (1,0),
		2 : (0,1),
		3 : (-1,0)
	},
	'directions' : [0,1,2,3]
}
#TODO - Check standard matrix notation. Maybe you i,j instead of x,y
#FIXED - When removing an element from a list while iterating along it in a FOR loop,
#		the loop will skip the next element in the list.
#BUG - size-2 ships placed on row 1 cannot be pointed up, but size-5 ships placed on row 3 can, and overlap into row 9

#NOTE - Setting a variable to be global allows a function to take its initial value from outside the def
#		To set the global variable within the def, the def must state that it is global within the def?

def set_to(old):
	new = []
	for element in old:
		new.append(element)
	return new

def yesno(question):
	while True:
		test = input(question+"(y/n): ")
		if test in YES:
			return 1
		elif test in NO:
			return 0

def print_board(board):
	print("")
	print("    0  1  2  3  4  5  6  7  8  9  ")
	print("  --------------------------------")
	for i in range(10):
		print(str(i)+" [ {}  {}  {}  {}  {}  {}  {}  {}  {}  {} ]".format(*board[i]))

def print_both():
	print("")
	print("            Player Board                          Computer Board         ")
	print("    0  1  2  3  4  5  6  7  8  9           0  1  2  3  4  5  6  7  8  9  ")
	print("  --------------------------------       --------------------------------")
	for i in range(10):
		print(str(i)+" [ {}  {}  {}  {}  {}  {}  {}  {}  {}  {} ]     ".format(*player_hide[i]),end="")
		print(str(i)+" [ {}  {}  {}  {}  {}  {}  {}  {}  {}  {} ]".format(*pc_hide[i]))

def check_valid(num):
	if len(num) != 2:
		return 1
	try:
		num = int(num)
	except ValueError:
		return 2
	return 0

def check_free(board,coords,n,d):
	# sets =[[+x,+y],...]
	# sets = [North,East,South,West]
	for i in range(1,n):
		#print("x:",coords[0] + i * cardinals[d][0])
		#print("y:",coords[1] + i * cardinals[d][1])
		if board[coords[1] + i * cardinals[d][1]][coords[0] + i * cardinals[d][0]] not in blanks:
			#print("Blocked in direction",d)
			return 0
	else:
		return 1

def check_moves(board,coords,n):
	available = set_to(directions)
	#Remove directions off board
	temp = set_to(available)
	for d in temp:
		try:
			assert coords[0] + (n-1) * cardinals[d][0] <= 9
			assert coords[0] + (n-1) * cardinals[d][0] >= 0 
			assert coords[1] + (n-1) * cardinals[d][1] <= 9
			assert coords[1] + (n-1) * cardinals[d][1] >= 0
		except AssertionError:
			available.remove(d)
			#print("Not enough space in "+str(d))

	temp = set_to(available)
	for d in temp:
		#print("Checking if blocked in "+str(d))
		try:
			assert check_free(board,coords,n,d) == 1
		except AssertionError:
			available.remove(d)
			#print("direction "+str(d)+" not free.")
	return available

def place_ship(board,coords,n,d,c):
	for i in range(n):
		board[coords[1] + i * cardinals[d][1]][coords[0] + i * cardinals[d][0]] = c

def place_random(board,n,c):
	while True:
		x = random.randint(0,9)
		y = random.randint(0,9)
		location = [x,y]
		if board[y][x] not in blanks:
			continue
		else:
			available = check_moves(board,location,n)
		if len(available) == 0:
			continue
		place_ship(board,location,n,available[random.randint(0,len(available)-1)],c)
		break
		
def place_choice(board,n,c):
	print("Placing a ship of length: "+str(n))
	print("To select a spot, input the 2-digit number corresponding to its coordinates.")
	test_int = 0
	while True:
		print_board(board)
		location = input("Where would you like to place the ship? ")

		while len(location) != 2:
			location = input("ERROR - Length NOT 2. Try Again: ")

		try:
			location = int(location)
		except ValueError:
			print("ERROR - Not a Number")
			continue

		print("Valid Input")
		x = math.floor(location / 10)
		y = location % 10
		coords = [x,y]
		print("You have chosen square "+str(x)+str(y)+".")

		#Check space is free
		if board[y][x] != '·':
			print("ERROR - chosen location not free")
			continue

		print("")
		#Check space has available moves
		available = check_moves(board,coords,n)		

		if len(available) == 0:
			print("ERROR - No directions available at this space.")
			continue

		board[y][x] = "x"
		print_board(board)

		print("Available Directions: {}".format(quote_directions(available)))
		#Recieve Input For Direction
		choice_dir = 10
		while choice_dir not in available:
			choice_dir = input("Please pick a direction: {}\n".format(quote_directions(available)))
			if choice_dir in NO:
				board[y][x] = "·"
				break
			try:
				choice_dir = int(choice_dir)
			except ValueError:
				choice_dir = 4

		if choice_dir in NO:
			continue
		break
	place_ship(board,coords,n,choice_dir,c)
	print_board(board)

def quote_directions(a):
	if len(a) == 1:
		string = dir_text[a[0]]
	elif len(a) == 2:
		string = dir_text[a[0]]+", "+dir_text[a[1]]
	elif len(a) == 3:
		string = dir_text[a[0]]+", "+dir_text[a[1]]+", "+dir_text[a[2]]
	else:
		string = dir_text[a[0]]+", "+dir_text[a[1]]+", "+dir_text[a[2]]+", "+dir_text[a[3]]
	return string

# PROGRAM START
print("Welcome to BATTLESHIPS!")
bool_play = 1
#Determine if using numpad
if yesno("Are you using a number pad?") == 1:
	dir_text = numpad['dir_text']
	cardinals = numpad['cardinals']
	directions = numpad['directions']
else:
	dir_text = no_numpad['dir_text']
	cardinals = no_numpad['cardinals']
	directions = no_numpad['directions']
#Determine dimensions of board?
#Determine number/length of ships?
#Determine number of goes per turn? - Assume 1 to start with.
#Initialising boards
player_hide = [["·"]*10 for i in range(10)]
pc_hide = [["·"]*10 for i in range(10)]
# player_display = [["."]*10 for i in range(10)]
pc_display = [["·"]*10 for i in range(10)]
#Establishing ships
ship_list = (2,3,4)
ship_icons = range(0,len(ship_list))
player_ships = []
for i in range(len(ship_list)):
	temp = [ship_icons[i]]*ship_list[i]
	player_ships.append(temp)
pc_ships = set_to(player_ships)
print(player_ships)
print(range(10))
x = range(10)
print(x)
print(x[2])
#Setting Up PC's board
for num in ship_icons:
	place_random(pc_hide,ship_list[num],num)
print_board(pc_hide)
#Setting Up Player board
for num in ship_icons:
	place_choice(player_hide,ship_list[num],num)
print_both()
#Check who starts
if yesno("Would you like to start?") == 1:
	turn = 1
else:
	turn = 0
#Start game
while bool_play == 1:
	if turn == 1:
		#Player Turn
		turn = 0
		#Pick a space
		valid_target = 1
		while valid_target != 0:
			target = input("Pick a location to attack: ")
			valid_target = check_valid(target)
			while valid_target != 0:
				print("That is not a 2-digit number!")
				target = input("Pick a location to attack: ")
				valid_target = check_valid(target)
			x = math.floor(location / 10)
			y = location % 10
			if pc_display[y][x] != ".":
				print("That space has already been targetted!")
				valid_target = 1
		#Space chosen, determine outcome
		if pc_hide[y][x] not in (".","X"):
			destroyed = pc_hide[y][x]
			
	else:
		#Computer Turn
		break



#Pick a space
#Check if it has already been chosen
	#If yes, pick another square, loop
#Check whether the spot has a ship space
	#If no, mark as a miss
	#If yes, mark as a hit
#Remove ship part from pc_ship list
	#If THAT SHIP's list has no elements, print "Ship destroyed"
