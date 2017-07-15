from tkinter import *
from globals import K


class Graphics():

    def __init__(self, root):

        self.k = K()

        self.createWindow(root)

        # create canvas
        self.canvas = Canvas(root)
        self.canvas.pack(expand = 1, fill = BOTH)

        self.loadImages()

        self.createImages()



    def createWindow(self, root):

        root.title("Chess")
        root.minsize(width = self.k.width, height = self.k.height)
        root.maxsize(width = self.k.width, height = self.k.height)



    def loadImages(self):

        self.BoardImage = PhotoImage(file = 'src/board.gif')
        self.GreenBoxImage = PhotoImage(file = 'src/GreenBox.gif')
        self.RedBoxImage = PhotoImage(file = 'src/RedBox.gif')
        self.YellowBoxImage = PhotoImage(file = 'src/YellowBox.gif')
        self.BlackPawnImage = PhotoImage(file = 'src/BlackPawn.gif')
        self.WhitePawnImage = PhotoImage(file = 'src/WhitePawn.gif')
        self.BlackKnightImage = PhotoImage(file = 'src/BlackKnight.gif')
        self.WhiteKnightImage = PhotoImage(file = 'src/WhiteKnight.gif')
        self.BlackKingImage = PhotoImage(file = 'src/BlackKing.gif')
        self.WhiteKingImage = PhotoImage(file = 'src/WhiteKing.gif')
        self.BlackQueenImage = PhotoImage(file = 'src/BlackQueen.gif')
        self.WhiteQueenImage = PhotoImage(file = 'src/WhiteQueen.gif')
        self.BlackRookImage = PhotoImage(file = 'src/BlackRook.gif')
        self.WhiteRookImage = PhotoImage(file = 'src/WhiteRook.gif')
        self.BlackBishopImage = PhotoImage(file = 'src/BlackBishop.gif')
        self.WhiteBishopImage = PhotoImage(file = 'src/WhiteBishop.gif')



    def restart(self):

        self.canvas.delete("all")
        self.createImages()



    def createNewPiece(self, tags, pos):

        if (tags[0] == "blkRook"):
            img = self.BlackRookImage
            newTag = ("token", "black", "rook")
        if (tags[0] == "whtRook"):
            img = self.WhiteRookImage
            newTag = ("token", "white", "rook")
        if (tags[0] == "blkBishop"):
            img = self.BlackBishopImage
            newTag = ("token", "black", "bishop")
        if (tags[0] == "whtBishop"):
            img = self.WhiteBishopImage
            newTag = ("token", "white", "bishop")
        if (tags[0] == "blkQueen"):
            img = self.BlackQueenImage
            newTag = ("token", "black", "queen")
        if (tags[0] == "whtQueen"):
            img = self.WhiteQueenImage
            newTag = ("token", "white", "queen")
        if (tags[0] == "blkKnight"):
            img = self.BlackKnightImage
            newTag = ("token", "black", "knight")
        if (tags[0] == "whtKnight"):
            img = self.WhiteKnightImage
            newTag = ("token", "white", "knight")

        self.canvas.create_image(pos[0] * self.k.space, pos[1] * self.k.space,
        image = img, anchor = "nw", tags = newTags)



    def createImages(self):

        # board
        self.canvas.create_image(0, 0, image = self.BoardImage, anchor = "nw",
                                 state = "disabled")


        #boxes
        self.canvas.create_image(0, 0, image = self.GreenBoxImage, anchor = "nw",
                                 state = "hidden", tags = "green")

        self.canvas.create_image(0, 0, image = self.RedBoxImage, anchor = "nw",
                                 state = "hidden", tags = "red")

        self.canvas.create_image(0, 0, image = self.YellowBoxImage, anchor = "nw",
                                 state = "hidden", tags = "yellow")


        # kings
        self.canvas.create_image(self.k.space * 3, 0, image = self.BlackKingImage,
                                 anchor = "nw", tags = ("token", "black", "king"))

        self.canvas.create_image(self.k.space*3, self.k.space*7, image = self.WhiteKingImage,
                                 anchor = "nw", tags = ("token", "white", "king"))


        # knights
        self.canvas.create_image(self.k.space, 0, image = self.BlackKnightImage,
                                 anchor = "nw", tags = ("token", "black", "knight"))

        self.canvas.create_image(6 * self.k.space, 0, image = self.BlackKnightImage,
                                 anchor = "nw", tags = ("token", "black", "knight"))

        self.canvas.create_image(self.k.space, self.k.space * 7, image = self.WhiteKnightImage,
                                 anchor = "nw", tags = ("token", "white", "knight"))

        self.canvas.create_image(self.k.space * 6, self.k.space * 7, image = self.WhiteKnightImage,
                                 anchor = "nw", tags = ("token", "white", "knight"))


        # queens
        self.canvas.create_image(self.k.space * 4, 0, image = self.BlackQueenImage,
                                 anchor = "nw", tags = ("token", "black", "queen"))

        self.canvas.create_image(self.k.space * 4, self.k.space * 7, image = self.WhiteQueenImage,
                                 anchor = "nw", tags = ("token", "white", "queen"))


        # bishops
        self.canvas.create_image(self.k.space * 2, 0, image = self.BlackBishopImage,
                                 anchor = "nw", tags = ("token", "black", "bishop"))

        self.canvas.create_image(self.k.space * 5, 0, image = self.BlackBishopImage,
                                 anchor = "nw", tags = ("token", "black", "bishop"))

        self.canvas.create_image(self.k.space * 2, self.k.space * 7, image = self.WhiteBishopImage,
                                 anchor = "nw", tags = ("token", "white", "bishop"))

        self.canvas.create_image(self.k.space * 5, self.k.space * 7, image = self.WhiteBishopImage,
                                 anchor = "nw", tags = ("token", "white", "bishop"))


        # rooks
        self.canvas.create_image(0, 0, image = self.BlackRookImage, anchor = "nw",
                                 tags = ("token", "black", "rook"))

        self.canvas.create_image(self.k.space * 7, 0, image = self.BlackRookImage,
                                 anchor = "nw", tags = ("token", "black", "rook"))

        self.canvas.create_image(0, self.k.space * 7, image = self.WhiteRookImage,
                                 anchor = "nw", tags = ("token", "white", "rook"))

        self.canvas.create_image(self.k.space * 7, self.k.space * 7, image = self.WhiteRookImage,
                                 anchor = "nw", tags = ("token", "white", "rook"))


        # pawns
        for i in range(0, self.k.width, self.k.space):

            self.canvas.create_image(i, self.k.space, image = self.BlackPawnImage,
                                     anchor = "nw", tags = ("token", "black", "pawn"))

            self.canvas.create_image(i, 6 * self.k.space, image = self.WhitePawnImage,
                                     anchor = "nw", tags = ("token", "white", "pawn"))


        # menu background
        self.rec = self.canvas.create_rectangle(0, 0, self.k.width, self.k.height,
        fill = "black", state = "hidden", stipple = "gray75", tags = "bg")


        # resume button
        self.canvas.create_text(self.k.width / 2, self.k.height / 3, text = "Resume",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "resumeText")

        self.canvas.create_rectangle(3 * self.k.space,  # origin x
        2.3 * self.k.space,                             # origin y
        5 * self.k.space,                               # destination x
        3 * self.k.space,                               # destination y
        fill = "black", activefill = "gray", tags = "resumeBg", state = "hidden")


        # restart button
        self.canvas.create_text(self.k.width / 2, self.k.height / 2, text = "Restart",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "restartText")

        self.canvas.create_rectangle(3 * self.k.space, 3.65 * self.k.space, 5 * self.k.space,
                                     4.35 * self.k.space, fill = "black", activefill = "gray",
                                     tags = "restartBg", state = "hidden")


        # quit button
        self.canvas.create_text(self.k.width / 2, 2 * self.k.height / 3, text = "Quit",
                                fill = "white", font = ("system", 20), state = "hidden", tags = "quitText")

        self.canvas.create_rectangle(3 * self.k.space, 5 * self.k.space, 5 * self.k.space,
                                     5.7 * self.k.space, fill = "black", activefill = "gray", tags = "quitBg",
                                     state = "hidden")


        # win menu
        self.canvas.create_rectangle(self.k.space, self.k.space, 7 * self.k.space,
                                     7 * self.k.space, fill = "gray", tags = "winBg", state = "hidden")

        self.canvas.create_text(self.k.width / 2, self.k.height / 3, text = "White Wins!",
                                fill = "white", font = ("system", 20), state = "hidden", tags = "whtWin")

        self.canvas.create_text(self.k.width / 2, self.k.height / 3,text = "Black Wins!", fill = "white",
                                font = ("system", 20), state = "hidden", tags = "blkWin")


        # promotion menu background
        self.canvas.create_text(self.k.width / 2, self.k.height / 3, text = "Choose Promotion", fill = "black",
                                font = ("system", 20), state = "hidden", tags = "promotionText")

        self.canvas.create_rectangle(2*self.k.space, 4*self.k.space, 3*self.k.space,5*self.k.space, fill = "gray",
                                     activefill = "white", tags = ("prom", "rookRec"), state = "hidden")

        self.canvas.create_rectangle(3*self.k.space, 4*self.k.space, 4*self.k.space, 5*self.k.space, fill = "gray",
                                     activefill = "white", tags = ("prom", "bishopRec"), state = "hidden")

        self.canvas.create_rectangle(4*self.k.space, 4*self.k.space, 5*self.k.space, 5*self.k.space, fill = "gray",
                                     activefill = "white", tags = ("prom", "queenRec"), state = "hidden")

        self.canvas.create_rectangle(5*self.k.space, 4*self.k.space, 6*self.k.space, 5*self.k.space, fill = "gray",
                                     activefill = "white", tags = ("prom", "knightRec"), state = "hidden")


        # black promotion menu pieces
        self.canvas.create_image(2*self.k.space, 4*self.k.space, image = self.BlackRookImage, anchor = "nw",
                                 tags = "blkRook", state = "hidden")

        self.canvas.create_image(3*self.k.space, 4*self.k.space, image = self.BlackBishopImage, anchor = "nw",
                                 tags = "blkBishop", state = "hidden")

        self.canvas.create_image(4*self.k.space, 4*self.k.space, image = self.BlackQueenImage, anchor = "nw",
                                 tags = "blkQueen", state = "hidden")

        self.canvas.create_image(5*self.k.space, 4*self.k.space, image = self.BlackKnightImage, anchor = "nw",
                                 tags = "blkKnight", state = "hidden")


        # white promotion menu pieces
        self.canvas.create_image(2*self.k.space, 4*self.k.space, image = self.WhiteRookImage, anchor = "nw",
                                 tags = "whtRook", state = "hidden")

        self.canvas.create_image(3*self.k.space, 4*self.k.space, image = self.WhiteBishopImage,
                                 anchor = "nw", tags = "whtBishop", state = "hidden")

        self.canvas.create_image(4*self.k.space, 4*self.k.space, image = self.WhiteQueenImage, anchor = "nw",
                                 tags = "whtQueen", state = "hidden")

        self.canvas.create_image(5*self.k.space, 4*self.k.space, image = self.WhiteKnightImage, anchor = "nw",
                                 tags = "whtKnight", state = "hidden")
