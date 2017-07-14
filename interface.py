from globals import K


class Interface():

	def __init__(self, graphics):

		# globals
		self.k = K()

		self.graphics = graphics

		# canvas from graphics class
		self.canvas = graphics.canvas



	def checkWin(self, unbind, restart):

		kings = self.canvas.find_withtag("king")

		if (self.canvas.gettags(kings[0])[1] == "white"):
			white = kings[0]
			black = kings[1]
		else:
			black = kings[0]
			white = kings[1]

		if (self.canvas.itemcget(black, "state") == "hidden"):
			unbind()
			self.whiteWin(restart)

		if (self.canvas.itemcget(white, "state") == "hidden"):
			unbind()
			self.blackWin(restart)



	def whiteWin(self, restart):

		self.findImages()

		self.canvas.itemconfig(self.winBg, state = "disabled")
		self.canvas.itemconfig(self.whtWin, state = "disabled")
		self.canvas.itemconfig(self.restartText, state = "disabled")
		self.canvas.itemconfig(self.restartBg, state = "normal")
		self.canvas.itemconfig(self.quitText, state = "disabled")
		self.canvas.itemconfig(self.quitBg, state = "normal")
		self.canvas.tag_raise(self.winBg)
		self.canvas.tag_raise(self.whtWin)
		self.canvas.tag_raise(self.restartBg)
		self.canvas.tag_raise(self.restartText)
		self.canvas.tag_raise(self.quitBg)
		self.canvas.tag_raise(self.quitText)

		self.canvas.tag_bind("restartBg", "<ButtonPress-1>", restart)
		self.canvas.tag_bind("quitBg", "<ButtonPress-1>", self.exitGame)



	def blackWin(self, restart):

		self.findImages()

		self.canvas.itemconfig(self.winBg, state = "disabled")
		self.canvas.itemconfig(self.blkWin, state = "disabled")
		self.canvas.itemconfig(self.restartText, state = "disabled")
		self.canvas.itemconfig(self.restartBg, state = "normal")
		self.canvas.itemconfig(self.quitText, state = "disabled")
		self.canvas.itemconfig(self.quitBg, state = "normal")
		self.canvas.tag_raise(self.winBg)
		self.canvas.tag_raise(self.blkWin)
		self.canvas.tag_raise(self.restartBg)
		self.canvas.tag_raise(self.restartText)
		self.canvas.tag_raise(self.quitBg)
		self.canvas.tag_raise(self.quitText)

		self.canvas.tag_bind("restartBg", "<ButtonPress-1>", restart)
		self.canvas.tag_bind("quitBg", "<ButtonPress-1>", self.exitGame)



	def menu(self, event, bind, showMenu, restart):

		self.findImages()

		if (self.canvas.itemcget(self.bg, "state") == "hidden"):

			self.canvas.itemconfig(self.bg, state = "disabled")
			self.canvas.itemconfig(self.resumeText, state = "disabled")
			self.canvas.itemconfig(self.resumeBg, state = "normal")
			self.canvas.itemconfig(self.restartText, state = "disabled")
			self.canvas.itemconfig(self.restartBg, state = "normal")
			self.canvas.itemconfig(self.quitText, state = "disabled")
			self.canvas.itemconfig(self.quitBg, state = "normal")
			self.canvas.tag_raise(self.bg)
			self.canvas.tag_raise(self.resumeBg)
			self.canvas.tag_raise(self.resumeText)
			self.canvas.tag_raise(self.restartBg)
			self.canvas.tag_raise(self.restartText)
			self.canvas.tag_raise(self.quitBg)
			self.canvas.tag_raise(self.quitText)

			self.canvas.tag_bind("resumeBg", "<ButtonPress-1>", showMenu)
			self.canvas.tag_bind("restartBg", "<ButtonPress-1>", restart)
			self.canvas.tag_bind("quitBg", "<ButtonPress-1>", self.exitGame)

		else:
			bind()
			self.hide(event)



	def hide(self, event):

		self.canvas.itemconfig(self.bg, state = "hidden")
		self.canvas.itemconfig(self.resumeBg, state = "hidden")
		self.canvas.itemconfig(self.resumeText, state = "hidden")
		self.canvas.itemconfig(self.restartBg, state = "hidden")
		self.canvas.itemconfig(self.restartText, state = "hidden")
		self.canvas.itemconfig(self.quitBg, state = "hidden")
		self.canvas.itemconfig(self.quitText, state = "hidden")

		self.canvas.tag_unbind("resumeBg", "<ButtonPress-1>")
		self.canvas.tag_unbind("restartBg", "<ButtonPress-1>")
		self.canvas.tag_unbind("quitBg", "<ButtonPress-1>")



	def findImages(self):

		self.bg = self.canvas.find_withtag("bg")
		self.resumeText = self.canvas.find_withtag("resumeText")
		self.resumeBg = self.canvas.find_withtag("resumeBg")
		self.restartText = self.canvas.find_withtag("restartText")
		self.restartBg = self.canvas.find_withtag("restartBg")
		self.quitText = self.canvas.find_withtag("quitText")
		self.quitBg = self.canvas.find_withtag("quitBg")
		self.winBg = self.canvas.find_withtag("winBg")
		self.whtWin = self.canvas.find_withtag("whtWin")
		self.blkWin = self.canvas.find_withtag("blkWin")

	def exitGame(self, event):

		exit()
