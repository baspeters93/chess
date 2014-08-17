"""
Pieces are named using the Forsyth-Edwards Notation (FEN):
    - Pieces are named using their first letter (K for King, Q for Queen but N for kNight)
    - White pieces are given an uppercase notation
"""
#base class Piece containing most of the common functions
class Piece(object):

    def __init__(self, color, position, board):

        self.position = position
        self.color = color
        self.movesMade = 0
        self.possibleMoves = []
        self.board = board

        self.setPossibleMoves()

        #set name of piece in compliance to FEN
        pieceName = self.__class__.__name__
        if self.color == "white":
            self.name = pieceName[:1]
        else:
            self.name = pieceName.lower()[:1]

    def __str__(self):

        return self.name

    def move(self, to):

        if to in self.possibleMoves:
            self.board[(self.position)] == None
            self.board[to] == self

class Pawn(Piece):

    def setPossibleMoves(self):

        """
        Pawns can advance two squares the first time they move and hit a piece that is adjacent to them.
        The biggest difference between pawns and the other pieces is that pawns can move in only one direction,
        therefore it is necessary to make a distinction based on the piece color
        """
        #TODO: Fix incredibly ugly checks and gazillion ifs
        row, col = self.position[0], self.position[1]
        if self.color == "white":
            if self.movesMade == 0:
                self.possibleMoves.extend([(row+2, col), (row+1, col)])

            #check for presence of black piece on upper right side of pawn
            if self.board[(row + 1, chr(ord(col) + 1))] is not None:
                if self.board[(row + 1, chr(ord(col) + 1))].color is not self.color:
                    self.possibleMoves.extend([(row + 1, chr(ord(col) + 1))])

            if self.board[(row + 1, chr(ord(col) - 1))] is not None:
                if self.board[(row + 1, chr(ord(col) - 1))].color is not self.color:
                    self.possibleMoves.extend([(row + 1, chr(ord(col) - 1))])

        #TODO: Implement black pawn checks


class Rook(Piece):

    def test(self):

        pass

class Knight(Piece):

    def test(self):

        pass

class Bishop(Piece):

    def test(self):

        pass


class King(Piece):

    def test(self):

        pass

    def canCastle(self):

        if self.movesMade is not 0:
            return False
        else:
            return True


class Queen(Piece):

    def test(self):

        pass

