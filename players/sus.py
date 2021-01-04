import pygame
from fall2020game.players import Annihilator
import math
import random


white = (255, 255, 255)
black = (0,0,0)
yellow = (255, 255, 0)
red = (255,0,0)
green =  (0,255,0)
lightblue = (0,188,255)
gold = (255,215,0)

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
        self.speed = 10



    def tick(self, win, player):
       # (dx, dy) = ((player.x - self.x) / (math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)+.01),
        #            (player.y - self.y) / (math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)+.01))
        #(self.x, self.y) = (self.x + dx * self.speed, self.y + dy * self.speed)

        self.vely = player.vely + random.randint(-10, 10)

        self.velx = player.velx + random.randint(-10, 10)

        self.y += self.vely
        self.x += self.velx


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, gold, self.rect)

    class Projectile_Bot:
        def __init__(self, Bot):
            self.x = Bot.x + 18
            self.y = Bot.y + 17
            self.height = 10.0
            self.width = 10.0
            # friction, slope, upwards velocity, x velocity
            self.velMultiply = 1.5

            self.velx = Bot.speed * self.velMultiply * Bot.dirx
            self.vely = Bot.speed * self.velMultiply * Bot.diry
            if Bot.dir == "right":
                self.velx = Bot.speed * self.velMultiply
                self.vely = 0
            if Bot.dir == "left":
                self.velx = Bot.speed * self.velMultiply * -1
                self.vely = 0
            if Bot.dir == "up":
                self.velx = 0
                self.vely = Bot.speed * self.velMultiply * -1
            if Bot.dir == "down":
                self.velx = 0
                self.vely = Bot.speed * self.velMultiply

            self.friction = 0.4
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        def tick(self, win, windowwidth, windowheight, bot):
            self.x += self.velx
            self.y += self.vely

            if self.x < 0 or self.y < 0 or self.x > windowwidth or self.y > windowheight:
                projectiles.remove(self)
            if self.rect.colliderect(bot.rect):
                bot.hp -= 10
                projectiles.remove(self)







