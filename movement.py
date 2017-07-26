from tkinter import *
from globals import K


class Movement():

    def __init__(self, canvas, position):

        # globals
        self.k = K()

        # canvas from graphics class
        self.canvas = canvas

        # position object from game class
        self.position = position



    def getMovement(self, event, data):

        dx = event.x - data["mx"]
        dy = event.y - data["my"]


        if ((data["px"] <= -20 and dx < 0) or
            (data["px"] >= self.k.width - 44 and dx > 0)):
            dx = 0

        if ((data["py"] <= -20 and dy < 0) or
            (data["py"] >= self.k.height - 59 and dy > 0)):
            dy = 0

        data["mx"] = event.x
        data["my"] = event.y

        return (dx, dy)



    def snap(self, data):

        pos = self.position.getPosition(data["px"], data["py"])

        dx = self.k.space * pos[0] - data["px"]
        dy = self.k.space * pos[1] - data["py"]

        self.move(data, dx, dy)



    def reset(self, data):

        dx = self.k.space * self.position.originalPosition[0] - data["px"]
        dy = self.k.space * self.position.originalPosition[1] - data["py"]

        self.move(data, dx, dy)



    def push(self, data):

        dx = dy = 0

        if (data["px"] < 0):
            dx = 10
        if (data["px"] >= self.k.width - 30):
            dx = -10
        if (data["py"] < 0):
            dy = 10
        if (data["py"] > self.k.height - 30):
            dy = -10

        self.move(data, dx, dy)



    def move(self, data, dx, dy):

       self.canvas.move(data["piece"], dx, dy)
