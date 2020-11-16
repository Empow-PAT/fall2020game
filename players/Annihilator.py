import pygame
import random
import time


white = (255, 255, 255)
black = (0,0,0)
yellow = (255, 255, 0)
red = (255,0,0)
green =  (0,255,0)
lightblue=(0,188,255)
gold = (255,215,0)
sheildColor = (51,255,255)
multiplayer = True
purple = (127,0,225)

font_name = pygame.font.match_font('arial')


def draw_text_sat(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, (x,y))

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
        self.dirx = 1
        self.diry = 1
        self.nickName = "Nickname"
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self,keys,win):
        if keys[pygame.K_a]:
            self.velx = -self.speed
            self.dirx = -1
        elif keys[pygame.K_d]:
            self.velx = self.speed
            self.dirx=1
        else:
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
            self.diry = -1
        elif keys[pygame.K_s]:
            self.vely = self.speed
            self.diry = 1
        else:
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

        self.x += self.velx
        self.y += self.vely

        if keys[pygame.K_SPACE]:
            projectile = Projectile_Annihal(self)
            projectiles.append(projectile)

        draw_text_sat(win, self.nickName, 24 ,self.x-len(self.nickName)*3, self.y-32)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, lightblue, self.rect)

projectiles = []

class Projectile_Annihal:
    def __init__(self,annihilator):
        self.x = annihilator.x
        self.y = annihilator.y
        self.height = 10.0
        self.width = 10.0
        # friction, slope, upwards velocity, x velocity
        self.velMultiply = 1.5

        self.velx = annihilator.speed*self.velMultiply*annihilator.dirx
        self.vely = annihilator.speed*self.velMultiply*annihilator.diry
        self.friction = 0.4
        #if self.velx == 0 and self.vely == 0:
            #self.velx = annihilator.dirx*annihilator.speed
    def tick(self,win,windowwidth,windowheight):
        self.x += self.velx
        self.y += self.vely

        if self.x < 0 or self.y < 0 or self.x > windowwidth or self.y > windowheight:
            projectiles.remove(self)


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(win, red, self.rect)

class Ultimate:
    def __init__ (self):
        self.x = Annihilator.x
        self.y = Annihilator.y
        self.diameter = 30
        self.time
        self.rect = pygame.Rect(self.x, self.y, self.diameter, self.diameter)
    def tick(self,win):
        self.diameter += 2
        self.time += 1
        self.rect = pygame.Rect(self.x, self.y, self.diameter, self.diameter)
        pygame.draw.ellipse(win, purple, self.rect)
