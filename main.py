from Tkinter import *
from graphics import Graphics
from position import Position
from input import Input
from capture import Capture


root = Tk()

graphics = Graphics(root)

position = Position()

capture = Capture(graphics.canvas, position.board)

input = Input(graphics.canvas, position, capture)

root.mainloop()
