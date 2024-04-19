import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represent a single alien in the fleet'''

    def __init__(self, ai_game):
        '''init the alien in starting position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load alien and make a rectangle
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        #start alien in the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store position as a float
        self.x = float(self.rect.x)

    def check_edges(self):
        '''return true if alien is at the edge of the screen'''
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= screen_rect.left)
        
    def update(self):
        '''moves aliens to the right or left'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x