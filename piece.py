"""
Pieces are named using the Forsyth-Edwards Notation (FEN):
    - Pieces are named using their first letter (K for King, Q for Queen but N for kNight)
    - White pieces are given an uppercase notation
"""

# base class Piece containing most of the common functions
class Piece(object):
    def __init__(self, color, position, board):

        self.position = position
        self.color = color
        self.movesMade = 0
        self.possibleMoves = []
        self.board = board

        self.setPossibleMoves()

        # set name of piece in compliance to FEN
        pieceName = self.__class__.__name__
        if self.color == "white":
            self.name = pieceName[:1]
        else:
            self.name = pieceName.lower()[:1]

    @property
    def __str__(self):

        return self.name

    def move(self, to):

        pass


class Pawn(Piece):
    def setPossibleMoves(self):

        """
        Pawns can advance two squares the first time they move and hit a piece that is adjacent to them.
        The biggest difference between pawns and the other pieces is that pawns can move in only one direction,
        therefore it is necessary to make a distinction based on the piece color
        """

        # TODO: Fix ugly checks and ifs
        self.possibleMoves = []

        row, col = self.position[0], self.position[1]
        if self.color == "white":

            forward = self.board.getAdjacent(self.position, "up")
            upright = self.board.getAdjacent(self.position, "upright")
            upleft = self.board.getAdjacent(self.position, "upleft")

            if self.movesMade == 0 and self.board.vertPathFree(self.position, (row + 2, col)):
                self.possibleMoves.extend([(row + 2, col), forward])

            if self.board.exists(forward) and self.board.isEmpty(forward):
                self.possibleMoves.append(forward)

            if self.board.exists(upright) and not self.board.isEmpty(upright):
                if self.board.isEnemy(upright, self.color):
                    self.possibleMoves.append(upright)

            if self.board.exists(upleft) and not self.board.isEmpty(upleft):
                if self.board.isEnemy(upleft, self.color):
                    self.possibleMoves.append(upleft)

        else:

            forward = self.board.getAdjacent(self.position, "down")
            downleft = self.board.getAdjacent(self.position, "downleft")
            downright = self.board.getAdjacent(self.position, "downright")

            if self.movesMade == 0 and self.board.vertPathFree(self.position, (row + 2, col)):
                self.possibleMoves.extend([(row - 2, col), forward])

            if self.board.exists(forward) and self.board.isEmpty(forward):
                self.possibleMoves.append(forward)

            if self.board.exists(downright) and not self.board.isEmpty(downright):
                if self.board.isEnemy(downright, self.color):
                    self.possibleMoves.append(downright)

            if self.board.exists(downleft) and not self.board.isEmpty(downleft):
                if self.board.isEnemy(downleft, self.color):
                    self.possibleMoves.append(downleft)


class Rook(Piece):
    def setPossibleMoves(self):
        """
        Rooks can advance in any vertical or horizontal direction, they can castle with the king as
        long as they havent made a single move yet.
        """
        # TODO: castling
        self.possibleMoves = []

        self.possibleMoves.extend(self.board.paths(self, "up", "down", "left", "right"))


class Knight(Piece):
    def setPossibleMoves(self):
        """
        Knights move two squares horizontally or vertically and then move one square left or right.
        """
        self.possibleMoves = []
        row, col = self.position[0], self.position[1]

        # TODO: find something less ugly
        tiles = [(row + 2, col), (row - 2, col), \
                 (row, chr(ord(col) + 2)), (row, chr(ord(col) - 2))]

        for tile in tiles:

            if tile[1] == col:
                left = self.board.getAdjacent(tile, "left")
                right = self.board.getAdjacent(tile, "right")

                if self.board.exists(left):
                    if self.board.isEmpty(left) or self.board.isEnemy(left, self.color):
                        self.possibleMoves.append(left)

                if self.board.exists(right):
                    if self.board.isEmpty(right) or self.board.isEnemy(right, self.color):
                        self.possibleMoves.append(right)

            else:
                up = self.board.getAdjacent(tile, "up")
                down = self.board.getAdjacent(tile, "down")

                if self.board.exists(up):
                    if self.board.isEmpty(up) or self.board.isEnemy(up, self.color):
                        self.possibleMoves.append(up)

                if self.board.exists(down):
                    if self.board.isEmpty(down) or self.board.isEnemy(down, self.color):
                        self.possibleMoves.append(down)


class Bishop(Piece):
    def setPossibleMoves(self):
        """
        Bishops can move only in queer directions
        """
        self.possibleMoves = []

        self.possibleMoves.extend(self.board.paths(self, "upright", "upleft", "downright", "downleft"))


class King(Piece):
    def setPossibleMoves(self):
        """
        Kings can move to any square that is directly adjacent to them.
        Kings can also castle.
        """
        self.possibleMoves = []

        for direction in self.board.directions:
            tile = self.board.getAdjacent(self.position, direction)

            if self.board.exists(tile):
                if self.board.isEmpty(tile):
                    self.possibleMoves.append(tile)

                else:
                    if self.board.isEnemy(tile, self.color):
                        self.possibleMoves.append(tile)

    # TODO: implement castling


class Queen(Piece):
    def setPossibleMoves(self):
        """
        Queens can move in all directions.
        """
        self.possibleMoves = []

        self.possibleMoves.extend(self.board.paths(self, "up", "down", "left", "right", \
                                                   "downright", "downleft", "upright", "upleft"))