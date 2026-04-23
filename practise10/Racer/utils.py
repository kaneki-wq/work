import pygame
import os

def load_image(relative_path, size=None):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, relative_path)

    image = pygame.image.load(full_path).convert_alpha()

    if size:
        image = pygame.transform.scale(image, size)

    return image


def load_sound(relative_path):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, relative_path)

    return pygame.mixer.Sound(full_path)