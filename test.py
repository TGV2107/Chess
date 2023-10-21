from Class.Pieces.Piece import *
from Class.Pieces.Rook import *
from Class.Game import *

game = Game()

test = game.board[0][0]
print(game.board[4][4])
game.board[4][4] = Rook("Black",4,4)
print(game.board[4][4])

print(game.board[4][4].getLegalMoves(game.board))
