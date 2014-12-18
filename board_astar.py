
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
Y = 6
X = 6

# Define winning conditions
xWin = X-1
yWin = (Y-1)/2
isFinished = False

class Car(object):
	"""Class that contains a car object which contains parameters name, length and direction"""
	def __init__(self, name, length, direction):
		self.name = name
		self.length = length
		self.direction = direction

class Board(object):
	"""Class that contains a board object which contains parameters X, Y, parent and board"""
	def __init__(self, y, x):
		self.y = Y
		self.x = X
		self.parent = None
		self.board = []
		self.value = 0
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
		car = Car(name, length, direction)
		if direction is 'h':
			for l in range(length):
				self.board[y][x + l] = car
		if direction is 'v':
			for l in range(length):
				self.board[y + l][x] = car

	def checkBoard(self):
		# check board for cars
		carnames = set([])
		for row in range(Y):
			for col in range(X):
				if self.board[row][col] != ' ':
					car = self.board[row][col]
					if car.name not in carnames:
						carnames.add(car.name)
						if car.direction == 'h':
							if self.checkMoveHorizontal(car, row, col, self):
								return True
						else: #direction == 'v'
							if self.checkMoveVertical(car, row, col, self):
								return True

	def checkMoveHorizontal(self, car, row, col, parent):
		# check moves for found car (if direction is horizontal)
		for i in range(col-1, -1, -1):
			if self.board[row][i] == ' ':
				if i == col-1:
					boardCopy = self.moveCarHorizontal('left', car.length, row, i, parent)
					boardCopy.addToQueue()
				else:
					boardCopy = boardCopy.moveCarHorizontal('left', car.length, row, i, parent)
					boardCopy.addToQueue()
			else:
				break
		for j in range(col+car.length, X):
			if self.board[row][j] == ' ':
				if j == col+car.length:
					boardCopy = self.moveCarHorizontal('right', car.length, row, j, parent)
					boardCopy.addToQueue()
				else:
					boardCopy = boardCopy.moveCarHorizontal('right', car.length, row, j, parent)
					boardCopy.addToQueue()
			else:
				break

	def checkMoveVertical(self, car, row, col, parent):
		# check moves for found car (if direction is vertical)
		for i in range(row-1, -1, -1):
			if self.board[i][col] == ' ':
				if i == row-1:
					boardCopy = self.moveCarVertical('up', car.length, i, i+car.length, col, parent)	
				else:
					boardCopy = boardCopy.moveCarVertical('up', car.length, i, i+car.length, col, parent)
				
				if boardCopy.addToQueue():
					return True
			else:
				break
		for j in range(row+car.length, Y):
			if self.board[j][col] == ' ':
				if j == row+car.length:
					boardCopy = self.moveCarVertical('down', car.length, j, j-car.length, col, parent)
				else:
					boardCopy = boardCopy.moveCarVertical('down', car.length, j, j-car.length, col, parent)
				if boardCopy.addToQueue():
					return True
			else:
				break

	def moveCarHorizontal(self, direction, length, y, x, parent):
		# Create copy of board with horizontal move made
		tuple2 = []
		L = range(X)
		if direction == 'left':
			L[x+length] = x
			L[x] = x+length
		else:
			L[x-length] = x
			L[x] = x-length
		for i in L:
			tuple2.append(self.board[y][i])
		tuple2 = tuple(tuple2)
		boardCopy = copy.copy(self)
		boardCopy.parent = parent
		boardCopy.board = []
		for i in range(X):
			if i != y:
				boardCopy.board.append(self.board[i])
			else:
				boardCopy.board.append(tuple2)
		boardCopy.board = tuple(boardCopy.board)
		return boardCopy

	def moveCarVertical(self, direction, length, y1, y2, x, parent):
		# Create copy of board with vertical move made
		tuple3 = []
		tuple4 = []
		L = range(Y)
		for i in L:
			if i == x:
				tuple3.append(self.board[y2][i])
				tuple4.append(' ')
			else:
				tuple3.append(self.board[y1][i])
				tuple4.append(self.board[y2][i])
		tuple3 = tuple(tuple3)
		tuple4 = tuple(tuple4)
		boardCopy = copy.copy(self)
		boardCopy.parent = parent
		boardCopy.board = []
		for i in range(Y):
			if i == y1:
				boardCopy.board.append(tuple3)
			elif i == y2:
				boardCopy.board.append(tuple4)
			else:
				boardCopy.board.append(self.board[i])
		boardCopy.board = tuple(boardCopy.board)
		return boardCopy


	def addToQueue(self):
		# add copy of board to Queue, if unique copy
		if self not in boardSet:
			boardSet.add(self)
			if self.checkWin():
				return True
			self.valueBoard()
			q.put((self.value, self))


	def checkWin(self):
		# Check if game is won
		if self.board[yWin][xWin] != ' ':
			if self.board[yWin][xWin].name == 0:
				global isFinished
				isFinished = True
				parents.append(self)
				return True

	def printBoard(self):
		# Print out board
		string = ''
		for i in range(X):
			for j in range(Y):
				if self.board[i][j] != ' ':
					string += str(self.board[i][j].name)
					string += ' '
				else:
					string += 'X'
					string += ' '
			string += '\n'
		print string

	def valueBoard(self):
		value1 = 0
		value2 = 0
		value3 = 0
		# Add 1 to score for every parent (previous step) of current board
		parents = []
		parentBoard = self.parent
		while parentBoard != None:
			parents.append(parentBoard)
			parentBoard = parentBoard.parent
		value2 = len(parents)

		# Add 1 to score for every car blocking the red car
		for i in range(X-1, -1, -1):
			if self.board[yWin][i] != ' ':
				if self.board[yWin][i].name == 0:
					break
				else:
					value1 += 1
					# If the spot above/below blocked spot is not empty +1 to score
					if self.board[yWin+1][i] != ' ' or self.board[yWin-1][i] != ' ':
						value3 += 1
		# Add 1 to score for every car blocking as car blocking the red car?


		self.value = value1+value2+value3



board = Board(Y, X)

# Board 2
board.addCar(0, 2, 'h', 2, 2)
board.addCar(1, 2, 'h', 0, 2)
board.addCar(2, 2, 'h', 0, 4)
board.addCar(3, 2, 'h', 1, 1)
board.addCar(4, 2, 'h', 1, 3)
board.addCar(5, 2, 'v', 2, 4)
board.addCar(6, 3, 'v', 1, 5)
board.addCar(7, 2, 'h', 3, 0)
board.addCar(8, 2, 'h', 3, 2)
board.addCar(9, 2, 'v', 4, 0)
board.addCar(10, 2, 'v', 4, 3)
board.addCar(11, 2, 'h', 4, 4)
board.addCar(12, 2, 'h', 5, 4)

board.board = tuple([tuple(l) for l in board.board])

q = Queue.PriorityQueue()
q.put((0, board))
boardSet = set([])
boardSet.add(board)


parents = []

while True:
	initialBoard = q.get()
	initialBoard[1].checkBoard()
	if isFinished:
		parentBoard = initialBoard[1]
		while parentBoard != None:
			parents.append(parentBoard)
			parentBoard = parentBoard.parent
		break


for board in reversed(parents):
	board.printBoard()

print "Moves:", len(parents)
print "Set Length:", len(boardSet)


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
