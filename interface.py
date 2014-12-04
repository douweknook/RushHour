# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014

import board
import random
from Tkinter import *

# Create root window
root = Tk()


colors = ['red', 'yellow', 'light blue', 'pink', 'goldenrod', 'lavender', 'pale green', 'blanched almond', 'green', 
			'medium sea green', 'dark orange', 'hot pink', 'thistle', 'navy', 'indian red', 'lemin chiffon', 
			'olive drab', 'sandy brown', 'salmon', 'dark turquoise', 'rosy brown', 'maroon', 'cyan', 
			'deep sky blue', 'aquamarine', 'lime green', 'misty rose']

# Function to draw the board and cars
def draw(self):
    	for i in range(board.x):
			for j in range(board.y):
				if self.board[j][i] == ' ':
					w = Label(root, bg='grey', text=str(self.board[j][i])) 
					w.grid(column=i, row=j, ipadx='22', ipady='20', padx=1, pady=1, sticky=W+E+N+S)
				else:
					w = Label(root, bg=colors[self.board[j][i].name], text=str(self.board[j][i].name)) 
					w.grid(column=i, row=j, ipadx='20', ipady='20', padx=1, pady=1, sticky=W+E+N+S)

for board in board.parentBoards:
	draw(board)
	
root.mainloop()