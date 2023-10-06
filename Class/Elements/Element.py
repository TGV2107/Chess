from typing import Any


class Element:
    """Super class des types d'éléments sur une page, ne pas appeler directement mais utiliser les enfants de la classe"""

    def __init__(self, ID : str, pos : tuple, type : str):
        
        self.ID = ID

        self.posx, self.posy = pos
        self.pos = pos

        self.type = type