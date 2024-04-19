import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        #screen code
        '''
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_hight))
        #fullscreen code
        '''
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            # Watch for keyboard and mouse events.
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            #print(len(self.bullets))
            #redraw screen
            self._update_screen()
            self.clock.tick(60)  

    def _update_screen(self):
        '''updates and flips screen'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_events(self):
        '''keypress and mouse movements'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() #return
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''responds to keydowns'''
        if event.key == pygame.K_DOWN:
            #move ship down
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''respons to keyup'''
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _fire_bullet(self):
        '''creates new bullet and adds it to bullet group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''updates position and removes old bullets'''
        #update bullet positions
        self.bullets.update()

        #get rid of bullets that disappear
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        '''responds to bullet alien collisions'''
        #removes B/A that collide
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        '''makes alien fleet'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = 3*alien_width, alien_height
        while current_y < (self.settings.screen_height - 2*alien_height):
            while current_x < (self.settings.screen_width - alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width
            current_x = 3*alien_width
            current_y += 2*alien_height

    def _create_alien(self, x_position, y_position):
        '''create alien, place in row'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        '''update positions'''
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        '''responds if aliens hit edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''drop fleet,reverse direction'''
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()