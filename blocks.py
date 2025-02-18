import pygame

class Block:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.offset = pygame.math.Vector2()

    def draw(self, player):
        self.offset.x = -(player.rect.x - pygame.display.get_surface().get_width() // 2)
        self.offset.y = -(player.rect.y - pygame.display.get_surface().get_height() // 2)

        offset_pos = self.rect.topleft + self.offset
        pygame.display.get_surface().blit(pygame.display.get_surface(), offset_pos)

