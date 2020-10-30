import game
import time


def speel(run: bool, vragenlijst, sorteerhoed: game):
    print(type(vragenlijst))
    scores_dict = {"FICT": 12, "IAT": 16, "SE": 15, "BDAM": 1}
    index = sorteerhoed.index
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
        sorteerhoed.winnaar(scores_dict)


def main():
    sorteerhoed = game.Game(0)
    run = sorteerhoed.setup()
    vragenlijst = sorteerhoed.lees_vragenlijst()
    speel(run, vragenlijst, sorteerhoed)
    print("hallo")


if __name__ == '__main__':
    main()
