import sys, pygame

from player import Player
from blocks import Block
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

        self.renderables = [
            Block(140, 10, 1000, 50, 'black'),
            Block(140, 760, 1000, 50, 'black'),
            Block(140, 60, 50, 700, 'black'),
            Block(1090, 60, 50, 700, 'black')
        ]

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
            self.check_events()

            # Redraws the screen during each pass through the loop
            self.update_screen()

    
    def check_events(self):
        # Responds to keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    
    def check_keydown_events(self, event):
        # Responds to keypresses
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.player.moving_down = True
        

    def check_keyup_events(self, event):
        # Responds to key releases
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.player.moving_down = False
        

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