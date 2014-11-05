# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014

import board
from Tkinter import *

# Create root window
root = Tk()

# Function to draw the board and cars
def draw():
		

    	for i in range(board.x):
			for j in range(board.y):
				if board.board[(i,j)] == 0:
					w = Label(root, bg='grey', text=str(board.board[(i,j)])) 
					w.grid(column=i, row=j, ipadx='20', ipady='15')
				elif board.board[(i,j)] == 1:
					w = Label(root, bg='red', text=str(board.board[(i,j)])) 
					w.grid(column=i, row=j, ipadx='20', ipady='15')
				elif board.board[(i,j)] == 2:
					w = Label(root, bg='blue', text=str(board.board[(i,j)])) 
					w.grid(column=i, row=j, ipadx='20', ipady='15')

draw()
root.mainloop()