import piece

from itertools import product


class Chessboard(object):
    def __init__(self):


        self.board = dict()

        columns = map(chr, range(97, 105))

        for row, column in product(range(1, 9), columns):
            self.board[(row, column)] = None

        # initialise the board with pieces
        for column in columns:
            self.board[(2, column)] = piece.Pawn(color="white", position=[2, column], board=self)

        for column in columns:
            self.board[(7, column)] = piece.Pawn(color="black", position=[7, column], board=self)

        self.board[(1, 'a')] = piece.Rook(color="white", position=[1, 'a'], board=self)
        self.board[(1, 'h')] = piece.Rook(color="white", position=[1, 'h'], board=self)
        self.board[(8, 'a')] = piece.Rook(color="black", position=[8, 'a'], board=self)
        self.board[(8, 'h')] = piece.Rook(color="black", position=[8, 'h'], board=self)

        self.board[(1, 'b')] = piece.Knight(color="white", position=[1, 'b'], board=self)
        self.board[(1, 'g')] = piece.Knight(color="white", position=[1, 'g'], board=self)
        self.board[(8, 'b')] = piece.Knight(color="black", position=[1, 'b'], board=self)
        self.board[(8, 'g')] = piece.Knight(color="black", position=[1, 'g'], board=self)

        self.board[(1, 'c')] = piece.Bishop(color="white", position=[1, 'c'], board=self)
        self.board[(1, 'f')] = piece.Bishop(color="white", position=[1, 'f'], board=self)
        self.board[(8, 'c')] = piece.Bishop(color="black", position=[8, 'c'], board=self)
        self.board[(8, 'f')] = piece.Bishop(color="black", position=[8, 'f'], board=self)

        self.board[(1, 'd')] = piece.Queen(color="white", position=[1, 'd'], board=self)
        self.board[(8, 'd')] = piece.Queen(color="black", position=[8, 'd'], board=self)

        self.board[(1, 'e')] = piece.King(color="white", position=[1, 'e'], board=self)
        self.board[(8, 'e')] = piece.King(color="black", position=[8, 'e'], board=self)

    def isInBoard(self, to):

        if to in self.board.keys():
            return True
        else:
            return False

    """
    checks whether a given path (between origin and target) is free.
    :returns boolean
    """

    # TODO: implement error classes
    def vertPathFree(self, origin, target):

        fromRow, fromCol = origin[0], origin[1]
        targetRow, targetCol = target[0], target[1]

        if targetCol is not fromCol:
            raise

        for row in range(fromRow, targetRow):
            if self.board[row, fromCol] is not None:
                return False

        return True

    """
    checks whether a given path (between origin and target) is free.
    :returns boolean
    """

    def horizPathFree(self, origin, target):

        fromRow, fromCol = origin[0], origin[1]
        targetRow, targetCol = target[0], target[1]

        if targetRow is not fromRow:
            raise

        for col in xrange(ord(fromCol), ord(targetCol)):
            col = chr(col)
            if self.board[fromRow, col] is not None:
                return False

        return True

    """
    checks whether a given tile (tuple) is valid and returns a bool
    """

    def exists(self, tile):

        row, col = tile[0], tile[1]

        if row < 1 or row > 8:
            return False
        if col < 'a' or col > 'h':
            return False

        return True

    """
    checks whether a given tile is empty (duh)
    """

    def isEmpty(self, tile):

        if self.board[tile] == None:
            return True

        else:
            return False

    """
    checks whether the piece on a tile is of enemy color (not own color)
    """

    def isEnemy(self, tile, ownColor):

        if self.board[tile].color is not ownColor:
            return True
        else:
            return False

    """
    The following methods get commonly used adjacent positions. Defining them as functions is ugly but a temporary fix.
    Note: we use the same 'angle' at all times, that is to say, we always define right and left from the White player's
    perspective. These are to be used mainly for pawns and the king.
    """

    #TODO: find a more elegant solution
    def getAdjacent(self, square, direction):

        row, col = square[0], square[1]

        if direction == "right":
            return row, chr(ord(col) + 1)

        elif direction == "left":
            return row, chr(ord(col) - 1)

        elif direction == "down":
            return row - 1, col

        elif direction == "up":
            return row + 1, col

        elif direction == "upright":
            return row + 1, chr(ord(col) + 1)

        elif direction == "upleft":
            return row + 1, chr(ord(col) - 1)

        elif direction == "downright":
            return row - 1, chr(ord(col) + 1)

        elif direction == "downleft":
            return row - 1, chr(ord(col) - 1)

        else:
            return False














