import pygame
import pygame.display as ui

from board import Chessboard
from player import Player


class Game(object):
    def __init__(self):

        self.board = Chessboard()

        self.player2 = Player("black")
        self.player1 = Player("white")

        self.players = (self.player1, self.player2)

        self.selected_piece = None

        self.turn = "p1"

        self.init_ui()

    def init_ui(self):

        """
        Initialize the GUI.
        """

        pygame.init()
        width = 800
        height = 800
        self.screen = ui.set_mode((width, height))
        ui.set_caption("Super awesome chess game!")

        """
        Check whether the UI has been initialized. If this is not the case, we break.
        """
        if ui.get_surface is None:
            raise

        self.draw_board()

    def draw_board(self):

        """
        Main function that will draw the pieces on the board according to the contents of our chessboard object.
        """
        """
        Draw the chess tiles on the board
        """
        red = (255, 0, 0)
        white = (150, 150, 150)
        black = (50, 50, 50)
        height = 800
        width = 800

        self.screen.fill(red)

        for x in range(0, width, width / 4):
            for y in range(0, height, height / 4):
                pygame.draw.rect(self.screen, white, (x, y, width / 8, height / 8))

        for x in range(width / 8, width, width / 4):
            for y in range(0, height, height / 4):
                pygame.draw.rect(self.screen, black, (x, y, width / 8, height / 8))

        for x in range(0, width, width / 4):
            for y in range(height / 8, height, height / 4):
                pygame.draw.rect(self.screen, black, (x, y, width / 8, height / 8))

        for x in range(width / 8, width, width / 4):
            for y in range(height / 8, height, height / 4):
                pygame.draw.rect(self.screen, white, (x, y, width / 8, height / 8))

        ui.update()

        for square in self.board.board:
            if self.board.board[square] is None:
                pass
            else:
                piece = self.board.board[square]
                image = pygame.transform.scale(piece.image, (100, 100))
                self.screen.blit(image, piece.coords)

        ui.update()

    def passturn(self):

        if self.turn == "p1":
            self.turn = "p2"
        else:
            self.turn = "p1"

    def show_possible_squares(self, piece):

        red = (200, 0, 0)
        green = (0, 200, 0)

        for move in piece.possible_moves:
            coords = self.board.map_square(move)
            if self.board.is_empty(move):
                pygame.draw.rect(self.screen, green, coords, 5)
            else:
                pygame.draw.rect(self.screen, red, coords, 5)
            ui.update()


def main():
    """
    Create game and players
    """

    game = Game()

    """
    Enter main game loop
    """
    while True:

        """
        We wait for an event to happen, if the user wants to quit the game, we exit without error.
        """
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        """
        If the our screen is clicked, we want to know what sprite (piece) was clicked.
        If it's the right players's piece, we show the possible squares and then handle the selected move accordingly.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            square = game.board.locate_square(pos)
            piece = game.board.board[square]

            if game.selected_piece is None:
                if piece is not None:
                    game.selected_piece = piece
                    game.show_possible_squares(piece)
            else:
                if square in game.selected_piece.possible_moves:
                    game.selected_piece.move(square)
                    game.selected_piece = None
                    game.draw_board()
                else:
                    pass


if __name__ == "__main__":
    main()