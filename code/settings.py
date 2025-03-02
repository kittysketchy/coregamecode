import pygame

class Settings:
    # Main class to manage the game settings

    def __init__(self):
        # Provisions the game and creates game resources
        pygame.init()

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720

        self.screen_bg_color = 'white'

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('')

        self.screen_rect = self.screen.get_rect()