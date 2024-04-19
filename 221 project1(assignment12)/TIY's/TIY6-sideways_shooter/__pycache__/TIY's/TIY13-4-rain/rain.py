import pygame
from pygame.sprite import Sprite

class Rain(Sprite):

    def __init__(self,ai_game):
        '''init rain class. loads image, sets x and y and makes floats of the value'''
        super().__init__()
        self.screen = ai_game.screen
            
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        '''raindrops decend at 1.5 pix a tick'''
        self.y += 1.5
        self.rect.y = self.y
        self.rect.x = self.x