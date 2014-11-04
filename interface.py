# Rush Hour
# board.py
#
# Jeroen, Wouter en Douwe
# Heuristieken, Minor Programmeren
# Universiteit van Amsterdam
#
# oktober 2014

import board

import Tkinter as tk

root = tk.Tk()

def draw():
    global frame
    frame = tk.Frame(root)
    frame.pack()

    for i,row in enumerate(board):
        for j,column in enumerate(row):
            name = str(i)+str(j)
            L = tk.Label(gameframe,text='    ',bg= "grey" if board[i][j] == None else board[i][j])
            L.grid(row=i,column=j,padx='3',pady='3')
            L.bind('<Button-1>',lambda e,i=i,j=j:on_click(i,j,e))

draw()