import pygame, parameters

from player import Player
from blocks import Block
from input.input import Input
from camera import Camera

class Game:
    # Main class to manage game assets and behaviour

    def __init__(self):
        # Provisions the game and creates game resources
        pygame.init()
        
        pygame.display.set_caption('')

        self.renderables = [
            Block(140, 10, 1000, 50, 'black'),
            Block(140, 760, 1000, 50, 'black'),
            Block(140, 60, 50, 700, 'black'),
            Block(1090, 60, 50, 700, 'black'),  

            Block(300, 200, 200, 30, 'gray'),
            Block(700, 300, 200, 30, 'gray'),
            Block(500, 450, 300, 30, 'gray'),
            Block(250, 600, 150, 30, 'gray'),
            Block(850, 600, 150, 30, 'gray')
        ]

        self.player = Player(self.renderables)

        self.input = Input(self.player)

        self.camera = Camera()

        self.dt = 0
    

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
            self.input.check_events()

            # Redraws the screen during each pass through the loop
            self.update_screen()

            # Clocks the game at 60 FPS
            self.dt = pygame.time.Clock().tick(60)

        
    def update_screen(self):
        # Updates images on the screen and flips to the new screen
        
        pygame.draw.rect(parameters.screen, parameters.screen_bg_color, parameters.screen_rect)
        self.camera.grasp_offset(self.player)
        self.camera.render()
        self.player.upgrade(self.dt)
    
        # Makes the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Makes a game instance and runs the game
    game = Game()
    game.run_game()