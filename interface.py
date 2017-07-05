from globals import K


class Interface():

    def __init__(self, canvas):

        # globals
        self.k = K()

        # canvas from graphics class
        self.canvas = canvas

        # menu background
        self.rec = self.canvas.create_rectangle(0, 0, self.k.width, self.k.height, fill = "black",
                                                state = "hidden", stipple = "gray75")

        # resume button
        self.resumeText = self.canvas.create_text(self.k.width / 2, self.k.height / 3, text = "Resume",
                                              fill = "white", font = ("system", 20), state = "hidden")

        self.resumeBg = self.canvas.create_rectangle(3 * self.k.space,   # origin x
                                                     2.3 * self.k.space, # origin y
                                                     5 * self.k.space,   # destination x
                                                     3 * self.k.space,   # destination y
                                                     fill = "black", activefill = "gray",
                                                     state = "hidden")

        # restart button
        self.restartText = self.canvas.create_text(self.k.width / 2, 2 * self.k.height / 3, text = "Restart",
                                              fill = "white", font = ("system", 20), state = "hidden")

        self.restartBg = self.canvas.create_rectangle(3 * self.k.space,   # origin x
                                                     5 * self.k.space, # origin y
                                                     5 * self.k.space,   # destination x
                                                     5.7 * self.k.space,   # destination y
                                                     fill = "black", activefill = "gray",
                                                     state = "hidden")


    def checkWin(self):

    	kings = self.canvas.find_withtag("king")

        if (self.canvas.gettags(kings[0])[1] == "white"):
			white = kings[0]
			black = kings[1]
        else:
			black = kings[0]
			white = kings[1]

        if (self.canvas.itemcget(black, "state") == "hidden"):
    		self.whiteWin()

        if (self.canvas.itemcget(white, "state") == "hidden"):
    		self.blackWin()



    def whiteWin(self):

        self.canvas.create_text((self.k.width / 2, self.k.height / 2),
    		 					 text = "White Wins!")



    def blackWin(self):

        self.canvas.create_text((self.k.width / 2, self.k.height / 2),
    		 					 text = "Black Wins!")



    def menu(self):

        if (self.canvas.itemcget(self.rec, "state") == "hidden"):
            self.canvas.itemconfig(self.rec, state = "disabled")
            self.canvas.itemconfig(self.resumeText, state = "disabled")
            self.canvas.itemconfig(self.resumeBg, state = "normal")
            self.canvas.itemconfig(self.restartText, state = "disabled")
            self.canvas.itemconfig(self.restartBg, state = "normal")
            self.canvas.tag_raise(self.rec)
            self.canvas.tag_raise(self.resumeBg)
            self.canvas.tag_raise(self.resumeText)
            self.canvas.tag_raise(self.restartBg)
            self.canvas.tag_raise(self.restartText)

        else:
            self.canvas.itemconfig(self.rec, state = "hidden")
            self.canvas.itemconfig(self.resumeBg, state = "hidden")
            self.canvas.itemconfig(self.resumeText, state = "hidden")
            self.canvas.itemconfig(self.restartBg, state = "hidden")
            self.canvas.itemconfig(self.restartText, state = "hidden")
