import pygame

class Ball:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Начальные координаты (центр экрана)
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = 25
        self.step = 20  # Шаг перемещения
        self.color = (255, 0, 0)  # Красный цвет (RGB)

    def move(self, direction):
        # direction — это кортеж (dx, dy), например (0, -20) для движения вверх
        new_x = self.x + direction[0]
        new_y = self.y + direction[1]

        # Проверка границ: шар не должен выходить за края экрана
        if (new_x - self.radius >= 0 and new_x + self.radius <= self.screen_width and
            new_y - self.radius >= 0 and new_y + self.radius <= self.screen_height):
            self.x = new_x
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)