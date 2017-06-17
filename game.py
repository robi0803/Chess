from Tkinter import *
from globals import K

from position import Position
from cpu import CPU


class Game():

	def __init__(self, canvas):

		# global variables
		self.k = K()

		# Tkinter object, draws images
		self.canvas = canvas

		# contains board and functions pertaining to position
		self.position = Position()
		self.position.update(self.canvas)

		# finds move for computer player
		self.cpu = CPU(self.position)

		# piece - piece identifier.  px, py - piece position.  mx, my - mouse position
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

		self.canvas.lift(self.movementData["piece"])

		self.updateCoords()
		self.originalPosition = self.getPosition()
		self.highlight()



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
			self.highlight()
		except TypeError:
			self.push()



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
			piece is moved to original position. movementData and Animation are
			cleared.
		'''

		if (self.canMove()):
			self.snap()
			self.position.capture(self.canvas, self.getPosition(),
								  self.canvas.gettags(self.movementData["piece"]))
			self.position.update(self.canvas)

			if (self.originalPosition != self.getPosition()):
				self.changeTurn()

		else:
			self.reset()

		self.checkWin()
		self.clearHighlight()
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

		dx = self.k.space * pos[0] - self.movementData["px"]
		dy = self.k.space * pos[1] - self.movementData["py"]

		self.move(dx, dy)



	def reset(self):

		dx = self.k.space * self.originalPosition[0] - self.movementData["px"]
		dy = self.k.space * self.originalPosition[1] - self.movementData["py"]

		self.move(dx, dy)



	def push(self):

		dx = dy = 0

		if (self.movementData["px"] < 0):
			dx = 10
		if (self.movementData["px"] >= self.k.width - 30):
			dx = -10

		if (self.movementData["py"] < 0):
			dy = 10
		if (self.movementData["py"] > self.k.height - 30):
			dy = -10

		self.move(dx, dy)



	def move(self, dx, dy):

		self.canvas.move(self.movementData["piece"], dx, dy)



	def changeTurn(self):

		self.canvas.tag_unbind("token", "<ButtonPress-1>")
		self.canvas.tag_unbind("token", "<B1-Motion>")
		self.canvas.tag_unbind("token", "<ButtonRelease-1>")

		if (self.getColor() == "white"):
			unbind = "white"
			bind = "black"
		else:
			unbind = "black"
			bind = "white"

		self.canvas.tag_unbind(unbind, "<ButtonPress-1>")
		self.canvas.tag_unbind(unbind, "<B1-Motion>")
		self.canvas.tag_unbind(unbind, "<ButtonRelease-1>")

		self.canvas.tag_bind(bind, "<ButtonPress-1>", self.mouseClick)
		self.canvas.tag_bind(bind, "<B1-Motion>", self.mouseMove)
		self.canvas.tag_bind(bind, "<ButtonRelease-1>", self.mouseRelease)



	def getColor(self):

		tags = self.canvas.gettags(self.movementData["piece"])
		return tags[1]



	def checkWin(self):

		kings = self.canvas.find_withtag("king")

		if (self.canvas.gettags(kings[0])[1] == "white"):
			white = kings[0]
			black = kings[1]
		else:
			black = kings[0]
			white = kings[1]

		if (self.canvas.itemcget(black, "state") == "hidden"):
			self.whiteWin()

		if (self.canvas.itemcget(white, "state") == "hidden"):
			self.blackWin()



	def whiteWin(self):

		self.canvas.create_text((self.k.width / 2, self.k.height / 2),
		 						 text = "White Wins!")



	def blackWin(self):

		self.canvas.create_text((self.k.width / 2, self.k.height / 2),
		 						 text = "Black Wins!")



	def highlight(self):

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



	def clearHighlight(self):

		self.canvas.itemconfig(self.green, state = "hidden")
		self.canvas.itemconfig(self.red, state = "hidden")
		self.canvas.itemconfig(self.yellow, state = "hidden")



	def updateCoords(self):

		coords = self.canvas.coords(self.movementData["piece"])
		self.movementData["px"] = coords[0]
		self.movementData["py"] = coords[1]



	def canMove(self):

		return self.position.canMove(self.canvas.gettags(self.movementData["piece"]),
							  		 self.originalPosition,
							  		 self.position.getPosition(self.movementData["px"],
									 						   self.movementData["py"]))



	def getPosition(self):

		return self.position.getPosition(self.movementData["px"], self.movementData["py"])
