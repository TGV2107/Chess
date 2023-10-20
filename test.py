from Class.Pieces.Piece import *
from Class.Pieces.Bishop import *
from Class.Game import *

game = Game()

test = game.board[0][2]
print(test)
print(game.board[1][3])
game.board[1][3] = None
print(game.board[1][3])

print(test.getLegalMoves(game.board))