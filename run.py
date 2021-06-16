"""File that combines all the files, as shown at the 5&6 lines, and runs them coherently. """
import sys
import pygame
from fall2020game.players import *
from fall2020game.players.Annihilator import Sheild
from fall2020game.players.Annihilator import UserAssist, HelperBot, Heal_Projectile
from fall2020game.sprites import *
from fall2020game.terrrain import *
import pygame_menu
import pickle_func
MenuPage = 1
pygame.init()
"""Defines the width of the room."""
windowwidth = 800
"""Defines the height of the room."""
windowheight = 800
"""Defines what white is(will come in handy later on.)"""
white = (255, 255, 255)
"""Defines what black is(will come in handy later on.)"""
black = (0, 0, 0)
shield_gen = 0

def ReturntoHome():
    MenuPage = 1
    menu2.disable()
    menu.enable()
    menu.mainloop(win, bgfun=menubackground)
HelperBotImage = "Images/HelperBot.png"
try:
    nickname = pickle_func.read('savename.pickle')
except FileNotFoundError:
    nickname = "ENTER NICKNAME"
try:
    keymode = pickle_func.read('savemode.pickle')
except FileNotFoundError:
    keymode = 0
def ChangeHBSkin_gabe():
    global HelperBotImage
    HelperBotImage = "Images/BillyHelperBot.png"

def ChangeHBSkin_javi():
    global HelperBotImage
    HelperBotImage = "Images/HelperBot.png"

def ChangeHBSkin_asmee():
    global HelperBotImage
    HelperBotImage = "Images/SHIP-1.png.png"
def ChangeHBSkin_asmee2():
    global HelperBotImage
    HelperBotImage = "Images/New Piskel.png"

def ChangeHBSkin_connor():
    global HelperBotImage
    HelperBotImage = "Images/ConnorHelperBot.png"

annnihilator = None
def change_nickname(value):
    global nickname, annihilator
    nickname = value
    pickle_func.write('savename.pickle', nickname)

def menubackground():
    if textin.get_value() == "ENTER NICKNAME" and textin.is_selected():
        textin.clear()
    AnnihilatorButton.set_position(40, 60)
    JaviBotButton.set_position(40, 360)
    GabeBotButton.set_position(200, 360)
    ConnorBotButton.set_position(360, 360)
    AsmeeBotButton.set_position(60, 440)
    AsmeeBotButton3.set_position(220, 440)

def start_game():
    global annihilator
    run = True
    #Constructors
    bot = Bot()
    sysAssist = UserAssist()
    annihilator = Annihilator(nickname)
    sheild = Sheild(annihilator)
    tank = Tank(nickname)

    BotPlay = [bot]
    Level1 = 0
    Level2 = 0
    Level3 = 0
    Level1B = 0

    astro = Astro()
    astro2 = Astro()
    astro3 = Astro()
    astro4 = Astro()
    astro5 = Astro()
    astro6 = Astro()
    astro7 = Astro()
    astro8 = Astro()
    astro9 = Astro()
    astro10 = Astro()
    astro11 = Astro()
    astro12 = Astro()
    astro13 = Astro()
    astro14 = Astro()
    astro15 = Astro()
    astro16 = Astro()
    astro17 = Astro()
    astro18 = Astro()
    astro19 = Astro()
    astro20 = Astro()
    astro_alive = [astro, astro2, astro3, astro4, astro5, astro6, astro7, astro8, astro9, astro10, astro11, astro12, astro13,astro14,astro15,astro16,astro17,astro18,astro19,astro20]

    #claymore = Claymore(windowwidth, windowheight)
    effect = Effect(windowwidth,windowheight)
    helperBot = HelperBot( annihilator, HelperBotImage)
    while run:
        pygame.time.delay(25)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        win.fill(black)
        win.blit(sprites["apod1"], (0, 0))
        helperBot.tick(win,annihilator)
        AllBotsDead = True
        #claymore.tic(win)

#   CCC        A        M       M    PPP        A      IIIIIII       GGGGGG      N     N
#  C   C      A A       M M   M M    P  P      A A        I         G            N N   N
# C          AAAAA      M   M   M    PPP      AAAAA       I        G   GGGGGG    N  N  N
#  C   C    A     A     M       M    P       A     A      I         G      G     N   N N
#   CCC    A       A    M       M    P      A       A  IIIIIII       GGGGG       N     N

        for item in BotPlay:
             if item.hp > 0:
                 item.tick(win, annihilator, BotPlay)
                 AllBotsDead = False
             else:
                item.rect = pygame.Rect(0, 0, 1000000, -10000)
                BotPlay.remove(item)
        #tank.tick(keys, win)
        #if AllBotsDead == False:
         #   bot.tick(win, annihilator)
        if len(BotPlay) == 0 and Level1 == 0:
            bot2 = Bot()
            BotPlay.append(bot2)
            Level1+=1
        if len(BotPlay) == 0 and Level1 == 1:
            if len(BotPlay) == 0 and Level1B == 0:
                bot3 = Bot()
                BotPlay.append(bot3)
                Level1B +=1
            if len(BotPlay) == 1 and Level1B == 1:
                bot4 = Bot()
                BotPlay.append(bot4)
                Level1 = 2
                Level2 = 1


        if len(BotPlay) == 0 and Level1 == 2:
            if Level2 == 1 and len(BotPlay) == 0:
                bot5 = Bot()
                BotPlay.append(bot5)
                Level2 += 1
        elif Level2 == 2 and len(BotPlay) == 1:
            bot6 = Bot()
            BotPlay.append(bot6)
            Level2 +=1
        elif Level2 == 3 and len(BotPlay) == 2:
            bot7 = Bot()
            BotPlay.append(bot7)
            Level2 += 1
        elif Level2 == 4 and len(BotPlay) == 3:
            bot8 = Bot()
            BotPlay.append(bot8)
            Level2 = 5
            Level3 = 1

        if len(BotPlay) == 0 and Level2 == 5:
            if Level3 == 1 and len(BotPlay) == 0:
                bot9 = Bot()
                BotPlay.append(bot9)
                Level3 += 1
        elif Level3 == 2 and len(BotPlay) == 1:
            bot10 = Bot()
            BotPlay.append(bot10)
            Level3 +=1
        elif Level3 == 3 and len(BotPlay) == 2:
            bot11 = Bot()
            BotPlay.append(bot11)
            Level3 += 1
        elif Level3 == 4 and len(BotPlay) == 3:
            bot12 = Bot()
            BotPlay.append(bot12)
            Level3 +=1
        elif Level3 == 1 and len(BotPlay) == 4:
            bot9 = Bot()
            BotPlay.append(bot9)
            Level3 += 1
        elif Level3 == 2 and len(BotPlay) == 5:
            bot10 = Bot()
            BotPlay.append(bot10)
            Level3 += 1
        elif Level3 == 3 and len(BotPlay) == 6:
            bot11 = Bot()
            BotPlay.append(bot11)
            Level3 += 1
        elif Level3 == 4 and len(BotPlay) == 7:
            bot12 = Bot()
            BotPlay.append(bot12)
            Level3 = 100

        #Tick Functions being called
        if annihilator.hp > 0:
            annihilator.tick(keys, win, sheild, keymode)

        elif annihilator.hp <= 0:
            "Turning off the menu page."
            MenuPage = 0
            menu.disable()
            run = False

        if sheild.hp > 0:
            sheild.tick(win,annihilator)
        for ult in ults:
            if ult.time < 120:
                ult.tick(win,bot)
        for projectile in projectiles:
            projectile.tick(win, windowwidth, windowheight, BotPlay, sheild)
        for projectile_Heal in Heal_Projectile:
            projectile_Heal.tick(win, annihilator)
        for projectilEn in enemyProjs:
            projectilEn.tick(win,annihilator, sheild, projectiles, windowwidth, windowheight)
        sysAssist.tick(win)
        for astro in astro_alive:
            astro.tick(astro_alive, win)
            if astro.rect.colliderect(annihilator.rect):
                astro_alive.remove(astro)
                annihilator.hp -= 10
            else:
                for bot in BotPlay:
                    if astro.rect.colliderect(bot.rect):
                        astro_alive.remove(astro)
                        bot.hp -= 10
                        break
        effect.tick(win, windowwidth, windowheight)
        if annihilator.rect.colliderect(effect.rect) and effect.counter >= 400:
            power(annihilator, bot)
            effect.counter = 0

        pygame.display.update()
if MenuPage == 1:
    from os import path
    here = path.dirname(path.abspath(__file__))

"""Defining the background menu."""
shipsbackground = pygame_menu.baseimage.BaseImage(
    image_path = path.join(here, "Images/Ships Background.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
backgroundmenu = pygame_menu.baseimage.BaseImage(
    image_path = path.join(here, "Images/Loading Page.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
"""Defining the play button."""
playbutton2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/Play Button.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
JaviBotButton2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/HelperBot.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
GabeBotButton2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/BillyHelperBot.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
ConnorBotButton2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/ConnorHelperBot.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
AsmeeBotButton2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/SHIP-1.png.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
AsmeeBotButton4 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/New Piskel.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
AnnihilatorButton2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/Annihilator Ships Image.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
"""Defining the ships button."""
ships2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/Ships.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

settingsbutton = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/SettingsButton.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

usespace = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/SpaceShoot.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)


usearrows = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/ArrowKeys.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)


goback = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here,"Images/Gobackbutton.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)


annihilatorUI = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/AnnihilatorUI.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)


instructbagr = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/Info.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

def arrowshooting():
    global keymode
    keymode = 1
    pickle_func.write("savemode.pickle", keymode)

def spaceshooting():
    global keymode
    keymode = 0
    pickle_func.write("savemode.pickle", keymode)

def option1():
    path.join(here, "Images/annihilatorUI.png")



X = path.join(here, "Images/X Button.png")

win = pygame.display.set_mode((windowwidth, windowheight))

pygame.display.set_caption("Astral Run")
myfont = pygame.font.SysFont('Impact', 100)  # change the 30 for a different text size
mytheme3 = pygame_menu.themes.Theme(
    title_close_button=False,
    title_font=pygame_menu.font.FONT_MUNRO,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    background_color=shipsbackground,
)
mytheme = pygame_menu.themes.Theme(
    title_close_button=False,
    title_font=pygame_menu.font.FONT_MUNRO,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    background_color=backgroundmenu,
)

infoscreen = pygame_menu.Menu("  ", windowwidth - 1, windowheight - 1, theme=mytheme3, onclose=pygame_menu.events.BACK)
backbutton = infoscreen.add.button("Back",pygame_menu.events.BACK, background_color=goback,font_size=50,font_color=("orange"), selection_effect=pygame_menu.widgets.NoneSelection())
infoscreen.add.label("Scroll down to see more advice!", font_color=("white"))
infoscreen.add.label("")
infoscreen.add.label("")
infoscreen.add.label("""You are a captain on a ship, lost in space.
You need to survive as people try to come rescue you.
As time goes on, more enemy bots with their own minds commandeer ships try to
find you and hunt you down""", max_char=-1, font_size=20, font_color=("grey"))
infoscreen.add.label("")
infoscreen.add.label("""Starting the game: 
            After clicking play, the ship will ask for your preferred shooting style. Click the one you want, then click the play button for a second time

Modules: 
            Press 'Q' for a devastating shockwave that damages all bot ships around you.
Shockwave cooldown is indicated by the 'Ultimate Cooldown' on the top right of your playing screen

Press 'X' for a speedy dash that'll leave opponents in the dust
Dash cooldown is indicated by the 'Dash Cooldown' on the top right of your playing screen

Finally, press 'E' for a mechanic to repair the ship of most damage
Repair is indicated by the 'Active Module Cooldown' on the top right of your playing screen

Passives: 
            At the beginning of the game, you will have shields raised. This will not come back once destroyed, but will regenerate after a short period, so long as you do not get hit during that period


Extras:
            When you start the game, a fast version of the instructions will flash on the bottom right of the screen
            Health is above your ship. Shield health is above your ship. Character name (should you choose one) is above your ship
            Powerups will occasionally appear in a random location, that will give your ship extra stregth to survive""", max_char=-1, font_size=17, font_color=("grey"))


infoscreen.add.label("")
infoscreen.add.label("")

ships_menu = pygame_menu.Menu("", windowwidth - 5, windowheight - 5, theme=mytheme3, onclose=pygame_menu.events.BACK, columns=6, rows=6)
AnnihilatorButton = ships_menu.add.button("        ", None, background_color=AnnihilatorButton2, font_size=72)

GabeBotButton = ships_menu.add.button("        ", ChangeHBSkin_gabe, background_color= GabeBotButton2, font_size=72,)
JaviBotButton = ships_menu.add.button("        ", ChangeHBSkin_javi, background_color= JaviBotButton2, font_size=72,)
ConnorBotButton = ships_menu.add.button("        ", ChangeHBSkin_connor, background_color= ConnorBotButton2, font_size=72,)
AsmeeBotButton = ships_menu.add.button("        ", ChangeHBSkin_asmee, background_color= AsmeeBotButton2, font_size=55,)
AsmeeBotButton3 = ships_menu.add.button("        ", ChangeHBSkin_asmee2, background_color= AsmeeBotButton4, font_size=55,)
ships_menu.add.button("Back",pygame_menu.events.BACK, background_color=goback,font_size=50,font_color=("orange"))

minimenu = pygame_menu.Menu("  ", windowwidth - 1, windowheight - 1, theme=mytheme, onclose=pygame_menu.events.BACK)
minimenu.add.label("")
minimenu.add.label("")
minimenu.add.label("")
shootarrows = minimenu.add.button("    ", arrowshooting, background_color=usearrows, font_size=72,
                                 selection_effect=pygame_menu.widgets.NoneSelection())

shootspace = minimenu.add.button("                    ", spaceshooting, background_color=usespace, font_size=50,
                                     selection_effect=pygame_menu.widgets.NoneSelection())

startthegamebutton = minimenu.add.button("       ",start_game, background_color=playbutton2, font_size=72,
                                         selection_effect=pygame_menu.widgets.NoneSelection())

backbutton = minimenu.add.button("Back",pygame_menu.events.BACK, background_color=goback,font_size=50,font_color=("orange"), selection_effect=pygame_menu.widgets.NoneSelection())

dontshowbutton = minimenu.add.button("Don't show this again", font_color=("white"))

menu = pygame_menu.Menu(" ", windowwidth-1,  windowheight-1, theme=mytheme)


menu.add.label("", selectable=True, selection_effect=pygame_menu.widgets.NoneSelection())
textin = pygame_menu.widgets.TextInput('', onchange=change_nickname, cursor_color=white)
textin.set_default_value(nickname)
menu.add.generic_widget(textin, True)
playbutton = menu.add.button("        ", minimenu, background_color=playbutton2, font_size=72, selection_effect=pygame_menu.widgets.NoneSelection())
#setting = menu.add.button("        ", minimenu, background_color=settingsbutton, font_size=72, selection_effect=pygame_menu.widgets.NoneSelection())
ships = menu.add.button("         ", ships_menu, background_color=ships2, font_size=36, selection_effect=pygame_menu.widgets.NoneSelection())
instruct = menu.add.button("Info", infoscreen, background_color=instructbagr, font_size=36, font_color=("black") ,selection_effect=pygame_menu.widgets.NoneSelection())
menu.mainloop(win, bgfun=menubackground)

if annihilator.hp >= 1:
    VictoryPage = pygame_menu.baseimage.BaseImage(
        image_path = path.join(here, "Images/VictoryPageRefurbished.png"),
        drawing_mode = pygame_menu.baseimage.IMAGE_MODE_FILL,
    )
else:
    VictoryPage = pygame_menu.baseimage.BaseImage(
        image_path=path.join(here, "Images/LoserPagePng.png"),
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    )

MenuReturnButton2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/Return To Home Button.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

mytheme2 = pygame_menu.themes.Theme(
    title_close_button=False,
    title_font=pygame_menu.font.FONT_MUNRO,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    background_color=VictoryPage,
)
menu2 = pygame_menu.Menu(" ", windowwidth - 1, windowheight - 1, theme=mytheme2)
menu2.add.label("", selectable=True, selection_effect=pygame_menu.widgets.NoneSelection())
MenuReturnButton = menu2.add.button("                           ", ReturntoHome, background_color=MenuReturnButton2, font_size=72,
                             selection_effect=pygame_menu.widgets.NoneSelection())
menu2.mainloop(win, bgfun=menubackground)
