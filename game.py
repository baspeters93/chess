import pygame

from board import Chessboard
from player import Player
import pygame.display as ui


class Game(object):
    def __init__(self):

        self.board = Chessboard()

        self.player2 = Player("black")
        self.player1 = Player("white")

        self.players = (self.player1, self.player2)

        self.turn = "p1"

        self.initUI()

    def initUI(self):

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
        if ui.get_surface == None:
            raise

        """
        Draw the chess tiles on the board
        """
        red = (255, 0, 0)
        white = (150, 150, 150)
        black = (50, 50, 50)

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

        self.drawBoard()

    def drawBoard(self):

        """
        Main function that will draw the pieces on the board according to the contents of our chessboard object.
        """

        for square in self.board.board:
            if self.board.board[square] is None:
                pass
            else:
                piece = self.board.board[square]
                image = pygame.transform.scale(piece.image, (100, 100))
                self.screen.blit(image, piece.coords)

        ui.update()

    def passTurn(self):

        if self.turn == "p1":
            self.turn = "p2"
        else:
            self.turn = "p1"


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


if __name__ == "__main__":
    main()