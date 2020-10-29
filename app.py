import pygame
import pandas as pd
import datetime

pygame.init()

scores_dict = {"SE": 0, "IAT": 0, "FICT": 0, "BDAM": 0}
specialisatie_dict = {"A": "",
                      "B": "",
                      "C": "",
                      "D": ""}


def setup():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Sorteerhoed Applicatie | Alpha Lions")

    return True

def lees_vragenlijst():
    vragenlijst = pd.read_excel("vragenlijst.xlsx")

    return vragenlijst

def speel(run, vragenlijst):
    # while run:



def main():
    run = setup()
    vragenlijst = lees_vragenlijst()
    speel(run, vragenlijst)
    print("hallo")


if __name__ == '__main__':
    main()
