import pygame
import math


white = (255, 255, 255)
black = (0,0,0)
yellow = (255, 255, 0)
red = (255,0,0)
green =  (0,255,0)
lightblue = (0,188,255)
gold = (255,215,0)

class Annihilator:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 25.0
        self.width = 25.0
        #friction, slope, upwards velocity, x velocity
        self.speed = 12
        self.velx = 0
        self.vely = 0
        self.hp = 1000
        self.friction = 0.4
        self.dirx = 0
        self.diry = 0
        self.nickName = "Nickname"
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)




class Bot:
    def __init__(self):
        self.height = 25.0
        self.width = 25.0
        self.x = 0
        self.y = 0 + self.height
        #gravity, friction, slope, upwards velocity, x velocity
        self.velx = 0
        self.vely = 0
        self.hp = 1000
        self.nickName = "Nickname"
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 9


    def tick(self, win, player):
       # (dx, dy) = ((player.x - self.x) / (math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)+.01),
        #            (player.y - self.y) / (math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)+.01))
        #(self.x, self.y) = (self.x + dx * self.speed, self.y + dy * self.speed)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, lightblue, self.rect)








