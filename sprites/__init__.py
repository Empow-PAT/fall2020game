import pygame

from os import listdir
from os.path import dirname, abspath, join

# This is the directory shared by this file.
HERE = dirname(abspath(__file__))


def load_sprites():
    """Load the image sprites from this folder, for easy access."""

    # Go through all the files, and add certain ones to `sprites`.
    sprites = {}
    for file_name in listdir(HERE):

        # If the file does not look like "sprite_*.png", move on.
        if file_name.startswith('sprite_') and file_name.endswith('.png'):

            # Get name of the image: "sprite_<name_wo_sprite>.png"
            name_wo_sprite = file_name[len('sprite_'):]
            name_wo_png = name_wo_sprite.split('.')[0]

            # Load the image, add it to the dictionary.
            file_full_path = join(HERE, file_name)
            sprites[name_wo_png] = pygame.image.load(file_full_path)

    return sprites


sprites = load_sprites()

