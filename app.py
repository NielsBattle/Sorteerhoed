import game
import pygame
import ButtonClass


def speel(run: bool, vragenlijst, sorteerhoed: game):
    state = "menu"
    grey = (245, 245, 245)
    scores_dict = {"FICT": 0, "IAT": 0, "SE": 0, "BDAM": 0}
    index = sorteerhoed.index
    while run:
        if state == "menu":
            button1_tekst = "Start"
            button2_tekst = "Statistieken"
            button3_tekst = "Verlaten"
            grey = (245, 245, 245)
            button1 = ButtonClass.Button(grey, 485, 355, 290, 75, 45, button1_tekst)
            button2 = ButtonClass.Button(grey, 485, 445, 290, 75, 45, button2_tekst)
            button3 = ButtonClass.Button(grey, 485, 535, 290, 75, 45, button3_tekst)
            sorteerhoed.redraw_menu(button1,button2,button3)
            pygame.display.update()
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.QUIT()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.is_over(position):
                         state = "vragen"
                    elif button2.is_over(position):
                        print("c")
                    elif button3.is_over(position):
                        pygame.QUIT()


        if state == "vragen":
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
            sorteerhoed.redraw_quiz(vraag, answer1, answer2, answer3, answer4)
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