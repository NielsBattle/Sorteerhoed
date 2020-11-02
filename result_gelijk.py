# Pygame on
import pygame
import ButtonClass

fict_spec = "Gryffindor"
bdam_spec = "Slytherin"
se_spec = "Hufflepuff"
iat_spec = "Ravenclaw"

spec_dict = {
    "Info": {
        "FICT": "Gryffindor",
        "BDAM": "Slytherin",
        "SE": "Hufflepuff",
        "IAT": "Ravenclaw"
    },
    "Kleuren" :{
        "FICT": (255, 120, 120),
        "BDAM": (90, 255, 90),
        "SE": (255, 255, 120),
        "IAT": (170, 170, 255)
    }
}

achtergrond = 'images/grote hal.jpg'

winnaars = list()
picture = ""
picture_twee = ""
picture_drie = ""
button_een = ""
button_twee = ""
ondertekst = ""
kleur_een = ""
kleur_twee = ""

def scherm(winnaars):
    if len(winnaars) == 1:
        picture = f"images/{winnaars[0]}_icon.png"
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
        iconX = 500
        iconY = 60
        textX = 70
        textY = 440

        # icon
        iconImg = pygame.image.load(picture)
        iconTransformed = pygame.transform.scale(iconImg, (250, 270))

        return picture, button_een, ondertekst1, kleur_een, iconX, iconY, iconTransformed, textX, textY, ondertekst2, ondertekst3

    elif len(winnaars) == 2:
        picture = f"images/{winnaars[0]}_icon.png"
        picture_twee = f"images/{winnaars[1]}_icon.png"
        button_een = spec_dict["Info"][winnaars[0]]
        button_twee = spec_dict["Info"][winnaars[1]]
        ondertekst = f"Je hebt een combinatie van {button_een} en {button_twee}! Begin opnieuw voor een exactere uitslag"
        kleur_een = spec_dict["Kleuren"][winnaars[0]]
        kleur_twee = spec_dict["Kleuren"][winnaars[1]]
        iconX = 160
        iconY = 60
        icon_tweeX = 850
        icon_tweeY = 60
        icon_drieX = 850
        icon_drieY = 60
        textX = 180
        textY = 540

        # icon
        iconImg = pygame.image.load(picture)
        iconTransformed = pygame.transform.scale(iconImg, (250, 270))

        # icon twee
        icon_tweeImg = pygame.image.load(picture_twee)
        icon_tweeTransformed = pygame.transform.scale(icon_tweeImg, (250, 270))

        return picture, picture_twee, button_een, button_twee, ondertekst, kleur_een, kleur_twee, iconX, iconY, icon_tweeX, icon_tweeY, icon_drieX, icon_drieY, iconTransformed, icon_tweeTransformed, textX, textY
    elif len(winnaars) == 3:
        picture = f"images/{winnaars[0]}_icon.png"
        picture_twee = f"images/{winnaars[1]}_icon.png"
        picture_drie = f"images/{winnaars[2]}_icon.png"
        button_een = spec_dict["Info"][winnaars[0]]
        button_twee = spec_dict["Info"][winnaars[1]]
        button_drie = spec_dict["Info"][winnaars[2]]
        ondertekst = f"Je hebt een combinatie van {button_een}, {button_twee} en {button_drie} Begin opnieuw voor een exactere uitslag!"
        kleur_een = spec_dict["Kleuren"][winnaars[0]]
        kleur_twee = spec_dict["Kleuren"][winnaars[1]]
        kleur_drie = spec_dict["Kleuren"][winnaars[2]]
        iconX = 160
        iconY = 60
        icon_tweeX = 500
        icon_tweeY = 60
        icon_drieX = 890
        icon_drieY = 60
        textX = 240
        textY = 540

        # icon
        iconImg = pygame.image.load(picture)
        iconTransformed = pygame.transform.scale(iconImg, (250, 270))

        # icon twee
        icon_tweeImg = pygame.image.load(picture_twee)
        icon_tweeTransformed = pygame.transform.scale(icon_tweeImg, (250, 270))

        # icon drie
        icon_drieImg = pygame.image.load(picture_drie)
        icon_drieTransformed = pygame.transform.scale(icon_drieImg, (250, 270))

        return picture, picture_twee, button_een, button_twee, ondertekst, kleur_een, kleur_twee, iconX, iconY, icon_tweeX, icon_tweeY, icon_drieX, icon_drieY, picture_drie, kleur_drie, button_drie, textX, textY, iconTransformed, icon_tweeTransformed, icon_drieTransformed
    else:
        print("Fout result_gelijk")

# scherm(winnaars1)
alle_variabelen = scherm(winnaars)
# scherm(winnaars3)

# Screen create
screen = pygame.display.set_mode((1280, 720))

# Text
FONT = pygame.font.Font("font/Harry_potter.ttf", 40)

# background
backgroundImg = pygame.image.load(achtergrond)
backgroundX = 0
backgroundY = 0

def border_een():
    screen.blit(borderimg, (alle_variabelen[7]+80,350))

# border
border = pygame.image.load('images/border.png')
borderimg = pygame.transform.scale(border, (100,50))

def background():
    screen.blit(backgroundImg, (backgroundX, backgroundY))

if len(winnaars) == 1: #Jasper was here
    def icon():
        screen.blit(alle_variabelen[6], (alle_variabelen[4], alle_variabelen[5]))
    def text():
        FONT = pygame.font.Font("font/Harry_potter.ttf", 40)
        label = FONT.render(alle_variabelen[2], True, (255, 255, 255))
        screen.blit(label, (alle_variabelen[7], alle_variabelen[8]))
    def text1():
        FONT = pygame.font.Font("font/Harry_potter.ttf", 40)
        label1 = FONT.render(alle_variabelen[9], True, (255, 255, 255))
        screen.blit(label1, (alle_variabelen[7], alle_variabelen[8]+50))
    def text2():
        FONT = pygame.font.Font("font/Harry_potter.ttf", 40)
        label2 = FONT.render(alle_variabelen[10], True, (255, 255, 255))
        screen.blit(label2, (alle_variabelen[7], alle_variabelen[8]+100))
    def back_button():
        back_button = ButtonClass.Button((alle_variabelen[3]), alle_variabelen[4] + 80, 350, 100, 50, 30, alle_variabelen[1])
        back_button.draw(screen, 0)
        return back_button
    def terug_button():
        terug_button = ButtonClass.Button((alle_variabelen[3]), 40, 650, 100, 50, 30,"Terug")
        terug_button.draw(screen, 0)
    def border_een():
        screen.blit(borderimg, (alle_variabelen[4] + 80, 350))

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
        terug_button = ButtonClass.Button((alle_variabelen[6]), alle_variabelen[9] + 80, 350, 100, 50, 30, alle_variabelen[3])
        terug_button.draw(screen, 0)
        return terug_button
    def back_button():
        terug_button = ButtonClass.Button((alle_variabelen[5]), alle_variabelen[7] + 80, 350, 100, 50, 30, alle_variabelen[2])
        terug_button.draw(screen, 0)
        return terug_button
    def border_een():
        screen.blit(borderimg, (alle_variabelen[7] + 80, 350))
    def border_twee():
        screen.blit(borderimg, (alle_variabelen[9] + 80, 350))
    def border_drie():
        screen.blit(borderimg, (alle_variabelen[11] + 80, 350))

if len(winnaars) == 3:
    def icon():
        screen.blit(alle_variabelen[18], (alle_variabelen[7], alle_variabelen[8]))
    def icon_twee():
        screen.blit(alle_variabelen[19], (alle_variabelen[9], alle_variabelen[10]))
    def icon_drie():
        screen.blit(alle_variabelen[20], (alle_variabelen[11], alle_variabelen[12]))
    def back_button():
        terug_button = ButtonClass.Button((alle_variabelen[5]), alle_variabelen[7] + 80, 350, 100, 50, 30, alle_variabelen[2])
        terug_button.draw(screen, 0)
        return terug_button
    def back_button_twee():
        terug_button = ButtonClass.Button((alle_variabelen[6]), alle_variabelen[9] + 80, 350, 100, 50, 30, alle_variabelen[3])
        terug_button.draw(screen, 0)
        return terug_button
    def back_button_drie():
        terug_button = ButtonClass.Button((alle_variabelen[14]), alle_variabelen[11] + 80, 350, 100, 50, 30, alle_variabelen[15])
        terug_button.draw(screen, 0)
        return terug_button
    def text():
        FONT = pygame.font.Font("font/Harry_potter.ttf", 40)
        label = FONT.render(alle_variabelen[4], True, (255, 255, 255))
        screen.blit(label, (alle_variabelen[16], alle_variabelen[17]))
    def border_een():
        screen.blit(borderimg, (alle_variabelen[7] + 80, 350))
    def border_twee():
        screen.blit(borderimg, (alle_variabelen[9] + 80, 350))
    def border_drie():
        screen.blit(borderimg, (alle_variabelen[11] + 80, 350))

# Game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False

    if len(winnaars) == 1:
        background()
        icon()
        back_button()
        border_een()
        text()
        text1()
        text2()
        terug_button()
    if len(winnaars) == 2:
        background()
        icon()
        back_button()
        border_een()
        icon_twee()
        back_button_twee()
        border_twee()
        text()
    if len(winnaars) == 3:
        background()
        icon()
        back_button()
        border_een()
        icon_twee()
        icon_drie()
        back_button_twee()
        back_button_drie()
        border_twee()
        border_drie()
        text()
    pygame.display.update()