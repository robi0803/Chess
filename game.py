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

		# piece - piece identifier.  px, py - piece position(472x472).  mx, my - mouse position(472x472)
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
			data and originalPosition are initialized to the piece closest
			to the mouse click event. This piece's image is raised to the top layer.
			A border is created around the current tile.
		'''

		self.data["piece"] = self.findClosest(event)
		self.data["mx"] = event.x
		self.data["my"] = event.y
		self.updateCoords()

		self.canvas.lift(self.data["piece"])
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
			The corresponding piece is moved and a border is created around the current
			tile. Try block is used to keep piece inside window.
		'''

		self.movement.drag(event, self.data)
		self.updateCoords()

		try:
			self.highlight.createBorder(self.getPosition(), self.data)

		except TypeError:
			self.movement.push(self.data)



	def mouseRelease(self, event):
		'''
		Called when a user generated mouse release event occurs. Places piece and
		clears data members.

		@param
			event:
				Mouse release event generated from Tkinter. Function is binded with
				event and is called when this event occurs.

		@post
			If in a legal position, piece is moved to the center of the tile and the
			game updates. Else,	piece is moved to original position. Variables are reset.
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
		'''
		Called during mouseRelease. Updates game and changes turn.

		@post
			Captured pieces, pieces that have been moved, and the board have all
			been updated. Special moves and a winner have both been checked for.
			If multiplayer game, the game changes turn. Else, the computer takes its
			turn.
		'''

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

			self.cpu.takeTurn(self.checkWin, self.graphics.createNewPiece, self.specialMoves.pawns)



	def findClosest(self, event):
		'''
		Prevents user from grabbing board. Four more locations are attempted
		if canvas.find_closest() doesn't return a piece.

		@param
			event:
				Tkinter event. event.x and event.y correspond to the location of
				the mouse click event. The origin is the top left corner, +x is right,
				and +y is down.

		@return
			The identifier of the piece.
		'''

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



	def bind(self):
		'''
		@post
			Bindings are added for pieces of current color.
		'''

		self.canvas.tag_bind(self.color, "<ButtonPress-1>", self.mouseClick)
		self.canvas.tag_bind(self.color, "<B1-Motion>", self.mouseMove)
		self.canvas.tag_bind(self.color, "<ButtonRelease-1>", self.mouseRelease)



	def unbind(self):
		'''
		@post
			Bindings are removed for pieces of current color.
		'''

		self.canvas.tag_unbind(self.color, "<ButtonPress-1>")
		self.canvas.tag_unbind(self.color, "<B1-Motion>")
		self.canvas.tag_unbind(self.color, "<ButtonRelease-1>")



	def changeTurn(self):
		'''
		Changes turn for multi-player game.

		@post
			Pieces are bound to other players color.
		'''

		self.unbind()
		self.changeColor()
		self.bind()



	def setColor(self):
		'''
		@post
			Sets color based off of current piece. If single-player game, also sets
			cpu color.
		'''

		tags = self.canvas.gettags(self.data["piece"])
		self.color = tags[1]

		if (self.singlePlayer):
			if (self.color == "white"):
				self.cpu.color = "black"
			else:
				self.cpu.color = "white"



	def changeColor(self):
		'''
		@post
			Changes color to opposing team.
		'''

		if (self.color == "token"):
			self.setColor()

		if (self.color == "white"):
			self.color = "black"
		else:
			self.color = "white"



	def updateCoords(self):
		'''
		@post
			The current coordinates of the image are updated. origin - topleft,
			+x - right(0-472), +y - down(0-472).
		'''

		coords = self.canvas.coords(self.data["piece"])
		self.data["px"] = coords[0]
		self.data["py"] = coords[1]



	def getPosition(self):
		'''
		@return
			position.getPosition(), current board position. origin - topleft,
			+x - right(0-7), +y - down(0-7).
		'''

		return self.position.getPosition(self.data["px"], self.data["py"])



	def canMove(self):
		'''
		@post
			position.canMove() is called. Checks if current piece can move to it's
			current location.
		'''

		return self.position.canMove(self.canvas.gettags(self.data["piece"]),
									 self.position.getPosition(self.data["px"], self.data["py"]))



	def checkWin(self):
		'''
		@post
			interface.checkWin() has been called.
		'''

		self.interface.checkWin(self.unbind, self.disableMenu, self.restart, self.showMain)



	def checkSpecials(self):
		'''
		@post
			specialMoves.pawns() is called. Checks for promotion / en passant.
		'''

		pos = self.getPosition()
		self.specialMoves.pawns(self.position.originalPosition, pos, self.unbind, self.createPiece)



	def createPiece(self, event):
		'''
		Used when promoting a pawn. Function is binded with mouseClick event
		in specialmoves.promote()

		@param
			event: Tkinter event used to find which piece user clicked on

		@post
			A new piece is created, The promotion menu is hidden, and the pieces are
			rebound.
		'''

		piece = self.canvas.find_closest(event.x, event.y)
		tags = self.canvas.gettags(piece)
		self.graphics.createNewPiece(tags, self.getPosition())
		self.specialMoves.hide()
		self.bind()



	def showMenu(self, event):
		'''
		@param
			event: Tkinter event, needed for interace.menu()

		@post
			Bindings are removed from pieces and in-game menu is brought up.
		'''

		self.unbind()
		self.interface.menu(event, self.bind, self.showMenu, self.restart, self.showMain)



	def disableMenu(self):
		'''
		@post
			In-game menu can no longer appear.
		'''

		self.root.unbind('<Escape>')



	def enableMenu(self):
		'''
		@post
			In-game menu can appear.
		'''

		self.root.bind('<Escape>', self.showMenu)



	def restart(self, event):
		'''
		Called from interface.menu(). Restarts game.

		@param
			event: Tkinter event, needed to bind functions

		@post
			Variables and board are reset.
		'''

		self.color = "token"
		self.bind()
		self.enableMenu()
		self.graphics.restart()
		self.position.updateBoard()



	def showMain(self, event):
		'''
		Brings up main menu.

		@param
			event: Tkinter event, needed to bind function

		@post
			Game is reset, bindings are removed, main menu is displayed.

		'''

		self.singlePlayer = False
		self.multiPlayer = False
		self.color = "token"
		self.unbind()
		self.disableMenu()
		self.graphics.restart()
		self.position.updateBoard()
		self.interface.mainMenu(self.setSinglePlayer, self.setMultiPlayer)



	def setSinglePlayer(self, event):
		'''
		Called from interface.mainMenu(). Sets up single player game.

		@param
			event: Tkinter event, needed to bind functions

		@post
			Variables for single player game are set, main menu is hidden, pieces
			are rebound, and in-game menu are enabled.
		'''

		self.singlePlayer = True
		self.multiPlayer = False
		self.interface.hideMain()
		self.bind()
		self.enableMenu()



	def setMultiPlayer(self, event):
		'''
		Called from interface.mainMenu(). Sets up multi player game.

		@param
			event: Tkinter event, needed to bind functions

		@post
			Variables for mutli player game are set, main menu is hidden, pieces
			are rebound, and in-game menu are enabled.
		'''

		self.multiPlayer = True
		self.singlePlayer = False
		self.interface.hideMain()
		self.bind()
		self.enableMenu()
