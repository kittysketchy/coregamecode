import pygame, parameters

class Camera:
    # Main class to manage the camera

    def __init__(self):
        self.offset = pygame.math.Vector2()

        # Inventory of renderables to be rendered onto the screen
        self.renderables = []


    def grasp_offset(self, player):
        # Grasps the offset for the player's position
        x = parameters.screen_width // 2 - player.rect.x
        y = parameters.screen_height // 2 - player.rect.y

        self.offset.x += (x - self.offset.x) * 0.1
        self.offset.y += (y - self.offset.y) * 0.1


    def merge(self, renderable):
        # Merges renderables into the renderables list
        if renderable not in self.renderables:
            self.renderables.append(renderable)


    def render(self):
        # Renders renderables onto the screen
        for renderable in self.renderables:
            if hasattr(renderable, 'image') and hasattr(renderable, 'rect'):
                parameters.screen.blit(renderable.image, renderable.rect.move(self.offset))
            elif hasattr(renderable, 'rect'):
                pygame.draw.rect(parameters.screen, renderable.color, renderable.rect.move(self.offset))