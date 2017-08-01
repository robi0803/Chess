from globals import K


class Interface():

	def __init__(self, graphics):

		# globals
		self.k = K()

		self.graphics = graphics

		# canvas from graphics class
		self.canvas = graphics.canvas



	def checkWin(self, unbind, disableMenu, restart, showMain):
		'''
		Checks for winner and displays win menu.

		@param
			unbind: game.unbind(), removes bindings from pieces
			disableMenu: game.disableMenu(), disables in-game menu
			restart: game.restart(), restarts game,
			showMain: game.showMain(), shows main menu

		@post
			If there is a winner the win menu is displayed.

		'''

		kings = self.canvas.find_withtag("king")

		if (self.canvas.gettags(kings[0])[1] == "white"):
			white = kings[0]
			black = kings[1]
		else:
			black = kings[0]
			white = kings[1]

		if (self.canvas.itemcget(black, "state") == "hidden"):
			self.win(unbind, disableMenu, restart, showMain)
			self.whiteWin()

		if (self.canvas.itemcget(white, "state") == "hidden"):
			self.win(unbind, disableMenu, restart, showMain)
			self.blackWin()



	def win(self, unbind, disableMenu, restart, showMain):
		'''
		@param
			unbind: game.unbind(), removes bindings from pieces
			disableMenu: game.disableMenu(), disables in-game menu
			restart: game.restart(), restarts game,
			showMain: game.showMain(), shows main menu

		@post
			Bindings are removed from pieces and in-game menu. Images for the
			win menu are initialized and the win menu is displayed.
		'''

		unbind()
		disableMenu()
		self.findWinImages()
		self.displayWinMenu(restart, showMain)



	def whiteWin(self):
		'''
		@post
			Title text for a white win is displayed
		'''

		self.canvas.itemconfig(self.whtWin, state = "disabled")
		self.canvas.tag_raise(self.whtWin)



	def blackWin(self):
		'''
		@post
			Title text for a black win is displayed
		'''

		self.canvas.itemconfig(self.blkWin, state = "disabled")
		self.canvas.tag_raise(self.blkWin)



	def displayWinMenu(self, restart, showMain):
		'''
		Displays win menu

		@param
			restart: game.restart(), restarts game,
			showMain: game.showMain(), shows main menu

		@post
			Win menu is displayed and bindings are added for its buttons.
		'''

		self.canvas.itemconfig(self.winBg, state = "disabled")
		self.canvas.itemconfig(self.winRestartText, state = "disabled")
		self.canvas.itemconfig(self.winMainText, state = "disabled")
		self.canvas.itemconfig(self.winQuitText, state = "disabled")

		self.canvas.itemconfig(self.winRestartBg, state = "normal")
		self.canvas.itemconfig(self.winMainBg, state = "normal")
		self.canvas.itemconfig(self.winQuitBg, state = "normal")

		self.canvas.tag_raise(self.winBg)
		self.canvas.tag_raise(self.winRestartBg)
		self.canvas.tag_raise(self.winMainBg)
		self.canvas.tag_raise(self.winQuitBg)
		self.canvas.tag_raise(self.winRestartText)
		self.canvas.tag_raise(self.winMainText)
		self.canvas.tag_raise(self.winQuitText)

		self.canvas.tag_bind("winRestartBg", "<ButtonPress-1>", restart)
		self.canvas.tag_bind("winMainBg", "<ButtonPress-1>", showMain)
		self.canvas.tag_bind("winQuitBg", "<ButtonPress-1>", self.exitGame)



	def findWinImages(self):
		'''
		@post
			Images for win menu are initialized.
		'''

		self.winBg = self.canvas.find_withtag("winBg")
		self.whtWin = self.canvas.find_withtag("whtWin")
		self.blkWin = self.canvas.find_withtag("blkWin")

		self.winRestartText = self.canvas.find_withtag("winRestartText")
		self.winMainText = self.canvas.find_withtag("winMainText")
		self.winQuitText = self.canvas.find_withtag("winQuitText")

		self.winRestartBg = self.canvas.find_withtag("winRestartBg")
		self.winMainBg = self.canvas.find_withtag("winMainBg")
		self.winQuitBg = self.canvas.find_withtag("winQuitBg")



	def menu(self, event, bind, showMenu, restart, main):
		'''
		Shows/Hides in-game menu.

		@param
			event: Tkinter event
			bind: game.bind(), adds bindings to pieces
			showMenu: game.showMenu(), calls interface.menu()
			restart: game.restart(), restarts game,
			main: game.showMain(), shows main menu

		@post
			If menu was hidden, it is now displayed. If menu was displayed, it is
			now hidden.
		'''

		self.findMenuImages()

		if (self.canvas.itemcget(self.menuBg, "state") == "hidden"):

			self.canvas.itemconfig(self.menuBg, state = "disabled")

			self.canvas.itemconfig(self.menuResumeText, state = "disabled")
			self.canvas.itemconfig(self.menuRestartText, state = "disabled")
			self.canvas.itemconfig(self.menuMainText, state = "disabled")
			self.canvas.itemconfig(self.menuQuitText, state = "disabled")

			self.canvas.itemconfig(self.menuResumeBg, state = "normal")
			self.canvas.itemconfig(self.menuRestartBg, state = "normal")
			self.canvas.itemconfig(self.menuMainBg, state = "normal")
			self.canvas.itemconfig(self.menuQuitBg, state = "normal")

			self.canvas.tag_raise(self.menuBg)
			self.canvas.tag_raise(self.menuResumeBg)
			self.canvas.tag_raise(self.menuRestartBg)
			self.canvas.tag_raise(self.menuMainBg)
			self.canvas.tag_raise(self.menuQuitBg)

			self.canvas.tag_raise(self.menuResumeText)
			self.canvas.tag_raise(self.menuRestartText)
			self.canvas.tag_raise(self.menuMainText)
			self.canvas.tag_raise(self.menuQuitText)

			self.canvas.tag_bind("menuResumeBg", "<ButtonPress-1>", showMenu)
			self.canvas.tag_bind("menuRestartBg", "<ButtonPress-1>", restart)
			self.canvas.tag_bind("menuMainBg", "<ButtonPress-1>", main)
			self.canvas.tag_bind("menuQuitBg", "<ButtonPress-1>", self.exitGame)

		else:
			bind()
			self.hideMenu()



	def hideMenu(self):
		'''
		@post
			In-game menu is hidden.
		'''

		self.canvas.itemconfig(self.menuBg, state = "hidden")

		self.canvas.itemconfig(self.menuResumeBg, state = "hidden")
		self.canvas.itemconfig(self.menuRestartBg, state = "hidden")
		self.canvas.itemconfig(self.menuMainBg, state = "hidden")
		self.canvas.itemconfig(self.menuQuitBg, state = "hidden")

		self.canvas.itemconfig(self.menuResumeText, state = "hidden")
		self.canvas.itemconfig(self.menuRestartText, state = "hidden")
		self.canvas.itemconfig(self.menuMainText, state = "hidden")
		self.canvas.itemconfig(self.menuQuitText, state = "hidden")

		self.canvas.tag_unbind("resumeBg", "<ButtonPress-1>")
		self.canvas.tag_unbind("restartBg", "<ButtonPress-1>")
		self.canvas.tag_unbind("quitBg", "<ButtonPress-1>")



	def findMenuImages(self):
		'''
		@post
			In-game menu images are initialized.
		'''

		self.menuBg = self.canvas.find_withtag("menuBg")

		self.menuResumeText = self.canvas.find_withtag("menuResumeText")
		self.menuRestartText = self.canvas.find_withtag("menuRestartText")
		self.menuMainText = self.canvas.find_withtag("menuMainText")
		self.menuQuitText = self.canvas.find_withtag("menuQuitText")

		self.menuResumeBg = self.canvas.find_withtag("menuResumeBg")
		self.menuRestartBg = self.canvas.find_withtag("menuRestartBg")
		self.menuMainBg = self.canvas.find_withtag("menuMainBg")
		self.menuQuitBg = self.canvas.find_withtag("menuQuitBg")



	def mainMenu(self, singlePlayer, multiPlayer):
		'''
		Displays main menu

		@param
			singlePlayer: game.setSinglePlayer(), sets up single player game
			multiPlayer: game.setMultiPlayer(), sets up multiPlayer game

		@post
			Main menu images are initialized, main menu is displayed. Bindings are
			added for main menu buttons.
		'''

		tokens = self.canvas.find_withtag("token")
		self.canvas.itemconfig("token", state = "hidden")

		self.findMainImages()

		self.canvas.itemconfig(self.mainBg, state = "disabled")
		self.canvas.itemconfig(self.winBg, state = "disabled")
		self.canvas.itemconfig(self.titleText, state = "disabled")

		self.canvas.itemconfig(self.mainSingleBg, state = "normal")
		self.canvas.itemconfig(self.mainMultiBg, state = "normal")
		self.canvas.itemconfig(self.mainQuitBg, state = "normal")

		self.canvas.itemconfig(self.mainSingleText, state = "disabled")
		self.canvas.itemconfig(self.mainMutliText, state = "disabled")
		self.canvas.itemconfig(self.mainQuitText, state = "disabled")

		self.canvas.tag_raise(self.mainBg)
		self.canvas.tag_raise(self.winBg)
		self.canvas.tag_raise(self.titleText)

		self.canvas.tag_raise(self.mainSingleBg)
		self.canvas.tag_raise(self.mainMultiBg)
		self.canvas.tag_raise(self.mainQuitBg)

		self.canvas.tag_raise(self.mainSingleText)
		self.canvas.tag_raise(self.mainMutliText)
		self.canvas.tag_raise(self.mainQuitText)

		self.canvas.tag_bind("mainSingleBg", "<ButtonPress-1>", singlePlayer)
		self.canvas.tag_bind("mainMultiBg", "<ButtonPress-1>", multiPlayer)
		self.canvas.tag_bind("mainQuitBg", "<ButtonPress-1>", self.exitGame)



	def hideMain(self):
		'''
		@post
			Bindings for main menu are removed, main menu is hidden.
		'''

		self.canvas.itemconfig(self.winBg, state = "hidden")
		self.canvas.itemconfig(self.mainBg, state = "hidden")
		self.canvas.itemconfig(self.titleText, state = "hidden")

		self.canvas.itemconfig(self.mainSingleBg, state = "hidden")
		self.canvas.itemconfig(self.mainMultiBg, state = "hidden")
		self.canvas.itemconfig(self.mainQuitBg, state = "hidden")

		self.canvas.itemconfig(self.mainSingleText, state = "hidden")
		self.canvas.itemconfig(self.mainMutliText, state = "hidden")
		self.canvas.itemconfig(self.mainQuitText, state = "hidden")

		self.canvas.tag_unbind("mainSingleBg", "<ButtonPress-1>")
		self.canvas.tag_unbind("mainMultiBg", "<ButtonPress-1>")
		self.canvas.tag_unbind("mainQuitBg", "<ButtonPress-1>")

		tokens = self.canvas.find_withtag("token")
		self.canvas.itemconfig("token", state = "normal")



	def findMainImages(self):
		'''
		@post
			Main menu images are initialized.
		'''

		self.winBg = self.canvas.find_withtag("winBg")
		self.mainBg = self.canvas.find_withtag("mainBg")
		self.titleText = self.canvas.find_withtag("titleText")

		self.mainSingleBg = self.canvas.find_withtag("mainSingleBg")
		self.mainMultiBg = self.canvas.find_withtag("mainMultiBg")
		self.mainQuitBg = self.canvas.find_withtag("mainQuitBg")

		self.mainSingleText = self.canvas.find_withtag("mainSingleText")
		self.mainMutliText = self.canvas.find_withtag("mainMutliText")
		self.mainQuitText = self.canvas.find_withtag("mainQuitText")



	def exitGame(self, event):
		'''
		@post
			Game is closed.
		'''

		exit()
