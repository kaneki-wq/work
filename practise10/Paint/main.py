import pygame
from settings import *
from tools import ToolManager
from ui import Button, ColorPalette

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

tool_manager = ToolManager()

buttons = [
    Button(10, 10, 80, 30, "Brush", TOOL_BRUSH),
    Button(100, 10, 80, 30, "Rect", TOOL_RECT),
    Button(190, 10, 80, 30, "Circle", TOOL_CIRCLE),
    Button(280, 10, 80, 30, "Eraser", TOOL_ERASER),
]

palette = ColorPalette()

screen.fill(WHITE)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # кнопки
            for btn in buttons:
                if btn.is_clicked(pos):
                    tool_manager.set_tool(btn.tool)

            # палитра
            color = palette.get_color(pos)
            if color:
                tool_manager.set_color(color)

        tool_manager.handle_event(event, screen)

    # UI поверх
    for btn in buttons:
        btn.draw(screen, font, tool_manager.current_tool == btn.tool)

    palette.draw(screen)

    pygame.display.flip()

pygame.quit()