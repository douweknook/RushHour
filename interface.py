# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014

import board
import Tkinter

root = Tkinter.Tk()
root.geometry('450x450')
#master.grid_columnconfigure()

def draw():

    for i in range(board.x):
		for j in range(board.y):
			if board.board[(i,j)] == 0:
				Tkinter.Label(root, bg='grey', text='0') .grid(column=i, row=j)
			elif board.board[(i,j)] == 1:
				Tkinter.Label(root, bg='red', text='1') .grid(column=i, row=j)
			#elif board.board[(i,j)] == 2:

#for i in enumerate(board.x):
 #  for j in enumerate(board.y):
  #      L = tk.Label(frame,text='    ',bg= "grey" if board.board[(i,j)] == 0 else board.board[(i,j)])
   #     L.grid(row=i,column=j,padx='3',pady='3')

draw()
root.mainloop()