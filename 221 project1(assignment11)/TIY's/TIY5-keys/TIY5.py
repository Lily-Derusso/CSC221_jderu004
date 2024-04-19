import sys
import pygame

class TIY5:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 800
        self.screen_hight = 400
        
        #screen code    
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_hight))

        pygame.display.set_caption("TIY5-keys")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)  

    def _update_screen(self):
        '''updates and flips screen'''
        self.screen.fill(self.bg_color)
        pygame.display.flip()

    def _check_events(self):
        '''keypress and mouse movements'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() #return
                elif event.type == pygame.KEYDOWN:
                    print(pygame.key.name(event.key))


if __name__ == '__main__':
    # Make a game instance, and run the game.
    tiy = TIY5()
    tiy.run_game()