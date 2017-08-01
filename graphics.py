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
        '''
        @param
            root: Tkinter root

        @post
            Window has been created
        '''

        root.title("Chess")
        root.minsize(width = self.k.width, height = self.k.height)
        root.maxsize(width = self.k.width, height = self.k.height)



    def loadImages(self):
        '''
        @post
            Images have been loaded
        '''

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
        '''
        @post
            All images have been deleted and recreated.
        '''

        self.canvas.delete("all")
        self.createImages()



    def createNewPiece(self, tags, pos):
        '''
        Used to promote pawn.

        @param
            tags: tags of piece to create
            pos: position of new piece

        @post
            New piece has been created.
        '''

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
        image = img, anchor = "nw", tags = newTag)



    def createImages(self):
        '''
        @post
            All images used throughout the game are created.
        '''

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
        self.canvas.create_image(4*self.k.space, 0, image = self.BlackKingImage,
                                 anchor = "nw", tags = ("token", "black", "king", "blackKing"))

        self.canvas.create_image(4*self.k.space, self.k.space*7, image = self.WhiteKingImage,
                                 anchor = "nw", tags = ("token", "white", "king", "whiteKing"))


        # knights
        self.canvas.create_image(1*self.k.space, 0, image = self.BlackKnightImage,
                                 anchor = "nw", tags = ("token", "black", "knight"))

        self.canvas.create_image(6*self.k.space, 0, image = self.BlackKnightImage,
                                 anchor = "nw", tags = ("token", "black", "knight"))

        self.canvas.create_image(self.k.space, self.k.space * 7, image = self.WhiteKnightImage,
                                 anchor = "nw", tags = ("token", "white", "knight"))

        self.canvas.create_image(self.k.space * 6, self.k.space * 7, image = self.WhiteKnightImage,
                                 anchor = "nw", tags = ("token", "white", "knight"))


        # queens
        self.canvas.create_image(3*self.k.space, 0, image = self.BlackQueenImage,
                                 anchor = "nw", tags = ("token", "black", "queen"))

        self.canvas.create_image(3*self.k.space, self.k.space * 7, image = self.WhiteQueenImage,
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
                                 anchor = "nw", tags = ("token", "black", "rook", "castleBlack"))

        self.canvas.create_image(0, self.k.space * 7, image = self.WhiteRookImage,
                                 anchor = "nw", tags = ("token", "white", "rook"))

        self.canvas.create_image(self.k.space * 7, self.k.space * 7, image = self.WhiteRookImage,
                                 anchor = "nw", tags = ("token", "white", "rook", "castleWhite"))


        # pawns
        for i in range(0, self.k.width, self.k.space):

            self.canvas.create_image(i, self.k.space, image = self.BlackPawnImage,
                                     anchor = "nw", tags = ("token", "black", "pawn"))

            self.canvas.create_image(i, 6 * self.k.space, image = self.WhitePawnImage,
                                     anchor = "nw", tags = ("token", "white", "pawn"))


        # main menu
        self.rec = self.canvas.create_rectangle(0, 0, self.k.width, self.k.height,
                                                fill = "black", stipple = "gray25",
                                                state = "hidden", tags = "mainBg", )

        self.canvas.create_text(self.k.width/2, self.k.height/4, text = "Chess",
                                fill = "white", font = ("Times", 40), state = "hidden",
                                tags = "titleText")

        self.canvas.create_rectangle(2 * self.k.space, 3 * self.k.space, 6 * self.k.space,
                                     3.7 * self.k.space, fill = "black", activefill = "gray",
                                     state = "hidden", tags = "mainSingleBg")

        self.canvas.create_rectangle(2 * self.k.space, 4.35 * self.k.space, 6 * self.k.space,
                                     5.05 * self.k.space, fill = "black", activefill = "gray",
                                     state = "hidden",  tags = "mainMultiBg")

        self.canvas.create_rectangle(2 * self.k.space, 5.7 * self.k.space, 6 * self.k.space,
                                     6.35 * self.k.space, fill = "black", activefill = "gray",
                                     state = "hidden", tags = "mainQuitBg",)

        self.canvas.create_text(self.k.width / 2, 3.35 * self.k.space, text = "Single-Player",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "mainSingleText")

        self.canvas.create_text(self.k.width / 2, 4.7 * self.k.space, text = "Multi-Player",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "mainMutliText")

        self.canvas.create_text(self.k.width / 2, 6.05 * self.k.space, text = "Quit",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "mainQuitText")


        # in-game menu
        self.rec = self.canvas.create_rectangle(0, 0, self.k.width, self.k.height,
                                                fill = "black", state = "hidden",
                                                stipple = "gray75", tags = "menuBg")

        self.canvas.create_text(self.k.width/2, 1.85*self.k.space, text = "Resume",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "menuResumeText")

        self.canvas.create_rectangle(2.5*self.k.space,    # origin x
                                     1.5*self.k.space,  # origin y
                                     5.5*self.k.space,    # destination x
                                     2.2*self.k.space,    # destination y
                                     fill = "black", activefill = "gray", state = "hidden",
                                     tags = "menuResumeBg")

        self.canvas.create_text(self.k.width/2, 3.2*self.k.space, text = "Restart",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "menuRestartText")

        self.canvas.create_rectangle(2.5*self.k.space, 2.85*self.k.space, 5.5*self.k.space,
                                     3.55*self.k.space, fill = "black", activefill = "gray",
                                     state = "hidden", tags = "menuRestartBg")

        self.canvas.create_text(self.k.width/2, 4.55*self.k.space, text = "Main Menu",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "menuMainText")

        self.canvas.create_rectangle(2.5*self.k.space, 4.2*self.k.space, 5.5*self.k.space,
                                     4.9*self.k.space, fill = "black", activefill = "gray",
                                     tags = "menuMainBg", state = "hidden")

        self.canvas.create_text(self.k.width/2, 5.9*self.k.space, text = "Quit",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "menuQuitText")

        self.canvas.create_rectangle(2.5*self.k.space, 5.55*self.k.space, 5.5*self.k.space,
                                     6.25*self.k.space, fill = "black", activefill = "gray",
                                     state = "hidden", tags = "menuQuitBg",)


        # win menu
        self.canvas.create_rectangle(self.k.space, self.k.space, 7*self.k.space,
                                     7*self.k.space, fill = "gray", state = "hidden",
                                     tags = "winBg")

        self.canvas.create_text(self.k.width/2, 2.2*self.k.space, text = "White Wins!",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "whtWin")

        self.canvas.create_text(self.k.width/2, 2.2*self.k.space, text = "Black Wins!",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "blkWin")

        self.canvas.create_text(self.k.width/2, 3.4*self.k.space, text = "Restart",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "winRestartText")

        self.canvas.create_rectangle(2.5*self.k.space, 3.05*self.k.space, 5.5*self.k.space,
                                     3.75*self.k.space, fill = "black", activefill = "gray",
                                     state = "hidden", tags = "winRestartBg")

        self.canvas.create_text(self.k.width/2, 4.55*self.k.space, text = "Main Menu",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "winMainText")

        self.canvas.create_rectangle(2.5*self.k.space, 4.2*self.k.space, 5.5*self.k.space,
                                     4.9*self.k.space, fill = "black", activefill = "gray",
                                     state = "hidden", tags = "winMainBg")

        self.canvas.create_text(self.k.width/2, 5.7*self.k.space, text = "Quit",
                                fill = "white", font = ("system", 20), state = "hidden",
                                tags = "winQuitText")

        self.canvas.create_rectangle(2.5*self.k.space, 5.35*self.k.space, 5.5*self.k.space,
                                     6.05*self.k.space, fill = "black", activefill = "gray",
                                     state = "hidden", tags = "winQuitBg")


        # promotion menu background
        self.canvas.create_text(self.k.width / 2, self.k.height / 3, text = "Choose Promotion",
                                fill = "black", font = ("system", 20), state = "hidden",
                                tags = "promotionText")

        self.canvas.create_rectangle(2*self.k.space, 4*self.k.space, 3*self.k.space,5*self.k.space,
                                     fill = "gray", activefill = "white", tags = ("prom", "rookRec"),
                                     state = "hidden")

        self.canvas.create_rectangle(3*self.k.space, 4*self.k.space, 4*self.k.space, 5*self.k.space,
                                     fill = "gray", activefill = "white", tags = ("prom", "bishopRec"),
                                     state = "hidden")

        self.canvas.create_rectangle(4*self.k.space, 4*self.k.space, 5*self.k.space, 5*self.k.space,
                                     fill = "gray", activefill = "white", tags = ("prom", "queenRec"),
                                     state = "hidden")

        self.canvas.create_rectangle(5*self.k.space, 4*self.k.space, 6*self.k.space, 5*self.k.space,
                                     fill = "gray", activefill = "white", tags = ("prom", "knightRec"),
                                     state = "hidden")


        # black promotion menu pieces
        self.canvas.create_image(2*self.k.space, 4*self.k.space, image = self.BlackRookImage,
                                 anchor = "nw", tags = "blkRook", state = "hidden")

        self.canvas.create_image(3*self.k.space, 4*self.k.space, image = self.BlackBishopImage,
                                 anchor = "nw", tags = "blkBishop", state = "hidden")

        self.canvas.create_image(4*self.k.space, 4*self.k.space, image = self.BlackQueenImage,
                                 anchor = "nw", tags = "blkQueen", state = "hidden")

        self.canvas.create_image(5*self.k.space, 4*self.k.space, image = self.BlackKnightImage,
                                 anchor = "nw", tags = "blkKnight", state = "hidden")


        # white promotion menu pieces
        self.canvas.create_image(2*self.k.space, 4*self.k.space, image = self.WhiteRookImage,
                                 anchor = "nw", tags = "whtRook", state = "hidden")

        self.canvas.create_image(3*self.k.space, 4*self.k.space, image = self.WhiteBishopImage,
                                 anchor = "nw", tags = "whtBishop", state = "hidden")

        self.canvas.create_image(4*self.k.space, 4*self.k.space, image = self.WhiteQueenImage,
                                 anchor = "nw", tags = "whtQueen", state = "hidden")

        self.canvas.create_image(5*self.k.space, 4*self.k.space, image = self.WhiteKnightImage,
                                 anchor = "nw", tags = "whtKnight", state = "hidden")
