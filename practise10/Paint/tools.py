import pygame
from settings import *

class ToolManager:
    def __init__(self):
        self.current_tool = TOOL_BRUSH
        self.color = BLACK
        self.start_pos = None

    def set_tool(self, tool):
        self.current_tool = tool

    def set_color(self, color):
        self.color = color

    def handle_event(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if self.current_tool == TOOL_RECT:
                pygame.draw.rect(screen, self.color,
                                 (*self.start_pos,
                                  event.pos[0] - self.start_pos[0],
                                  event.pos[1] - self.start_pos[1]), 2)

            elif self.current_tool == TOOL_CIRCLE:
                radius = int(((event.pos[0] - self.start_pos[0]) ** 2 +
                              (event.pos[1] - self.start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, self.color,
                                   self.start_pos, radius, 2)

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                if self.current_tool == TOOL_BRUSH:
                    pygame.draw.circle(screen, self.color, event.pos, 5)

                elif self.current_tool == TOOL_ERASER:
                    pygame.draw.circle(screen, WHITE, event.pos, 10)