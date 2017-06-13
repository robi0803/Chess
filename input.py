from Tkinter import *
from globals import K


class Input():

	def __init__(self, canvas, position, capture):

		# global variables
		self.k = K()

		# Tkinter object, draws images
		self.canvas = canvas

		# handles information for capture
		self.capture = capture

		# contains board and functions pertaining to position
		self.position = position
		self.position.update(self.canvas)

		# current piece identifier, location, and mouse location
		self.movementData = { "piece" : None, "px" : 0, "py" : 0, "mx" : 0 , "my" : 0}

		#location of piece before moving
		self.originalPosition = None

		# binds events to functions, allows user to click and drag
		self.canvas.tag_bind("token", "<ButtonPress-1>", self.mouseClick)
		self.canvas.tag_bind("token", "<B1-Motion>", self.mouseMove)
		self.canvas.tag_bind("token", "<ButtonRelease-1>", self.mouseRelease)

		#boxes used in animation
		self.green = self.canvas.find_withtag("green")
		self.red = self.canvas.find_withtag("red")
		self.yellow = self.canvas.find_withtag("yellow")




	def mouseClick(self, event):

		'''
		Called when a user generated mouse click event occurs.

		@param
			event: Mouse click event generated from Tkinter. Function is binded with
				   event and is called when this event occurs.

		@post
			movementData and originalPosition are initialized to the piece closest
			to the mouse click event
		'''

		self.movementData["piece"] = self.canvas.find_closest(event.x, event.y)
		self.movementData["mx"] = event.x
		self.movementData["my"] = event.y

		self.updateCoords()
		self.originalPosition = self.getPosition()



	def mouseMove(self, event):

		'''
		Called when a user generated mouse movement event occurs. Does nothing
		unless data members have been initialized by mouseClick

		@param
			event: Mouse movement event generated from Tkinter. Function is binded with
				   event and is called when this event occurs.

		@post
			The corresponding piece is moved and animate() has been called
		'''

		change = self.getMovement(event)
		self.move(change[0], change[1])

		try:
			self.animate()
		except TypeError:
			self.reset()



	def mouseRelease(self, event):

		'''
		Called when a user generated mouse up event occurs. Places piece if in a
		legal position and clears data members.

		@param
			event:
				Mouse release event generated from Tkinter. Function is binded with
				event and is called when this event occurs.

		@post
			If in a legal position, piece is moved to the center of the tile, else
			piece is moved to original position. movementData and animation are
			cleared.
		'''

		if (self.canMove()):
			self.snap()
			self.capture.updateCapture(self.getPosition(),
								 	   self.canvas.gettags(self.movementData["piece"]))
			self.position.update(self.canvas)
		else:
			self.reset()

		self.clearAnimation()
		self.movementData["piece"] = NONE
		self.movementData["mx"] = 0
		self.movementData["my"] = 0



	def getMovement(self, event):

		dx = event.x - self.movementData["mx"]
		dy = event.y - self.movementData["my"]

		if ((self.movementData["px"] <= -20 and dx < 0) or
			(self.movementData["px"] >= self.k.width - 44 and dx > 0) ):
			 	dx = 0

		if ((self.movementData["py"] <= -20 and dy < 0) or
			(self.movementData["py"] >= self.k.height - 59 and dy > 0) ):
			 	dy = 0

		self.movementData["mx"] = event.x
		self.movementData["my"] = event.y
		self.updateCoords()

		return (dx, dy)



	def snap(self):

		pos = self.getPosition()

		snapX = self.k.space * pos[0] - self.movementData["px"]
		snapY = self.k.space * pos[1] - self.movementData["py"]

		self.move(snapX, snapY)



	def reset(self):

		snapX = self.k.space * self.originalPosition[0] - self.movementData["px"]
		snapY = self.k.space * self.originalPosition[1] - self.movementData["py"]

		self.move(snapX, snapY)



	def animate(self):

		pos = self.getPosition()
		x = pos[0] * self.k.space
		y = pos[1] * self.k.space

		if (self.originalPosition == pos):
			self.canvas.itemconfig(self.green, state = "hidden")
			self.canvas.itemconfig(self.red, state = "hidden")
			self.canvas.itemconfig(self.yellow, state = "normal")
			self.canvas.coords(self.yellow, (x - 1, y - 1) )

		elif (not self.canMove() ):
			self.canvas.itemconfig(self.green, state = "hidden")
			self.canvas.itemconfig(self.red, state = "normal")
			self.canvas.itemconfig(self.yellow, state = "hidden")
			self.canvas.coords(self.red, (x - 1, y - 1) )

		elif (self.canMove() ):
			self.canvas.itemconfig(self.green, state = "normal")
			self.canvas.itemconfig(self.yellow, state = "hidden")
			self.canvas.itemconfig(self.red, state = "hidden")
			self.canvas.coords(self.green, (x - 1, y - 1) )



	def clearAnimation(self):

		self.canvas.itemconfig(self.green, state = "hidden")
		self.canvas.itemconfig(self.red, state = "hidden")
		self.canvas.itemconfig(self.yellow, state = "hidden")



	def updateCoords(self):

		coords = self.canvas.coords(self.movementData["piece"])
		self.movementData["px"] = coords[0]
		self.movementData["py"] = coords[1]



	def move(self, dx, dy):

		self.canvas.move(self.movementData["piece"], dx, dy)



	def canMove(self):

		return self.position.canMove(self.canvas.gettags(self.movementData["piece"]),
							  		 self.originalPosition,
							  		 self.position.getPosition(self.movementData["px"],
									 						   self.movementData["py"]))



	def getPosition(self):

		return self.position.getPosition(self.movementData["px"], self.movementData["py"])
