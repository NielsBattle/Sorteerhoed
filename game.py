import matplotlib.pyplot as plt
import pandas as pd
import pygame
import results


class Game:
    def __init__(self):
        self.index = 0

    @staticmethod
    def setup():
        # Setup method for setting up pygame and pandas
        pygame.init()
        pd.set_option("display.max_columns", None)
        pd.set_option("display.width", None)
        pd.set_option("display.max_rows", None)
        pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Sorteerhoed Applicatie | Alpha Lions")
        pygame.mixer_music.load("sound/HarryPotter.mp3")
        pygame.mixer_music.play(-1)
        icon = pygame.image.load("images/harrypottericon_epg_icon.ico")
        pygame.display.set_icon(icon)
        pygame.font.init()

        return True

    @staticmethod
    def lees_vragenlijst():
        # Function for reading the questions and returning the questions and answers
        vragenlijst = pd.read_excel("vragenlijst.xlsx")

        return vragenlijst

    def winnaar(self, scores_dict: dict):
        # Function for deciding who has the highest score
        winner_spec = []
        groups = list(scores_dict.keys())
        labels = [groups[0], groups[1], groups[2], groups[3]]
        sizes = [scores_dict[labels[0]], scores_dict[labels[1]], scores_dict[labels[2]], scores_dict[labels[3]]]
        colours = ["black", 'blue', 'gold', 'silver']
        plt.pie(sizes, labels=labels, colors=colours)
        plt.axis("equal")
        plt.show()

        highest_score = max(sizes)
        dubbele = 0
        for x in sizes:
            count = sizes.count(x)
            if count > 1:
                dubbele += 1
        if dubbele >= 3 and sizes.count(highest_score) == 1:
            # append winning spec
            winner_spec.append(max(scores_dict, key=scores_dict.get))
        else:
            for spec in scores_dict.items():
                if spec[1] == highest_score:
                    # append winning spec with same score
                    winner_spec.append(spec[0])

        outcome_df = self.open_outcome()
        self.write_outcome(winner_spec, outcome_df)

        # Return winning spec list
        return winner_spec

    @staticmethod
    def redraw_menu(button1, button2, button3):
        win = pygame.display.get_surface()
        sorteerhoed = pygame.image.load("images/sorting_hat.png")
        scroll = pygame.image.load("images/unnamed.png")
        hogwarts = pygame.image.load("images/Hogwarts.jpg")
        win.blit(hogwarts, [0, 0])
        win.blit(sorteerhoed, [475, 40])
        font_titel = pygame.font.Font("font/Harry_potter.ttf", 75)
        titel = font_titel.render("Sorteerhoed Alpha Lions", True, (255, 255, 255))
        win.blit(scroll, [375, 250])
        win.blit(titel, [375, 200])
        button1.draw(win, 0)
        button2.draw(win, 0)
        button3.draw(win, 0)

    @staticmethod
    def redraw_quiz(vraag_db, antwoord1, antwoord2, antwoord3, antwoord4):
        # draw elements to window
        background_image = pygame.image.load("images/forest.jpg").convert()
        sorting_hat = pygame.image.load("images/sorting_hat.png")
        text_bulb = pygame.image.load("images/text_bulb.png")
        fontvraag = pygame.font.Font('font/Harry_potter.ttf', 40)
        vraag = fontvraag.render(vraag_db, True, (0, 0, 0), (255, 255, 255))
        win = pygame.display.get_surface()

        win.blit(background_image, [0, 0])
        win.blit(text_bulb, [0, 0])
        win.blit(sorting_hat, [-20, 470])
        win.blit(vraag, (
            40 + (text_bulb.get_width() / 2 - vraag.get_width() / 2), 52))
        antwoord1.draw(win, 0)
        antwoord2.draw(win, 0)
        antwoord3.draw(win, 0)
        antwoord4.draw(win, 0)

    def redraw_stats(self, back_button):
        hogwarts = pygame.image.load("images/Hogwarts_dark.png")
        win = pygame.display.get_surface()
        win.blit(hogwarts, [0, 0])
        spec_count = self.count_spec()
        count_se = pygame.font.Font("font/Harry_potter.ttf", 75)
        fict = count_se.render(str(spec_count[0]), True, (255, 255, 255))
        bdam = count_se.render(str(spec_count[1]), True, (255, 255, 255))
        se = count_se.render(str(spec_count[2]), True, (255, 255, 255))
        iat = count_se.render(str(spec_count[3]), True, (255, 255, 255))
        win.blit(fict, [250, 400])
        win.blit(bdam, [500, 400])
        win.blit(se, [750, 400])
        win.blit(iat, [1000, 400])
        back_button.draw(win, 100)
        gryffindor = pygame.image.load("images/FICT_icon.png")
        slytherin = pygame.image.load("images/BDAM_icon.png")
        hufflepuff = pygame.image.load("images/SE_icon.png")
        ravenclaw = pygame.image.load("images/IAT_icon.png")
        win = pygame.display.get_surface()
        shrink_gryffindor = pygame.transform.scale(gryffindor, (250, 270))
        shrink_slytherin = pygame.transform.scale(slytherin, (250, 270))
        shrink_hufflepuff = pygame.transform.scale(hufflepuff, (250, 270))
        shrink_ravenclaw = pygame.transform.scale(ravenclaw, (250, 270))
        win.blit(shrink_gryffindor, [125, 100])
        win.blit(shrink_slytherin, [375, 100])
        win.blit(shrink_hufflepuff, [625, 100])
        win.blit(shrink_ravenclaw, [875, 100])

    @staticmethod
    def redraw_result(uitkomst, back_button):
        testing = results.scherm(uitkomst)
        screen = pygame.display.get_surface()
        results.scherm2(uitkomst, testing, screen)
        back_button.draw(screen, 100)

    @staticmethod
    def open_outcome():
        uitslag_db = pd.read_excel("Uitslagen.xlsx")
        uitslag_db_df = pd.DataFrame(uitslag_db)

        return uitslag_db_df

    @staticmethod
    def write_outcome(winner_spec: list, dataframe):
        new_dataframe = dataframe
        for x in winner_spec:
            new_dataframe = new_dataframe.append({"Winnaar": x}, ignore_index=True)
        new_dataframe.to_excel('Uitslagen.xlsx', index=False)

    @staticmethod
    def count_spec():
        uitslag_db = pd.read_excel("Uitslagen.xlsx")
        fict = 0
        bdam = 0
        se = 0
        iat = 0
        for x in uitslag_db["Winnaar"]:
            if x == "FICT":
                fict += 1
            elif x == "BDAM":
                bdam += 1
            elif x == "SE":
                se += 1
            elif x == "IAT":
                iat += 1
            else:
                print("Fout met tellen")
        return fict, bdam, se, iat
