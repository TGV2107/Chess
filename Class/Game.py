import random

from Class.Pieces.Bishop import *
from Class.Pieces.King import *
from Class.Pieces.Knight import *
from Class.Pieces.Pawn import *
from Class.Pieces.Piece import *
from Class.Pieces.Queen import *
from Class.Pieces.Rook import *


class Game:

    def __init__(self):

        #création de la matrice d'échiquier
        self.board = [
            [Rook("Black"), Knight("Black"), Bishop("Black"), Queen("Black"), King("Black"), Bishop("Black"), Knight("Black"), Rook("Black")],
            [Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black"),Pawn("Black")],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [Pawn("White",6,0), Pawn("White",6,1), Pawn("White",6,2), Pawn("White",6,3), Pawn("White",6,4), Pawn("White",6,5), Pawn("White",6,6), Pawn("White",6,7)],
            [Rook("White",7,0), Knight("White",7,1), Bishop("White",7,2), Queen("White",7,3), King("White",7,4), Bishop("White",7,5), Knight("White",7,6), Rook("White",7,7)]
            ]
        
        self.turn = "White"
        self.gameState = "Playing"


