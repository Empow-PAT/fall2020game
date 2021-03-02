import time
import pygame
import random
import requests
from os import listdir
from os.path import dirname, abspath, join
from fall2020game import sprites

black = (0,0,0)

pygame.init()
windowwidth = 500
windowheight = 500
HERE = dirname(abspath(__file__))
file_path = join(HERE, "sprites/astro.png")
sprite2 = pygame.image.load(file_path)

class Astro:
    def __init__(self):
        self.win = pygame.display.set_mode((windowwidth, windowheight))
        self.speed = 0.05
        self.health = 10
        self.x = random.randint(50,350)
        self.y = random.randint(50,350)
        self.yd = random.randint(-10,10)
        self.xd = random.randint(-10,10)
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.transform.scale(sprite2, (self.width, self.height))
    def tick(self):
        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.height)
        pygame.display.set_caption("ninja battle")
        self.win.blit(self.img, (self.x, self.y))
        if self.x >windowwidth - self.width:
            self.x = windowwidth - self.width
            self.xd = random.randint(-10,0)
        if self.x < 0:
            self.x = 0
            self.xd = random.randint(0,10)
        if self.y >windowheight - self.height:
            self.y = windowheight - self.height
            self.yd = random.randint(-10, 0)
        if self.y < 0:
            self.y = 0
            self.yd = random.randint(0,10)
        for a in alive:
            if a.rect.colliderect(self.rect) and a.rect != self.rect:
                alive.remove(self)

win = pygame.display.set_mode((windowwidth,windowheight))
astro = Astro()
astro2 = Astro()
astro3 = Astro()
astro4 = Astro()
astro5 = Astro()
astro6 = Astro()
astro7 = Astro()
astro8 = Astro()
astro9 = Astro()
astro10 = Astro()
astro11 = Astro()
astro12 = Astro()
astro13 = Astro()
run = True
alive = [astro, astro2, astro3, astro4, astro5, astro6, astro7, astro8, astro9, astro10, astro11, astro12, astro13]


while run:
    win.fill(black)
    time.sleep(0.01)
    for astro in alive:
        astro.tick()

    pygame.display.update()













