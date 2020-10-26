__all__ = ['PlayerWaving']

import pygame
from fall2020game.sprites import sprites

# Load in the image(s) you want
images = [sprites[str(n)] for n in range(4)]

class PlayerWaving:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.width = 50
        self.height = 50
        self.vely = 0
        self.gravity = 1
        self.jumping = False
        self.jumppower = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.coincount = 0

        # Resize the image so it matches the player
        self.imagenum = 0
        self.image = pygame.transform.scale(images[self.imagenum], (self.width, self.height))

    def tick(self, time, keys, windowwidth, windowheight):
        if time % 10 == 0:
            if self.imagenum < len(images) - 1:
                self.imagenum += 1
            else:
                self.imagenum = 0

        self.image = pygame.transform.scale(images[self.imagenum], (self.width, self.height))

        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_UP] and self.jumping == False:
            self.vely = -self.jumppower
            self.jumping = True

        self.vely += self.gravity
        self.y += self.vely

        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
        if self.x < 0:
            self.x = 0
        if self.y > windowwidth - self.height:
            self.y = windowwidth - self.height
            self.vely = 0
            self.jumping = False
        if self.y < 0:
            self.y = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def position(self):
        return self.x, self.y

