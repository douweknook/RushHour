# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014

import board_astar as board
from Tkinter import *

boardIndex = len(board.parents)-1
parentsAmount = len(board.parents)
currentStep = -1

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

# Function to draw the board and cars
def drawBoard(self, canvasBoard):
	colors = ['red', 'yellow', 'light blue', 'pink', 'goldenrod', 'pale green', 'blanched almond', 'green', 
				'medium sea green', 'dark orange', 'blue', 'indian red', 'olive drab', 'sandy brown', 'salmon', 
				'dark turquoise', 'rosy brown', 'maroon', 'cyan', 'deep sky blue', 'aquamarine', 'navy', 'lime green', 
				'misty rose']
	for i in range(board.X):
		for j in range(board.Y):
			if self.board[j][i] == ' ':
				boardSpace = Canvas(canvasBoard, width=80, height=80, bg="grey90")
				boardSpace.create_text(40, 40, text=str(self.board[j][i]))
				boardSpace.grid(row=j, column=i, sticky=W+E+N+S)

				#w = Label(boardSpace, bg='grey', text=str(self.board[j][i]))
				#w.grid(row = j, column=i, padx=1, pady=1, sticky=W+E+N+S)
			else:
				boardSpace = Canvas(canvasBoard, width=80, height=80, bg=colors[self.board[j][i].name])
				boardSpace.create_text(40, 40, text=str(self.board[j][i].name))
				boardSpace.grid(row=j, column=i, sticky=W+E+N+S)
				#w = Label(boardSpace, bg=colors[self.board[j][i].name], text=str(self.board[j][i].name)) 
				#w.grid(column=i, row=j, padx=1, pady=1, sticky=W+E+N+S)

def drawSettings(self, steps, configurations, currentStep):
	returnValuesFrame = Frame(self, width=100, height=100, padx=25, pady=25)
	returnValuesFrame.grid(row=0, column=0, sticky=W)
	
	updateSteps(returnValuesFrame, steps)
	updateConfigurations(returnValuesFrame, configurations)
	updateCurrentStep(returnValuesFrame, currentStep)
	nextBoardButton = Button(returnValuesFrame, text='Show Next Step', command=nextBoard).grid(row=4, column=0, pady=25)

	# selectBoardFrame = Frame(canvasSettings, width=250, height=200, padx=25, pady=25)
	# selectBoardFrame.grid(row=1, column=0, sticky=W)

	# #MODES: text, mode
	# MODES = [("6x6 board 1", "1"),
	# 		("6x6 board 2", "2"),
	# 		("6x6 board 3", "3"),
	# 		("9x9 board 1", "4"),
	# 		("9x9 board 2", "5"),
	# 		("9x9 board 3", "6"),
	# 		("12x12 board", "7")]

	# v = IntVar()
	# v.set(1) # initializing the choice

	# for text, mode in MODES:
	# 	boardOption = Radiobutton(selectBoardFrame, text=text, variable=v, value=mode, command=printout)
	# 	boardOption.grid(row=mode, column=0, sticky=W)


def updateSteps(self, steps):
	stepsLabel = Label(self, text='Steps:').grid(row=0, column=0, sticky=W)
	stepsValue = Label(self, text=steps).grid(row=0, column=1, sticky=W)

def updateConfigurations(self, configurations):
	configurationsLabel = Label(self, text='Configurations found:').grid(row=1, column=0, sticky=W)
	configurationsValue = Label(self, text=configurations).grid(row=1, column=1, sticky=W)

def updateCurrentStep(self, step):
	currentStepLabel = Label(self, text='Current Step:').grid(row=2, column=0, sticky=W)
	currentStepValue = Label(self, text=step).grid(row=2, column=1, sticky=W)

def noMoreSteps(self):
	noMoreStepsLabel = Label(self, text="No more steps!").grid(row=3, column=0, sticky=W, padx=25)

def nextBoard():
	global parentsAmount
	global boardIndex
	global currentStep
	if parentsAmount != 0:
		drawBoard(board.parents[boardIndex], canvasBoard)
		boardIndex -= 1
		parentsAmount -= 1
		currentStep += 1
		drawSettings(canvasSettings, len(board.parents)-1, len(board.boardSet), currentStep)
	else:
		noMoreSteps(canvasSettings)

#drawBoard(board.initialBoard, canvasBoard)
drawSettings(canvasSettings, len(board.parents)-1, len(board.boardSet), currentStep)

root.mainloop()