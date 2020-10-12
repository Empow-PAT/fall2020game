import sys
import pygame
from fall2020game.players import *


def main():
    pygame.init()

    windowwidth = 400
    windowheight = 400
    win = pygame.display.set_mode((windowwidth, windowheight))
    pygame.display.set_caption("Starter")
    black = (0, 0, 0)
    white = (255, 255, 255)

    myfont = pygame.font.SysFont('Impact', 30)  # change the 30 for a different text size


    run = True
    while run:
        pygame.time.delay(25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        win.fill(black)

        textsurface = myfont.render("""GAME OVER.""", False, white)
        win.blit(textsurface, (0, 0))  # change the coordinates to put it in a different place

        pygame.display.update()


if __name__ == '__main__':
    main()

