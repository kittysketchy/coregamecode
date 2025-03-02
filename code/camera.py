import pygame

class Camera:
    # Main class to manage the camera

    def __init__(self, settings):
        self.settings = settings

        self.offset = pygame.math.Vector2()

        # Inventory of renderables to be rendered onto the screen
        self.renders = []


    def get_offset(self, player):
        # Computes the offset for the player's position
        self.offset.x = -(player.x - self.settings.screen_width / 2)
        self.offset.y = -(player.y - self.settings.screen_height / 2)


    def merge(self, renderable):
        # Merges renderables into the renders list
        self.renders.append(renderable)


    def render(self):
        # Renders renderables onto the screen
        for renderable in self.renders:
            if hasattr(renderable, 'image') and hasattr(renderable, 'rect'):
                self.settings.screen.blit(renderable.image, renderable.rect.move(self.offset))
            elif hasattr(renderable, 'rect'):
                pygame.draw.rect(self.settings.screen, renderable.color, renderable.rect.move(self.offset))

        # Clears the renders list
        self.renders.clear()