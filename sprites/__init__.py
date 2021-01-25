import pygame

from os import listdir
from os.path import dirname, abspath, join

from datetime import date
from random import *
import requests
import os

while True:
    # Gets today's date
    date = date.today()
    # Splits the date at every "-" because date format is "DD-MM-YYYY"
    split_date = str(date).split("-")
    # Gets a random number from 2015 to the current year for the Year variable
    Year = randint(2015, int(split_date[0]))
    # Checks if the random Year is equal to the current year
    if str(Year) == split_date[0]:
        # Creates a Month variable using a random number from January(1) to the current month
        Month = randint(1, int(split_date[1]))
    else:
        # Creates a Month variable using a random number from January(1) to December(12)
        Month = randint(1, 12)
    # Checks if the random Month is equal to the current month
    if str(Month) == split_date[1]:
        # Creates a Day variable using a random number from 1 to the current day in the month
        Day = randint(1, int(split_date[2]))
    else:
        # Creates a Day variable using a random number from 1 to 30
        Day = randint(1, 28)

    req = requests.get(f"https://api.nasa.gov/planetary/apod?api_key=Guv4egEEeC4kQxHBTEu4DDH26HGW4cWLNCYo2Npd&date={Year}-{Month}-{Day}")
    # Prints the media type of the image and the url of the image
    print(req.json()['media_type'], req.json()['url'])
    # Checks if the file is an image and not a video
    if req.json()['media_type'] == 'image':
        # Gets the url of the image
        apod_url = req.json()['url']
        # Breaks out of the forever loop
        break

# Sets the name variable to "apod1"
name = "apod1"

if not os.path.isfile(f"{name}.jpg"):
    open(os.path.join(f'{name}.jpg'), 'xb')

f = open(os.path.join(f"{name}.jpg"), "wb")

# Checks if the file "apod1.jpg" doesn't exist


f.write(requests.get(apod_url).content)

HERE = dirname(abspath(__file__))


def load_sprites():
    """Load the image sprites from this folder, for easy access."""
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
            print(file_full_path)
            sprites[name_wo_png] = pygame.image.load(file_full_path)

    return sprites


sprites = load_sprites()

