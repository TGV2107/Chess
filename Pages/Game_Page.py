
from Class.Game import *
from Class.Pieces.Bishop import *
from Class.Pieces.King import *
from Class.Pieces.Knight import *
from Class.Pieces.Pawn import *
from Class.Pieces.Piece import *
from Class.Pieces.Queen import *
from Class.Pieces.Rook import *


class Game_Page:

    def __init__(self, game: Game(), elements: list = []):
        self.game = game
        self.elements = elements

