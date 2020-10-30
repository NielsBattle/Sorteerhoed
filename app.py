import GameClass
import time

specialisatie_dict = {"A": "",
                      "B": "",
                      "C": "",
                      "D": ""}


def speel(run, vragenlijst, index):
    scores_dict = {"SE": 0, "IAT": 0, "FICT": 0, "BDAM": 0}
    while run:
        if index == 15:
            break
        print(str(vragenlijst["vraag"][index]))
        print(str(vragenlijst["antwoord1"][index]))
        print(str(vragenlijst["antwoord2"][index]))
        print(str(vragenlijst["antwoord3"][index]))
        print(str(vragenlijst["antwoord4"][index]))
        print("\n")
        index += 1

    while True:
        print("running")
        time.sleep(1)


def main():
    game = GameClass.Game(0)
    run = game.setup()
    vragenlijst = game.lees_vragenlijst()
    speel(run, vragenlijst, game.index)
    print("hallo")


if __name__ == '__main__':
    main()
