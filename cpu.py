from tkinter import *
from globals import K

import random


class CPU():

	def __init__(self, position, canvas):

		self.k = K()

		self.position = position

		self.canvas = canvas

		self.color = "none"



	def takeTurn(self, checkWin):

		temp = self.position.originalPosition

		move = self.getMove()
		self.movePiece(move)

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


		temp = best = self.getStats(moves[0])
		bestMove = moves[0]
		for move in moves:
			temp = self.getStats(move)
			if (temp > best):
				best = temp
				bestMove = move

		return bestMove



	def getStats(self, move):

		tags = move[0]
		newPos = move[1]
		curPos = move[2]


		if (self.color == "white"):
			enemy = "black"
		else:
			enemy = "white"


		stats = 0

		if (self.position.isVulnerable(curPos, self.color) and
			not self.position.isVulnerable(newPos, self.color)):

			if (tags[2] == "pawn"):
				stats += 10

			elif (tags[2] == "rook"):
				stats += 30

			elif (tags[2] == "knight"):
				stats += 30

			elif (tags[2] == "bishop"):
				stats += 30

			elif (tags[2] == "queen"):
				stats += 50

			elif (tags[2] == "king"):
				stats += 90

		if (self.position.isVulnerable(newPos, self.color)):

			if (tags[2] == "pawn"):
				stats -= 10

			elif (tags[2] == "rook"):
				stats -= 30

			elif (tags[2] == "knight"):
				stats -= 30

			elif (tags[2] == "bishop"):
				stats -= 30

			elif (tags[2] == "queen"):
				stats -= 50

			elif (tags[2] == "king"):
				stats -= 70


		# if (can capture)
		if (enemy == self.position.board[newPos[0]][newPos[1]][1]):

			enemyClass = self.position.board[newPos[0]][newPos[1]][2]

			if (enemyClass == "pawn"):
				stats += 10

			elif (enemyClass == "rook"):
				stats += 30

			elif (enemyClass == "knight"):
				stats += 30

			elif (enemyClass == "bishop"):
				stats += 30

			elif (enemyClass == "queen"):
				stats += 50

			elif (enemyClass == "king"):
				stats += 100


		return stats



	def randomMove(self, moves):

		random.seed()

		return moves[ random.randint(0, len(moves) - 1) ]
