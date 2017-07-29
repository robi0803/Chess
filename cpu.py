from tkinter import *
from globals import K

import random


class CPU():

	def __init__(self, position, canvas):

		self.k = K()

		self.position = position

		self.canvas = canvas

		self.color = "none"



	def takeTurn(self, checkWin, createNewPiece):

		temp = self.position.originalPosition

		move = self.getMove()
		self.movePiece(move)

		if (move[0][2] == "pawn"): self.checkPromotion(move[0][0], move[1], createNewPiece)

		self.position.capture(move[1], move[0])
		self.position.updateMoved(move[0][0])
		self.position.updateBoard()

		checkWin()

		self.position.originalPosition = temp







	def movePiece(self, move):

		piece = move[0][0]
		final = move[1]
		original = move[2]

		dx = final[0] * self.k.space - original[0] * self.k.space
		dy = final[1] * self.k.space - original[1] * self.k.space

		self.canvas.move(piece, dx, dy)



	def getMove(self):

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
		temp = best = self.getStats(moves[0], team)

		for move in moves:
			temp = self.getStats(move, team)
			if (temp > best):
				best = temp
				tiedMoves = []
				tiedMoves.append(move)

			elif (temp == best):
				tiedMoves.append(move)

		random.seed()
		return tiedMoves[ random.randint(0, len(tiedMoves) - 1) ]



	def getStats(self, move, team):

		stats = 0
		newPos = move[1]
		curPos = move[2]

		if (self.color == "white"):
			enemy = "black"
		else:
			enemy = "white"


		# if (curPos is vulnerable)
		for piece in team:
			tags = piece[2]
			if (self.position.isVulnerable((piece[0], piece[1]), self.color)):
				stats += self.filter(tags)


		# if (newPos is vulnerable)
		self.position.board[newPos[0]][newPos[1]] = self.position.board[curPos[0]][curPos[1]]
		self.position.board[curPos[0]][curPos[1]] = "none"
		team = self.position.findTeam(self.color)

		for piece in team:
			tags = piece[2]
			if (self.position.isVulnerable((piece[0], piece[1]), self.color)):
				stats -= self.filter(tags)

		self.position.updateBoard()


		# if (can capture)
		if (enemy == self.position.board[newPos[0]][newPos[1]][1]):
			tags = move[0]
			enemyClass = self.position.board[newPos[0]][newPos[1]][2]
			stats += self.capture(enemyClass)
			stats -= (1/4)*self.filter(tags)

		return stats



	def filter(self, tags):

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



	def capture(self, enemyClass):

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

		if (self.color == "black" and pos[1] == 7):
			self.canvas.delete(piece)
			tags = ["blkQueen"]
			createNewPiece(tags, pos)

		elif (self.color == "white" and pos[1] == 0):
			self.canvas.delete(piece)
			tags = ["whtQueen"]
			createNewPiece(tags, pos)
