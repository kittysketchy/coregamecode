import pygame

class Player:
    # A class to manage the player

    def __init__(self):
        # Initializes the player
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()

        # Loads the ship image and gets its rect
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        # Starts the player at the center of the screen
        self.rect.center = self.screen_rect.center

        # Stores a float value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_left = False
        self.moving_right = False
        self_moving_up = False
        self.moving_down = False

    
    def update(self):
        # Updates the player's position based on the movement flags
        # Updates the player's x value, not the rect's
        if self.moving_left and self.rect.left > 0:
            self.x -= 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1 

        # Updates the rect object's x value from player's
        self.rect.x = self.x

        # Updates the player's y value, not the rect's
        if self.moving_up and self.rect.top > 0:
            self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        # Updates the rect object's y value from player's
        self.rect.y = self.y


    def draw_player(self):
        # Draws the player at its current location
        self.screen.blit(self.image, self.rect)

