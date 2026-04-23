import pygame
import random
from settings import *
from utils import load_image

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = load_image("assets/images/coin.png", (30, 30))

        x = random.randint(ROAD_LEFT + 20, ROAD_RIGHT - 20)
        self.rect = self.image.get_rect(center=(x, -50))

    def move(self, speed):
        self.rect.move_ip(0, speed)

        if self.rect.top > HEIGHT:
            self.kill()