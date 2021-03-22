"""File that combines all the files, as shown at the 4&5 lines, and runs them coherently. """
import sys
import pygame
import pygame_menu
from fall2020game.players import *
from fall2020game.players.Annihilator import Sheild
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

# Creates a file called "coins" using pickle
#pickle_func.create_file('coins')
# Creates a file called "username" using pickle
#pickle_func.create_file('username')
# Creates a variable with the value of the "coins" file
#coins = pickle_func.read('coins')
# Creates a variable with the value of the "username" file
#default_user = pickle_func.read('username')


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
    bot = Bot()
    annihilator = Annihilator(nickname,bot)
    sheild = Sheild(annihilator,bot)
    tank = Tank(nickname)

    BotPlay = [bot]
    Level1 = 0
    Level2 = 0
    Level3 = 0

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
#       annihilator.tick(keys, win)

        for item in BotPlay:
             if item.hp > 0:
                 item.tick(win, annihilator)
                 AllBotsDead = False
        #tank.tick(keys, win)
        #if AllBotsDead == False:
         #   bot.tick(win, annihilator)
        if AllBotsDead == True and Level1 == 0:
            bot2 = Bot()
            BotPlay.append(bot2)
            Level1+=1
        if len(BotPlay) > 1:
            if Level1 == 1:
                print("Hello")
                #if BotPlay[1].StaggerTimer == 100:
                #print(BotPlay[1].StaggerTimer)
                bot3 = Bot()
                BotPlay.append(bot3)
                BotPlay[2].speed -= 0
                Level1 +=1
            if AllBotsDead == True and Level1 == 2:
                Level2 += 1


        if len(BotPlay) > 1 and Level1 == 2:
            if Level2 == 1 and len(BotPlay) == 3:
                bot4 = Bot()
                BotPlay.append(bot4)
                print("HI")
                Level2 += 1
            elif Level2 == 2 and len(BotPlay) == 4:
                BotPlay[3].speed -= 1
                bot5 = Bot()
                BotPlay.append(bot5)
                Level2 +=1
            elif Level2 == 3 and len(BotPlay) == 5:
                BotPlay[4].speed -= 2
                bot6 = Bot()
                BotPlay.append(bot6)
                Level2 += 1
            elif Level2 == 4 and len(BotPlay) == 6:
                BotPlay[5].speed -= 3
                bot7 = Bot()
                BotPlay.append(bot7)
                Level2 = 5
                Level3 += 1

        if len(BotPlay) > 1 and Level2 == 5:
            if Level3 == 1 and len(BotPlay) == 3:
                BotPlay[6].speed -= 4
                bot8 = Bot()
                BotPlay.append(bot8)
                print("HI")
                Level2 += 1
            elif Level2 == 2 and len(BotPlay) == 4:
                BotPlay[6].speed -= 3
                bot9 = Bot()
                BotPlay.append(bot9)
                Level2 +=1
            elif Level2 == 3 and len(BotPlay) == 5:
                BotPlay[7].speed -= 2
                bot10 = Bot()
                BotPlay.append(bot10)
                Level2 += 1
            elif Level2 == 4 and len(BotPlay) == 6:
                BotPlay[8].speed -= 1
                bot11 = Bot()
                BotPlay.append(bot11)
                Level2 += 1

        # if AllBotsDead == True and Level2 == 1:
        #         bot8 = Bot()
        #         BotPlay.append(bot8)
        #         if BotPlay[7].StaggerTimer == 200:
        #             bot9 = Bot()
        #             BotPlay.append(bot9)
        #             if BotPlay[8].StaggerTimer == 200:
        #                 bot10 = Bot()
        #                 BotPlay.append(bot10)
        #                 if BotPlay[9].StaggerTimer == 200:
        #                     bot11 = Bot()
        #                     BotPlay.append(bot11)
        #                     if BotPlay[10].StaggerTimer == 200:
        #                         bot12 = Bot()
        #                         BotPlay.append(bot12)
        #                         if BotPlay[11].StaggerTimer == 200:
        #                             bot13 = Bot()
        #                             BotPlay.append(bot13)
        #                             if BotPlay[12].StaggerTimer == 200:
        #                                 bot14 = Bot()
        #                                 BotPlay.append(bot14)
        #                                 if BotPlay[13].StaggerTimer == 200:
        #                                     bot15 = Bot()
        #                                     BotPlay.append(bot15)


        if annihilator.hp > 0:
            annihilator.tick(keys, win, sheild)
        #tank.tick(keys, win)
        #if bot.hp > 0:
           # bot.tick(win, annihilator)
        if sheild.hp > 0:
            sheild.tick(win,annihilator)
        for ult in ults:
            if ult.time < 120:
                ult.tick(win,bot)
        for projectile in projectiles:
            projectile.tick(win, windowwidth, windowheight, bot, sheild)
        for projectilEn in enemyProjs:
            projectilEn.tick(win,annihilator, bot)
        pygame.display.update()

from os import path
here = path.dirname(path.abspath(__file__))
print(here)

"""Defining the background menu."""
backgroundmenu = pygame_menu.baseimage.BaseImage(
    image_path = path.join(here, "Images/Loading Page.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
"""Defining the play button."""
playbutton2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/Play Button.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
"""Defining the ships button."""
ships2 = pygame_menu.baseimage.BaseImage(
    image_path=path.join(here, "Images/Ships.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

X = path.join(here, "Images/X Button.png")     

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
