import pygame

from os import listdir
from os.path import dirname, abspath, join

from datetime import date
from random import *
import requests
import os

date = date.today()
split_date = str(date).split("-")
Year = randint(2015, int(split_date[0]))
if str(Year) == split_date[0]:
    Month = randint(1, int(split_date[1]))
else:
    Month = randint(1, 12)
if str(Month) == split_date[1]:
    Day = randint(1, int(split_date[2]))
else:
    Day = randint(1, 30)


apodddds = "https://api.nasa.gov/planetary/apod?api_key=Guv4egEEeC4kQxHBTEu4DDH26HGW4cWLNCYo2Npd&date="+str(Year)+"-"+str(Month)+"-"+str(Day)+""
req1 = requests.get(apodddds)
apod1 = req1.json()
variable = apod1
name = "apod1"

if not os.path.exists(name+".jpg"):
    with open(os.path.join("sprites/",name+".jpg"), "wb") as f:
        # try:
        f.write(requests.get(variable["url"]).content)

HERE = dirname(abspath(__file__))

def load_sprites():
    sprites = {}
    for file_name in listdir(HERE):
        if file_name.startswith('sprite_') and file_name.endswith('.png'):
            name_wo_sprite = file_name[len('sprite_'):]
            name_wo_png = name_wo_sprite.split('.')[0]
            file_full_path = join(HERE, file_name)
            sprites[name_wo_png] = pygame.image.load(file_full_path)
        if file_name == name + (".jpg"):
            name_wo_png = file_name.split('.')[0]
            file_full_path = join(HERE, file_name)
            sprites[name_wo_png] = pygame.image.load(file_full_path)
    return sprites

sprites = load_sprites()

