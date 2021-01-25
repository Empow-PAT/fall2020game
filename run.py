import sys
import pygame
from fall2020game.players import *
from fall2020game.sprites import *
import pygame_menu
import pickle_func

pygame.init()
"""Defines the width of the room."""
windowwidth = 800
"""Defines the height of the room."""
windowheight = 800
"""Defines what white is(will come in handy later on.)"""
white = (255, 255, 255)
"""Defines what black is(will come in handy later on.)"""
black = (0, 0, 0)

pickle_func.create_file('coins')

pickle_func.create_file('username')

coins = pickle_func.read('coins')

default_user = pickle_func.read('username')


nickname = "Nickname"

annnihilator = None

def change_nickname(value):

    global nickname, annihilator

    nickname = value

def menubackground():

    if textin.get_value() == "ENTER NICKNAME" and textin.selected:

        textin.clear()

    textin._cursor_color=(255, 255, 255)

def start_game():

    global annihilator

    run = True

    annihilator = Annihilator(nickname)

    #tank = Tank(nickname)

    bot = Bot()
    BotPlay = [bot]
    StorageBotPlay = 1

    menu.disable()

    while run:

        pygame.time.delay(25)

        events = pygame.event.get()

        for event in events:

            if event.type == pygame.QUIT:

                run = False

        keys = pygame.key.get_pressed()

        win.fill(black)

        win.blit(sprites["apod1"], (0, 0))
        AllBotsDead = True
        annihilator.tick(keys, win)
        Level1 = 0
        Level2 = 0
        Level3 = 0
        for item in BotPlay:
             item.tick(win, annihilator)
             if item.hp > 0:
                 AllBotsDead = False
        #tank.tick(keys, win)
        if AllBotsDead == False:
            bot.tick(win, annihilator)
        if AllBotsDead == True:
                bot2 = Bot()
                bot3 = Bot()
                BotPlay.append(bot2)
                BotPlay.append(bot3)
                Level1 += 1

        if AllBotsDead == True and Level1 == 1:
                bot4 = Bot()
                bot5 = Bot()
                bot6 = Bot()
                bot7 = Bot()
                BotPlay.append(bot4)
                BotPlay.append(bot5)
                BotPlay.append(bot6)
                BotPlay.append(bot7)
                Level2 += 1

                if AllBotsDead == True and Level2 == 1:
                    bot8 = Bot()
                    bot9 = Bot()
                    bot10 = Bot()
                    bot11 = Bot()
                    bot12 = Bot()
                    bot13 = Bot()
                    bot14 = Bot()
                    bot15 = Bot()
                    BotPlay.append(bot8)
                    BotPlay.append(bot9)
                    BotPlay.append(bot10)
                    BotPlay.append(bot11)
                    BotPlay.append(bot12)
                    BotPlay.append(bot13)
                    BotPlay.append(bot14)
                    BotPlay.append(bot15)







        for ult in ults:

            if ult.time < 120:

                ult.tick(win)

        for projectile in projectiles:

            #if not projectile.velx == 0 and not projectile.vely == 0:
            projectile.tick(win, windowwidth, windowheight,bot)

        pygame.display.update()
"""Defining the background menu."""
backgroundmenu = pygame_menu.baseimage.BaseImage(
    image_path="Images/Loading Page.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
"""Defining the play button."""
playbutton2 = pygame_menu.baseimage.BaseImage(
    image_path="Images/Play Button.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
"""Defining the ships button."""
ships2 = pygame_menu.baseimage.BaseImage(
    image_path="Images/Ships.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

X = "Images/X Button.png"

win = pygame.display.set_mode((windowwidth, windowheight))

pygame.display.set_caption("Astral Run")

myfont = pygame.font.SysFont('Impact', 100)  # change the 30 for a different text size

mytheme = pygame_menu.themes.Theme(
    menubar_close_button=False,
    title_font=pygame_menu.font.FONT_MUNRO,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    background_color=backgroundmenu,
)

menu = pygame_menu.Menu(windowheight-1, windowwidth-1, " ", theme=mytheme)

menu.add_label("", selectable=True)

textin = menu.add_text_input('', default="ENTER NICKNAME", onchange=change_nickname)

playbutton = menu.add_button("        ", start_game, background_color=playbutton2, font_size=72, widget_selection_effect=pygame_menu.widgets.NoneSelection())

ships = menu.add_button("         ", None, background_color=ships2, font_size=36, widget_selection_effect=pygame_menu.widgets.NoneSelection())

menu.mainloop(win, bgfun=menubackground)
