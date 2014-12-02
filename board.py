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
xWin = 5
yWin = 2

class Car(object):
	"""Class that contains a car object"""
	def __init__(self, name, length, direction):
		self.name = name
		self.length = length
		self.direction = direction

	def __hash__(self):
		return hash(self.name)

	def __eq__(self, other):
		return isinstance(other, Car) and self.name == other.name

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
		b = tuple([tuple(l) for l in self.board])
		return hash(b)

	def addCar(self, name, length, direction, y, x):
		# Add a car to the board
		car = Car(name, length, direction)
		if direction is 'h':
			for l in range(length):
				self.board[y][x + l] = car
		if direction is 'v':
			for l in range(length):
				self.board[y + l][x] = car
	
	def moveCar(self, car, amount, y, x):
		# Move car on board
		if car.direction is 'h':
			for l in range(car.length):
				self.board[y][x + l] = ' '
			x += amount			
			for l in range(car.length):
				self.board[y][x + l] = car
		else:
			for l in range(car.length):
				self.board[y + l][x] = ' '		
			y += amount	
			for l in range(car.length):
				self.board[y + l][x] = car			

	def solve(self):
		# Check all possible moves for current board	
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
							for i in range(col-1, -1, -1):
								if self.board[row][i] == ' ':	
									boardCopy = self.copyBoard()
									boardCopy.moveCar(car, i-col, row, col)
									if boardCopy not in boardSet:
										boardSet.add(boardCopy)
										if boardCopy.checkWin():
											return True
										q.put(boardCopy)
								else:
									break
							for j in range(col+car.length, x):
								if self.board[row][j] == ' ':
									boardCopy = self.copyBoard()
									boardCopy.moveCar(car, j-(col+(car.length-1)), row, col)
									if boardCopy not in boardSet:
										boardSet.add(boardCopy)
										if boardCopy.checkWin():
											return True
										q.put(boardCopy)
								else:
									break
						if car.direction == 'v':
							for i in range(row-1, -1, -1):
								if self.board[i][col] == ' ':
									boardCopy = self.copyBoard()									
									boardCopy.moveCar(car, i-row, row, col)
									if boardCopy not in boardSet:
										boardSet.add(boardCopy)
										if boardCopy.checkWin():
											return True
										q.put(boardCopy)
								else:
									break
							for j in range(row+car.length, y):
								if self.board[j][col] == ' ':
									boardCopy = self.copyBoard()
									boardCopy.moveCar(car, j-(row+(car.length-1)), row, col)
									if boardCopy not in boardSet:
										boardSet.add(boardCopy)
										if boardCopy.checkWin():
											return True
										q.put(boardCopy)
								else:
									break
		return False

	def copyBoard(self):
		# Make a copy of the board
		tempCopy = copy.deepcopy(self)
		tempCopy.parent = self
		return tempCopy

	def checkWin(self):
		# Check if game is won
		if self.board[yWin][xWin] != ' ':
			if self.board[yWin][xWin].name == 0:
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


q = Queue.Queue()
q.put(board)

boardCopy = board.copyBoard()

boardSet = set([])
boardSet.add(boardCopy)

while True:
#for i in range(10):
	initialBoard = q.get()
	print "loop done"
	if initialBoard.solve():
		initialBoard.printBoard()
		print "Win!"
		break


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