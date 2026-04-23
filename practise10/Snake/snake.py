import pygame
from settings import CELL, GREEN, DARK_GREEN


class Snake:

    def __init__(self):
        # Начальное тело змейки
        self.body = [(100, 100), (80, 100), (60, 100)]

        # Направление движения
        self.dx = CELL
        self.dy = 0

    def move(self):

        # Новая голова
        head_x = self.body[0][0] + self.dx
        head_y = self.body[0][1] + self.dy

        new_head = (head_x, head_y)

        # Добавляем голову
        self.body.insert(0, new_head)

        # Удаляем хвост
        self.body.pop()

        return new_head

    def grow(self):
        # Увеличение длины
        tail = self.body[-1]
        self.body.append(tail)

    def draw(self, screen):

        # Рисуем змейку
        for i, segment in enumerate(self.body):

            # Голова ярче
            if i == 0:
                color = GREEN
            else:
                color = DARK_GREEN

            pygame.draw.rect(
                screen,
                color,
                (segment[0], segment[1], CELL, CELL)
            )

            # Контур
            pygame.draw.rect(
                screen,
                (0, 60, 0),
                (segment[0], segment[1], CELL, CELL),
                1
            )

    def change_direction(self, key):

        if key == pygame.K_UP and self.dy == 0:
            self.dx = 0
            self.dy = -CELL

        elif key == pygame.K_DOWN and self.dy == 0:
            self.dx = 0
            self.dy = CELL

        elif key == pygame.K_LEFT and self.dx == 0:
            self.dx = -CELL
            self.dy = 0

        elif key == pygame.K_RIGHT and self.dx == 0:
            self.dx = CELL
            self.dy = 0

    def check_self_collision(self):

        return self.body[0] in self.body[1:]
