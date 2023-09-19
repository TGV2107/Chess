from Class.Button import *
import random

def Main_Menu(screen):

    #bouton "Partie à deux joueurs"
    button_TwoPlayer = Button("Partie à deux joueurs",pygame.font.SysFont("Comic Sans MS", 10, bold=True), (255,255,255), (200,200), (540,360), pygame.image.load("Assets/IMG/bouton_collection.png"))
    button_TwoPlayer.Blit(screen)

    return button_TwoPlayer.rect
