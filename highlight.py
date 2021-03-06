from globals import K


class Highlight():

	def __init__(self, canvas, position):

		self.k = K()

		self.canvas = canvas

		self.position = position



	def createBorder(self, pos, data):
		'''
		Creates a border around the tile the current piece is hovering above.

		@param
			pos: current position of piece
			data: game.data, contains piece identifier, piece position, mouse position

		@post
			If piece is in original Position, a yellow border is created. If piece is
			in a legal position, a green border is created. If piece is in a illegal
			position, a red border is created.
		'''

		self.findImages()

		canMove = self.position.canMove(self.canvas.gettags(data["piece"]),
										self.position.getPosition(data["px"],
																  data["py"]))

		x = pos[0] * self.k.space
		y = pos[1] * self.k.space

		if (self.position.originalPosition == pos):
			self.canvas.itemconfig(self.green, state = "hidden")
			self.canvas.itemconfig(self.red, state = "hidden")
			self.canvas.itemconfig(self.yellow, state = "normal")
			self.canvas.coords(self.yellow, (x - 1, y - 1))

		elif (not canMove):
			self.canvas.itemconfig(self.green, state = "hidden")
			self.canvas.itemconfig(self.red, state = "normal")
			self.canvas.itemconfig(self.yellow, state = "hidden")
			self.canvas.coords(self.red, (x - 1, y - 1))

		elif (canMove):
			self.canvas.itemconfig(self.green, state = "normal")
			self.canvas.itemconfig(self.yellow, state = "hidden")
			self.canvas.itemconfig(self.red, state = "hidden")
			self.canvas.coords(self.green, (x - 1, y - 1))



	def clearBorder(self):
		'''
		@post
			Border is hidden.
		'''

		self.canvas.itemconfig(self.green, state = "hidden")
		self.canvas.itemconfig(self.red, state = "hidden")
		self.canvas.itemconfig(self.yellow, state = "hidden")



	def findImages(self):
		'''
		@post
			Images needed for border are initialized.
		'''

		self.green = self.canvas.find_withtag("green")
		self.red = self.canvas.find_withtag("red")
		self.yellow = self.canvas.find_withtag("yellow")
