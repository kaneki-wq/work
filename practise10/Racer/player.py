import pygame
from settings import *
from utils import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = load_image("assets/images/player.png", (50, 80))
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT - 100))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > ROAD_LEFT:
            self.rect.move_ip(-PLAYER_SPEED, 0)

        if keys[pygame.K_RIGHT] and self.rect.right < ROAD_RIGHT:
            self.rect.move_ip(PLAYER_SPEED, 0)