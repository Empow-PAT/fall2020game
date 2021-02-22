__all__ = ["Bot", "draw_text_sat", "Enemy_proj", "enemyProjs"]

import pygame
from fall2020game.players import Annihilator
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
        self.hp = 500
        self.nickName = "Nickname"
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 6
        self.timer = 0


    def tick(self, win, player):
        draw_text_sat(win, str(self.hp), 18 ,self.x-3, self.y-32)
        win.blit(bot, self.rect)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        #Jittery movement
        #self.vely = player.vely + random.randint(-10, 10)
        #self.velx = player.velx + random.randint(-10, 10)

        #Works but is a little weird when on top of player
        if self.x > player.x:
            self.velx = -player.speed+3
        else:
            self.velx = player.speed-3

        if self.y < player.y:
            self.vely = player.speed - 3
        else:
            self.vely = -player.speed + 3

        self.y += self.vely
        self.x += self.velx
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.timer >= 5:
            projectilEn = Enemy_proj(player,self)
            enemyProjs.append(projectilEn)
            self.timer=0

        self.timer += 1

# class Projectile_Bot:
#         def __init__(self, Bot):
#             self.x = Bot.x + 18
#             self.y = Bot.y + 17
#             self.height = 10.0
#             self.width = 10.0
#             # friction, slope, upwards velocity, x velocity
#             self.velMultiply = 1.5
#
#             self.velx = Bot.speed * self.velMultiply * Bot.dirx
#             self.vely = Bot.speed * self.velMultiply * Bot.diry
#             if Bot.dir == "right":
#                 self.velx = Bot.speed * self.velMultiply
#                 self.vely = 0
#             if Bot.dir == "left":
#                 self.velx = Bot.speed * self.velMultiply * -1
#                 self.vely = 0
#             if Bot.dir == "up":
#                 self.velx = 0
#                 self.vely = Bot.speed * self.velMultiply * -1
#             if Bot.dir == "down":
#                 self.velx = 0
#                 self.vely = Bot.speed * self.velMultiply
#
#             self.friction = 0.4
#             self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
#
#         def tick(self, win, windowwidth, windowheight, bot):
#             self.x += self.velx
#             self.y += self.vely
#
#             if self.x < 0 or self.y < 0 or self.x > windowwidth or self.y > windowheight:
#                 projectiles.remove(self)
#             if self.rect.colliderect(bot.rect):
#                 bot.hp -= 10
#                 projectiles.remove(self)
enemyProjs = []

class Enemy_proj:
    def __init__(self,annihilator, bot):
        self.x = bot.x + 16.5
        self.y = bot.y + 17
        self.height = 10.0
        self.width = 10.0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # friction, slope, upwards velocity, x velocity
        self.velMultiply = 1.5


        if self.x > annihilator.x:
            self.velx = -9
        else:
            self.velx = 9

        if self.y < annihilator.y:
            self.vely = 9
        else:
            self.vely = -9


        if abs(self.x-annihilator.x) > abs(self.y-annihilator.y):
            if self.x - annihilator.x>0:
                self.velx=-9
                self.vely=0
            else:
                self.velx = 9
                self.vely = 0
        else:
            if self.y - annihilator.y>0:
                self.vely=-9
                self.velx=0
            else:
                self.vely = 9
                self.velx = 0

    def tick(self, win, annihilator):
        if self.rect.colliderect(annihilator.rect) and annihilator.hp > 0:
            annihilator.hp -= 10
            enemyProjs.remove(self)
        self.y += self.vely
        self.x += self.velx
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(win, lightblue, self.rect)




