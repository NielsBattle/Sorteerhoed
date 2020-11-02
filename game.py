import pygame
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


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
        # pygame.mixer_music.load("sound/HarryPotter.mp3")
        # pygame.mixer_music.play(-1)
        icon = pygame.image.load("images/harrypottericon_epg_icon.ico")
        pygame.display.set_icon(icon)

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

    def redraw_menu(self, button1, button2, button3):
        win = pygame.display.get_surface()
        sorteerhoed = pygame.image.load("images/sorting_hat.png")
        scroll = pygame.image.load("images/unnamed.png")
        forest = pygame.image.load("images/forest.jpg")
        win.blit(forest, [0, 0])
        win.blit(sorteerhoed, [475, 40])
        font_titel = pygame.font.Font("font/Harry_potter.ttf", 75)
        titel = font_titel.render("Sorteerhoed Alpha Lions", True,(255, 255, 255))
        win.blit(scroll, [375, 250])
        win.blit(titel, [375, 200])
        button1.draw(win, 0)
        button2.draw(win, 0)
        button3.draw(win, 0)

    def redraw_quiz(self, vraag_db, antwoord1, antwoord2, antwoord3, antwoord4):
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
        win.blit(vraag, [40, 40])
        antwoord1.draw(win, 0)
        antwoord2.draw(win, 0)
        antwoord3.draw(win, 0)
        antwoord4.draw(win, 0)

    def open_outcome(self):
        uitslag_db = pd.read_excel("Uitslagen.xlsx")
        uitslag_db_df = pd.DataFrame(uitslag_db)

        return uitslag_db_df

    def write_outcome(self, winner_spec: list, dataframe):
        new_dataframe = dataframe
        print(new_dataframe)
        for x in winner_spec:
            new_dataframe = new_dataframe.append({"Winnaar": x}, ignore_index=True)
            print(f"{new_dataframe}")
            # break
        print(new_dataframe)
        new_dataframe.to_excel('Uitslagen.xlsx', index=False)

