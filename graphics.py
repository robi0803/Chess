from Tkinter import *
from globals import K


class Graphics():

    def __init__(self, root):

        self.k = K()

        self.createWindow(root)

        self.loadImages()

        self.createImages(root)



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



    def createImages(self, root):

        # create canvas
        self.canvas = Canvas(root)
        self.canvas.pack(expand = 1, fill = BOTH)

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
                                 anchor = "nw", tags = ("token", "black", "king") )

        self.canvas.create_image(self.k.space * 3, self.k.space * 7,
                                 image = self.WhiteKingImage,
                                 anchor = "nw", tags = ("token", "white", "king") )

        # knights
        self.canvas.create_image(self.k.space, 0, image = self.BlackKnightImage,
                                 anchor = "nw", tags = ("token", "black", "knight") )

        self.canvas.create_image(6 * self.k.space, 0,
                                 image = self.BlackKnightImage, anchor = "nw",
                                 tags = ("token", "black", "knight") )

        self.canvas.create_image(self.k.space, self.k.space * 7,
                                 image = self.WhiteKnightImage, anchor = "nw",
                                 tags = ("token", "white", "knight") )

        self.canvas.create_image(self.k.space * 6, self.k.space * 7,
                                 image = self.WhiteKnightImage, anchor = "nw",
                                 tags = ("token", "white", "knight") )

        # queens
        self.canvas.create_image(self.k.space * 4, 0, image = self.BlackQueenImage,
                                 anchor = "nw", tags = ("token", "black", "queen") )

        self.canvas.create_image(self.k.space * 4, self.k.space * 7,
                                 image = self.WhiteQueenImage, anchor = "nw",
                                 tags = ("token", "white", "queen") )

        # bishops
        self.canvas.create_image(self.k.space * 2, 0, image = self.BlackBishopImage,
                                 anchor = "nw", tags = ("token", "black", "bishop") )

        self.canvas.create_image(self.k.space * 5, 0, image = self.BlackBishopImage,
                                 anchor = "nw", tags = ("token", "black", "bishop") )

        self.canvas.create_image(self.k.space * 2, self.k.space * 7,
                                 image = self.WhiteBishopImage, anchor = "nw",
                                 tags = ("token", "white", "bishop") )

        self.canvas.create_image(self.k.space * 5, self.k.space * 7,
                                 image = self.WhiteBishopImage, anchor = "nw",
                                 tags = ("token", "white", "bishop") )

        # rooks
        self.canvas.create_image(0, 0, image = self.BlackRookImage, anchor = "nw",
                                 tags = ("token", "black", "rook") )

        self.canvas.create_image(self.k.space * 7, 0, image = self.BlackRookImage,
                                 anchor = "nw", tags = ("token", "black", "rook") )

        self.canvas.create_image(0, self.k.space * 7, image = self.WhiteRookImage,
                                 anchor = "nw", tags = ("token", "white", "rook") )

        self.canvas.create_image(self.k.space * 7, self.k.space * 7,
                                 image = self.WhiteRookImage, anchor = "nw",
                                 tags = ("token", "white", "rook") )
        # pawns
        for i in range(0, self.k.width, self.k.space):
            self.canvas.create_image(i, self.k.space, image = self.BlackPawnImage,
                                     anchor = "nw", tags = ("token", "black", "pawn") )

            self.canvas.create_image(i, 6 * self.k.space, image = self.WhitePawnImage,
                                     anchor = "nw", tags = ("token", "white", "pawn") )
