import sys, pygame

class Input:
    # Main class to manage player input

    def check_events(self, player):
        # Responds to keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event, player)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event, player)

    
    def check_keydown_events(self, event, player):
        # Responds to keypresses
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            player.moving_left = True
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            player.moving_right = True
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            player.moving_up = True
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            player.moving_down = True
        

    def check_keyup_events(self, event, player):
        # Responds to key releases
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            player.moving_left = False
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            player.moving_right = False
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            player.moving_up = False
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            player.moving_down = False