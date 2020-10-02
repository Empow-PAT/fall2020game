import pygame

from os import listdir
from os.path import dirname, abspath, join

HERE = dirname(abspath(__file__))

def load_sprites():
    sprites = {}
    for file_name in listdir(HERE):
        if file_name.startswith('sprite_') and file_name.endswith('.png'):
            name_wo_sprite = file_name[len('sprite_'):]
            name_wo_png = name_wo_sprite.split('.')[0]
            file_full_path = join(HERE, file_name)
            sprites[name_wo_png] = pygame.image.load(file_full_path) 
    return sprites

sprites = load_sprites()

