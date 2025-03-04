import pygame, parameters

class Player:
    # Main class to manage the player

    def __init__(self):
        # Loads the ship image and gets its rect
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        self.image.set_colorkey('#E6E6E6')

        # Starts the player at the center of the screen
        self.rect.center = parameters.screen_rect.center

        # Movement flags
        self.moving_left = self.moving_right = False
        self.moving_up = self.moving_down = False

    
    def update(self):
        # Updates the player's position based on the movement flags
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_right and self.rect.right < parameters.screen_rect.right:
            self.rect.x += 1 

        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < parameters.screen_rect.bottom:
            self.rect.y += 1