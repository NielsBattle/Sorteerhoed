# Pygame on
import pygame
import ButtonClass

# TODO delete this block
# fict_spec = "Gryffindor"
# bdam_spec = "Slytherin"
# se_spec = "Hufflepuff"
# iat_spec = "Ravenclaw"

spec_dict = {
    "Info": {
        "FICT": "Gryffindor",
        "BDAM": "Slytherin",
        "SE": "Hufflepuff",
        "IAT": "Ravenclaw"
    },
    "Kleuren": {
        "FICT": (255, 120, 120),
        "BDAM": (90, 255, 90),
        "SE": (255, 255, 120),
        "IAT": (170, 170, 255)
    }
}

achtergrond = 'images/grote hal.jpg'

picture = ""
picture_twee = ""
picture_drie = ""
button_een = ""
button_twee = ""
ondertekst = ""
kleur_een = ""
kleur_twee = ""


def scherm(winnaars: list):
    print(winnaars)
    if len(winnaars) == 1:
        image = f"images/{winnaars[0]}_icon.png"
        button_een = spec_dict["Info"][winnaars[0]]
        if winnaars[0] == "IAT":
            ondertekst1 = "Jij bent net zo geschikt voor Ravenclaw als voor Interactietechnologie!"
            ondertekst2 = "Jij bent intelligent, creatief en ziet de situatie snel in."
            ondertekst3 = "Je bent trots over je eigen creaties en gemotiveerd door te leren in je vak."
        elif winnaars[0] == "FICT":
            ondertekst1 = "Jij bent net zo geschikt voor Gryffindor als voor Forencsisch ICT!"
            ondertekst2 = "Je leert kennis te hebben van computers, software, databases, netwerken, multimedi"
            ondertekst3 = "Je weet waar de zwakke plekken zitten, welke informatie dan op straat ligt en wat daaraan te doen is."
        elif winnaars[0] == "BDAM":
            ondertekst1 = "Jij bent net zo geschikt voor Slytherin als voor Business-Data management!"
            ondertekst2 = "Je bent extreem goed in het begrijpen en gebruiken van Data"
            ondertekst3 = "Je kan altijd de beste beslissing voor het team bepalen"
        elif winnaars[0] == "SE":
            ondertekst1 = "Jij bent net zo geschikt voor Hufflepuff als voor Software Engineering!"
            ondertekst2 = "Je leert software voor diverse systemen te ontwerpen, te realiseren en te implementeren"
            ondertekst3 = "Je bent goed in een goede basis te bouwen"

        kleur_een = spec_dict["Kleuren"][winnaars[0]]
        icon_x = 500
        icon_y = 60
        text_x = 70
        text_y = 440

        # icon
        icon_img = pygame.image.load(image)
        icon_transformed = pygame.transform.scale(icon_img, (250, 270))

        return image, button_een, ondertekst1, kleur_een, icon_x, icon_y, icon_transformed, text_x, text_y, ondertekst2, ondertekst3

    elif len(winnaars) == 2:
        image = f"images/{winnaars[0]}_icon.png"
        image_twee = f"images/{winnaars[1]}_icon.png"
        button_een = spec_dict["Info"][winnaars[0]]
        button_twee = spec_dict["Info"][winnaars[1]]
        ondertekst = f"Je hebt een combinatie van {button_een} en {button_twee}! Begin opnieuw voor een exactere uitslag"
        kleur_een = spec_dict["Kleuren"][winnaars[0]]
        kleur_twee = spec_dict["Kleuren"][winnaars[1]]
        icon_x = 160
        icon_y = 60
        icon_twee_x = 850
        icon_twee_y = 60
        icon_drie_x = 850
        icon_drie_y = 60
        text_x = 180
        text_y = 540

        # icon
        icon_img = pygame.image.load(image)
        icon_transformed = pygame.transform.scale(icon_img, (250, 270))

        # icon twee
        icon_twee_img = pygame.image.load(image_twee)
        icon_twee_transformed = pygame.transform.scale(icon_twee_img, (250, 270))

        return image, image_twee, button_een, button_twee, ondertekst, kleur_een, kleur_twee, icon_x, icon_y, icon_twee_x, icon_twee_y, icon_drie_x, icon_drie_y, icon_transformed, icon_twee_transformed, text_x, text_y
    elif len(winnaars) == 3:
        image = f"images/{winnaars[0]}_icon.png"
        image_twee = f"images/{winnaars[1]}_icon.png"
        image_drie = f"images/{winnaars[2]}_icon.png"
        button_een = spec_dict["Info"][winnaars[0]]
        button_twee = spec_dict["Info"][winnaars[1]]
        button_drie = spec_dict["Info"][winnaars[2]]
        ondertekst = f"Je hebt een combinatie van {button_een}, {button_twee} en {button_drie} Begin opnieuw voor een exactere uitslag!"
        kleur_een = spec_dict["Kleuren"][winnaars[0]]
        kleur_twee = spec_dict["Kleuren"][winnaars[1]]
        kleur_drie = spec_dict["Kleuren"][winnaars[2]]
        icon_x = 160
        icon_y = 60
        icon_twee_x = 500
        icon_twee_y = 60
        icon_drie_x = 890
        icon_drie_y = 60
        text_x = 240
        text_y = 540

        # icon
        icon_img = pygame.image.load(image)
        icon_transformed = pygame.transform.scale(icon_img, (250, 270))

        # icon twee
        icon_twee_img = pygame.image.load(image_twee)
        icon_twee_transformed = pygame.transform.scale(icon_twee_img, (250, 270))

        # icon drie
        icon_drie_img = pygame.image.load(image_drie)
        icon_drie_transformed = pygame.transform.scale(icon_drie_img, (250, 270))

        return image, image_twee, button_een, button_twee, ondertekst, kleur_een, kleur_twee, icon_x, icon_y, icon_twee_x, icon_twee_y, icon_drie_x, icon_drie_y, image_drie, kleur_drie, button_drie, text_x, text_y, icon_transformed, icon_twee_transformed, icon_drie_transformed
    else:
        print("Fout result_gelijk")

# scherm(winnaars1)
alle_variabelen = tuple()
winnaars = []
def jemoeder(winnaars: list):
    alle_variabelen = scherm(winnaars)
    winnaars = winnaars

print(winnaars)
print(alle_variabelen)

# scherm(winnaars3)

# Screen create
screen = pygame.display.set_mode((1280, 720))

# Text
# font = pygame.font.Font("font/Harry_potter.ttf", 40)

# background
backgroundImg = pygame.image.load(achtergrond)
background_x = 0
background_y = 0


def border_een():
    screen.blit(border_img, (alle_variabelen[7] + 80, 350))


# border
border = pygame.image.load('images/border.png')
border_img = pygame.transform.scale(border, (100, 50))


def background():
    screen.blit(backgroundImg, (background_x, background_y))


if len(winnaars) == 1:  # Jasper was here
    def icon():
        screen.blit(alle_variabelen[6], (alle_variabelen[4], alle_variabelen[5]))


    def text():
        font = pygame.font.Font("font/Harry_potter.ttf", 40)
        label = font.render(alle_variabelen[2], True, (255, 255, 255))
        screen.blit(label, (alle_variabelen[7], alle_variabelen[8]))


    def text1():
        font = pygame.font.Font("font/Harry_potter.ttf", 40)
        label1 = font.render(alle_variabelen[9], True, (255, 255, 255))
        screen.blit(label1, (alle_variabelen[7], alle_variabelen[8] + 50))


    def text2():
        font = pygame.font.Font("font/Harry_potter.ttf", 40)
        label2 = font.render(alle_variabelen[10], True, (255, 255, 255))
        screen.blit(label2, (alle_variabelen[7], alle_variabelen[8] + 100))


    def back_button():
        back_button = ButtonClass.Button((alle_variabelen[3]), alle_variabelen[4] + 80, 350, 100, 50, 30,
                                         alle_variabelen[1])
        back_button.draw(screen, 0)
        return back_button


    def terug_button():
        terug_button = ButtonClass.Button((alle_variabelen[3]), 40, 650, 100, 50, 30, "Terug")
        terug_button.draw(screen, 0)


    def border_een():
        screen.blit(border_img, (alle_variabelen[4] + 80, 350))

if len(winnaars) == 2:
    def icon():
        screen.blit(alle_variabelen[13], (alle_variabelen[7], alle_variabelen[8]))


    def icon_twee():
        screen.blit(alle_variabelen[14], (alle_variabelen[9], alle_variabelen[10]))


    def text():
        FONT = pygame.font.Font("font/Harry_potter.ttf", 40)
        label = FONT.render(alle_variabelen[4], True, (255, 255, 255))
        screen.blit(label, (alle_variabelen[15], alle_variabelen[16]))


    def back_button_twee():
        terug_button = ButtonClass.Button((alle_variabelen[6]), alle_variabelen[9] + 80, 350, 100, 50, 30,
                                          alle_variabelen[3])
        terug_button.draw(screen, 0)
        return terug_button


    def back_button():
        terug_button = ButtonClass.Button((alle_variabelen[5]), alle_variabelen[7] + 80, 350, 100, 50, 30,
                                          alle_variabelen[2])
        terug_button.draw(screen, 0)
        return terug_button


    def border_een():
        screen.blit(border_img, (alle_variabelen[7] + 80, 350))


    def border_twee():
        screen.blit(border_img, (alle_variabelen[9] + 80, 350))


    def border_drie():
        screen.blit(border_img, (alle_variabelen[11] + 80, 350))

if len(winnaars) == 3:
    def icon():
        screen.blit(alle_variabelen[18], (alle_variabelen[7], alle_variabelen[8]))


    def icon_twee():
        screen.blit(alle_variabelen[19], (alle_variabelen[9], alle_variabelen[10]))


    def icon_drie():
        screen.blit(alle_variabelen[20], (alle_variabelen[11], alle_variabelen[12]))


    def back_button():
        terug_button = ButtonClass.Button((alle_variabelen[5]), alle_variabelen[7] + 80, 350, 100, 50, 30,
                                          alle_variabelen[2])
        terug_button.draw(screen, 0)
        return terug_button


    def back_button_twee():
        terug_button = ButtonClass.Button((alle_variabelen[6]), alle_variabelen[9] + 80, 350, 100, 50, 30,
                                          alle_variabelen[3])
        terug_button.draw(screen, 0)
        return terug_button


    def back_button_drie():
        terug_button = ButtonClass.Button((alle_variabelen[14]), alle_variabelen[11] + 80, 350, 100, 50, 30,
                                          alle_variabelen[15])
        terug_button.draw(screen, 0)
        return terug_button


    def text():
        font = pygame.font.Font("font/Harry_potter.ttf", 40)
        label = font.render(alle_variabelen[4], True, (255, 255, 255))
        screen.blit(label, (alle_variabelen[16], alle_variabelen[17]))


    def border_een():
        screen.blit(border_img, (alle_variabelen[7] + 80, 350))


    def border_twee():
        screen.blit(border_img, (alle_variabelen[9] + 80, 350))


    def border_drie():
        screen.blit(border_img, (alle_variabelen[11] + 80, 350))

# # Game loop
# running = True
# while running:
#
#     screen.fill((0, 0, 0))
#
#     for event in pygame.event.get():
#         position = pygame.mouse.get_pos()
#         if event.type == pygame.QUIT:
#             running = False
#
#     if len(winnaars) == 1:
#         background()
#         icon()
#         back_button()
#         border_een()
#         text()
#         text1()
#         text2()
#         terug_button()
#     if len(winnaars) == 2:
#         background()
#         icon()
#         back_button()
#         border_een()
#         icon_twee()
#         back_button_twee()
#         border_twee()
#         text()
#     if len(winnaars) == 3:
#         background()
#         icon()
#         back_button()
#         border_een()
#         icon_twee()
#         icon_drie()
#         back_button_twee()
#         back_button_drie()
#         border_twee()
#         border_drie()
#         text()
#     pygame.display.update()
