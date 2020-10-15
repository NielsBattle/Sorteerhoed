def vragen_ophalen():
    vragen = []
    with open("", "r") as f:
        content = f.read()
        losse_zinnen = content.splitlines()
        for zin in losse_zinnen:
            vraag = {
                "vraag": "",
                "antwoorden": [],
                "juiste_antwoord": ""
            }

            zin_en_antwoord = zin.split(":")
            vraag["vraag"] = zin_en_antwoord[0]
            antwoorden = zin_en_antwoord[1].split("|")

            gefilterde_antwoorden = []
            for antwoord in antwoorden:
                if antwoord.startswith("["):
                    antwoord = antwoord.replace("[", "")
                    vraag["juiste_antwoord"] = antwoord
                gefilterde_antwoorden.append(antwoord)
            vraag["antwoorden"] = gefilterde_antwoorden
            vragen.append(vraag)
        f.close()
    return vragen


def main():
    print("hallo")


if __name__ == '__main__':
    main()