import sys
import pygame
from players import *


def main():
    pygame.init()

    windowwidth = 400
    windowheight = 400
    win = pygame.display.set_mode((windowwidth, windowheight))
    pygame.display.set_caption("Images and text")
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)

    # Load in the font you want
    myfont = pygame.font.SysFont('Impact', 30)  # change the 30 for a different text size

    # Choose which version of the player we're using.
    if sys.argv[1].lower() == 'wave':
        player = PlayerWaving()
    elif sys.argv[1].lower() == 'strobe':
        player = PlayerStrobing()


    run = True
    time = 0
    while run:
        pygame.time.delay(25)
        time += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        win.fill(black)

        player.tick(time, keys, windowwidth, windowheight)
        win.blit(player.image, player.position())

        #Add in text
        textsurface = myfont.render("Score: "+str(int(time/25)), False, white)
        win.blit(textsurface, (0, 0))  # change the coordinates to put it in a different place

        textsurface2 = myfont.render("Alien Game", False, blue)
        win.blit(textsurface2, (0, windowheight-50))  # change the coordinates to put it in a different place

        pygame.display.update()


if __name__ == '__main__':
    main()

