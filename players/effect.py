#The effects will be randomly generated
#What effect you will get will be randomized between power up and debuff
#What the specific power up/debuff will be randomly generated

import random
import pygame
from fall2020game import run
from fall2020game.players import Annihilator
from fall2020game.players import sus

__all__ = ["power"]

def power(player,keys,effecT):
    #Buff
    if effecT == 1 or effecT == 3:
        powerup = 0
        if powerup == 1 or powerup == 2 or powerup == 3 or powerup == 4 or powerup == 5:
            #Health buff
            player.hp += 100
        if keys[pygame.K_r]:
            #Regeneration power-up(only for a few seconds to a minute)
            repair = random.randint(1,60)
            timer = repair * 40
            while timer > 0:
                player.hp += 4
                print("Healing")
                timer -= 1
        elif powerup == 10 or powerup == 11 or powerup == 12:
            #Speed buff
            player.speed += 1
        elif powerup == 13 or powerup == 14:
            #Invisibility power-up(only for a few seconds to a minute)
            global cloak
            cloak = random.randint(1,60)
        elif powerup == 15:
            #Damage buff
            player.damage += 2
        elif powerup == 16:
            #Call for help
            pass

    #Debuff
    if effecT == 2:
        debuff = random.randint(1,15)
        if debuff == 1 or debuff == 2 or debuff == 3 or debuff == 4 or debuff == 5:
            #Health debuff
            player.hp -= 100
        elif debuff == 6 or debuff == 7 or debuff == 8 or debuff == 9:
            #bot regeneration debuff(only a few seconds to a minute)
            global bot_repair
            bot_repair = random.randint(1,60)
        elif debuff == 10 or debuff == 11 or debuff == 12:
            #Slowness debuff
            player.speed -= 1
        elif debuff == 13 or debuff == 14:
            #bot invisibility debuff(only a few seconds to a minute)
            global bot_cloak
            bot_cloak = random.randint(1,60)
        elif debuff == 15:
            #Weakness debuff
            player.damage -= 2