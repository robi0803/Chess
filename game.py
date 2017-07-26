from tkinter import *
from globals import K

from position import Position
from specialmoves import SpecialMoves
from movement import Movement
from interface import Interface
from highlight import Highlight
from cpu import CPU


class Game():

	def __init__(self, graphics, root):

		# global variables
		self.k = K()

		# piece - piece identifier.  px, py - piece position.  mx, my - mouse position
		self.data = { "piece" : None, "px" : 0, "py" : 0, "mx" : 0 , "my" : 0}

		# keeps track of current turn
		self.color = "token"

		# true when menu is displayed, else false
		self.menuOn = False

		# tkinter root
		self.root = root

		# creates window and all images
		self.graphics = graphics

		# Canvas from graphics class. Tkinter object, draws images
		self.canvas = graphics.canvas

		# functions for special moves.
		self.specialMoves = SpecialMoves(self.canvas)

		# contains board and functions pertaining to position
		self.position = Position(self.canvas, self.specialMoves)
		self.position.updateBoard()

		# contains functions for moving pieces
		self.movement = Movement(self.canvas, self.position)

		# handles menues
		self.interface = Interface(graphics)

		# creates highlights around boxes
		self.highlight = Highlight(self.canvas, self.position)

		# finds move for computer player
		self.cpu = CPU(self.position, self.canvas)

		# brings up main menu, starts game
		self.showMain(0)



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

		self.data["piece"] = self.findClosest(event)
		self.data["mx"] = event.x
		self.data["my"] = event.y

		self.canvas.lift(self.data["piece"])

		#self.position.update()

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
			The corresponding piece is moved and createBorder() has been called. Try block
			is used to keep piece inside window.
		'''

		change = self.movement.getMovement(event, self.data)
		self.movement.move(self.data, change[0], change[1])

		self.updateCoords()

		try:
			self.highlight.createBorder(self.getPosition(), self.data)

		except TypeError:
			self.movement.push(self.data)



	def mouseRelease(self, event):

		'''
		Called when a user generated mouse release event occurs. Places piece if in a
		legal position and clears data members.

		@param
			event:
				Mouse release event generated from Tkinter. Function is binded with
				event and is called when this event occurs.

		@post
			If in a legal position, piece is moved to the center of the tile and the
			game updates. Else	piece is moved to original position. Variables are reset.
		'''

		if (self.canMove()):
			self.movement.snap(self.data)

			if (self.position.originalPosition != self.getPosition()):
				self.updateGame()

		else:
			self.movement.reset(self.data)

		self.position.rookMoved = False
		self.highlight.clearBorder()

		self.data["piece"] = NONE
		self.data["mx"] = 0
		self.data["my"] = 0



	def updateGame(self):

		self.position.capture(self.getPosition(), self.canvas.gettags(self.data["piece"]))
		self.checkSpecials()
		self.position.updateMoved(self.data["piece"])
		self.position.updateBoard()
		self.checkWin()


		if (self.multiPlayer):
			self.changeTurn()

		else:
			if (self.color == "token"):
				self.unbind()
				self.setColor()
				self.bind()

			self.cpu.takeTurn(self.checkWin)



	def checkWin(self):

		self.interface.checkWin(self.unbind, self.disableMenu, self.restart, self.showMain)



	def findClosest(self, event):

		piece = self.canvas.find_closest(event.x, event.y)
		tags = self.canvas.gettags(piece)

		if (len(tags) < 2):

			pieces = []

			piece1 = self.canvas.find_closest(event.x + 20, event.y + 20)
			tags1 = self.canvas.gettags(piece1)
			pieces.append((piece1, tags1))

			piece2 = self.canvas.find_closest(event.x + 20, event.y - 20)
			tags2 = self.canvas.gettags(piece2)
			pieces.append((piece2, tags2))

			piece3 = self.canvas.find_closest(event.x - 20, event.y + 20)
			tags3 = self.canvas.gettags(piece3)
			pieces.append((piece3, tags3))

			piece4 = self.canvas.find_closest(event.x - 20, event.y - 20)
			tags4 = self.canvas.gettags(piece4)
			pieces.append((piece4, tags4))

			for pair in pieces:

				if (len(pair[1]) > 2):
					piece = pair[0]

		return piece



	def checkSpecials(self):

		pos = self.getPosition()
		self.specialMoves.pawns(self.position.originalPosition, pos, self.unbind, self.createPiece)



	def createPiece(self, event):

		piece = self.canvas.find_closest(event.x, event.y)
		tags = self.canvas.gettags(piece)
		self.graphics.createNewPiece(tags, self.getPosition())
		self.specialMoves.hide()
		self.bind()



	def showMenu(self, event):

		self.unbind()
		self.interface.menu(event, self.bind, self.showMenu, self.restart, self.showMain)



	def showMain(self, event):

		self.singlePlayer = False
		self.multiPlayer = False
		self.unbind()
		self.disableMenu()
		self.color = "token"
		self.graphics.restart()
		self.interface.mainMenu(self.setSinglePlayer, self.setMultiPlayer)



	def setSinglePlayer(self, event):

		self.singlePlayer = True
		self.multiPlayer = False
		self.interface.hideMain()
		self.bind()
		self.enableMenu()



	def setMultiPlayer(self, event):

		self.multiPlayer = True
		self.singlePlayer = False
		self.interface.hideMain()
		self.bind()
		self.root.bind('<Escape>', self.showMenu)



	def restart(self, event):

		self.color = "token"
		self.bind()
		self.enableMenu()
		self.graphics.restart()



	def changeTurn(self):

		self.unbind()
		self.changeColor()
		self.bind()



	def disableMenu(self):

		self.root.unbind('<Escape>')



	def enableMenu(self):

		self.root.bind('<Escape>', self.showMenu)



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

		if (self.color == "white"):
			self.cpu.color = "black"
		else:
			self.cpu.color = "white"



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
