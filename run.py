import sys
import pygame
from fall2020game.players import *


def main():
    global run
    pygame.init()

    windowwidth = 800
    windowheight = 800
    win = pygame.display.set_mode((windowwidth, windowheight))

    pygame.display.set_caption("Starter")
    black = (0, 0, 0)
    white = (255, 255, 255)

    myfont = pygame.font.SysFont('Impact', 100)  # change the 30 for a different text size
    annihilator = Annihilator()

    class PlayButton:
        def __init__(self):
            self.Color = (150, 240, 30)
            self.x = 200
            self.y = 400
            self.width = 400
            self.height = 100
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        def tick(self, win):
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

            pygame.draw.rect(win, self.Color, self.rect)
    playbutton = PlayButton()

    run = True
    while run:

        pygame.time.delay(25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        win.fill(black)
        annihilator.tick(keys, win)
        playbutton.tick(win)

        for projectile in projectiles:
            projectile.tick(win, windowwidth, windowheight)

        textsurface = myfont.render(""" PLAY """, False, white)
        win.blit(textsurface, (300, 390))  # change the coordinates to put it in a different place

        pygame.display.update()


if __name__ == '__main__':
    main()




