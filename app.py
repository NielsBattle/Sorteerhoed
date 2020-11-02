import game
import pygame
import ButtonClass
import time

def speel(run: bool, vragenlijst, sorteerhoed: game):
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    grey = (245, 245, 245)
    darkerGrey = (96, 96, 96)
    print(type(vragenlijst))
    scores_dict = {"FICT": 0, "IAT": 0, "SE": 0, "BDAM": 0}
    index = sorteerhoed.index
    while run:
        if index == 15:
            uitkomst = sorteerhoed.winnaar(scores_dict)

        vraag = vragenlijst["vraag"][index]
        answer1 = ButtonClass.Button(grey, 40, 125, 1100, 75,30, vragenlijst["antwoord1"][index])
        answer2 = ButtonClass.Button(grey, 40, 215, 1100, 75,30, vragenlijst["antwoord2"][index])
        answer3 = ButtonClass.Button(grey, 40, 305, 1100, 75,30, vragenlijst["antwoord3"][index])
        answer4 = ButtonClass.Button(grey, 40, 395, 1100, 75,30, vragenlijst["antwoord4"][index])
        #textRect = vraag.get_rect()
        sorteerhoed.redrawWindow(vraag,answer1,answer2,answer3,answer4)
        pygame.display.update()
        # gamequit
        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()
                quit()

            # hoveractions
            # if event.type == pygame.MOUSEMOTION:
            #     if answer1.is_over(position):
            #         answer1.color = darkerGrey
            #     elif answer2.is_over(position):
            #         answer2.color = darkerGrey
            #     elif answer3.is_over(position):
            #         answer3.color = darkerGrey
            #     elif answer4.is_over(position):
            #         answer4.color = darkerGrey
            #     else:
            #         answer1.color = grey
            #         answer2.color = grey
            #         answer3.color = grey
            #         answer4.color = grey

            if event.type == pygame.MOUSEBUTTONDOWN:
                if answer1.is_over(position):
                    #fict
                    scores_dict["FICT"] +=1
                    print(scores_dict)
                    index += 1
                elif answer2.is_over(position):
                    #iat
                    scores_dict["IAT"] += 1
                    print(scores_dict)
                    index += 1
                elif answer3.is_over(position):
                    #se
                    scores_dict["SE"] += 1
                    print(scores_dict)
                    index += 1
                elif answer4.is_over(position):
                    #bdam
                    scores_dict["BDAM"] += 1
                    print(scores_dict)
                    index += 1

    # while True:
    #     print("running")
    #     time.sleep(1)
    #     sorteerhoed.winnaar(scores_dict)

def main():
    sorteerhoed = game.Game(0)
    run = sorteerhoed.setup()
    vragenlijst = sorteerhoed.lees_vragenlijst()
    speel(run, vragenlijst, sorteerhoed)
    print("hallo")


if __name__ == '__main__':
    main()
