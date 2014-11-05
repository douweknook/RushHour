# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014


from collections import OrderedDict

# Define board dimensions
x = 6
y = 6

# Function to add car to board
def addCar(name, length, direction, coordinate):
	#TODO
	return car

# Function to move car
def moveCar(name, direction, amount):
	#TODO
	return

# Create all coordinates for the board
coordinates = {}
for row in range(x):
    for col in range(y):
             coordinates[(row,col)] = 0

# Order coordinates dictionary to form board
board = OrderedDict(sorted(coordinates.items(), key=lambda x: x[0]))

board[(0,0)] = 1
board[(0,2)] = 1
board[(0,4)] = 1
board[(2,0)] = 1
board[(3,0)] = 1

# Print out board (delete when we implement TKinter visualization?)
string = ''
for i in range(x):
	for j in range(y):
		string += str(board[(i,j)])
		string += ' '
	string += '\n'
print string

# Board representation
# 0,0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5
# - - - - - - - - - - - - - - - - - 
# 1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5
# - - - - - - - - - - - - - - - - - 
# 2,0 | 2,1 | 2,2 | 2,3 | 2,4 | 2,5
# - - - - - - - - - - - - - - - - - 
# 3,0 | 3,1 | 3,2 | 3,3 | 3,4 | 3,5
# - - - - - - - - - - - - - - - - - 
# 4,0 | 4,1 | 4,2 | 4,3 | 4,4 | 4,5
# - - - - - - - - - - - - - - - - - 
# 5,0 | 5,1 | 5,2 | 5,3 | 5,4 | 5,5