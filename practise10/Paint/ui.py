import pygame
from settings import *

class Button:
    def __init__(self, x, y, w, h, text, tool):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.tool = tool

    def draw(self, screen, font, active=False):
        color = (150, 150, 250) if active else GRAY
        pygame.draw.rect(screen, color, self.rect)
        label = font.render(self.text, True, BLACK)
        screen.blit(label, (self.rect.x + 5, self.rect.y + 5))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class ColorPalette:
    def __init__(self):
        self.rects = []
        for i, color in enumerate(COLORS):
            self.rects.append((pygame.Rect(10 + i * 40, 50, 30, 30), color))

    def draw(self, screen):
        for rect, color in self.rects:
            pygame.draw.rect(screen, color, rect)

    def get_color(self, pos):
        for rect, color in self.rects:
            if rect.collidepoint(pos):
                return color
        return None