from Class.Pieces.Piece import *
from Class.Pieces.Queen import *
from Class.Game import *

game = Game()

test = game.board[0][3]
print(test)
print(test.color)

print(test.getLegalMoves(game.board))
