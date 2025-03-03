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

        # Stores float values for the ship's horizontal and vertical positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_left = self.moving_right = self.moving_up = self.moving_down = False

    
    def update(self):
        # Updates the player's position based on the movement flags
        # Updates the player's x value, not the rect's x value
        if self.moving_left and self.rect.left > 0:
            self.x -= 2
        if self.moving_right and self.rect.right < parameters.screen_rect.right:
            self.x += 2 

        # Updates the rect object's x value from player's x value
        self.rect.x = self.x

        # Updates the player's y value, not the rect's y value
        if self.moving_up and self.rect.top > 0:
            self.y -= 2
        if self.moving_down and self.rect.bottom < parameters.screen_rect.bottom:
            self.y += 2

        # Updates the rect object's y value from player's y value
        self.rect.y = self.y