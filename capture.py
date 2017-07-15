from tkinter import *
from globals import K


class Capture():

    def __init__(self, canvas, board):

        k = K()

        self.canvas = canvas

        self.board = board



    def updateCapture(self, position, tags):

        if (len(self.board[position[0]][position[1]]) >= 2 and
           (self.board[position[0]][position[1]][0] != tags[1]) ):

            self.canvas.itemconfig(self.board[position[0]][position[1]][2], state = "hidden")
