from tkinter import *
from os.path import dirname, abspath, join

import pygame
#from fall2020game import *
#cly = images["cly"]
import random
HERE = dirname(abspath(__file__))
file_path = join(HERE, "../Images/cly.png")
cly = pygame.image.load(file_path)

class Claymore:
    def __init__(self, windowwith, windowhight):
        self.hp = 3

        self.rect = cly.get_rect()
        self.x = random.randint(0, windowwith)
        self.y = random.randint(0, windowhight)
        self.rect.center = self.x, self.y
    def attack(self):
        print("You have been hit by a claymore")
        self.hp -= 10

    def checkHp(self, Annihilator):
        if Annihilator.hp <=0:
            print("Your dead ")
    def tic(self, win ):
        win.blit(cly, (self.x, self.y))
        #root = Tk()
        #self.x = Claymore.x
        #self.y = Claymore.y
        #photo=PhotoImage(file="")
        #label=label(root,image=photo)
        #label.pack()
        #root.mainloop()

# class Pic:
#     def tic(self):
#         self.rect.center
#
#
# claymore1 = Claymore()
# claymore2 = Claymore()
#
# claymore1.attack()
# claymore1.attack()
# claymore2.checkHp()
#claymore2.checkHp()
