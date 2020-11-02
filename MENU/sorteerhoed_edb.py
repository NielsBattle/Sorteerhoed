#edb menu
# =====PyGame en benodigde functies importen=====
import pygame
import sys
from pygame.locals import *
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Sorteerhoed Alphalions')
# =====Font selecteren=====
font = pygame.font.SysFont(None, 25)
font2 = pygame.font.SysFont(None, 25)
font3 = pygame.font.SysFont(None, 40)

# =====Muziek veranderen=====
def muziek_change(nr):
    pygame.mixer.music.stop()
    pygame.mixer.music.play(-1)

 


# =====Vragen ophalen=====
# def vragen_ophalen():
#     with open("meerkeuzevragen.txt") as my_file:
#         data = my_file.read()
#     lijst_vragen = data.split('\n')
#     vragenlijst = []
# # =====Vragen en antwoorden splitten=====
#     for item in lijst_vragen:
#         if len(item) > 1:
#             vraag_split = item.split(';')
#             vragenlijst.append(vraag_split)
#     return vragenlijst

 


# =====Functie om tekst op het scherm te tonen, centreert de tekst=====
def write(text, x, y, color, font):
    screen = pygame.display.get_surface()
    text = font.render(text, 1, pygame.Color(color))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
    return text

 


# =====Globale variabelen (Sorry voor de luiheid :( )=====
click = False
#vragen = vragen_ophalen()
spec = 0

 


# =====Main menu tonen=====
def main_menu():
    #pygame.mixer.music.play(-1)
    while True:
        # =====Background img tonen=====
        global click
        screen = pygame.display.get_surface()
        #screen.blit(menuImg, (0, 0))
        # ===== Muis positie bijhouden en knoppen een positie geven =====
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(15, 585, 525, 125)
        button_2 = pygame.Rect(560, 585, 525, 125)
        pygame.display.update()
        # ===== Knoppen klikbaar maken =====
        if button_1.collidepoint((mx, my)):
            if click:
                #game()
                print("a")
        if button_2.collidepoint((mx, my)):
            if click:
                help()

        # ===== Sluit app af op kruisje =====
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mainClock.tick(60)

main_menu()

