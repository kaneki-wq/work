import pygame
import random
from settings import *
from utils import load_image

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = load_image("assets/images/enemy.png", (50, 80))

        x = random.randint(ROAD_LEFT + 30, ROAD_RIGHT - 30)
        self.rect = self.image.get_rect(center=(x, -100))

    def move(self, speed):
        self.rect.move_ip(0, speed)

        if self.rect.top > HEIGHT:
            x = random.randint(ROAD_LEFT + 30, ROAD_RIGHT - 30)
            self.rect.center = (x, -100)