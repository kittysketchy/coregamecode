import pygame

class Camera:
    # A class to manage the camera

    def __init__(self, screen_objects):
        self.offset = pygame.math.Vector2()
        self.screen_objects = screen_objects

    def show_screen(self, player):
        self.offset.x = player.rect.centerx - pygame.display.get_surface().get_width() // 2
        self.offset.y = player.rect.centery - pygame.display.get_surface().get_height() // 2

        for screen_object in self.screen_objects:
            offset_pos = screen_object.rect.topleft - self.offset
            if hasattr(screen_object, 'color'):
                pygame.draw.rect(pygame.display.get_surface(), screen_object.color, offset_pos)
            else:
                player.draw_player()