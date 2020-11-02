import game
import pygame
import ButtonClass


def speel(run: bool, vragenlijst, sorteerhoed: game):
    grey = (245, 245, 245)
    scores_dict = {"FICT": 0, "IAT": 0, "SE": 0, "BDAM": 0}
    index = sorteerhoed.index
    while run:
        if index == 15:
            # Check if index is out of bound
            uitkomst = sorteerhoed.winnaar(scores_dict)
            print(uitkomst)
            break

        # Get question from question dataframe
        vraag = vragenlijst["vraag"][index]
        # Get answers from answer dataframe
        answer1 = ButtonClass.Button(grey, 40, 125, 1100, 75, 30, vragenlijst["antwoord1"][index])
        answer2 = ButtonClass.Button(grey, 40, 215, 1100, 75, 30, vragenlijst["antwoord2"][index])
        answer3 = ButtonClass.Button(grey, 40, 305, 1100, 75, 30, vragenlijst["antwoord3"][index])
        answer4 = ButtonClass.Button(grey, 40, 395, 1100, 75, 30, vragenlijst["antwoord4"][index])
        sorteerhoed.redrawWindow(vraag, answer1, answer2, answer3, answer4)
        pygame.display.update()
        # gamequit
        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if answer1.is_over(position):
                    scores_dict["FICT"] += 1
                    print(scores_dict)
                    index += 1
                elif answer2.is_over(position):
                    scores_dict["IAT"] += 1
                    print(scores_dict)
                    index += 1
                elif answer3.is_over(position):
                    scores_dict["SE"] += 1
                    print(scores_dict)
                    index += 1
                elif answer4.is_over(position):
                    scores_dict["BDAM"] += 1
                    print(scores_dict)
                    index += 1


def main():
    # Initialize Game Object
    sorteerhoed = game.Game()
    # Star game setup
    run = sorteerhoed.setup()
    # Get questions and answers from Excelsheet
    vragenlijst = sorteerhoed.lees_vragenlijst()
    speel(run, vragenlijst, sorteerhoed)


if __name__ == '__main__':
    main()

#####edb
# import pygame
# import matplotlib
#
# sorteerhoed = pygame.image.load('sorting_hat.png')
# scroll = pygame.image.load('unnamed.png')
# forest = pygame.image.load("forest.jpg")
#
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# grey = (245, 245, 245)
# darkerGrey = (96, 96, 96)
#
# pygame.init()
# size = (1280, 720)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Sorteerhoed2")
# win = pygame.display.set_mode((1280, 720))
#
# antwoord_b = "Start"
# antwoord_c = "Statistieken"
# antwoord_d = "Verlaten"
#
# # The loop will carry on until the user exit the game (e.g. clicks the close button).
# carryOn = True
#
#
# # buttons class
# class button():
#     def __init__(self, color, x, y, width, height, font_size, text=''):
#         self.color = color
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.fontSize = font_size
#         self.text = text
#
#     def draw(self, win, outline=None):
#         # Call this method to draw the button on the screen
#         if outline:
#             pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
#
#         pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
#
#         if self.text != '':
#             font = pygame.font.Font('Harry_potter.ttf', self.fontSize)
#             text = font.render(self.text, 1, (0, 0, 0))
#             win.blit(text, (
#                 self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
#
#     def isOver(self, pos):
#         # Pos is the mouse position or a tuple of (x,y) coordinates
#         if pos[0] > self.x and pos[0] < self.x + self.width:
#             if pos[1] > self.y and pos[1] < self.y + self.height:
#                 return True
#         return False
#
#
# # draw elements to window
# def redrawWindow():
#     screen.blit(forest, [0, 0])
#     screen.blit(sorteerhoed, [475, 40])
#     font_titel = pygame.font.Font("Harry_potter.ttf", 75)
#     titel = font_titel.render("Sorteerhoed Alpha Lions", (255, 255, 255), (255, 255, 255))
#     screen.blit(scroll, [375, 250])
#     screen.blit(titel, [375, 200])
#     answer2.draw(win, 0)
#     answer3.draw(win, 0)
#     answer4.draw(win, 0)
#
#
# run = True
#
# # buttons declaren
# answer2 = button(grey, 485, 355, 290, 75, 45, antwoord_b)
# answer3 = button(grey, 485, 445, 290, 75, 45, antwoord_c)
# answer4 = button(grey, 485, 535, 290, 75, 45, antwoord_d)
#
# while run:
#     redrawWindow()
#     pygame.display.update()
#     # gamequit
#     for event in pygame.event.get():
#         position = pygame.mouse.get_pos()
#         if event.type == pygame.QUIT:
#             run = False
#             pygame.QUIT()
#             quit()
#
#         # hoveractions
#         if event.type == pygame.MOUSEMOTION:
#             if answer2.isOver(position):
#                 answer2.color = darkerGrey
#             elif answer3.isOver(position):
#                 answer3.color = darkerGrey
#             elif answer4.isOver(position):
#                 answer4.color = darkerGrey
#             else:
#                 answer2.color = grey
#                 answer3.color = grey
#                 answer4.color = grey
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if answer2.isOver(position):
#                 print("b")
#             elif answer3.isOver(position):
#                 print("c")
#             elif answer4.isOver(position):
#                 print("d")
