class Piece:
    '''Permet de créer une pièce d'échec'''

    def __init__(self, type, color):

        self.Type = type

        self.Color = color

        self.LegalMoves = []

    def setLegalMoves(self, LegalMoves):

        self.LegalMoves = LegalMoves