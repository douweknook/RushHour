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
y = 6
x = 6

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
		return self.y, self.x


cars = []

# Function to add car to board
def addCar(name, length, direction, y, x):
	car = Car(name, length, direction, y, x)
	cars.append(car)
	if direction is 'h':
		for l in range(length):
			board[(y, x + l)] = car.name
	if direction is 'v':
		for l in range(length):
			board[(y + l, x)] = car.name
	return cars	

# Function to move car
def moveCar(name, amount):
	if amount >= 0:
		for i in range(0, amount):
			for car in cars:
				if name == car.getName():
					var = car
					board[(car.y, car.x)] = ' '
					cars.remove(car)

			if var.getDirection() == 'h':
				var.x += 1
				addCar(var.name, var.length, var.direction, var.y, var.x)
			if var.getDirection() == 'v':
				var.y += 1
				addCar(var.name, var.length, var.direction, var.y, var.x)

	elif amount < 0:
		for i in range(0, amount, -1):
			for car in cars:
				if name == car.getName():
					var = car
					board[(car.y, car.x+car.length-1)] = ' '
					cars.remove(car)

			if var.getDirection() == 'h':
				var.x -= 1
				addCar(var.name, var.length, var.direction, var.y, var.x)
			if var.getDirection() == 'v':
				var.y -= 1
				addCar(var.name, var.length, var.direction, var.y, var.x)


	return

# Create all coordinates for the board
coordinates = {}
for row in range(y):
    for col in range(x):
             coordinates[(row,col)] = ' '

# Order coordinates dictionary to form board
board = OrderedDict(sorted(coordinates.items(), key=lambda x: x[0]))

# Car(name, length, direction, y, x)
addCar(0, 2, 'h', 2, 3) #Red car
addCar(1, 2, 'h', 0, 3)
addCar(2, 3, 'v', 0, 2)
addCar(3, 3, 'v', 0, 5)
addCar(4, 2, 'v', 4, 0)
addCar(5, 2, 'h', 4, 1)
addCar(6, 3, 'v', 3, 3)
addCar(7, 2, 'h', 3, 4)
addCar(8, 2, 'h', 5, 4)

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