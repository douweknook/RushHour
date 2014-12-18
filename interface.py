# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014

from Tkinter import *
solution = 'Solutions/Extra/Board3newAstarsolution.txt'

def readBoardSize(self):
	file = open(self, 'r')
	boardSize = file.readlines()[0]
	file.close()
	return int(boardSize)

def readMoves(self):
	file = open(self, 'r')
	movesAmount = file.readlines()[1]
	file.close()
	return int(movesAmount)

def readConfigurations(self):
	file = open(self, 'r')
	configurationsAmount = file.readlines()[2]
	file.close()
	return int(configurationsAmount)

def readRuntime(self):
	file=open(self, 'r')
	runtimeAmount = file.readlines()[3]
	return runtimeAmount

def readSolution(self, boardSize):
	boardsList = []
	file = open(self, 'r')
	lines = file.readlines()[5:]
	board = []
	for i in range(boardSize):
		for line in lines:
			line.strip()
			row = []
			for u in line.split():
				row.append(u)
			if row:
				board.append(row)

	for i in range(0, len(board)/boardSize, boardSize):
		newboard = []
		for j in range(i, i+boardSize):
			newboard.append(board[j])
		boardsList.append(newboard)
	return boardsList

# Function to draw the board and cars
def drawBoard(self, boardSize, canvasBoard):
	colors = ['red', 'yellow', 'light blue', 'pink', 'goldenrod', 'pale green', 'green', 
				'medium sea green', 'dark orange', 'blue', 'indian red', 'olive drab', 'sandy brown', 'salmon', 
				'dark turquoise', 'rosy brown', 'maroon', 'cyan', 'deep sky blue', 'aquamarine', 'navy', 'lime green', 
				'gold', 'cyan', 'firebrick', 'sienna', 'purple', 'lime green', 'sea green', 'violet red',
				'deep pink', 'dark slate blue', 'forest green', 'orchid', 'chartreuse', 'chocolate', 'spring green', 
				'orange red', 'lawn green', 'maroon', 'darkorange', 'yellow2']
	for i in range(boardSize):
		for j in range(boardSize):
			if self[j][i] == 'X':
				boardSpace = Canvas(canvasBoard, width=70, height=70, bg="grey90")
				boardSpace.create_text(40, 40)
				boardSpace.grid(row=j, column=i, sticky=W+E+N+S)
			else:
				boardSpace = Canvas(canvasBoard, width=70, height=70, bg=colors[int(self[j][i])])
				boardSpace.create_text(40, 40, text=self[j][i])
				boardSpace.grid(row=j, column=i, sticky=W+E+N+S)

def drawSettings(self, steps, configurations, runtime, currentStep):
	returnValuesFrame = Frame(self, width=100, height=150, padx=25, pady=25)
	returnValuesFrame.grid(row=0, column=0, sticky=W)
	
	updateSteps(returnValuesFrame, steps)
	updateConfigurations(returnValuesFrame, configurations)
	updateRuntime(returnValuesFrame, runtime)
	updateCurrentStep(returnValuesFrame, currentStep)
	previousBoardButton = Button(returnValuesFrame, text='Show Previous Step', command=previousBoard).grid(row=5, column=0, pady=25)
	nextBoardButton = Button(returnValuesFrame, text='Show Next Step', command=nextBoard).grid(row=5, column=1, pady=25)


def updateSteps(self, steps):
	stepsLabel = Label(self, text='Steps:').grid(row=0, column=0, sticky=W)
	stepsValue = Label(self, text=steps).grid(row=0, column=1, sticky=W)

def updateConfigurations(self, configurations):
	configurationsLabel = Label(self, text='Configurations found:').grid(row=1, column=0, sticky=W)
	configurationsValue = Label(self, text=configurations).grid(row=1, column=1, sticky=W)

def updateRuntime(self, runtime):
	runtimeLabel = Label(self, text='Runtime:').grid(row=2, column=0, sticky=W)
	runtimeValue = Label(self, text=runtime).grid(row=2, column=1, sticky=W)

def updateCurrentStep(self, step):
	currentStepLabel = Label(self, text='Current Step:').grid(row=3, column=0, sticky=W)
	currentStepValue = Label(self, text=step).grid(row=3, column=1, sticky=W)

def nextBoard():
	global boardIndex
	global currentStep
	if boardIndex > 0:
		boardIndex -= 1
		drawBoard(boardsList[boardIndex], boardSize, canvasBoard)
		currentStep += 1
		drawSettings(canvasSettings, len(boardsList)-1, configurationsAmount, runtime, currentStep)

def previousBoard():
	global parentsAmount
	global boardIndex
	global currentStep
	if boardIndex < parentsAmount:
		boardIndex += 1
		drawBoard(boardsList[boardIndex], boardSize, canvasBoard)
		currentStep -= 1
		drawSettings(canvasSettings, len(boardsList)-1, configurationsAmount, runtime, currentStep)

boardSize = readBoardSize(solution)
movesAmount = readMoves(solution)
configurationsAmount = readConfigurations(solution)
runtime = readRuntime(solution)
boardsList = readSolution(solution, boardSize)
boardsList.reverse()

boardIndex = len(boardsList)-1
parentsAmount = len(boardsList)-1
currentStep = 0

# Create root window
root = Tk()
root.title("Rush Hour")
mainframe = Frame(root)
mainframe.grid(row=0, column=0, sticky=W+E+N+S)
canvasBoard = Canvas(mainframe)
canvasBoard.grid(row=0, column=1)
canvasSettings = Canvas(mainframe)
canvasSettings.grid(row=0, column=2)

Grid.columnconfigure(canvasBoard, 0, weight=1)
Grid.rowconfigure(canvasBoard, 0, weight=1)

drawBoard(boardsList[boardIndex], boardSize, canvasBoard)
drawSettings(canvasSettings, movesAmount-1, configurationsAmount, runtime, currentStep)

root.mainloop()