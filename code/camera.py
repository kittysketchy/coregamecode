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
        if hasattr(renderable, 'image') and hasattr(renderable, 'rect'):
            self.renders.append((renderable.image, renderable.rect))
        elif hasattr(renderable, 'rect'):
            self.renders.append(renderable.rect)


    def render(self):
        # Renders renderables onto the screen
        for renderable in self.renders:
            if isinstance(renderable, tuple):
                image, rect = renderable
                self.screen.blit(image, rect.move(self.offset))
            elif isinstance(renderable, pygame.Rect):
                pygame.draw.rect(self.screen, 'black', renderable.move(self.offset))

        # Clears the renders list
        self.renders.clear()