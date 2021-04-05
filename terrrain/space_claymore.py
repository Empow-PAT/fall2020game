from tkinter import *

class Claymore:
    def __init__(self):
        self.hp = 3

    def attack(self):
        print("You have been hit by a claymore")
        self.hp -= 10

    def checkHp(self):
        if self.life <=0:
            print("Your dead ")
    def tic(self ):
        root = Tk()
        self.x = Claymore.x
        self.y = Claymore.y
        photo=PhotoImage(file="")
        label=label(root,image=photo)
        label.pack()
    root.mainloop()

claymore1 = Claymore()
claymore2 = Claymore()

claymore1.attack()
claymore1.attack()
claymore2.checkHp()
claymore2.checkHp()