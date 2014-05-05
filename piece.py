class Piece(object):

    def __init__(self, name, player):
        self.name = name
        self.player = player

    def move(self, fromtile, totile):
        if self.move_is_allowed(fromtile, totile):
            totile.piece = self
            fromtile.piece = None
            return True
        else:
            print"that is an illegal move"
            return False

class Pawn(Piece):

    def __init__(self, player):
        Piece.__init__(self, name, player)

    def move_is_allowed(self, fromtile, totile):
        pass


