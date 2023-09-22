import random

from Class.Pieces.Piece import *
from Class.Pieces.Pawn import *
from Class.Pieces.Rook import *
from Class.Pieces.Knight import *
from Class.Pieces.Bishop import *
from Class.Pieces.Queen import *
from Class.Pieces.King import *

class Game:

    def __init__(self):

        #création de la matrice d'échiquier
        self.Board = [
            [Rook("Black"), Knight("Black"), Bishop("Black"), Queen("Black"), King("Black"), Bishop("Black"), Knight("Black"), Rook("Black")],
            [Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black")],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White")],
            [Rook("White"), Knight("White"), Bishop("White"), Queen("White"), King("White"), Bishop("White"), Knight("White"), Rook("White")]
            ]
        
        self.turn = "White"
        self.gameStatus = "Playing"

