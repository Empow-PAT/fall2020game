"""
This is a python file which has every object that the annihilator ship class
will generally use
"""

__all__ = ["Annihilator", "Projectile_Annihal", "ults", "projectiles"]

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
darkblue = (0,0,139)
font_name = pygame.font.match_font('arial')


def draw_text_sat(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, (x,y))


class Annihilator:
    def __init__(self, nickname):
        self.Proj_Timer = 0
        self.x = windowwidth/2
        self.y = windowheight/2
        self.height = 38.0
        self.width = 38.0
        #friction, slope, upwards velocity, x velocity
        self.speed = 3
        self.velx = 0
        self.vely = 0
        self.max_hp = 1000
        self.hp = 1000
        self.damage = 20
        self.friction = 0.4
        self.dir = "right"
        self.nickName = nickname
        self.ultTimer = 0
        self.ModTimer = 0
        self.ModActTimer=81
        self.DashTimer=0
        self.DashActTimer=11
        self.DashCol = 255
        self.DashRadi = 10
        self.DashRect = pygame.Rect(self.x-self.DashRadi/3+6, self.y-self.DashRadi/3+6, self.DashRadi, self.DashRadi)
        self.Dashx = 0
        self.Dashy = 0
        self.ModAnimSize = 76
        self.modRect = pygame.Rect(self.x-self.ModAnimSize/3+6, self.y-self.ModAnimSize/3+6, self.ModAnimSize, self.ModAnimSize)
        self.ModGoDown = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self,keys,win,sheild, keymode):
        if self.x > 800 - self.width:
            self.x = 800 - self.width
            self.velx = 0

        if self.x < 0:
            self.x = 0
        if self.y > windowheight - self.height:
            self.y = windowheight - self.height
            self.vely = 0
        if self.y < 0:
            self.y = 0
        self.Proj_Timer += 1
        self.DashRect = pygame.Rect(self.Dashx, self.Dashy, self.DashRadi, self.DashRadi)
        self.modRect = pygame.Rect(self.x-self.ModAnimSize/3+6, self.y-self.ModAnimSize/3+6, self.ModAnimSize, self.ModAnimSize)
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
        #Ultimate
        if keys[pygame.K_q]:
            if self.ultTimer == 0:
                ult = Ultimate(self)
                ults.append(ult)
                self.ultTimer = 320
        #Active Module Activation
        if keys[pygame.K_e]:
            if self.ModTimer < 1:
                self.ModActTimer = 0
                self.ModTimer = 800
        # Active Module Healing
        if self.ModActTimer < 81:
            self.ModActTimer += 1
            pygame.draw.ellipse(win, green, self.modRect, 5)
            if self.hp<1000:
                self.hp += 7
        #Active Module cooldown going down
        if self.ModTimer>0:
            self.ModTimer-=1



        # Dash Activation
        if keys[pygame.K_x]:
            if self.DashTimer < 1:
                self.DashActTimer = 0
                self.DashTimer = 120
                self.Dashx = self.x - self.DashRadi / 7.5 + 15
                self.Dashy = self.y - self.DashRadi / 7.5 + 15
        # Dash Boosting
        if self.DashActTimer < 11:
            self.DashActTimer += 1
            self.DashCol-=5
            self.DashRadi+=15
            pygame.draw.ellipse(win, (self.DashCol,self.DashCol,self.DashCol), self.DashRect,10)
            self.speed = 15
        else:
            self.speed=3
            self.DashCol=255
            self.DashRadi=10
        # Dash cooldown going down
        if self.DashTimer > 0:
            self.DashTimer -= 1


        self.x += self.velx
        self.y += self.vely

        if keys[pygame.K_SPACE] and keymode == 0:
            if self.Proj_Timer >= 3:
                projectile = Projectile_Annihal(self)
                projectiles.append(projectile)
                self.Proj_Timer = 0

        if keys[pygame.K_UP] and keymode == 1:
            self.dir = ("up")
            if self.Proj_Timer >= 5:
                projectile = Projectile_Annihal(self)
                projectiles.append(projectile)
                self.Proj_Timer = 0

        elif keys[pygame.K_RIGHT] and keymode == 1:
            self.dir = ("right")
            if self.Proj_Timer >= 5:
                projectile = Projectile_Annihal(self)
                projectiles.append(projectile)
                self.Proj_Timer = 0

        elif keys[pygame.K_LEFT] and keymode == 1:
            self.dir = ("left")
            if self.Proj_Timer >= 5:
                projectile = Projectile_Annihal(self)
                projectiles.append(projectile)
                self.Proj_Timer = 0

        elif keys[pygame.K_DOWN] and keymode == 1:
            self.dir = ("down")
            if self.Proj_Timer >= 5:
                projectile = Projectile_Annihal(self)
                projectiles.append(projectile)
                self.Proj_Timer = 0
        if self.ultTimer > 0:
            self.ultTimer -= 1


        if self.ModAnimSize < 76:
            self.ModGoDown = False
        elif self.ModAnimSize > 152:
            self.ModGoDown = True

        if self.ModGoDown == False:
            self.ModAnimSize+=5
        else:
            self.ModAnimSize-=5



        #Drawing HP

        self.gui = "Ultimate Cooldown: " + str(int(self.ultTimer/35)) + "secs"
        self.gui2 = "Active Module Cooldown: " + str(int(self.ModTimer/35)) + "secs"
        self.gui3 = "Dash Cooldown: " + str(int(self.DashTimer / 35)) + "secs"

        #Drawing Health Bar
        pygame.draw.rect(win, red, (self.x-25, self.y-20, 100, 15))
        pygame.draw.rect(win, green, (self.x - 25, self.y - 20, self.hp/10, 15))
        #Drawing Sheild Bar
        if sheild.hp > 0:
            pygame.draw.rect(win, white, (self.x - 25, self.y - 40, 100, 10))
            pygame.draw.rect(win, sheildColor, (self.x - 25, self.y - 40, sheild.hp, 10))
        #Drawing Cooldown Timers
        draw_text_sat(win, self.gui, 14, 700-(len(self.gui)*5), 25, white)
        draw_text_sat(win, self.gui2, 14, 700-(len(self.gui2)*5), 50, white)
        draw_text_sat(win, self.gui3, 14, 700 - (len(self.gui3) * 5), 75, white)


        draw_text_sat(win, self.nickName, size=20, x=self.x + 12, y=self.y - 22, color=darkblue)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.dir == "right":
            annihiRotate = pygame.transform.rotate(annihilatorimg, 270)
        if self.dir == "left":
            annihiRotate = pygame.transform.rotate(annihilatorimg, 90)
        if self.dir == "up":
            annihiRotate = pygame.transform.rotate(annihilatorimg, 0)
        if self.dir == "down":
            annihiRotate = pygame.transform.rotate(annihilatorimg, 180)
        self.modRect = pygame.Rect(self.x-self.ModAnimSize/3+6, self.y-self.ModAnimSize/3+6, self.ModAnimSize, self.ModAnimSize)
        self.DashRect = pygame.Rect(self.Dashx, self.Dashy, self.DashRadi, self.DashRadi)
        win.blit(annihiRotate, self.rect)

projectiles = []
Heal_Projectile = []
ults = []
bot = sus.Bot()
class Projectile_Annihal:
    def __init__(self,annihilator):
        self.x = annihilator.x + 16.5
        self.y = annihilator.y + 17
        self.height = 10.0
        self.width = 10.0
        self.velMultiply = 1.5
        self.damage = annihilator.damage

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


    def tick(self,win,windowwidth,windowheight,BotPlay, sheild):
        self.x += self.velx
        self.y += self.vely
        for b in BotPlay:
            if self.rect.colliderect(b.rect):
                b.hp -= self.damage
            if self.x < 0 or self.y < 0 or self.x > windowwidth or self.y > windowheight or self.rect.colliderect(b.rect):
                projectiles.remove(self)
                break

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(win, red, self.rect)

class Ultimate:
    def __init__ (self,annihilator):
        self.x = annihilator.x + 16
        self.y = annihilator.y + 16
        self.diameter = 30
        self.radius = 15
        self.time = 0
        self.surface = pygame.Surface((windowwidth, windowheight),pygame.SRCALPHA)
        self.rect = pygame.Rect(self.x, self.y, self.diameter, self.diameter)
        self.alpha = 255
    def tick(self,win,bot):
        self.diameter += 8
        self.radius = self.diameter / 2
        self.time += 2
        if self.alpha > 15:
            self.alpha -= 3.75

        self.surface.fill((0,0,0,0))
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.diameter, self.diameter)
        if (self.x + (self.diameter/2) < bot.x) or (self.x - (self.diameter/2) > bot.x) or (self.y + self.diameter/2 < bot.y) or (self.y - (self.diameter/2) > bot.y):
            bot.hp -= 50
        pygame.draw.ellipse(self.surface, (127,0,225,self.alpha), self.rect, 15)
        win.blit(self.surface, (0,0))

class Sheild:
    def __init__(self,annihilator):
        self.diam = 72
        self.x = annihilator.x - ((annihilator.width/2)*self.diam/72)
        self.y = annihilator.y - ((annihilator.height/2)*self.diam/72)
        self.nonHitTime=0
        self.rect = pygame.Rect(self.x, self.y, self.diam, self.diam)
        self.hp = 100
    def tick(self,win,annihilator):
        self.x = annihilator.x - (annihilator.width / 2)
        self.y = annihilator.y - (annihilator.height / 2)
        self.rect = pygame.Rect(self.x, self.y, self.diam, self.diam)
        pygame.draw.ellipse(win, sheildColor, self.rect, int(annihilator.ModAnimSize/18))
        self.nonHitTime+=1
        if self.nonHitTime > 160 and self.hp<100:
            self.hp+=1

class UserAssist:
    def __init__(self):
        self.UserAssist1 = "Use Q for Ultimate"
        self.UserAssist2 = "Use E for Active Module"
        self.UserAssist3 = "Use X for Dash"
        self.UserAssist4 = "WASD to move"
        self.UserAssist5 = "Rodger, Fire at will"
        self.Timer = 0
    def tick(self,win):
        if self.Timer > 0 and self.Timer < 200:
            draw_text_sat(win, self.UserAssist1, 14, windowwidth/2-50, windowheight - 18, white)
        if self.Timer > 20 and self.Timer < 200:
            draw_text_sat(win, self.UserAssist2, 14, windowwidth/2-50, windowheight - 36, white)
        if self.Timer > 40 and self.Timer < 200:
            draw_text_sat(win, self.UserAssist3, 14, windowwidth/2-50, windowheight - 54, white)
        if self.Timer > 60 and self.Timer < 200:
            draw_text_sat(win, self.UserAssist4, 14, windowwidth/2-50, windowheight - 72, white)
        if self.Timer > 80 and self.Timer < 200:
            draw_text_sat(win, self.UserAssist5, 14, windowwidth/2-50, windowheight - 90, white)
        self.Timer += 1


class HelperBot:
    def __init__(self,annihilator, HelperBotimage):
        self.y = annihilator.y
        self.x = annihilator.x
        self.HealerTimer = 0
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load(HelperBotimage)
        self.image= pygame.transform.scale(self.image,(self.width,self.height))
    def tick(self,win, annihilator):
        self.HealerTimer += 1
        self.y = annihilator.y + 70
        self.x = annihilator.x
        win.blit(self.image, (self.x,self.y))
        if self.HealerTimer >= 20:
            self.HealerTimer = 0
            Heal_Projectile.append(Projectile_Heal(self))
class Projectile_Heal:
    def __init__(self, HelperBot):
        self.x = HelperBot.x
        self.y = HelperBot.y
        self.width = 15
        self.height = 15
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self, win, annihilator):
        self.y -= 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(win, green, self.rect,2)
        if self.rect.colliderect(annihilator.rect):
            Heal_Projectile.remove(self)
            if annihilator.hp >= annihilator.max_hp:
                annihilator.hp = 1000
            else:
                annihilator.hp += 30



