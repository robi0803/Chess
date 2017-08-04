try:
	from tkinter import *
except ImportError:
	from Tkinter import *
from globals import K
import random


class CPU():

	def __init__(self, position, canvas):

		self.k = K()

		self.position = position

		self.canvas = canvas

		self.color = "none"



	def takeTurn(self, checkWin, createNewPiece, pawns):
		'''
		Handles the computers turn.

		@param
			checkWin: game.checkWin, checks for winner
			createNewPiece: graphics.createPiece, promotes pawn

		@post
			The best move is found and the piece is moved. A pawn promotion is checked
			for. The game updates and checks for a winner.
		'''

		temp = self.position.originalPosition

		move = self.getMove()
		self.movePiece(move)

		if (move[0][2] == "pawn"):
			self.checkPromotion(move[0][0], move[1], createNewPiece)
			pawns(move[2], move[1], 0, 0)

		self.position.capture(move[1], move[0])
		self.position.updateMoved(move[0][0])
		self.position.updateBoard()

		checkWin()

		self.position.originalPosition = temp



	def movePiece(self, move):
		'''
		Moves piece given a move

		@param
			move: move from getMove(), ((identifier, color, type), new position, original position)

		@post
			The piece is moved.
		'''

		piece = move[0][0]
		final = move[1]
		original = move[2]

		dx = final[0] * self.k.space - original[0] * self.k.space
		dy = final[1] * self.k.space - original[1] * self.k.space

		self.canvas.move(piece, dx, dy)



	def getMove(self):
		'''
		Finds best move. The algorithm is as follows.

			for piece in team:
				for every position:
					if (piece can move to position):
						append to Moves[]

			for move in Moves[]:
				temp = get stats of move

				if (temp > best move):
					clear tiedMoves[]
					best move = temp
					append temp to tiedMoves[]

				if (temp == best move):
					append temp to tiedMoves[]

		@return
			A random move from tiedMoves[] is returned.

		'''

		team = self.position.findTeam(self.color)
		moves = []

		for piece in team:
			self.position.originalPosition = (piece[0], piece[1])

			for x in range(8):
				for y in range(8):
					if (self.position.canMove(piece[2], (x, y)) and
						self.position.originalPosition != (x, y)):

						moves.append((piece[2],                 # tags
									 (x, y),                    # new position
									 (piece[0], piece[1])))     # original position

		tiedMoves = []
		if (len(moves) != 0):
			temp = best = self.getStats(moves[0])

			for move in moves:
				temp = self.getStats(move)
				if (temp > best):
					best = temp
					tiedMoves = []
					tiedMoves.append(move)

				elif (temp == best):
					tiedMoves.append(move)

		random.seed()
		return tiedMoves[ random.randint(0, len(tiedMoves) - 1) ]



	def getStats(self, move):
		'''
		Finds stats for a given move. The algorithm is as follows.

			for all cpu pieces:
				if (piece is currently vulnerable):
					add to stats

			for all player pieces:
				if (piece is currently vulnerable):
					subtract from stats

			move piece to new position

			for all cpu pieces:
				if (piece is currently vulnerable):
					subtract from stats

			for all player pieces:
				if (piece is currently vulnerable):
					add to stats

			if (move results in capture of enemy):
				add to stats
				if (move results in piece being vulnerable):
					subtract from stats

		@param
			move: move from getMove(), ((identifier, color, type), new position, original position)

		@return
			Stats is returned.

		'''

		stats = 0
		newPos = move[1]
		curPos = move[2]

		if (self.color == "white"):
			player = "black"
		else:
			player = "white"


		# if (cpu is vulnerable from curPos)
		cpuTeam = self.position.findTeam(self.color)
		for piece in cpuTeam:
			tags = piece[2]
			if (self.position.isVulnerable((piece[0], piece[1]), self.color)):
				stats += self.filter(tags)


		# if (player is vulnerable from curPos)
		playerTeam = self.position.findTeam(player)
		for piece in playerTeam:
			tags = piece[2]
			if (self.position.isVulnerable((piece[0], piece[1]), player)):
				stats -= (1/8)*self.filter(tags)


		# move to newPos
		self.position.board[newPos[0]][newPos[1]] = self.position.board[curPos[0]][curPos[1]]
		self.position.board[curPos[0]][curPos[1]] = "none"

		# if (cpuTeam is vulnerable from newPos)
		cpuTeam = self.position.findTeam(self.color)
		for piece in cpuTeam:
			tags = piece[2]
			if (self.position.isVulnerable((piece[0], piece[1]), self.color)):
				stats -= self.filter(tags)

		# if (piece is vulnerable from newPos)
		check = False
		if (self.position.isVulnerable((newPos[0], newPos[1]), self.color)):
			check = True
			temp = self.filter(move[0])

		# if (player is vulnerable for newPos)
		playerTeam = self.position.findTeam(player)
		for piece in playerTeam:
			tags = piece[2]
			if (self.position.isVulnerable((piece[0], piece[1]), player)):
				stats += (1/8)*self.filter(tags)

		# move back to curPos
		self.position.updateBoard()

		# if (can capture)
		if (player == self.position.board[newPos[0]][newPos[1]][1]):
			tags = move[0]
			pieceType = self.position.board[newPos[0]][newPos[1]][2]
			stats += self.filterCapture(pieceType)
			if (check):
				stats -= temp

		return stats



	def filter(self, tags):
		'''
		Finds value of stats based on piece type

		@param
			tags: tag of current piece

		@return
			returns stats
		'''

		if (tags[2] == "pawn"):
			stats = 25
		elif (tags[2] == "rook"):
			stats = 50
		elif (tags[2] == "knight"):
			stats = 50
		elif (tags[2] == "bishop"):
			stats = 50
		elif (tags[2] == "queen"):
			stats = 100
		elif (tags[2] == "king"):
			stats = 500

		return stats



	def filterCapture(self, enemyClass):
		'''
		Finds value of stats based on piece type

		@param
			tags: tag of current piece

		@return
			returns stats
		'''

		if (enemyClass == "pawn"):
			stats = 25
		elif (enemyClass == "rook"):
			stats = 50
		elif (enemyClass == "knight"):
			stats = 50
		elif (enemyClass == "bishop"):
			stats = 50
		elif (enemyClass == "queen"):
			stats = 100
		elif (enemyClass == "king"):
			stats = 1000

		return stats



	def checkPromotion(self, piece, pos, createNewPiece):
		'''
		Checks for pawn promotion.

		@param
			piece: piece identifier
			pos: piece position
			createNewPiece: graphics.createPiece, promotes pawn

		@post
			If pawn makes it to opposite side of board it is promoted to queen.
		'''

		if (self.color == "black" and pos[1] == 7):
			self.canvas.delete(piece)
			tags = ["blkQueen"]
			createNewPiece(tags, pos)

		elif (self.color == "white" and pos[1] == 0):
			self.canvas.delete(piece)
			tags = ["whtQueen"]
			createNewPiece(tags, pos)
