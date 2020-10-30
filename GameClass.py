import pygame
import pandas as pd


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
