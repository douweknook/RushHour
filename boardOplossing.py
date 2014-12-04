
# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014

import copy
import Queue

# Define board dimensions
y = 6
x = 6
steps = 0

class Car(object):
	"""Class that contains a car object"""
	def __init__(self, name, length, direction, y, x):
		self.name = name
		self.length = length
		self.y = y
		self.x = x
		self.direction = direction

	def getCoordinates(self):
		# Get the coordinates (x and y) of the car object
		return self.y, self.x


class Board(object):
	"""Class that contains a board object"""
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.board = []
		for row in range(self.y):
			self.board.append([])
		    	for col in range(self.x):
		        	self.board[row].append(' ')

	def __eq__(self, other):
		return self.board == other.board



	def __hash__(self):
		return hash(self.board)

	def addCar(self, name, length, direction, y, x):
		# Add a car to the board
		car = Car(name, length, direction, y, x)
		if direction is 'h':
			for l in range(length):
				self.board[y][x + l] = car
		if direction is 'v':
			for l in range(length):
				self.board[y + l][x] = car
	
	def moveCar(self, car, amount):

		# Move car on board
		carCopy = copy.deepcopy(car)

		# remove car from board
		if car.direction is 'h':
			for l in range(car.length):
				self.board[car.y][car.x + l] = ' '
		if car.direction is 'v':
			for l in range(car.length):
				self.board[car.y + l][car.x] = ' '

	

		# update car.x/car.y
		if carCopy.direction == 'h':
			carCopy.x += amount
		if carCopy.direction == 'v':
			carCopy.y += amount

		# redraw car

		if carCopy.direction is 'h':
			for l in range(carCopy.length):
				self.board[carCopy.y][carCopy.x + l] = carCopy
		if carCopy.direction is 'v':
			for l in range(carCopy.length):
				self.board[carCopy.y + l][carCopy.x] = carCopy

	'''def remind(self):
		self.parent = board OID

'''
	def checkPossibleMoves(self):
		# Check all possible moves for current board
		movesList = []		
		carnames = []
		for row in range(y):
			for col in range(x):
				if self.board[row][col] != ' ':
					car = self.board[row][col]
					if car.name in carnames:
						continue
					else:
						carnames.append(car.name)
						if car.direction == 'h':
							for i in range(car.x-1, -1, -1): #0 is aangepast van -1
								if self.board[row][i] == ' ':	
									movesList.append([car, i-car.x])
								else:
									break
							for j in range(car.x+car.length, x):
								if self.board[row][j] == ' ':
									movesList.append([car, j-(car.x+(car.length-1))])
								else:
									break
						if car.direction == 'v':
							for i in range(car.y-1, -1, -1): #same as aboveee
								if self.board[i][col] == ' ':
									movesList.append([car, i-car.y])
								else:
									break
							for j in range(car.y+car.length, y):
								if self.board[j][col] == ' ':
									movesList.append([car, j-(car.y+(car.length-1))])
								else:
									break

		return movesList

	def copyBoard(self):
		# Make a copy of the board
		return copy.deepcopy(self)

	def checkWin(self):
		# Check if game is won
		if self.board[2][5] != ' ':
			if self.board[2][5].name == 0:
				print "	WIN!!!"
				return True
			else:
				return False
		else:
			return False

	def printBoard(self):
		# Print out board
		string = ''
		for i in range(x):
			for j in range(y):
				if self.board[i][j] != ' ':
					string += str(self.board[i][j].name)
					string += ' '
				else:
					string += 'X'
					string += ' '
			string += '\n'
		print string

	def makeString(self):
		# Print out board
		string = ''
		for i in range(x):
			for j in range(y):
				if self.board[i][j] != ' ':
					string += str(self.board[i][j].name)
				else:
					string += 'X'
		return string

board = Board(y, x)

board.addCar(0, 2, 'h', 2, 3) #Car 0 is the red car

board.addCar(1, 2, 'h', 0, 3)
board.addCar(2, 3, 'v', 0, 2)
board.addCar(3, 3, 'v', 0, 5)
board.addCar(4, 2, 'v', 4, 0)
board.addCar(5, 2, 'h', 4, 1)
board.addCar(6, 3, 'v', 3, 3)
board.addCar(7, 2, 'h', 3, 4)
#board.addCar(8, 2, 'h', 5, 4)

# Add board to Queue
q = Queue.Queue()
q.put(board)

boardCopy = board.copyBoard()

#boardCopy.board = tuple([tuple(l) for l in boardCopy.board])


boardSet = set([])
boardCopyString = boardCopy.makeString()
boardSet.add(boardCopyString)


while boardCopy.checkWin() != True:
	initialBoard = q.get()
	print "Initial Board"
	initialBoard.printBoard()

	movesList = initialBoard.checkPossibleMoves()
	#print "movesList: ", movesList
	for move in range(len(movesList)):
		#print movesList[move][0].name
		boardCopy = initialBoard.copyBoard()

		boardCopy.moveCar(movesList[move][0], movesList[move][1])
		temp = boardCopy.board
		boardCopy.board = tuple([tuple(l) for l in boardCopy.board])
		#boardCopyString = boardCopy.makeString()
		steps+=1
		if boardCopy not in boardSet:
			boardSet.add(boardCopy)
			boardCopy.board = temp
			q.put(boardCopy)
			#print boardSet
			print len(boardSet)

		"""boardCopy.board = tuple([tuple(l) for l in boardCopy.board])
		if boardCopy not in boardSet:
			boardSet.add(boardCopy)
			boardCopy.board = list([list(l) for l in boardCopy.board])
			q.put(boardCopy)

			print len(boardSet)"""
	


print steps





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