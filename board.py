
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


	def addToQueue(self):
		# add copy of board to Queue, if unique copy
		if self not in boardSet:
			boardSet.add(self)
			if self.checkWin():
				return True
			q.put(self)


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

board = Board(Y, X)

# Board 4
board.addCar(0, 2, 'h', 4, 1)#redcar
board.addCar(1, 2, 'v', 0, 0)
board.addCar(2, 3, 'h', 0, 1)
board.addCar(3, 3, 'v', 0, 5)
board.addCar(4, 3, 'h', 1, 6)
board.addCar(5, 3, 'v', 1, 3)
board.addCar(6, 3, 'v', 2, 8)
board.addCar(7, 2, 'h', 3, 0)
board.addCar(8, 3, 'h', 3, 5)
board.addCar(9, 2, 'v', 4, 0)
board.addCar(10, 2, 'v', 4, 3)
board.addCar(11, 3, 'v', 5, 2)
board.addCar(12, 3, 'h', 5, 5)
board.addCar(13, 3, 'v', 5, 8)
board.addCar(14, 2, 'h', 6, 0)
board.addCar(15, 2, 'v', 6, 3)
board.addCar(16, 2, 'h', 6, 4)
board.addCar(17, 2, 'v', 7, 0)
board.addCar(18, 2, 'v', 7, 4)
board.addCar(19, 3, 'h', 8, 1)
board.addCar(20, 2, 'h', 8, 5)
board.addCar(21, 2, 'h', 8, 7)


board.board = tuple([tuple(l) for l in board.board])

q = Queue.Queue()
q.put(board)
boardSet = set([])
boardSet.add(board)

parents = []

while True :
	initialBoard = q.get()
	initialBoard.checkBoard()
	if isFinished:
		parentBoard = initialBoard
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
