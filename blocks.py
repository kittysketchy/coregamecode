import pygame

class Block:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, offset):
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect.move(offset))