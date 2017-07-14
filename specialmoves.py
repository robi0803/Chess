from Tkinter import *
from globals import K


class SpecialMoves():

	def __init__(self, canvas):

		self.k = K()

		self.canvas = canvas

		self.enPassant = None

		self.color = None



	def filter(self, pos1, pos2, unbind, createPiece):

		piece = self.canvas.find_closest(pos2[0] * self.k.space, pos2[1] * self.k.space)
		tags = self.canvas.gettags(piece)
		self.color = tags[1]

		if (tags[2] == "pawn"):

			# promote
			if ((tags[1] == "black" and pos2[1] == 7) or
			(tags[1] == "white" and pos2[1] == 0)):

				unbind()
				self.promote(pos2, piece, createPiece)

			# en passant
			self.checkEnPassant(pos2)

			if ((tags[1] == "black" and (pos1[1] == 1 and pos2[1] == 3)) or
			(tags[1] == "white" and (pos1[1] == 6 and pos2[1] == 4))):
				self.markEnPassant(pos1, piece)
			else:
				self.enPassant = None



	def promote(self, pos, piece, createPiece):

		bg = self.canvas.find_withtag("winBg")
		text = self.canvas.find_withtag("promotionText")
		rookRec = self.canvas.find_withtag("rookRec")
		bishopRec = self.canvas.find_withtag("bishopRec")
		queenRec = self.canvas.find_withtag("queenRec")
		knightRec = self.canvas.find_withtag("knightRec")

		self.canvas.itemconfig(bg, state = "disabled")
		self.canvas.itemconfig(text, state = "disabled")
		self.canvas.itemconfig(rookRec, state = "normal")
		self.canvas.itemconfig(bishopRec, state = "normal")
		self.canvas.itemconfig(queenRec, state = "normal")
		self.canvas.itemconfig(knightRec, state = "normal")

		self.canvas.tag_raise(bg)
		self.canvas.tag_raise(text)
		self.canvas.tag_raise(rookRec)
		self.canvas.tag_raise(bishopRec)
		self.canvas.tag_raise(queenRec)
		self.canvas.tag_raise(knightRec)

		if (self.color == "black"):

			blkRook = self.canvas.find_withtag("blkRook")
			blkBishop = self.canvas.find_withtag("blkBishop")
			blkQueen = self.canvas.find_withtag("blkQueen")
			blkKnight = self.canvas.find_withtag("blkKnight")

			self.canvas.itemconfig(blkRook, state = "disabled")
			self.canvas.itemconfig(blkBishop, state = "disabled")
			self.canvas.itemconfig(blkQueen, state = "disabled")
			self.canvas.itemconfig(blkKnight, state = "disabled")

			self.canvas.tag_raise(blkRook)
			self.canvas.tag_raise(blkBishop)
			self.canvas.tag_raise(blkQueen)
			self.canvas.tag_raise(blkKnight)

		else:

			whtRook = self.canvas.find_withtag("whtRook")
			whtBishop = self.canvas.find_withtag("whtBishop")
			whtQueen = self.canvas.find_withtag("whtQueen")
			whtKnight = self.canvas.find_withtag("whtKnight")

			self.canvas.itemconfig(whtRook, state = "disabled")
			self.canvas.itemconfig(whtBishop, state = "disabled")
			self.canvas.itemconfig(whtQueen, state = "disabled")
			self.canvas.itemconfig(whtKnight, state = "disabled")

			self.canvas.tag_raise(whtRook)
			self.canvas.tag_raise(whtBishop)
			self.canvas.tag_raise(whtQueen)
			self.canvas.tag_raise(whtKnight)

		self.canvas.delete(piece)
		self.canvas.tag_bind("prom", "<ButtonPress-1>", createPiece)



	def hide(self):

		bg = self.canvas.find_withtag("winBg")
		text = self.canvas.find_withtag("promotionText")
		rookRec = self.canvas.find_withtag("rookRec")
		bishopRec = self.canvas.find_withtag("bishopRec")
		queenRec = self.canvas.find_withtag("queenRec")
		knightRec = self.canvas.find_withtag("knightRec")

		self.canvas.itemconfig(bg, state = "hidden")
		self.canvas.itemconfig(text, state = "hidden")
		self.canvas.itemconfig(rookRec, state = "hidden")
		self.canvas.itemconfig(bishopRec, state = "hidden")
		self.canvas.itemconfig(queenRec, state = "hidden")
		self.canvas.itemconfig(knightRec, state = "hidden")

		if (self.color == "black"):

			blkRook = self.canvas.find_withtag("blkRook")
			blkBishop = self.canvas.find_withtag("blkBishop")
			blkQueen = self.canvas.find_withtag("blkQueen")
			blkKnight = self.canvas.find_withtag("blkKnight")

			self.canvas.itemconfig(blkRook, state = "hidden")
			self.canvas.itemconfig(blkBishop, state = "hidden")
			self.canvas.itemconfig(blkQueen, state = "hidden")
			self.canvas.itemconfig(blkKnight, state = "hidden")

		else:

			whtRook = self.canvas.find_withtag("whtRook")
			whtBishop = self.canvas.find_withtag("whtBishop")
			whtQueen = self.canvas.find_withtag("whtQueen")
			whtKnight = self.canvas.find_withtag("whtKnight")

			self.canvas.itemconfig(whtRook, state = "hidden")
			self.canvas.itemconfig(whtBishop, state = "hidden")
			self.canvas.itemconfig(whtQueen, state = "hidden")
			self.canvas.itemconfig(whtKnight, state = "hidden")



	def markEnPassant(self, pos1, piece):

		self.enPassantPiece = piece

		if (self.color == "black"):
			self.enPassant = (pos1[0], pos1[1] + 1)
		else:
			self.enPassant = (pos1[0], pos1[1] - 1)



	def checkEnPassant(self, pos):

		if (pos == self.enPassant):
			self.canvas.itemconfig(self.enPassantPiece, state = "hidden")		
