#The effects will be randomly generated
#What effect you will get will be randomized between power up and debuff
#What the specific power up/debuff will be randomly generated

import random
import pygame
from fall2020game.sprites import sprites

PowerUp_or_Debuff = sprites["Power-up or Debuff Item"]
PowerUp_or_Debuff = pygame.transform.scale(PowerUp_or_Debuff, (42, 42))

__all__ = ["power", "Effect"]

def power(player,bot):
    #Buff
    Affect = random.randint(1,3)
    if Affect == 1 or Affect == 3:
        powerup = random.randint(1,15)
        if powerup == 1 or powerup == 2 or powerup == 3 or powerup == 4 or powerup == 5:
            #Health buff
            print("Maximum health increase")
            player.max_hp += 100
        if powerup == 6 or powerup == 7 or powerup == 8 or powerup == 9:
            #Regeneration power-up(only for a few seconds to a minute)
            repair = random.randint(1,60)
            repair_timer = repair * 40
            print("repairing")
            while repair_timer > 0 and player.hp <= player.max_hp - 0.025 and player.hp != 0:
                player.hp += 0.025
                repair_timer -= 1
        if powerup == 10 or powerup == 11 or powerup == 12:
            #Speed buff
            print("Speed increased")
            player.speed += 0.5
        if powerup == 13 or powerup == 14:
            #Invisibility power-up(only for a few seconds to a minute)
            cloak = random.randint(1,60)
            cloak_timer = cloak * 40
            player.temp_max_hp = player.hp
            print("cloaked")
            while cloak_timer > 0:
                if player.hp < player.temp_max_hp:
                    player.hp = player.temp_max_hp
                cloak_timer -= 1
        if powerup == 15:
            #Damage buff
            print("Damage increase")
            player.damage += 2

    #Debuff
    if Affect == 2:
        debuff = random.randint(1,15)
        if debuff == 1 or debuff == 2 or debuff == 3 or debuff == 4 or debuff == 5:
            #Bot Max Health Debuff
            bot.max_hp += 100
            print("Bot maximum health increase")
        elif debuff == 6 or debuff == 7 or debuff == 8 or debuff == 9:
            #bot regeneration debuff(only a few seconds to a minute)
            bot_repair = random.randint(1,60)
            bot_timer = bot_repair * 40
            while bot_timer > 0 and bot.hp <= bot.max_hp - 0.025 and bot.hp != 0:
                bot.hp += 0.025
                bot_timer -= 1
            print("Bot repairing")
        elif debuff == 10 or debuff == 11 or debuff == 12:
            #Bot Speed Debuff
            bot.speed += 1
            print("Bot speed increase")
        elif debuff == 13 or debuff == 14:
            #bot invisibility debuff(only a few seconds to a minute)
            bot_cloak = random.randint(1,60)
            bot_cloak_timer = bot_cloak * 40
            bot.temp_max_hp = bot.hp
            print("bot cloaked")
            while bot_cloak_timer > 0:
                if bot.hp < bot.temp_max_hp:
                    bot.hp = bot.temp_max_hp
                bot_cloak_timer -= 1
        elif debuff == 15:
            #Bot Streangth Debuff
            bot.damage += 2
            print("Bot damage increase")


class Effect:
    def __init__(self,windowwidth,windowheight):
        self.rect = PowerUp_or_Debuff.get_rect()
        self.x = random.randint(0, windowwidth)
        self.y = random.randint(0, windowheight)
        self.rect.center = self.x,self.y
        self.counter = 0

    def tick(self,win,windowwidth,windowheight):
        if self.counter == 0:
            self.x = random.randint(0, windowwidth)
            self.y = random.randint(0, windowheight)
        self.rect.center = self.x, self.y
        if self.counter >= 400:
            win.blit(PowerUp_or_Debuff, self.rect)
        self.counter += 1