from itertools import product

import piece


class Chessboard(object):
    def __init__(self):
        self.board = dict()

        self.directions = ["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"]

        columns = map(chr, range(97, 105))

        for row, column in product(range(1, 9), columns):
            self.board[(row, column)] = None

        for column in columns:
            self.board[(2, column)] = piece.Pawn(color="white", position=(2, column), board=self)

        for column in columns:
            self.board[(7, column)] = piece.Pawn(color="black", position=(7, column), board=self)

        # TODO: loop this
        self.board[(1, 'a')] = piece.Rook(color="white", position=(1, 'a'), board=self)
        self.board[(1, 'h')] = piece.Rook(color="white", position=(1, 'h'), board=self)
        self.board[(8, 'a')] = piece.Rook(color="black", position=(8, 'a'), board=self)
        self.board[(8, 'h')] = piece.Rook(color="black", position=(8, 'h'), board=self)

        self.board[(1, 'b')] = piece.Knight(color="white", position=(1, 'b'), board=self)
        self.board[(1, 'g')] = piece.Knight(color="white", position=(1, 'g'), board=self)
        self.board[(8, 'b')] = piece.Knight(color="black", position=(8, 'b'), board=self)
        self.board[(8, 'g')] = piece.Knight(color="black", position=(8, 'g'), board=self)

        self.board[(1, 'c')] = piece.Bishop(color="white", position=(1, 'c'), board=self)
        self.board[(1, 'f')] = piece.Bishop(color="white", position=(1, 'f'), board=self)
        self.board[(8, 'c')] = piece.Bishop(color="black", position=(8, 'c'), board=self)
        self.board[(8, 'f')] = piece.Bishop(color="black", position=(8, 'f'), board=self)

        self.board[(1, 'd')] = piece.Queen(color="white", position=(1, 'd'), board=self)
        self.board[(8, 'd')] = piece.Queen(color="black", position=(8, 'd'), board=self)

        self.board[(1, 'e')] = piece.King(color="white", position=(1, 'e'), board=self)
        self.board[(8, 'e')] = piece.King(color="black", position=(8, 'e'), board=self)


    """
    checks whether a given path (between origin and target) is free.
    :returns boolean
    """

    # TODO: implement error classes
    def vert_path_free(self, origin, target):

        from_row, from_col = origin[0], origin[1]
        target_row, targetCol = target[0], target[1]

        if targetCol is not from_col:
            raise

        for row in range(from_row, target_row):
            if self.board[row, from_col] is not None:
                return False

        return True

    """
    checks whether a given path (between origin and target) is free.
    :returns boolean
    """

    def horiz_path_free(self, origin, target):

        from_row, from_col = origin[0], origin[1]
        target_row, target_col = target[0], target[1]

        if target_row is not from_row:
            raise

        for col in xrange(ord(from_col), ord(target_col)):
            col = chr(col)
            if self.board[from_row, col] is not None:
                return False

        return True

    """
    checks whether a given tile (tuple) is valid and returns a bool
    """

    @staticmethod
    def exists(tile):

        row, col = tile[0], tile[1]

        if row < 1 or row > 8:
            return False
        if col < 'a' or col > 'h':
            return False

        return True

    """
    checks whether a given tile is empty (duh)
    """

    def is_empty(self, tile):

        if self.board[tile] is None:
            return True

        else:
            return False

    """
    checks whether the piece on a tile is of enemy color (not own color)
    """

    def is_enemy(self, tile, own_color):

        if self.board[tile].color is not own_color:
            return True
        else:
            return False

    """
    The following methods get commonly used adjacent positions. Defining them as functions is ugly but a temporary fix.
    Note: we use the same 'angle' at all times, that is to say, we always define right and left from the White player's
    perspective. These are to be used mainly for pawns and the king.
    """

    # TODO: find a more elegant solution
    @staticmethod
    def get_adjacent(square, direction):

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


    def paths(self, piece, *directions):
        possible_moves = []

        for direction in directions:

            if direction not in self.directions:
                continue
            tile = self.get_adjacent(piece.position, direction)

            while self.exists(tile):

                if self.is_empty(tile):
                    possible_moves.append(tile)
                elif self.is_enemy(tile, piece.color):
                    possible_moves.append(tile)
                    break
                else:
                    break

                tile = self.get_adjacent(tile, direction)

        return possible_moves

    def locate_square(self, pos):
        """
        This function finds returns the piece on a given coordinate and None if there is none
        """
        for square in self.board:

            minx = (ord(square[1]) - 97)
            minx = int((minx / 8.0) * 800)
            maxx = minx + 100

            miny = int((square[0] / 8.0) * 800 - 100)
            maxy = miny + 100

            x = pos[0]
            y = pos[1]

            if x in range(minx, maxx) and y in range(miny, maxy):
                return square

    @staticmethod
    def map_square(pos):
        """
        Gets a position on the board and returns the coords of the square on the board
        """
        minx = (ord(pos[1]) - 97)
        minx = int((minx / 8.0) * 800)

        miny = int((pos[0] / 8.0) * 800 - 100)

        return (minx, miny, 100, 100)
