from tkinter import *

class Claymore:
    def __init__(self):
        self.hp = 3

    def attack(self):
        print("You have been hit a claymore")
        self.hp -= 10

    def checkHp(self):
        if self.life <=0:
            print("Your dead ")
    root = Tk()
    photo=PhotoImage(file="")
    label=label(root,image=photo)
    label.pack()
    root.mainloop()
