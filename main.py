from tkinter import *
from graphics import Graphics
from game import Game

root = Tk()

graphics = Graphics(root)

game = Game(graphics, root)

root.mainloop()
