import piece

from itertools import product

class Chessboard(object):

    def __init__(self):

        colors = ["black, white"]
        #create the default dict that represents the board
        self.board = dict()

        columns = map(chr, range(97,105))

        for row,column in product(range(1,9), columns):
            self.board[(row, column)] = None

        #initialise the board with pieces
        for column in columns:
            self.board[(2, column)] = piece.Pawn(color="white", position=[2, column])

        for column in columns:
            self.board[(7, column)] = piece.Pawn(color="black", position=[7, column])

        self.board[(1, 'a')] = piece.Rook(color="white", position=[1, 'a'], board=self.board)
        self.board[(1, 'h')] = piece.Rook(color="white", position=[1, 'h'], board=self.board)
        self.board[(8, 'a')] = piece.Rook(color="black", position=[8, 'a'], board=self.board)
        self.board[(8, 'h')] = piece.Rook(color="black", position=[8, 'h'], board=self.board)

        self.board[(1, 'b')] = piece.Knight(color="white", position=[1, 'b'], board=self.board)
        self.board[(1, 'g')] = piece.Knight(color="white", position=[1, 'g'], board=self.board)
        self.board[(8, 'b')] = piece.Knight(color="black", position=[1, 'b'], board=self.board)
        self.board[(8, 'g')] = piece.Knight(color="black", position=[1, 'g'], board=self.board)

        self.board[(1, 'c')] = piece.Bishop(color="white", position=[1, 'c'], board=self.board)
        self.board[(1, 'f')] = piece.Bishop(color="white", position=[1, 'f'], board=self.board)
        self.board[(8, 'c')] = piece.Bishop(color="black", position=[8, 'c'], board=self.board)
        self.board[(8, 'f')] = piece.Bishop(color="black", position=[8, 'f'], board=self.board)

        self.board[(1, 'd')] = piece.Queen(color="white", position=[1, 'd'], board=self.board)
        self.board[(8, 'd')] = piece.Queen(color="black", position=[8, 'd'], board=self.board)

        self.board[(1, 'e')] = piece.King(color="white", position=[1, 'e'], board=self.board)
        self.board[(8, 'e')] = piece.King(color="black", position=[8, 'e'], board=self.board)

    def showBoard(self):

        pass










