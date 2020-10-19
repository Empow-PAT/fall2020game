import pygame
import random
import time





white = (255, 255, 255)
black = (0,0,0)
yellow = (255, 255, 0)
red = (255,0,0)
green =  (0,255,0)
lightblue=(0,188,255)
gold = (255,215,0)
sheildColor = (51,255,255)
multiplayer = True


class Annihilator:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 25.0
        self.width = 25.0
        #gravity, friction, slope, upwards velocity, x velocity
        self.velx = 0
        self.vely = 0
        self.hp = 1000
        self.nickName = "Nickname"
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self,keys,win):
        if keys[pygame.K_a]:
            self.velx = -12
        elif keys[pygame.K_d]:
            self.velx = 12
        else:
            if self.velx > 0:
                self.velx -= 0.4
            if self.velx < 0:
                self.velx += 0.4

        if keys[pygame.K_w]:
            self.vely = -12
        elif keys[pygame.K_s]:
            self.vely = 12
        else:
            if self.vely > 0:
                self.vely -= 0.4
            if self.vely < 0:
                self.vely += 0.4

        self.x += self.velx
        self.y += self.vely

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, lightblue, self.rect)

