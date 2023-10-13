import pygame

from Class.Game import *
from Pages.Game_Page import *
from Pages.Main_Menu import *


class Window:
    """Class générale étant la fenêtre affiché"""

    def __init__(self, screen) -> None:
        """Constructeur de la fenêtre"""
        
        self.ScreenName = "Main_Menu"
        self.Screen = screen

        self.elements_list = []
        self.button_list = []
        self.previous_button = None

        self.game = None

    
    def getElements(self):
        """Fonction permettant la récupération des éléments de chaque page"""
        #FAIRE GAME PAGE

        pygame.display.flip()
        self.Screen.fill((0,0,0))

        if self.ScreenName == "Main_Menu":

            self.elements_list = Main_Menu(self.Screen)

        elif self.ScreenName == "Game_Page" :

            self.elements_list = self.game.start_game()


    def blit(self):
        """Permet l'affichague des éléments d'une page et le revoie aux fonctions en lien avec chaque boutons, permet également le traitement des événements"""
        window = self
        previous_button = None
        running = True
        isMOUSEBUTTONDOWN = False

        for event in pygame.event.get(): #récupération des événements de pygame
            
            if event.type == pygame.QUIT: #si la fenêtre a été fermée
                
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN: #si la souris a été cliquée
                
                isMOUSEBUTTONDOWN = True
                button = event.button

        for element in self.elements_list: #traitement de chaque élément

            element.Blit(self.Screen) #affichage

            if element.type == "Button" and isMOUSEBUTTONDOWN: #gestion des boutons

                if element.rect.collidepoint(event.pos) and not(element.__eq__(previous_button)): #appel des fonctions

                    if element.page == "Main_Menu":
                        
                        window = Main_Page_Relayeur(window, element, button)

                    if element.page == "Game_Page":

                        window = self.game.getButtonAction(window, element)
                    
                    previous_button = element


        #return : running -> permet de stopper le programme (si False)
        return running