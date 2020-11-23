import sys
import pygame
from fall2020game.players import *
from fall2020game.sprites import *
import pygame_menu

pygame.init()

windowwidth = 800
windowheight = 800
white = (255, 255, 255)
black = (0, 0, 0)

nickname = "Javi"

def change_nickname(value):
    global nickname
    nickname = value

def start_game():
    run = True
    annihilator = Annihilator(nickname)
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
        annihilator.tick(keys, win)
        bot.tick(win, annihilator)
        for ult in ults:
            if ult.time < 120:
                ult.tick(win)
        for projectile in projectiles:
            projectile.tick(win, windowwidth, windowheight)

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

menu.add_text_input('', default=nickname, onchange=change_nickname)
playbutton = menu.add_button("        ", start_game, background_color=playbutton2, font_size=72, widget_selection_effect=pygame_menu.widgets.NoneSelection())
ships = menu.add_button("         ", None, background_color=ships2, font_size=36, widget_selection_effect=pygame_menu.widgets.NoneSelection())
menu.mainloop(win)
