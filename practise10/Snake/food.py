import random
import pygame
from settings import WIDTH, HEIGHT, CELL, RED


class Food:

    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):

        while True:

            x = random.randint(
                0,
                (WIDTH - CELL) // CELL
            ) * CELL

            y = random.randint(
                0,
                (HEIGHT - CELL) // CELL
            ) * CELL

            if (x, y) not in snake_body:
                return (x, y)

    def draw(self, screen):

        center = (
            self.position[0] + CELL // 2,
            self.position[1] + CELL // 2
        )

        # Круглая еда
        pygame.draw.circle(
            screen,
            RED,
            center,
            CELL // 2
        )

        # Блик
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (center[0] - 4, center[1] - 4),
            3
        )
