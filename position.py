from Tkinter import *
from globals import K


class Position():

    def __init__(self):

        self.k = K()

        self.board = [[ "none" for j in xrange(0, 8)] for i in xrange(0, 8) ]



    def update(self, canvas):

        x = 0
        for i in range(10, self.k.width + 10, self.k.space):
            y = 0
            for j in range(10, self.k.height + 10, self.k.space):

                piece = canvas.find_closest(i, j)
                coords = canvas.coords(piece)
                tags = canvas.gettags(piece)

                if (len(tags) >= 3):
                    self.board[x][y] = (piece, tags[1], tags[2])
                else : self.board[x][y] = "none"

                y += 1
            x += 1



    def capture(self, canvas, pos, tags):

        x = pos[0]
        y = pos[1]

        #if there is a piece and it is a different color
        if (len(self.board[x][y]) >= 2 and
           (self.board[x][y][1] != tags[1]) ):

            canvas.itemconfig(self.board[x][y][0], state = "hidden")



    def getPosition(self, px, py):

        x = y = None
        for i in xrange(0, 8):
            if ((px <  (self.k.space * (i + 1) - 30)) and
                (px >= (self.k.space) * i - 30) ):
                    x = i
            if ((py <  (self.k.space * (i + 1) - 7)) and
                (py >= (self.k.space * i - 54)) ):
                    y = i

        return (x, y)



    def canMove(self, tags, pos1, pos2):

        check = False

        if (pos1 == pos2): check = True

        elif (self.pathBlocked(pos1, pos2) ): check = False

        elif (self.occupied(tags, pos2) ): check = False

        elif (tags[2] == "pawn"):
            check = self.pawn(tags, pos1, pos2)

        elif (tags[2] == "rook"):
            check = self.rook(tags, pos1, pos2)

        elif (tags[2] == "knight"):
            check = self.knight(tags, pos1, pos2)

        elif (tags[2] == "bishop"):
            check = self.bishop(tags, pos1, pos2)

        elif (tags[2] == "queen"):
            check = self.queen(tags, pos1, pos2)

        elif (tags[2] == "king"):
            check = self.king(tags, pos1, pos2)

        return check



    def occupied(self, tags, pos):

        if (tags[1] == self.board[pos[0]][pos[1]][1]):
            check = True
        else:
            check = False

        return check



    def pathBlocked(self, pos1, pos2):

        check = False

        if (pos1[0] == pos2[0] or pos1[1] == pos2[1]):
            check = self.rookPath(pos1, pos2)
        if (abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1]) ):
            check = self.bishopPath(pos1, pos2)

        return check



    def rookPath(self, pos1, pos2):

        check = False

        above = pos2[1] - pos1[1] < 0 and pos1[0] == pos2[0]
        below = pos2[1] - pos1[1] > 0 and pos1[0] == pos2[0]
        right = pos2[0] - pos1[0] > 0 and pos1[1] == pos2[1]
        left  = pos2[0] - pos1[0] < 0 and pos1[1] == pos2[1]

        #horizontal check
        x = pos1[0] + 1
        y = pos1[1]

        while (not check and x < pos2[0] and right):
            if (self.board[x][y] != "none"):
                check = True
            x += 1

        x = pos1[0] - 1

        while (not check and x > pos2[0] and left):
            if (self.board[x][y] != "none"):
                check = True
            x -= 1

        #vertical check
        x = pos1[0]
        y = pos1[1] - 1

        while (not check and y > pos2[1] and above):
            if (self.board[x][y] != "none"):
                check = True
            y -= 1

        y = pos1[1] + 1

        while (not check and y < pos2[1] and below):
            if (self.board[x][y] != "none"):
                check = True
            y += 1

        return check



    def bishopPath(self, pos1, pos2):

        check = False

        west = pos2[0] - pos1[0] < 0
        east = pos2[0] - pos1[0] > 0
        north = pos2[1] - pos1[1] < 0
        south = pos2[1] - pos1[1] > 0

        #southeast
        x = pos1[0] + 1
        y = pos1[1] + 1

        while (not check and x < pos2[0] and south and east):
            if (self.board[x][y] != "none"):
                check = True
            x += 1
            y += 1

        #northeast
        x = pos1[0] + 1
        y = pos1[1] - 1

        while (not check and x < pos2[0] and north and east):
            if (self.board[x][y] != "none"):
                check = True
            x += 1
            y -= 1

        #northwest
        x = pos1[0] - 1
        y = pos1[1] - 1

        while (not check and x > pos2[0] and north and west):
            if (self.board[x][y] != "none"):
                check = True
            x -= 1
            y -= 1

        #southwest
        x = pos1[0] - 1
        y = pos1[1] + 1

        while (not check and x > pos2[0] and south and west):
            if (self.board[x][y] != "none"):
                check = True
            x -= 1
            y += 1

        return check



    def pawn(self, tags, pos1, pos2):

        check = False

        below = pos2[1] - pos1[1] == 1
        above = pos2[1] - pos1[1] == -1
        right = pos2[0] - pos1[0] == 1
        left = pos2[0] - pos1[0] == -1
        inCol = pos1[0] == pos2[0]

        if (tags[1] == "black"):
            if (below and inCol):
                check = True

            if (below and (right or left) and
               self.board[pos2[0]][pos2[1]][0] == "white" ):
                    check = True

            if (pos1[1] == 1):
                if (pos2[1] - pos1[1] == 2 and inCol):
                    check = True

        if (tags[1] == "white"):
            if (above and inCol):
                check = True

            if (above and (right or left) and
               (self.board[pos2[0]][pos2[1]][0] == "black") ):
                    check = True

            if (pos1[1] == 6):
                if (pos2[1] - pos1[1] == -2 and inCol):
                    check = True

        return check



    def rook(self, tags, pos1, pos2):

        check = False

        if ( (pos1[0] == pos2[0] and pos1[1] != pos2[1]) or
             (pos1[0] != pos2[0] and pos1[1] == pos2[1]) ):
                 check = True;

        return check



    def knight(self, tags, pos1, pos2):

        check = False

        if ((abs(pos2[1] - pos1[1]) == 2 and abs(pos2[0] - pos1[0]) == 1) or
            (abs(pos2[0] - pos1[0]) == 2 and abs(pos2[1] - pos1[1]) == 1) ):
                check = True

        return check



    def bishop(self, tags, pos1, pos2):

        check = False

        if (abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1]) ):
            check = True

        return check



    def queen(self, tags, pos1, pos2):

        check = False

        check = self.rook(tags, pos1, pos2)

        if (not check):
            check = self.bishop(tags, pos1, pos2)

        return check



    def king(self, tags, pos1, pos2):

        check = False

        if ((abs(pos2[0] - pos1[0]) == 1 or pos1[0] == pos2[0]) and
            (abs(pos2[1] - pos1[1]) == 1 or pos1[1] == pos2[1]) ):
                check = True

        return check
