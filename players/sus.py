import pygame
import random
import math
from fall2020game.Images import sprites

white = (255, 255, 255)
black = (0,0,0)
yellow = (255, 255, 0)
red = (255,0,0)
green =  (0,255,0)
lightblue = (0,188,255)
gold = (255,215,0)
font_name = pygame.font.match_font('arial')
bot = sprites["Enemy Ship.png"]
bot = pygame.transform.scale(bot, (30,30))
def draw_text_sat(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, (x,y))

class Bot:
    def __init__(self):
        self.height = 30.0
        self.width = 30.0
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
        draw_text_sat(win, str(self.hp), 18 ,self.x-3, self.y-32)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(bot, self.rect)

        self.vely = player.vely + random.randint(-10, 10)

        self.velx = player.velx + random.randint(-10, 10)

        self.y += self.vely
        self.x += self.velx







