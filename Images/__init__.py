import pygame

from os import listdir
from os.path import dirname, abspath, join


HERE = dirname(abspath(__file__))


def load_sprites():
    """Load the image sprites from this folder, for easy access."""
    sprites = {}
    for file_name in listdir(HERE):
        if file_name.startswith('') and file_name.endswith('.png'):
            file_full_path = join(HERE, file_name)
            sprites[file_full_path] = pygame.image.load(file_full_path)

    return sprites


sprites = load_sprites()
print(sprites)


