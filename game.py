import pygame
import pandas as pd
import matplotlib.pyplot as plt


class Game:
    def __init__(self, index):
        self.index = index

    @staticmethod
    def setup():
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

        return True

    @staticmethod
    def lees_vragenlijst():
        vragenlijst = pd.read_excel("vragenlijst.xlsx")

        return vragenlijst

    def winnaar(self, scores_dict: dict):
        groups = list(scores_dict.keys())
        labels = [groups[0], groups[1], groups[2], groups[3]]
        sizes = [scores_dict[labels[0]], scores_dict[labels[1]], scores_dict[labels[2]], scores_dict[labels[3]]]
        colours = ["black", 'blue', 'gold', 'silver']
        plt.pie(sizes, labels=labels, colors=colours)
        plt.axis("equal")
        plt.show()

        highest_score = max(sizes)
        dubbele = 0
        # for x in sizes:
        #     count = sizes.count(x)
        #     if count > 1:
        #         dubbele += 1
        # if dubbele > and sizes.count(highest_score) == 1:
        #     print("werk ik nog aan")

        winnaar_spec = ""
        for specialisatie in scores_dict.items():
            if specialisatie[1] == highest_score:
                winnaar_spec = specialisatie[0]

        return winnaar_spec
