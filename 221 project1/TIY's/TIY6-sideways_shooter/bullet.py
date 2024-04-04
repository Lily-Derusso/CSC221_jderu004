import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''manages bullets fired from ship'''

    def __init__(self,ai_game):
        '''creates bullet object at ship position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet rect at (0, 0) then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                        self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        #stores bullet position as a float
        self.x = float(self.rect.x)

    def update(self):
            '''move bullet up the screen'''
            #update the position of the bullet
            self.x += self.settings.bullet_speed
            #update rect position
            self.rect.x = self.x

    def draw_bullet(self):
            '''draws bullet to screen'''
            pygame.draw.rect(self.screen, self.color, self.rect)