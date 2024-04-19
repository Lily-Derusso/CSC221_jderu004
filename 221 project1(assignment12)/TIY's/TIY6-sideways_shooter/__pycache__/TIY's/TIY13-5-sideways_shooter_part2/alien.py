import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''little alien'''

    def __init__(self, ai_game):
        '''init alien set start'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()
        #alien top right
        self.rect.x = ai_game.settings.screen_width - self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        '''move alien up and down'''
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y

    def check_edges(self):
        '''return true if aliens hit edge of screen'''
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)
    