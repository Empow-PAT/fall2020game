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
    black = (0, 0, 0)


    windowwidth = 800
    windowheight = 800
    win = pygame.display.set_mode((windowwidth, windowheight))
    win = pygame.display.set_mode((windowwidth, windowheight))
    win.fill(black)

    menu = pygame_menu.Menu(windowheight-1, windowwidth-1, 'Astral Run',theme=pygame_menu.themes.THEME_DARK)
    menu.add_text_input('Player 1 : ', default='Nickname', onchange=Nickname)
    menu.add_button('Play', gameStart)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    pygame.display.update()

    menu.mainloop(win)
if __name__ == '__main__':




    main()
