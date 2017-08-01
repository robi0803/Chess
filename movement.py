try:
	from tkinter import *
except ImportError:
	from Tkinter import *
from globals import K


class Movement():

	def __init__(self, canvas, position):

		# globals
		self.k = K()

		# canvas from graphics class
		self.canvas = canvas

		# position object from game class
		self.position = position



	def drag(self, event, data):
		'''
		Allows user to drag piece held in game.data. Called every frame a mouse movement
		event occurs.

		@param
			event: Tkinter event
			data: game.data, contains piece identifier, piece locaiton, and mouse location

		@post
			The movement for the frame has been calculated and is passed into move().
		'''

		change = self.getMovement(event, data)
		self.move(data, change[0], change[1])




	def move(self, data, dx, dy):
		'''
		@param
			data: gamme.data, contains piece identifier
			dx: distance to move in x direction
			dy: distance to move in y direction

		@post
			The piece in game.data is moved dx and dy from it's original position.
		'''

		self.canvas.move(data["piece"], dx, dy)



	def getMovement(self, event, data):
		'''
		Finds how much a piece should be moved each frame.

		@param
			event: Tkinter event, used to find mouse position
			data: game.data, contains mouse and piece position.

		@return
			A tuple containing the distance to be moved.
		'''

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
		'''
		@param
			data: game.data, contains piece position.

		@post
			The movement needed to move to the piece in game.data to the center of
			a tile is calculated and passed into move()
		'''

		pos = self.position.getPosition(data["px"], data["py"])

		dx = self.k.space * pos[0] - data["px"]
		dy = self.k.space * pos[1] - data["py"]

		self.move(data, dx, dy)



	def reset(self, data):
		'''
		@param
			data: game.data, contains image position.

		@post
			The movement needed to move the piece in game.data to its original position
			is calculated and passed into move().
		'''

		dx = self.k.space * self.position.originalPosition[0] - data["px"]
		dy = self.k.space * self.position.originalPosition[1] - data["py"]

		self.move(data, dx, dy)



	def push(self, data):
		'''
		@param
			data: game.data, contains image position.

		@post
			The movement needed to keep the piece in game.data inside the window
			is calculated and passed into move().
		'''

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
