from Tkinter import *
from globals import K

from position import Position
from movement import Movement
from rules import Interface
from highlight import Highlight
from cpu import CPU


class Game():

	def __init__(self, canvas, root):

		# global variables
		self.k = K()

		# piece - piece identifier.  px, py - piece position.  mx, my - mouse position
		self.data = { "piece" : None, "px" : 0, "py" : 0, "mx" : 0 , "my" : 0}

		# Canvas from graphics class. Tkinter object, draws images
		self.canvas = canvas

		# contains board and functions pertaining to position
		self.position = Position(self.canvas)
		self.position.update()

		# contains functions for moving pieces
		self.movement = Movement(self.canvas, self.position)

		# handles turn change and win
		self.interface = Interface(self.canvas)

		# creates highlights around boxes
		self.highlight = Highlight(self.canvas, self.position)

		# finds move for computer player
		self.cpu = CPU(self.position)

		# keeps track of current turn
		self.color = "token"

		# binds events to functions, allows user to click and drag
		self.canvas.tag_bind(self.color, "<ButtonPress-1>", self.mouseClick)
		self.canvas.tag_bind(self.color, "<B1-Motion>", self.mouseMove)
		self.canvas.tag_bind(self.color, "<ButtonRelease-1>", self.mouseRelease)

		# true when menu is displayed, else false
		self.menuOn = False

		# binds menu to escape key
		root.bind('<Escape>', self.showMenu)



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

		self.data["piece"] = self.canvas.find_closest(event.x, event.y)
		self.data["mx"] = event.x
		self.data["my"] = event.y

		self.canvas.lift(self.data["piece"])

		self.updateCoords()

		self.position.originalPosition = self.getPosition()

		self.highlight.createBorder(self.getPosition(), self.data)



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

		change = self.movement.getMovement(event, self.data)
		self.movement.move(change[0], change[1], self.data)

		self.updateCoords()

		try:
			self.highlight.createBorder(self.getPosition(), self.data)
		except TypeError:
			self.movement.push(self.data)



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
			self.movement.snap(self.data)
			self.position.capture(self.getPosition(), self.canvas.gettags(self.data["piece"]))
			self.position.update()

			if (self.position.originalPosition != self.getPosition()):
				self.changeTurn()

		else:
			self.movement.reset(self.data)

		self.interface.checkWin()

		self.highlight.clearBorder()

		self.data["piece"] = NONE
		self.data["mx"] = 0
		self.data["my"] = 0



	def showMenu(self, event):

		if (not self.menuOn):
			self.unbind()
			self.menuOn = True
		else:
			self.bind()
			self.menuOn = False

		self.interface.menu()



	def changeTurn(self):

		self.unbind()
		self.changeColor()
		self.bind()



	def unbind(self):

		self.canvas.tag_unbind(self.color, "<ButtonPress-1>")
		self.canvas.tag_unbind(self.color, "<B1-Motion>")
		self.canvas.tag_unbind(self.color, "<ButtonRelease-1>")



	def bind(self):

		self.canvas.tag_bind(self.color, "<ButtonPress-1>", self.mouseClick)
		self.canvas.tag_bind(self.color, "<B1-Motion>", self.mouseMove)
		self.canvas.tag_bind(self.color, "<ButtonRelease-1>", self.mouseRelease)



	def setColor(self):

		tags = self.canvas.gettags(self.data["piece"])
		self.color = tags[1]



	def changeColor(self):

		if (self.color == "token"):
			self.setColor()

		if (self.color == "white"):
			self.color = "black"
		else:
			self.color = "white"



	def updateCoords(self):

		coords = self.canvas.coords(self.data["piece"])
		self.data["px"] = coords[0]
		self.data["py"] = coords[1]



	def canMove(self):

		return self.position.canMove(self.canvas.gettags(self.data["piece"]),
							  		 self.position.getPosition(self.data["px"],
									 						   self.data["py"]))



	def getPosition(self):

		return self.position.getPosition(self.data["px"], self.data["py"])
