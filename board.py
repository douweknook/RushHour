
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

#import interface


# Define board dimensions
Y = 9
X = 9
xWin = 8
yWin = 4
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
		#print x
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
			if self.board[yWin][xWin].name == '00':
				global isFinished
				isFinished = True 
				print "WIN!"
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
					string += 'XX'
					string += ' '
			string += '\n'
		print string

def animate(board):
	import interface
	interface.teken()

board = Board(Y, X)

# # Board 1
# board.addCar(0, 2, 'h', 2, 3) #Car 0 is the red car
# board.addCar(1, 2, 'h', 0, 3)
# board.addCar(2, 3, 'v', 0, 2)
# board.addCar(3, 3, 'v', 0, 5)
# board.addCar(4, 2, 'v', 4, 0)
# board.addCar(5, 2, 'h', 4, 1)
# board.addCar(6, 3, 'v', 3, 3)
# board.addCar(7, 2, 'h', 3, 4)
# board.addCar(8, 2, 'h', 5, 4)


# # Board 2

# board.addCar(0, 2, 'h', 2, 2)
# board.addCar(1, 2, 'h', 0, 2)
# board.addCar(2, 2, 'h', 0, 4)
# board.addCar(3, 2, 'h', 1, 1)
# board.addCar(4, 2, 'h', 1, 3)
# board.addCar(5, 2, 'v', 2, 4)
# board.addCar(6, 3, 'v', 1, 5)
# board.addCar(7, 2, 'h', 3, 0)
# board.addCar(8, 2, 'h', 3, 2)

# board.addCar(9, 2, 'v', 4, 0)
# board.addCar(10, 2, 'v', 4, 3)
# board.addCar(11, 2, 'h', 4, 4)
# board.addCar(12, 2, 'h', 5, 4)

# # Board 3
# board.addCar(0, 2, 'h', 2, 0)
# board.addCar(1, 2, 'h', 0, 1)
# board.addCar(2, 3, 'h', 0, 3)
# board.addCar(3, 2, 'h', 1, 1)
# board.addCar(4, 2, 'v', 1, 3)
# board.addCar(5, 2, 'h', 1, 4)
# board.addCar(6, 2, 'v', 2, 2)
# board.addCar(7, 2, 'v', 2, 5)
# board.addCar(8, 2, 'h', 3, 0)
# board.addCar(9, 2, 'h', 3, 3)
# board.addCar(10, 2, 'v', 4, 0)
# board.addCar(11, 2, 'v', 4, 2)
# board.addCar(12, 2, 'h', 4, 4)

# # Board 4
# board.addCar('00', 2, 'h', 4, 1)#redcar
# board.addCar('01', 2, 'v', 0, 0)
# board.addCar('02', 3, 'h', 0, 1)
# board.addCar('03', 3, 'v', 0, 5)
# board.addCar('04', 3, 'h', 1, 6)
# board.addCar('05', 3, 'v', 1, 3)
# board.addCar('06', 3, 'v', 2, 8)
# board.addCar('07', 2, 'h', 3, 0)
# board.addCar('08', 3, 'h', 3, 5)
# board.addCar('09', 2, 'v', 4, 0)
# board.addCar('10', 2, 'v', 4, 3)
# board.addCar('11', 3, 'v', 5, 2)
# board.addCar('12', 3, 'h', 5, 5)
# board.addCar('13', 3, 'v', 5, 8)
# board.addCar('14', 2, 'h', 6, 0)
# board.addCar('15', 2, 'v', 6, 3)
# board.addCar('16', 2, 'h', 6, 4)
# board.addCar('17', 2, 'v', 7, 0)
# board.addCar('18', 2, 'v', 7, 4)
# board.addCar('19', 3, 'h', 8, 1)
# board.addCar('20', 2, 'h', 8, 5)
# board.addCar('21', 2, 'h', 8, 7)


# # Board 5
# board.addCar('00', 2, 'h', 4, 6)
# board.addCar('01', 3, 'h', 0, 0)
# board.addCar('02', 3, 'v', 0, 3)
# board.addCar('03', 2, 'v', 0, 5)
# board.addCar('04', 2, 'v', 0, 6)
# board.addCar('05', 2, 'h', 1, 7)
# board.addCar('06', 2, 'h', 2, 4)
# board.addCar('07', 2, 'v', 2, 6)
# board.addCar('08', 2, 'h', 3, 4)
# board.addCar('09', 2, 'h', 3, 7)
# board.addCar('10', 3, 'h', 4, 2)
# board.addCar('11', 3, 'v', 4, 5)
# board.addCar('12', 3, 'v', 4, 8)
# board.addCar('13', 2, 'v', 5, 0)
# board.addCar('14', 2, 'v', 5, 2)
# board.addCar('15', 2, 'h', 6, 3)
# board.addCar('16', 2, 'h', 6, 6)
# board.addCar('17', 2, 'v', 7, 0)
# board.addCar('18', 2, 'v', 7, 1)
# board.addCar('19', 2, 'h', 7, 2)
# board.addCar('20', 2, 'h', 8, 2)
# board.addCar('21', 2, 'v', 7, 4)
# board.addCar('22', 3, 'h', 7, 5)
# board.addCar('23', 2, 'v', 7, 8)

#board6
board.addCar('00', 2, 'h', 4, 0)#redcar
board.addCar('01', 2, 'h', 0, 0)
board.addCar('02', 2, 'h', 0, 2)
board.addCar('03', 2, 'v', 0, 4)
board.addCar('04', 2, 'v', 0, 7)

board.addCar('05', 2, 'v', 1, 1)

board.addCar('06', 3, 'h', 1, 1)
board.addCar('07', 2, 'h', 1, 5)
board.addCar('08', 2, 'h', 2, 2)
board.addCar('09', 2, 'v', 2, 4)
board.addCar('10', 2, 'v', 2, 5)#lichtblauwe auto

board.addCar('11', 2, 'h', 2, 7)
board.addCar('12', 2, 'v', 3, 2)
board.addCar('13', 3, 'v', 3, 3)
board.addCar('14', 3, 'h', 3, 6)
board.addCar('15', 2, 'v', 5, 1)
board.addCar('16', 2, 'h', 5, 4)
board.addCar('17', 2, 'h', 5, 6)
board.addCar('18', 3, 'v', 5, 8)
board.addCar('19', 3, 'v', 6, 0)
board.addCar('20', 2, 'h', 6, 2)
board.addCar('21', 3, 'v', 6, 4)
board.addCar('22', 3, 'h', 6, 5)
board.addCar('23', 2, 'h', 7, 2)
board.addCar('24', 2, 'h', 7, 5)
board.addCar('25', 3, 'h', 8, 1)

# #board7
# board.addCar('00', 2, 'h', 5, 2)#redcar
# board.addCar('01', 2, 'v', 0, 0)
# board.addCar('02', 2, 'v', 0, 6)
# board.addCar('03', 3, 'h', 0, 7)
# board.addCar('04', 2, 'h', 0, 10)
# board.addCar('05', 2, 'v', 1, 5)
# board.addCar('06', 2, 'v', 1, 10)
# board.addCar('07', 2, 'v', 1, 11)
# board.addCar('08', 3, 'h', 2, 0)
# board.addCar('09', 2, 'h', 2, 3)
# board.addCar('10', 3, 'v', 2, 6)
# board.addCar('11', 2, 'h', 2, 7)
# board.addCar('12', 3, 'v', 3, 0)#paarse waggie
# board.addCar('13', 3, 'v', 3, 1)
# board.addCar('14', 2, 'v', 3, 5)
# board.addCar('15', 2, 'h', 3, 7)
# board.addCar('16', 2, 'h', 3, 9)
# board.addCar('17', 3, 'h', 4, 2)
# board.addCar('18', 3, 'h', 4, 7)
# board.addCar('19', 2, 'v', 5, 4)#oranje waggie naast redcar
# board.addCar('20', 2, 'v', 5, 5)
# board.addCar('21', 3, 'h', 6, 0)
# board.addCar('22', 2, 'v', 6, 3)
# board.addCar('23', 3, 'v', 6, 6)#kern waggie
# board.addCar('24', 2, 'v', 6, 7)
# board.addCar('25', 2, 'v', 6, 9)
# board.addCar('26', 2, 'h', 6, 10)
# board.addCar('27', 3, 'h', 7, 0)
# board.addCar('28', 2, 'h', 7, 4)
# board.addCar('29', 2, 'h', 7, 10)
# board.addCar('30', 2, 'h', 8, 0)
# board.addCar('31', 2, 'v', 8, 2)
# board.addCar('32', 3, 'h', 8, 3)
# board.addCar('33', 3, 'h', 8, 7)
# board.addCar('34', 2, 'v', 8, 11)
# board.addCar('35', 3, 'h', 9, 3)
# board.addCar('36', 3, 'v', 9, 6)#grijze waggie onder kern waggie
# board.addCar('37', 2, 'h', 9, 8)
# board.addCar('38', 3, 'v', 9, 10)
# board.addCar('39', 2, 'v', 10, 9)
# board.addCar('40', 2, 'v', 10, 11)
# board.addCar('41', 2, 'h', 11, 1)
# board.addCar('42', 3, 'h', 11, 3)
# board.addCar('43', 2, 'h', 11, 7)

board.board = tuple([tuple(l) for l in board.board])

q = Queue.Queue()
q.put(board)
boardSet = set([])
boardSet.add(board)


board.printBoard()
#steps = 0
parents = []


while True:
#for i in range(100000):

	initialBoard = q.get()
	#print "loop done"
	initialBoard.printBoard()
	#interface.draw(initialBoard)
	initialBoard.checkBoard()
	if isFinished:

		print "Win!"
		#initialBoard.printBoard()
		
		parentBoard = initialBoard
		while parentBoard != None:

			#parentBoard.printBoard()
			#interface.draw(parentBoard)
			parents.insert(0, parentBoard)
			parentBoard = parentBoard.parent
			
			#interface.draw(board)
		break


for board in parents:
	board.printBoard()

print len(parents)



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
