
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
import cProfile

# Define board dimensions
y = 6
x = 6
xWin = 5
yWin = 2
isFinished = False

class Car(object):
	"""Class that contains a car object"""
	def __init__(self, name, length, direction):
		self.name = name
		self.length = length
		self.direction = direction

class Board(object):
	"""Class that contains a board object"""
	def __init__(self, y, x):
		self.y = y
		self.x = x
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
	

	def moveCarHorizontal(self, direction, length, y, x):
		# Create copy of board with horizontal move made
		tuple2 = []
		L = range(6)
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
		boardCopy.parent = self
		boardCopy.board = []
		for i in range(6):
			if i != y:
				boardCopy.board.append(self.board[i])
			else:
				boardCopy.board.append(tuple2)
		boardCopy.board = tuple(boardCopy.board)
		return boardCopy

	def moveCarVertical(self, direction, length, y1, y2, x):
		# Create copy of board with vertical move made
		tuple3 = []
		tuple4 = []
		L = range(6)
		for i in L:
			if i == x:
				tuple3.append(self.board[y2][i])
				tuple4.append(self.board[y1][i])
			else:
				tuple3.append(self.board[y1][i])
				tuple4.append(self.board[y2][i])
		tuple3 = tuple(tuple3)
		tuple4 = tuple(tuple4)

		boardCopy = copy.copy(self)
		boardCopy.parent = self
		boardCopy.board = []
		for i in range(6):
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
		for row in range(y):
			for col in range(x):
				if self.board[row][col] != ' ':
					car = self.board[row][col]
					if car.name not in carnames:
						carnames.add(car.name)
						if car.direction == 'h':
							if self.checkMoveHorizontal(car, row, col):
								return True
						else: #direction == 'v'
							if self.checkMoveVertical(car, row, col):
								return True

	def checkMoveHorizontal(self, car, row, col):
		# check moves for found car (if direction is horizontal)
		for i in range(col-1, -1, -1):
			if self.board[row][i] == ' ':
				if i == col-1:
					#print "MOVE LEFT 1"
					boardCopy = self.moveCarHorizontal('left', car.length, row, i)
					boardCopy.addToQueue()
				else:
					#print "MOVE LEFT 2"
					boardCopy = boardCopy.moveCarHorizontal('left', car.length, row, i)
					boardCopy.addToQueue()
			else:
				break
		for j in range(col+car.length, x):
			if self.board[row][j] == ' ':
				if j == col+car.length:
					#print "MOVE RIGHT 1"
					boardCopy = self.moveCarHorizontal('right', car.length, row, j)
					boardCopy.addToQueue()
				else:
					#print "MOVE RIGHT 2"
					boardCopy = boardCopy.moveCarHorizontal('right', car.length, row, j)
					boardCopy.addToQueue()
			else:
				break

	def checkMoveVertical(self, car, row, col):
		# check moves for found car (if direction is vertical)
		for i in range(row-1, -1, -1):
			if self.board[i][col] == ' ':
				if i == row-1:
					#print "MOVE UP 1"
					boardCopy = self.moveCarVertical('up', car.length, i, i+car.length, col)	
				else:
					#print "MOVE UP 2"
					boardCopy = boardCopy.moveCarVertical('up', car.length, i, i+car.length, col)
				
				if boardCopy.addToQueue():
					return True
			else:
				break
		for j in range(row+car.length, y):
			if self.board[j][col] == ' ':
				if j == row+car.length:
					#print "MOVE DOWN 1"
					boardCopy = self.moveCarVertical('down', car.length, j, j-car.length, col)
				else:
					#print "MOVE DOWN 2"
					boardCopy = boardCopy.moveCarVertical('down', car.length, j, j-car.length, col)
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
				print "WIN!"
				return True

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

board = Board(y, x)

'''
board.addCar(0, 2, 'h', 2, 3) #Car 0 is the red car
board.addCar(1, 2, 'h', 0, 3)
board.addCar(2, 3, 'v', 0, 2)
board.addCar(3, 3, 'v', 0, 5)
board.addCar(4, 2, 'v', 4, 0)
board.addCar(5, 2, 'h', 4, 1)
board.addCar(6, 3, 'v', 3, 3)
board.addCar(7, 2, 'h', 3, 4)
board.addCar(8, 2, 'h', 5, 4)

'''
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
board.addCar(12, 2, 'h', 5,4)
 


board.board = tuple([tuple(l) for l in board.board])

q = Queue.Queue()
q.put(board)
boardSet = set([])
boardSet.add(board)

board.printBoard()
steps = 0
while True:
#for i in range(1000):

	initialBoard = q.get()
	print "loop done"
	initialBoard.checkBoard()
	if isFinished:
		print "Win!"
		#initialBoard.printBoard()
		
		parentBoard = initialBoard
		while parentBoard != None:
			parentBoard.printBoard()
			steps += 1
			parentBoard = parentBoard.parent
		print steps
		break

#print len(boardSet)


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
