import pygame

class Camera:
    # Main class to manage the camera

    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()

        # Screen settings
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        
        # Inventory of renderables to be rendered onto the screen
        self.renders = []


    def get_offset(self, player):
        # Computes the offset for the player's position
        self.offset.x = -(player.x - self.screen_width / 2)
        self.offset.y = -(player.y - self.screen_height / 2)


    def merge(self, renderable):
        # Merges renderables into the renders list
        self.renders.append(renderable)


    def render(self):
        # Renders renderables onto the screen
        for renderable in self.renders:
            if hasattr(renderable, 'image') and hasattr(renderable, 'rect'):
                self.screen.blit(renderable.image, renderable.rect.move(self.offset))
            elif hasattr(renderable, 'rect'):
                pygame.draw.rect(self.screen, renderable.color, renderable.rect.move(self.offset))

        # Clears the renders list
        self.renders.clear()