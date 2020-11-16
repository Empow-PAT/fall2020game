import sys
import pygame
from fall2020game.players import *
import pygame_menu
nickname = "Javi"


def Nickname(value):
    global nickname

    nickname = value


def main(gameStart=None):
    global nickname
    pygame.init()
    nickname = "Nickname"
    black = pygame_menu.baseimage.BaseImage(
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

    windowwidth = 800
    windowheight = 800
    win = pygame.display.set_mode((windowwidth, windowheight))
    mytheme = pygame_menu.themes.Theme(
        menubar_close_button=False,
        title_font=pygame_menu.font.FONT_MUNRO,
        title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
        background_color=black,
        widget_selection_effect=pygame_menu.widgets.NoneSelection(),
    )
    menu = pygame_menu.Menu(windowheight-1, windowwidth-1, " ", theme=mytheme)

    menu.add_text_input('', default='ENTER NICKNAME HERE', onchange=Nickname, cursor_selection_enable=True, selection_effect= pygame_menu.widgets.HighlightSelection())
    playbutton = menu.add_button("        ", gameStart, background_color=playbutton2, font_size=72)
    ships = menu.add_button("         ", gameStart, background_color=ships2, font_size=36)
    pygame.display.update()

    menu.mainloop(win)


if __name__ == '__main__':
    main()
