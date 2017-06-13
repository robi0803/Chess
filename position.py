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
                    self.board[x][y] = (tags[1], tags[2], piece)
                else : self.board[x][y] = "none"

                y += 1
            x += 1



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

        elif (self.occupied(tags, pos2)): check = False

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

        if (tags[1] == self.board[pos[0]][pos[1]][0]):
            check = True
        else:
            check = False

        return check

        '''


    def pathBlocked(self, pos1, pos2):

        check = True

        if (pos1[0] == pos2[0]):
            i = pos1[1]
            while (check and i < pos2[1] ):
                if ()

        '''


    def pawn(self, tags, pos1, pos2):

        check = False

        if (tags[1] == "black"):
            if (pos1[1] == pos2[1] - 1 and
                pos1[0] == pos2[0]):
                    check = True

            if (pos1[1] == pos2[1] - 1
                and
               (pos1[0] == pos2[0] - 1 or
                pos1[0] == pos2[0] + 1)
                and
               (self.board[pos2[0]][pos2[1]][0] == "white") ):
                    check = True

            if (pos1[1] == 1):
                if (pos1[1] == pos2[1] - 2 and
                    pos1[0] == pos2[0]):
                        check = True

        if (tags[1] == "white"):
            if (pos1[1] == pos2[1] + 1 and
                pos1[0] == pos2[0]):
                    check = True

            if (pos1[1] == pos2[1] + 1
                and
               (pos1[0] == pos2[0] - 1 or
                pos1[0] == pos2[0] + 1)
                and
               (self.board[pos2[0]][pos2[1]][0] == "black") ):
                    check = True

            if (pos1[1] == 6):
                if (pos1[1] == pos2[1] + 2 and
                    pos1[0] == pos2[0]):
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

        if (((pos1[1] == pos2[1] - 2 or
              pos1[1] == pos2[1] + 2)
              and
             (pos1[0] == pos2[0] - 1 or
              pos1[0] == pos2[0] + 1))
            or
            ((pos1[0] == pos2[0] - 2 or
              pos1[0] == pos2[0] + 2)
              and
             (pos1[1] == pos2[1] - 1 or
              pos1[1] == pos2[1] + 1)) ):
                check = True

        return check



    def bishop(self, tags, pos1, pos2):

        check = False

        for i in range(0, 8):
            if ((pos1[0] == pos2[0] + i or
                 pos1[0] == pos2[0] - i)
                 and
                (pos1[1] == pos2[1] + i or
                 pos1[1] == pos2[1] - i) ):
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

        if ((pos1[0] == pos2[0] + 1 or
             pos1[0] == pos2[0] - 1 or
             pos1[0] == pos2[0])
             and
            (pos1[1] == pos2[1] + 1 or
             pos1[1] == pos2[1] - 1 or
             pos1[1] == pos2[1]) ):
                check = True

        return check
