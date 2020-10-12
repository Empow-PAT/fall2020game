import pygame
import random
import time

windowwidth = 1000
windowheight = 750
white = (255, 255, 255)
black = (0,0,0)
yellow = (255, 255, 0)
red = (255,0,0)
green =  (0,255,0)
lightblue=(0,188,255)
gold = (255,215,0)
sheildColor = (51,255,255)
multiplayer = True

pygame.init()

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

    def tick(self):
        if keys[pygame.K_a]:
            self.x-=10
            self.velx
        if keys[pygame.K_d]:
            self.x += 10
            self.dir = "right"