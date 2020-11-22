import sys
import pygame
from fall2020game.players import *
from fall2020game.sprites import *
import pygame_menu
nickname = "Javi"


def Nickname(value):
    global nickname

    nickname = value
    
gameStart = False
def start_game():
    global gameStart
    gameStart = True

def main():
    global nickname
    global gameStart
    
    pygame.init()
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

    pygame.display.set_caption("Starter")
    black = (0, 0, 0)
    white = (255, 255, 255)

    myfont = pygame.font.SysFont('Impact', 30)  # change the 30 for a different text size
    annihilator = Annihilator()
    mytheme = pygame_menu.themes.Theme(
        menubar_close_button=False,
        title_font=pygame_menu.font.FONT_MUNRO,
        title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
        background_color=black,
        widget_selection_effect=pygame_menu.widgets.NoneSelection(),
    )
    menu = pygame_menu.Menu(windowheight-1, windowwidth-1, " ", theme=mytheme)

    menu.add_text_input('', default='ENTER NICKNAME HERE', onchange=Nickname, cursor_selection_enable=True, selection_effect= pygame_menu.widgets.HighlightSelection())
    playbutton = menu.add_button("        ", start_game, background_color=playbutton2, font_size=72)
    ships = menu.add_button("         ", None, background_color=ships2, font_size=36)
    pygame.display.update()

    menu.mainloop(win)

    run = True
    while run:

        pygame.time.delay(25)

        if not gameStart:
            menu.draw(win)
        else:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False

        keys = pygame.key.get_pressed()
        annihilator.tick(keys)

        win.blit(sprites["apod1"],(0,0))

        textsurface = myfont.render(""" PLAY """, False, white)
        win.blit(textsurface, (300, 390))  # change the coordinates to put it in a different place

        pygame.display.update()


if __name__ == '__main__':
    main()
