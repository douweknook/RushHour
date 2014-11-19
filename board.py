import copy
import Queue

# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014


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

	def getCoordinates(self):
		return self.y, self.x

class Board(object):
	"""docstring for Board"""
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.board = []
		for row in range(self.y):
			self.board.append([])
		    	for col in range(self.x):
		        	self.board[row].append(' ')

	# Function to add car to board
	def addCar(self, name, length, direction, y, x):
		car = Car(name, length, direction, y, x)
		if direction is 'h':
			for l in range(length):
				self.board[y][x + l] = car
		if direction is 'v':
			for l in range(length):
				self.board[y + l][x] = car
	

	# Function to move car
	def moveCar(self, car, amount):
		# remove car from board
		if car.direction is 'h':
			for l in range(car.length):
				self.board[car.y][car.x + l] = ' '
		if car.direction is 'v':
			for l in range(car.length):
				self.board[car.y + l][car.x] = ' '

		# update car.x/car.y
		if car.direction == 'h':
			car.x += amount
			#print car.x, amount
		if car.direction == 'v':
				car.y += amount
				#print car.y, amount

		# redraw car
		if car.direction is 'h':
			for l in range(car.length):
				self.board[car.y][car.x + l] = car
		if car.direction is 'v':
			for l in range(car.length):
				#print l
				self.board[car.y + l][car.x] = car
				print car.y+l


	def checkPossibleMoves(self):
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
							for i in range(car.x-1, -1, -1):
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
							for i in range(car.y-1, -1, -1):
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
		return copy.deepcopy(self)

	def checkWin(self):
		if self.board[2][5].name == 0:
			return True
		else:
			return False


board = Board(y, x)

board.addCar(0, 2, 'h', 2, 3) #Car 0 is the red car
board.addCar(1, 2, 'h', 0, 3)
board.addCar(2, 3, 'v', 0, 2)
board.addCar(3, 3, 'v', 0, 5)
board.addCar(4, 2, 'v', 4, 0)
board.addCar(5, 2, 'h', 4, 1)
board.addCar(6, 3, 'v', 3, 3)
board.addCar(7, 2, 'h', 3, 4)
board.addCar(8, 2, 'h', 5, 4)


# Add board to Queue
q = Queue.Queue()
q.put(board)

board.board = tuple(board.board)
boardHash = hash(board)

boardSet = set([])
boardSet.add(boardHash)


while board.checkWin() != True:
	board = q.get()
	#board.board = list(board.board)
	movesList = board.checkPossibleMoves()
	print movesList
	for move in range(len(movesList)):
		#print movesList[move][0].name
		boardCopy = board.copyBoard()
		#print boardCopy
		boardCopy.moveCar(movesList[move][0], movesList[move][1])
		#print move
		boardCopy.board = tuple(boardCopy.board)
		boardHash = hash(boardCopy)
		if boardHash not in boardSet:
			#print boardSet
			boardSet.add(boardHash)
			#boardCopy.board = list(boardCopy.board)
			q.put(boardCopy)
	
'''
#LOOP until win == true
#load board from Queue
#CheckPossibleMoves
#Loop over MovesList
	#copyBoard
	#moveCar
	#If duplicate = false
		#add to Queue
'''

#board.checkWin()

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