import pygame, parameters

import utils.utils

class Player:
    # Main class to manage the player

    def __init__(self, renderables):
        # Loads the ship image and gets its rect
        self.images = utils.utils.import_folder('assets', 'idle')
        self.image = self.images[0]
        self.rect = self.image.get_rect().inflate(-20, -5)
        self.previous_rect = self.rect.copy()

        self.image_index = 0

        self.image.set_colorkey('#E6E6E6')

        # Starts the player at the center of the screen
        self.rect.center = parameters.screen_rect.center

        # Movement flags
        self.moving_left = self.moving_right = False
        self.moving_up = self.moving_down = False

        self.renderables = renderables

        self.frame_timer = 0
        self.frame_duration = 150

        self.facing_right = True

        self.gravity = 1

        self.jump_images = utils.utils.import_folder('assets', 'jump')

    
    def move(self, dt):
        # Updates the player's position based on the movement flags
        self.move_x(dt)
        self.check_collision(True)
        self.move_y(dt)
        self.check_collision(False)


    def animate(self, dt):
        self.frame_timer += dt

        if self.frame_timer >= self.frame_duration:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.frame_timer = 0.0

        self.image = self.images[self.image_index] if self.facing_right else pygame.transform.flip(self.images[self.image_index], True, False)
        

    def move_x(self, dt):
        # Responsible for handling movement on the horizontal axis
        if self.moving_left:
            self.facing_right = False
             
            if self.rect.left > 0:
                self.rect.x -= 1 * dt
        if self.moving_right:
            self.facing_right = True

            if self.rect.right < parameters.screen_rect.right:
                self.rect.x += 1 * dt

    
    def move_y(self, dt):
        # Responsible for handling movement on the vertical axis
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 2 * dt
        if self.moving_down and self.rect.bottom < parameters.screen_rect.bottom:
            self.rect.y += 1 * dt

        self.rect.y += self.gravity * dt


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


    def upgrade(self, dt):
        self.animate(dt)
        self.previous_rect = self.rect.copy()
        self.move(dt)