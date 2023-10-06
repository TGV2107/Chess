
import pygame

from Class.Elements.Element import *


class Button(Element):
    '''Permet de créer un bouton enfant de Element avec une image une position et une taille définie, le rect est automatiquement affecté'''

    def __init__(self, ID, pos: tuple, scale : tuple, image : pygame.image.load, page : str):
        super().__init__(ID, pos, "Button")

        self.image = pygame.transform.scale(image, scale)

        self.rect = image.get_rect()

        self.rect.x = self.posx
        self.rect.y = self.posy

        self.page = page

    def Blit(self, screen): #affichage
        
        screen.blit(self.image, self.rect)