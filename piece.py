"""
Pieces are named using the Forsyth-Edwards Notation (FEN):
    - Pieces are named using their first letter (K for King, Q for Queen but N for kNight)
    - White pieces are given an uppercase notation

They are all subclasses of Pygame sprites, this allows for easier handling of the pieces in the GUI.
"""
import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self, color, position, board):

        pygame.sprite.Sprite.__init__(self)

        self.position = position
        self.color = color
        self.movesMade = 0
        self.possible_moves = []
        self.board = board

        self.set_possible_moves()

        # set name of piece in compliance to FEN
        piece_name = self.__class__.__name__
        if self.color == "white":
            self.name = piece_name[:1]
        else:
            self.name = piece_name.lower()[:1]

        self.load_image()
        self.set_coords()

    def set_coords(self):

        """
        Map position of piece to coordinate on the screen
        """

        y = self.position[0]
        x = (ord(self.position[1]) - 97)
        x = (x / 8.0) * 800
        y = (y / 8.0) * 800 - 100

        coords = (x, y)
        self.coords = coords

    @property
    def __str__(self):

        return self.name

    def move(self, to):
        """
        Function to carry out the actual move. We assume the move has been checked already.
        """
        self.position = to
        self.board.board[self.position] = None
        self.board.board[to] = self
        self.set_coords()

    def set_possible_moves(self):

        pass

    def load_image(self):

        pass


class Pawn(Piece):
    def load_image(self):
        if self.color == "black":
            self.image = pygame.image.load("images/bpawn.png")
            # self.image = pygame.transform.scale(self.image, (100,100))
        else:
            self.image = pygame.image.load("images/wpawn.png")

    def set_possible_moves(self):

        """
        Pawns can advance two squares the first time they move and hit a piece that is adjacent to them.
        The biggest difference between pawns and the other pieces is that pawns can move in only one direction,
        therefore it is necessary to make a distinction based on the piece color
        """

        # TODO: Fix ugly checks and ifs
        self.possible_moves = []

        row, col = self.position[0], self.position[1]
        if self.color == "white":

            forward = self.board.get_adjacent(self.position, "up")
            upright = self.board.get_adjacent(self.position, "upright")
            upleft = self.board.get_adjacent(self.position, "upleft")

            if self.movesMade == 0 and self.board.vert_path_free(self.position, (row + 2, col)):
                self.possible_moves.extend([(row + 2, col), forward])

            if self.board.exists(forward) and self.board.is_empty(forward):
                self.possible_moves.append(forward)

            if self.board.exists(upright) and not self.board.is_empty(upright):
                if self.board.is_enemy(upright, self.color):
                    self.possible_moves.append(upright)

            if self.board.exists(upleft) and not self.board.is_empty(upleft):
                if self.board.is_enemy(upleft, self.color):
                    self.possible_moves.append(upleft)

        else:

            forward = self.board.get_adjacent(self.position, "down")
            downleft = self.board.get_adjacent(self.position, "downleft")
            downright = self.board.get_adjacent(self.position, "downright")

            if self.movesMade == 0 and self.board.vert_path_free(self.position, (row + 2, col)):
                self.possible_moves.extend([(row - 2, col), forward])

            if self.board.exists(forward) and self.board.is_empty(forward):
                self.possible_moves.append(forward)

            if self.board.exists(downright) and not self.board.is_empty(downright):
                if self.board.is_enemy(downright, self.color):
                    self.possible_moves.append(downright)

            if self.board.exists(downleft) and not self.board.is_empty(downleft):
                if self.board.is_enemy(downleft, self.color):
                    self.possible_moves.append(downleft)


class Rook(Piece):
    def load_image(self):
        if self.color == "black":
            self.image = pygame.image.load("images/brook.png")
        else:
            self.image = pygame.image.load("images/wrook.png")

    def set_possible_moves(self):
        """
        Rooks can advance in any vertical or horizontal direction, they can castle with the king as
        long as they havent made a single move yet.
        """
        # TODO: castling
        self.possible_moves = []

        self.possible_moves.extend(self.board.paths(self, "up", "down", "left", "right"))


class Knight(Piece):
    def load_image(self):
        if self.color == "black":
            self.image = pygame.image.load("images/bknight.png")
        else:
            self.image = pygame.image.load("images/wknight.png")

    def set_possible_moves(self):
        """
        Knights move two squares horizontally or vertically and then move one square left or right.
        """
        self.possible_moves = []
        row, col = self.position[0], self.position[1]

        # TODO: find something less ugly
        tiles = [(row + 2, col), (row - 2, col),
                 (row, chr(ord(col) + 2)), (row, chr(ord(col) - 2))]

        for tile in tiles:

            if tile[1] == col:
                left = self.board.get_adjacent(tile, "left")
                right = self.board.get_adjacent(tile, "right")

                if self.board.exists(left):
                    if self.board.is_empty(left) or self.board.is_enemy(left, self.color):
                        self.possible_moves.append(left)

                if self.board.exists(right):
                    if self.board.is_empty(right) or self.board.is_enemy(right, self.color):
                        self.possible_moves.append(right)

            else:
                up = self.board.get_adjacent(tile, "up")
                down = self.board.get_adjacent(tile, "down")

                if self.board.exists(up):
                    if self.board.is_empty(up) or self.board.is_enemy(up, self.color):
                        self.possible_moves.append(up)

                if self.board.exists(down):
                    if self.board.is_empty(down) or self.board.is_enemy(down, self.color):
                        self.possible_moves.append(down)


class Bishop(Piece):
    def load_image(self):
        if self.color == "black":
            self.image = pygame.image.load("images/bbishop.png")
        else:
            self.image = pygame.image.load("images/wbishop.png")

    def set_possible_moves(self):
        """
        Bishops can move only in queer directions
        """
        self.possible_moves = []

        self.possible_moves.extend(self.board.paths(self, "upright", "upleft", "downright", "downleft"))


class King(Piece):
    def load_image(self):
        if self.color == "black":
            self.image = pygame.image.load("images/bking.png")
        else:
            self.image = pygame.image.load("images/wking.png")

    def set_possible_moves(self):
        """
        Kings can move to any square that is directly adjacent to them.
        Kings can also castle.
        """
        self.possible_moves = []

        for direction in self.board.directions:
            tile = self.board.get_adjacent(self.position, direction)

            if self.board.exists(tile):
                if self.board.is_empty(tile):
                    self.possible_moves.append(tile)

                else:
                    if self.board.is_enemy(tile, self.color):
                        self.possible_moves.append(tile)

                        # TODO: implement castling


class Queen(Piece):
    def load_image(self):
        if self.color == "black":
            self.image = pygame.image.load("images/bqueen.png")
        else:
            self.image = pygame.image.load("images/wqueen.png")

    def set_possible_moves(self):
        """
        Queens can move in all directions.
        """
        self.possible_moves = []

        self.possible_moves.extend(self.board.paths(self, "up", "down", "left", "right",
                                                   "downright", "downleft", "upright", "upleft"))