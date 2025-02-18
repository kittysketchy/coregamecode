import sys, pygame

from player import Player
from blocks import Block

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
        pygame.display.set_caption("")

        self.screen_rect = self.screen.get_rect()

        self.player = Player()

        self.blocks = [Block(100, 100, 50, 500, 'red'), Block(1150, 100, 50, 500, 'blue'), Block(250, 600, 800, 50, 'green')]

        self.offset = pygame.math.Vector2()

    
    def run_game(self):
        # Starts the main loop for the game
        while True:
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
        self.compute_offset()
        self.update_entities()
    
        # Makes the most recently drawn screen visible
        pygame.display.flip()


    def compute_offset(self):
        # Computes the offset for the player's position
        self.offset.x = -(self.player.x - self.screen_width / 2)
        self.offset.y = -(self.player.y - self.screen_height / 2)


    def update_entities(self):
        # Updates the entities on the screen
        self.player.draw_player(self.offset)
        self.player.update()

        for block in self.blocks:
            block.draw(self.offset)

if __name__ == '__main__':
    # Makes a game instance and runs the game
    game = Game()
    game.run_game()