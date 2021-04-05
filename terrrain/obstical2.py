import time
import pygame
import random
from os.path import dirname, abspath, join

HERE = dirname(abspath(__file__))
file_path = join(HERE, "../sprites/astro.png")
sprite2 = pygame.image.load(file_path)

class Astro:
    def __init__(self):
        self.speed = 0.05
        self.health = 10
        self.x = random.randint(50,50)
        self.y = random.randint(25,1000)
        self.yd = random.randint(-10,10)
        self.xd = random.randint(-10,10)
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.transform.scale(sprite2, (self.width, self.height))
    def tick(self, astro_alive, win):
        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.height)
        win.blit(self.img, (self.x, self.y))
        if self.x >800 - self.width:
            self.x = random.randint(50,50)
            self.y = random.randint(25, 1000)
            self.xd = random.randint(-10,10)
            while self.xd == 0:
                self.xd = random.randint(-10, 10)
        if self.x < 0:
            self.x = random.randint(50,50)
            self.y = random.randint(25, 1000)
            self.xd = random.randint(-10, 10)
            while self.xd == 0:
                self.xd = random.randint(-10, 10)
        if self.y >800 - self.height:
            self.y = random.randint(25, 1000)
            self.x = random.randint(50, 50)
            self.yd = random.randint(-10, 10)
            while self.yd == 0:
                self.yd = random.randint(-10, 10)

        if self.y < 0:
            self.y = random.randint(25,1000)
            self.x = random.randint(50,50)
            self.yd = random.randint(-10, 10)
            while self.yd == 0:
                self.yd = random.randint(-10, 10)
        for a in astro_alive:
            if a.rect.colliderect(self.rect) and a.rect != self.rect:
                astro_alive.remove(self)
        self.x += self.xd
        self.y += self.yd