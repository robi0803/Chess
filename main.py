from Tkinter import *
from graphics import Graphics
from position import Position
from game import Game


root = Tk()

graphics = Graphics(root)

game = Game(graphics.canvas)

root.mainloop()
