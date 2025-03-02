import pygame

from player import Player
from blocks import Block
from input import Input
from camera import Camera

class Game:
    # Main class to manage game assets and behaviour

    def __init__(self):
        # Initializes the game and creates game resources
        pygame.init()

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720

        self.screen_bg_color = 'white'

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('')

        self.screen_rect = self.screen.get_rect()

        self.player = Player()

        self.renderables = [Block(140, 10, 1000, 50, 'black'), Block(140, 760, 1000, 50, 'black'), Block(140, 60, 50, 700, 'black'), Block(1090, 60, 50, 700, 'black')]

        self.input = Input()

        self.camera = Camera()
    

    def gather_renderables(self):
        # Gathers renderables into the camera's inventory
        self.camera.merge(self.player)

        for renderable in self.renderables:
            self.camera.merge(renderable)

    
    def run_game(self):
        # Starts the main loop for the game
        while True:
            # Gathers renderables into the camera's inventory
            self.gather_renderables()
            
            # Watches for events
            self.input.check_events(self.player)

            # Redraws the screen during each pass through the loop
            self.update_screen()
        

    def update_screen(self):
        # Updates images on the screen and flips to the new screen
        
        pygame.draw.rect(self.screen, self.screen_bg_color, self.screen_rect)
        self.camera.get_offset(self.player)
        self.camera.render()
        self.player.update()
    
        # Makes the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Makes a game instance and runs the game
    game = Game()
    game.run_game()