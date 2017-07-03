from globals import K


class Interface():

    def __init__(self, canvas):

        # globals
        self.k = K()

        # canvas from graphics class
        self.canvas = canvas

        # menu background
        self.rec = self.canvas.create_rectangle(0, 0, self.k.height, self.k.width, fill = "black",
                                                state = "hidden", stipple = "gray75")



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
            self.canvas.tag_raise(self.rec)
        else:
            self.canvas.itemconfig(self.rec, state = "hidden")
