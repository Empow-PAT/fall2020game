"""This is a python file which has every object that the tank ship class will generally use"""

__all__ = ["Tank", "Sheilds", "Projectile_Tank"]

import pygame
import random
import time
from fall2020game.players import sus

white = (255, 255, 255)
black = (0,0,0)
yellow = (255, 255, 0)
red = (255,0,0)
green =  (0,255,0)
lightblue=(0,188,255)
gold = (255,215,0)
sheildColor = (51,255,255)
multiplayer = True
purple = (127,0,225,1)
windowwidth = 1024
windowheight = 768

font_name = pygame.font.match_font('arial')


def draw_text_sat(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, (x,y))


class Tank:
    def __init__(self, nickname):
        self.x = 0
        self.y = 0
        self.height = 25.0
        self.width = 25.0
        #friction, slope, upwards velocity, x velocity
        self.speed = 3
        self.velx = 0
        self.vely = 0
        self.hp = 2000
        self.max_hp = 2000
        self.friction = 0.4
        self.dir = "right"
        self.nickName = nickname
        self.ultTimer = 0
        self.ModTimer = 0
        self.ModActTimer = 81
        self.DashTimer = 0
        self.DashActTimer = 11
        self.ModAnimSize = 76
        self.modRect = pygame.Rect(self.x - self.ModAnimSize / 3 + 7.5, self.y - self.ModAnimSize / 3 + 7.5, self.ModAnimSize, self.ModAnimSize)
        self.ModGoDown = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self,keys,win,sheild):
        self.modRect = pygame.Rect(self.x - self.ModAnimSize / 3 + 7.5, self.y - self.ModAnimSize / 3 + 7.5, self.ModAnimSize, self.ModAnimSize)
        if keys[pygame.K_a]:
            self.velx = -self.speed
            self.dir = "left"
        elif keys[pygame.K_d]:
            self.velx = self.speed
            self.dir = "right"
        else:
            self.dirx=0
            if self.velx > 0:
                if self.velx > self.friction:
                    self.velx -= self.friction
                if self.velx < self.friction:
                    self.velx = 0
            if self.velx < 0:
                if self.velx < -self.friction:
                    self.velx += self.friction
                if self.velx > -self.friction:
                    self.velx = 0

        if keys[pygame.K_w]:
            self.vely = -self.speed
            self.dir = "up"
        elif keys[pygame.K_s]:
            self.vely = self.speed
            self.dir = "down"
        else:
            self.diry=0
            if self.vely > 0:
                if self.vely > self.friction:
                    self.vely -= self.friction
                if self.vely < self.friction:
                    self.vely = 0
            if self.vely < 0:
                if self.vely < -self.friction:
                    self.vely += self.friction
                if self.vely > -self.friction:
                    self.vely = 0

        if keys[pygame.K_q]:
            if self.ultTimer == 0:
                ult = Ultimate_Tank(self)
                ults_Tank.append(ult)
                self.ultTimer = 200
                # Active Module Activation

        self.x += self.velx
        self.y += self.vely

        if keys[pygame.K_SPACE]:
            projectile = Projectile_Tank(self)
            projectiles_tank.append(projectile)
        if self.ultTimer > 0:
            self.ultTimer -= 1

        draw_text_sat(win, self.nickName, 18 ,self.x-len(self.nickName)*3, self.y-32)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, lightblue, self.rect)
        self.gui = "Ultimate Cooldown: " + str(int(self.ultTimer / 35)) + "secs"
        self.gui2 = "Active Module Cooldown: " + str(int(self.ModTimer / 35)) + "secs"
        self.gui3 = "Dash Cooldown: " + str(int(self.DashTimer / 35)) + "secs"
        # Drawing Health Bar
        pygame.draw.rect(win, red, (self.x - 25, self.y - 20, 100, 10))
        pygame.draw.rect(win, green, (self.x - 25, self.y - 20, self.hp / 10, 10))
        # Drawing Sheild Bar
        pygame.draw.rect(win, white, (self.x - 25, self.y - 40, 100, 10))
        pygame.draw.rect(win, sheildColor, (self.x - 25, self.y - 40, sheild.hp, 10))
        # Drawing Cooldown Timers
        draw_text_sat(win, self.gui, 14, 700 - (len(self.gui) * 5), 25)
        draw_text_sat(win, self.gui2, 14, 700 - (len(self.gui2) * 5), 50)
        draw_text_sat(win, self.gui3, 14, 700 - (len(self.gui3) * 5), 75)

projectiles_tank = []
ults_Tank = []
bot = sus.Bot()

class Sheilds:
    def __init__(self):
        self.width = Tank.width+5
        self.height = Tank.height+5
        self.x = Tank.x
        self.y = Tank.y
        self.alph = 0
        self.rect = pygame.Rect(self.x,self.y, self.width, self.height)
        self.surface = pygame.Surface((self.width,self.height))
        self.hp = 5
    def tick(self,win):
        self.x = Tank.x
        self.y = Tank.y
        for projectile in projectiles_tank:
            if self.rect.colliderect(projectile):
                self.alph = 1
                self.hp -= 1
                projectiles_tank.remove(projectile)
        if self.alph < 0:
            self.alph -= 2
        else:
            self.alph = 0

        self.y = Tank.y - 10
        self.rect = pygame.Rect(self.x,self.y, self.width, self.height)
        self.surface.fill((51,255,255,self.alph))
        win.blit(self.surface,(self.x,self.y))

class Projectile_Tank:
    def __init__(self,tank):
        self.x = tank.x + 16.5
        self.y = tank.y + 17
        self.height = 10.0
        self.width = 10.0
        # friction, slope, upwards velocity, x velocity
        self.velMultiply = 2

        self.velx = tank.speed*self.velMultiply*tank.dirx
        self.vely = tank.speed*self.velMultiply*tank.diry
        if tank.dir == "right":
            self.velx = tank.speed * self.velMultiply
            self.vely=0
        if tank.dir == "left":
            self.velx = tank.speed * self.velMultiply*-1
            self.vely = 0
        if tank.dir == "up":
            self.velx = 0
            self.vely = tank.speed * self.velMultiply*-1
        if tank.dir == "down":
            self.velx = 0
            self.vely = tank.speed * self.velMultiply

        self.friction = 0.4
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def tick(self,win,windowwidth,windowheight,BotPlay,sheild):
        self.x += self.velx
        self.y += self.vely

        for b in BotPlay:
            if self.rect.colliderect(b.rect):
                b.hp -= 10
            if self.x < 0 or self.y < 0 or self.x > windowwidth or self.y > windowheight or self.rect.colliderect(
                    b.rect):
                projectiles_tank.remove(self)
                break


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(win, red, self.rect)

#class Ultimate_Tank:
    #def __init__ (self,tank):
        #self.x = tank.x
        #self.y = tank.y
        #self.width
        #self.time = 0
        #self.surface = pygame.Surface((windowwidth, windowheight),pygame.SRCALPHA)
        #self.rect = pygame.Rect(self.x, self.y, self.diameter, self.diameter)
        #self.alpha = 255
        #self.timer = 0
    #def tick(self,win):
        #self.timer+=1
