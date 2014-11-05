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

# Class Car

class Car(object):
	def __init__(self, name, length, direction, y, x):
		self.name = name
		self.length = length
		self.y = y
		self.x = x
		self.direction = direction

	def getName(self):
		return self.name

	def getDirection(self):
		return self.direction

	def getLength(self):
		return self.length

	def getCoordinates(self):
		coordinates = (self.y, self.x)
		return coordinates



# Function to add car to board
def addCar(name, length, direction, y, x):
	car = Car(name, length, direction, y, x)
	if direction is 'h':
		board[(y, x)] = car.name
		board[(y, x + 1)] = car.name
	if direction is 'v':
		board[(y, x)] = car.name
		board[(y + 1, x)] = car.name	

# Function to move car
def moveCar(name, direction, amount):
	
	return

# Create all coordinates for the board
coordinates = {}
for row in range(x):
    for col in range(y):
             coordinates[(row,col)] = 0

# Order coordinates dictionary to form board
board = OrderedDict(sorted(coordinates.items(), key=lambda x: x[0]))

addCar(1, 2, 'h', 0, 2)
addCar(2, 2, 'v', 2, 1)


# Print out board (delete when we implement TKinter visualization?)
string = ''
for i in range(x):
	for j in range(y):
		string += str(board[(i,j)])
		string += ' '
	string += '\n'
print string

print car.getName()


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