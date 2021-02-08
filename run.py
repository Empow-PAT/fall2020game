"""File that combines all the files, as shown at the 4&5 lines, and runs them coherently. """
import sys
import pygame
from fall2020game.players import *
from fall2020game.sprites import *
import pygame_menu
#from fall2020game.tests.pickle_func.py import *

pygame.init()

windowwidth = 800
windowheight = 800
white = (255, 255, 255)
black = (0, 0, 0)

#pickle_func.create_file('coins')
#pickle_func.create_file('username')
#coins = pickle_func.read('coins')
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
    annihilator = Annihilator(nickname)
    tank = Tank(nickname)
    bot = Bot()

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
        if annihilator.hp > 0:
            annihilator.tick(keys, win)
        #tank.tick(keys, win)
        if bot.hp > 0:
            bot.tick(win, annihilator)
        else:
            bot.rect = pygame.Rect(1000000000000,10000000000,0,0)
        for ult in ults:
            if ult.time < 120:
                ult.tick(win)
        for projectile in projectiles:
            projectile.tick(win, windowwidth, windowheight,bot)
        for projectilEn in enemyProjs:
            projectilEn.tick(win,annihilator)
        pygame.display.update()


backgroundmenu = pygame_menu.baseimage.BaseImage(
    image_path="Images/Loading Page.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
playbutton2 = pygame_menu.baseimage.BaseImage(
    image_path="Images/Play Button.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
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
