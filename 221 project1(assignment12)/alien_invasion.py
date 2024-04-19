import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
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
            (self.settings.screen_width, self.settings.screen_height))
        #fullscreen code
        '''
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        
        #create an instance to store game stats
        self.stats = GameStats(self)
        #start game in active state
        self.game_active = True

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            # Watch for keyboard and mouse events.
            if self.game_active:    
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
        if event.key == pygame.K_RIGHT:
            #move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''respons to keyup'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #check for bullets that hit
        #if o get rid of them
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        '''respondsto bullets hitting aliens'''
        #removes bullet and alien that collided
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if not self.aliens:
            #destroy existing bullets and respawn fleet
            self.bullets.empty()
            self._create_fleet()


    
    def _create_fleet(self):
        '''makes fleet of aliens'''
        #make an alien and keep adding aliens till there is no room left
        #spacing between is 1 alien width and 1 alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
                #self.aliens.add(alien)

            #finished a row, reset x and increment y
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        '''makes an alien and puts in the fleet'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        '''updates the positions of the aliens, checks if at edge'''
        self._check_fleet_edges()
        self.aliens.update()
        #look for alien_ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #check if aiens hit bottom
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        '''responds if an alien reaches the edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''drops fleet andchanges direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        '''respond to ship being hit by alien'''
        if self.stats.ships_left > 0:
            #loose 1 life
            self.stats.ships_left -= 1
            #get rid of remaining bullets and ships
            self.bullets.empty()
            self.aliens.empty()
            #new fleet + recenter ship again
            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        '''checks if any alien reaches the bottom'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #treat same as ship hit
                self._ship_hit()
                break

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
