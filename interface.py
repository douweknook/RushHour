# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014

import board
<<<<<<< Updated upstream
=======
from time import time, sleep

>>>>>>> Stashed changes
from Tkinter import *

# Create root window
root = Tk()
root.title("Rush Hour")
mainframe = Frame(root)
mainframe.grid(row=0, column=0, sticky=W+E+N+S)
canvasBoard = Canvas(mainframe, width=500, height=300)
canvasBoard.grid(row=0, column=0)
canvasSettings = Canvas(mainframe, width=250, height=300)
canvasSettings.grid(row=0, column=1)

Grid.columnconfigure(canvasBoard, 0, weight=1)
Grid.rowconfigure(canvasBoard, 0, weight=1)

# Function to draw the board and cars
<<<<<<< Updated upstream
def drawBoard():
=======

root = Tk()

aboard = board.board
def draw(self):

	

>>>>>>> Stashed changes
	colors = ['red', 'yellow', 'light blue', 'pink', 'goldenrod', 'lavender', 'pale green', 'blanched almond', 'green', 
				'medium sea green', 'dark orange', 'hot pink', 'thistle', 'navy', 'indian red', 'lemin chiffon', 
				'olive drab', 'sandy brown', 'salmon', 'dark turquoise', 'rosy brown', 'maroon', 'cyan', 
				'deep sky blue', 'aquamarine', 'lime green', 'misty rose']
	for i in range(6):
		for j in range(6):
			#boardSpace = Frame(canvasBoard, width=100, height=100)
			#boardSpace.grid(row=j, column=i, padx=1, pady=1, sticky=W+E+N+S)
			#boardSpace.columnconfigure(0, weight=2)
			#boardSpace.rowconfigure(0, weight=2)
			if board.board.board[j][i] == ' ':
				w = Label(canvasBoard, bg='grey', text=str(board.board.board[j][i]))
				w.grid(column=i, row=j, ipadx=25, ipady=25, padx=1, pady=1, sticky=W+E+N+S)
			else:
<<<<<<< Updated upstream
				w = Label(canvasBoard, bg=colors[board.board.board[j][i].name], text=str(board.board.board[j][i].name)) 
				w.grid(column=i, row=j, ipadx=25, ipady=25, padx=1, pady=1, sticky=W+E+N+S)

def drawSettings():
	stepsLabel = Label(canvasSettings, )

drawBoard()
root.mainloop()
=======
				w = Label(root, bg=colors[self.board[j][i].name], text=str(self.board[j][i].name)) 
				w.grid(column=i, row=j, ipadx='20', ipady='20', padx=1, pady=1, sticky=W+E+N+S)
	print ' he'
	
	for iboard in board.parents:
		aboard = iboard	
		continue

print "hoi"
root.after(1000, draw(aboard))
>>>>>>> Stashed changes

# for board in board.parents:
# 	root.after(1000, draw(board))

root.mainloop()

