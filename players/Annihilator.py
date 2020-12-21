"""This is a python file which has every object that the annihilator ship class will generally use"""
import pygame
import random
import time
from fall2020game.players import sus
from fall2020game.Images import sprites

white = (255, 255, 255)
black = (0,0,0)
annihilatorimg = sprites["Annihilator.png"]
annihilatorimg = pygame.transform.scale(annihilatorimg, (42,42))
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

class Annihilator:
    def __init__(self, nickname):
        self.x = 0
        self.y = 0
        self.height = 38.0
        self.width = 38.0
        #friction, slope, upwards velocity, x velocity
        self.speed = 12
        self.velx = 0
        self.vely = 0
        self.hp = 1000
        self.friction = 0.4
        self.dir = "right"
        self.nickName = nickname
        self.ultTimer = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self,keys,win):
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
                ult = Ultimate(self)
                ults.append(ult)
                self.ultTimer = 200

        self.x += self.velx
        self.y += self.vely

        if keys[pygame.K_SPACE]:
            projectile = Projectile_Annihal(self)
            projectiles.append(projectile)
        if self.ultTimer > 0:
            self.ultTimer -= 1
        self.gui = self.nickName + "'s Hp: " + str(self.hp)
        draw_text_sat(win, self.gui, 18, self.x - len(self.gui) * 3, self.y - 32)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.dir == "right":
            annihiRotate = pygame.transform.rotate(annihilatorimg, 270)
        if self.dir == "left":
            annihiRotate = pygame.transform.rotate(annihilatorimg, 90)
        if self.dir == "up":
            annihiRotate = pygame.transform.rotate(annihilatorimg, 0)
        if self.dir == "down":
            annihiRotate = pygame.transform.rotate(annihilatorimg, 180)
        win.blit(annihiRotate, self.rect)

projectiles = []
ults = []
bot = sus.Bot()
class Projectile_Annihal:
    def __init__(self,annihilator):
        self.x = annihilator.x + 18
        self.y = annihilator.y + 17
        self.height = 10.0
        self.width = 10.0
        # friction, slope, upwards velocity, x velocity
        self.velMultiply = 1.5

        self.velx = annihilator.speed*self.velMultiply*annihilator.dirx
        self.vely = annihilator.speed*self.velMultiply*annihilator.diry
        if annihilator.dir == "right":
            self.velx = annihilator.speed * self.velMultiply
            self.vely=0
        if annihilator.dir == "left":
            self.velx = annihilator.speed * self.velMultiply*-1
            self.vely = 0
        if annihilator.dir == "up":
            self.velx = 0
            self.vely = annihilator.speed * self.velMultiply*-1
        if annihilator.dir == "down":
            self.velx = 0
            self.vely = annihilator.speed * self.velMultiply

        self.friction = 0.4
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def tick(self,win,windowwidth,windowheight,bot):
        self.x += self.velx
        self.y += self.vely

        if self.rect.colliderect(bot.rect):
            bot.hp -= 10
        if self.x < 0 or self.y < 0 or self.x > windowwidth or self.y > windowheight or self.rect.colliderect(bot.rect):
            projectiles.remove(self)


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(win, red, self.rect)

class Ultimate:
    def __init__ (self,annihilator):
        self.x = annihilator.x
        self.y = annihilator.y
        self.diameter = 30
        self.time = 0
        self.surface = pygame.Surface((windowwidth, windowheight),pygame.SRCALPHA)
        self.rect = pygame.Rect(self.x, self.y, self.diameter, self.diameter)
        self.alpha = 255
    def tick(self,win):
        self.diameter += 4
        self.x -= 2
        self.y -= 2
        self.time += 2
        if self.alpha > 15:
            self.alpha -= 4.5

        self.surface.fill((0,0,0,0))
        self.rect = pygame.Rect(self.x, self.y, self.diameter, self.diameter)
        if self.rect.colliderect(bot.rect):
            pass
        if (self.x + (self.diameter/2) < bot.x) or (self.x - (self.diameter/2) > bot.x) or (self.y + self.diameter/2 < bot.y) or (self.y - (self.diameter/2) > bot.y):
            bot.hp -= 1
        pygame.draw.ellipse(self.surface, (127,0,225,self.alpha), self.rect, 15)
        win.blit(self.surface, (0,0))