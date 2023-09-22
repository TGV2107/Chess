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
        self.Board = [
            [Rook("Black",0,0), Knight("Black",0,1), Bishop("Black",0,2), Queen("Black",0,3), King("Black",0,4), Bishop("Black",0,5), Knight("Black",0,7), Rook("Black",0,8)],
            [Pawn("Black",1,0),Pawn("Black",1,1),Pawn("Black",1,2),Pawn("Black",1,3),Pawn("Black",1,4),Pawn("Black",1,5),Pawn("Black",1,6),Pawn("Black",1,7)],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [Pawn("White",6,0), Pawn("White",6,1), Pawn("White",6,2), Pawn("White",6,3), Pawn("White",6,4), Pawn("White",6,5), Pawn("White",6,6), Pawn("White",6,7)],
            [Rook("White",7,0), Knight("White",7,1), Bishop("White",7,2), Queen("White",7,3), King("White",7,4), Bishop("White",7,5), Knight("White",7,6), Rook("White",7,7)]
            ]
        
        self.turn = "White"
        self.gameStatus = "Playing"

