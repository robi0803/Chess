try:
	from tkinter import *
except ImportError:
	from Tkinter import *
from globals import K

class Position():

	def __init__(self, canvas, specialMoves):

		# globals
		self.k = K()

		self.canvas = canvas

		self.specialMoves = specialMoves

		# location of piece before moving
		self.originalPosition = None

		# list of all piece moved
		self.moved = []

		self.rookMoved = False
		self.specialMovesOn = True

		# stores ( identifier : color : type ) for each space
		self.board = [[ "none" for j in range(0, 8)] for i in range(0, 8) ]



	def updateBoard(self):
		'''
		@post
			board contians the position of every piece.
		'''

		x = 0
		for i in range(10, self.k.width + 10, self.k.space):
			y = 0
			for j in range(10, self.k.height + 10, self.k.space):

				piece = self.canvas.find_closest(i, j)
				coords = self.canvas.coords(piece)
				tags = self.canvas.gettags(piece)

				if (len(tags) >= 3):
					self.board[x][y] = (piece, tags[1], tags[2])
				else : self.board[x][y] = "none"

				y += 1
			x += 1



	def getPosition(self, px, py):
		'''
		Returns board(8x8) coordinates given image(472x472) coordinates.

		@param
			px: x coordinate of piece position
			py: y coordinate of piece position

		@return
			A tuple containing the board coordinates is returned.
		'''

		x = y = None
		for i in range(8):
			if ((px <  (self.k.space * (i + 1) - 30)) and
				(px >= (self.k.space) * i - 30) ):
					x = i
			if ((py <  (self.k.space * (i + 1) - 7)) and
				(py >= (self.k.space * i - 54)) ):
					y = i

		return (x, y)



	def capture(self, pos, tags):
		'''
		Hides enemy piece.

		@param
			pos:  position of space to check
			tags: tags of attacking piece

		@post
			If there is an enemy piece at pos, the enemy piece is hidden.
		'''

		x = pos[0]
		y = pos[1]

		#if there is a piece and it is a different color
		if (len(self.board[x][y]) > 1 and
		   (self.board[x][y][1] != tags[1]) ):

			self.canvas.itemconfig(self.board[x][y][0], state = "hidden")



	def findTeam(self, color):
		'''
		@param
			color: the color of the team to findClosest

		@return
			A list containg all pieces of the team is returned.
			( x-coordinate, y-coordinate, (identifier, color, type) )
		'''

		team = []

		for x in range(8):
			for y in range(8):
				if (len(self.board[x][y]) != 1 and self.board[x][y][1] == color):
					team.append((x, y, self.board[x][y]))

		return team



	def updateMoved(self, piece):
		'''
		@param
		 	piece: the piece that has been moved

		@post
			The list of pieces that have been moved is updated.
		'''

		self.moved.append(piece)



	def canMove(self, tags, pos2):
		'''
		Checks if a given piece can move to a given position. Also handles castling.

		@param
			tags: tags of piece to check
			pos2: position piece is moving to

		@return
			True if can move, else False.
		'''

		pos1 = self.originalPosition
		check = False

		if (pos1 == pos2): check = True

		if (tags[2] == "king"):
			check = self.king(tags, pos2)

		if (self.pathBlocked(pos2)): check = False

		elif (self.occupied(tags, pos2)): check = False

		elif (tags[2] == "pawn"):
			check = self.pawn(tags, pos2)

		elif (tags[2] == "rook"):
			check = self.rook(tags, pos2)

		elif (tags[2] == "knight"):
			check = self.knight(tags, pos2)

		elif (tags[2] == "bishop"):
			check = self.bishop(tags, pos2)

		elif (tags[2] == "queen"):
			check = self.queen(tags, pos2)

		return check



	def occupied(self, tags, pos):
		'''
		@param
			tags: tags of piece to check
			pos: position to check

		@return
			True if occupied by piece of same color, else False.
		'''

		if (tags[1] == self.board[pos[0]][pos[1]][1]):
			check = True
		else:
			check = False

		return check



	def pathBlocked(self, pos2):
		'''
		@param
			pos2: position to check

		@return
			True if any piece is blocking the path to pos2, else False.
		'''

		pos1 = self.originalPosition
		check = False

		if (pos1[0] == pos2[0] or pos1[1] == pos2[1]):
			check = self.rookPath(pos2)
		if (abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])):
			check = self.bishopPath(pos2)

		return check



	def rookPath(self, pos2):
		'''
		Called in pathBlocked()

		@param
			pos2: position to check

		@return
			True if any piece is blocking the path right, left, above or below
			pos2, else False.
		'''

		pos1 = self.originalPosition
		check = False

		above = pos2[1] - pos1[1] < 0 and pos1[0] == pos2[0]
		below = pos2[1] - pos1[1] > 0 and pos1[0] == pos2[0]
		right = pos2[0] - pos1[0] > 0 and pos1[1] == pos2[1]
		left  = pos2[0] - pos1[0] < 0 and pos1[1] == pos2[1]

		# horizontal check
		x = pos1[0] + 1
		y = pos1[1]

		while (not check and x < pos2[0] and right):
			if (self.board[x][y] != "none"):
				check = True
			x += 1

		x = pos1[0] - 1

		while (not check and x > pos2[0] and left):
			if (self.board[x][y] != "none"):
				check = True
			x -= 1

		# vertical check
		x = pos1[0]
		y = pos1[1] - 1

		while (not check and y > pos2[1] and above):
			if (self.board[x][y] != "none"):
				check = True
			y -= 1

		y = pos1[1] + 1

		while (not check and y < pos2[1] and below):
			if (self.board[x][y] != "none"):
				check = True
			y += 1

		return check



	def bishopPath(self, pos2):
		'''
		Called in pathBlocked()

		@param
			pos2: position to check

		@return
			True if any piece is blocking the path northwest, northeast, southwest
			or southeast of pos2, else False.
		'''

		pos1 = self.originalPosition
		check = False

		west = pos2[0] - pos1[0] < 0
		east = pos2[0] - pos1[0] > 0
		north = pos2[1] - pos1[1] < 0
		south = pos2[1] - pos1[1] > 0

		# southeast
		x = pos1[0] + 1
		y = pos1[1] + 1

		while (not check and x < pos2[0] and south and east):
			if (self.board[x][y] != "none"):
				check = True
			x += 1
			y += 1

		# northeast
		x = pos1[0] + 1
		y = pos1[1] - 1

		while (not check and x < pos2[0] and north and east):
			if (self.board[x][y] != "none"):
				check = True
			x += 1
			y -= 1

		# northwest
		x = pos1[0] - 1
		y = pos1[1] - 1

		while (not check and x > pos2[0] and north and west):
			if (self.board[x][y] != "none"):
				check = True
			x -= 1
			y -= 1

		# southwest
		x = pos1[0] - 1
		y = pos1[1] + 1

		while (not check and x > pos2[0] and south and west):
			if (self.board[x][y] != "none"):
				check = True
			x -= 1
			y += 1

		return check



	def pawn(self, tags, pos2):
		'''
		Called from canMove(), checks if pawn can move.

		@param
			tags: tags of piece to check
			pos2: position to check

		@return
			True if pawn can move, else False.
		'''

		pos1 = self.originalPosition
		check = False

		below = pos2[1] - pos1[1] == 1
		above = pos2[1] - pos1[1] == -1
		right = pos2[0] - pos1[0] == 1
		left = pos2[0] - pos1[0] == -1
		inCol = pos1[0] == pos2[0]
		empty = self.board[pos2[0]][pos2[1]] == "none"


		if (tags[1] == "black"):

			if (below and inCol and empty):
				check = True

			if (below and (right or left) and
				self.board[pos2[0]][pos2[1]][1] == "white"):
				check = True

			if (below and (right or left) and
				self.specialMoves.enPassant == pos2):
				check = True

			if (pos1[1] == 1 and pos2[1] - pos1[1] == 2 and inCol and empty):
				check = True


		if (tags[1] == "white"):

			if (above and inCol and empty):
				check = True

			if (above and (right or left) and
			   (self.board[pos2[0]][pos2[1]][1] == "black")):
				check = True

			if (above and (right or left) and
				self.specialMoves.enPassant == pos2):
					check = True

			if (pos1[1] == 6 and pos2[1] - pos1[1] == -2 and inCol and empty):
				check = True

		return check



	def rook(self, tags, pos2):
		'''
		Called from canMove(), checks if rook can move.

		@param
			tags: tags of piece to check
			pos2: position to check

		@return
			True if rook can move, else False.
		'''

		pos1 = self.originalPosition
		check = False

		if ((pos1[0] == pos2[0] and pos1[1] != pos2[1]) or
			(pos1[0] != pos2[0] and pos1[1] == pos2[1])):
			check = True;

		return check



	def knight(self, tags, pos2):
		'''
		Called from canMove(), checks if knight can move.

		@param
			tags: tags of piece to check
			pos2: position to check

		@return
			True if knight can move, else False.
		'''

		pos1 = self.originalPosition
		check = False

		if ((abs(pos2[1] - pos1[1]) == 2 and abs(pos2[0] - pos1[0]) == 1) or
			(abs(pos2[0] - pos1[0]) == 2 and abs(pos2[1] - pos1[1]) == 1)):
			check = True

		return check



	def bishop(self, tags, pos2):
		'''
		Called from canMove(), checks if bishop can move.

		@param
			tags: tags of piece to check
			pos2: position to check

		@return
			True if bishop can move, else False.
		'''

		pos1 = self.originalPosition
		check = False

		if (abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])):
			check = True

		return check



	def queen(self, tags, pos2):
		'''
		Called from canMove(), checks if queen can move.

		@param
			tags: tags of piece to check
			pos2: position to check

		@return
			True if queen can move, else False.
		'''

		pos1 = self.originalPosition

		check = False

		check = self.rook(tags, pos2)

		if (not check):
			check = self.bishop(tags, pos2)

		return check



	def king(self, tags, pos2):
		'''
		Called from canMove(), checks if king can move and castle.

		@param
			tags: tags of piece to check
			pos2: position to check

		@post
			If king can castle, the appropiate rook is moved automatically. If
			the king leaves the castle position, the rook is moved back.

		@return
			True if pawn can move, else False.
		'''

		pos1 = self.originalPosition
		check = False

		if ((abs(pos2[0] - pos1[0]) == 1 or pos1[0] == pos2[0]) and
			(abs(pos2[1] - pos1[1]) == 1 or pos1[1] == pos2[1])):
			check = True

		if (self.canCastle(tags, pos2) and self.specialMovesOn):
			check = True
			self.castle(tags)
		elif (self.rookMoved == True and self.specialMovesOn):
			self.resetRook(tags)

		return check



	def canCastle(self, tags, pos2):
		'''
		Called from king(), checks if king can castle.

		@param
			tags: tags of piece to check
			pos2: position to check

		@return
			True if king can castle, else False.
		'''

		check = True
		color = tags[1]

		if (color == "white"):

			rook = self.canvas.find_withtag("castleWhite")
			king = self.canvas.find_withtag("whiteKing")

			# king or rook has moved
			for piece in self.moved:
				if (piece == king or piece == rook):
					check = False

			# moving to castle position
			if (pos2 != (6,7)):
				check = False

			# king is in check
			i = 4
			while (check == True and i < 7):
				check = not self.isVulnerable((i,7), color)
				i += 1

			# spaces are empty
			i = 5
			while (check == True and i < 7):
				if (self.board[i][7] != "none"):
					check = False
				i += 1

		if (color == "black"):

			rook = self.canvas.find_withtag("castleBlack")
			king = self.canvas.find_withtag("blackKing")

			for piece in self.moved:
				if (piece == king or piece == rook):
					check = False

			if (pos2 != (6,0)):
				check = False

			i = 4
			while (check == True and i < 7):
				check = not self.isVulnerable((i,0), color)
				i += 1

			i = 5
			while (check == True and i < 7):
				if (self.board[i][0] != "none"):
					check = False
				i += 1

		return check



	def castle(self, tags):
		'''
		Called from king(), moves appropiate rook to castle position.

		@param
			tags: tags of piece to check

		@post
			Rook has been moved, rookMoved is set to True
		'''

		color = tags[1]

		if (color == "white"):

			rook = self.canvas.find_withtag("castleWhite")
			coords = self.canvas.coords(rook)

			if (self.getPosition(coords[0], coords[1]) != (5, 7)):
				self.canvas.move(rook, -2 * self.k.space, 0)
				self.rookMoved = True

		if (color == "black"):

			rook = self.canvas.find_withtag("castleBlack")
			coords = self.canvas.coords(rook)

			if (self.getPosition(coords[0], coords[1]) != (5, 0)):
				self.canvas.move(rook, -2 * self.k.space, 0)
				self.rookMoved = True



	def resetRook(self, tags):
		'''
		Called from king(), resets Rook to original position.

		@param
			tags: tags of piece to check

		@post
			Rook is moved back original position and rookMoved is set to False.
		'''

		color = tags[1]
		self.rookMoved = False

		if (color == "white"):
			rook = self.canvas.find_withtag("castleWhite")
			self.canvas.move(rook, 2 * self.k.space, 0)

		if (color == "black"):
			rook = self.canvas.find_withtag("castleBlack")
			self.canvas.move(rook, 2 * self.k.space, 0)



	def isVulnerable(self, pos, color):
		'''
		@param
			pos: the position to check
			color: the color of the piece to check

		@return
			True if pos is vulnerable, else False.
		'''

		firstTurn = False
		vulnerable = False

		if (color == "white"):
			enemy = "black"
		elif (color == "black"):
			enemy = "white"
		else:
			firstTurn = True

		if (not firstTurn):
			team = self.findTeam(enemy)
			temp = self.originalPosition
			self.specialMovesOn = False

			i = 0
			while (not vulnerable and i < len(team)):

				self.originalPosition = (team[i][0], team[i][1])
				tags = team[i][2]

				if (self.canMove(tags, (pos[0], pos[1]))):
					vulnerable = True

				if (tags[2] == "pawn" and self.originalPosition[0] - pos[0] == 0 and
				   (abs(self.originalPosition[1]) - pos[1] == 1 or
					abs(self.originalPosition[1] - pos[1] == 2))):
					vulnerable = False

				if (self.originalPosition == pos):
					vulnerable = False

				i += 1
			self.originalPosition = temp
			self.specialMovesOn = True

		return vulnerable
