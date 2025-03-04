import pygame, parameters

class Player:
    # Main class to manage the player

    def __init__(self, renderables):
        # Loads the ship image and gets its rect
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.previous_rect = self.rect.copy()

        self.image.set_colorkey('#E6E6E6')

        # Starts the player at the center of the screen
        self.rect.center = parameters.screen_rect.center

        # Movement flags
        self.moving_left = self.moving_right = False
        self.moving_up = self.moving_down = False

        self.renderables = renderables

    
    def move(self):
        # Updates the player's position based on the movement flags
        self.move_x()
        self.check_collision(True)
        self.move_y()
        self.check_collision(False)


    def move_x(self):
        # Responsible for handling movement on the horizontal axis
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_right and self.rect.right < parameters.screen_rect.right:
            self.rect.x += 1

    
    def move_y(self):
        # Responsible for handling movement on the vertical axis
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < parameters.screen_rect.bottom:
            self.rect.y += 1


    def check_collision(self, x):
        for renderable in self.renderables:
            if renderable.rect.colliderect(self.rect):
                if x:
                    if self.rect.right >= renderable.rect.left and self.previous_rect.left <= renderable.previous_rect.right:
                        self.rect.right = renderable.rect.left
                    
                    if self.rect.left <= renderable.rect.right and self.previous_rect.left >= renderable.previous_rect.right:
                        self.rect.left = renderable.rect.right
                else:
                    if self.rect.bottom >= renderable.rect.top and self.previous_rect.bottom <= renderable.previous_rect.top:
                        self.rect.bottom = renderable.rect.top
                    
                    if self.rect.top <= renderable.rect.bottom and self.previous_rect.top >= renderable.previous_rect.bottom:
                        self.rect.top = renderable.rect.bottom


    def upgrade(self):
        self.previous_rect = self.rect.copy()
        self.move()