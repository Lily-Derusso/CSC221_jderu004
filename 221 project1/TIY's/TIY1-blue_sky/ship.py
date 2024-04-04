import pygame

class Ship:
    '''class to manage the player ship'''

    def __init__(self, ai_game):
        '''init ship and sets start position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loading image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.tiy = pygame.image.load('images/TIY12-2.bmp')
        self.tiy_rect = self.tiy.get_rect()

        #start ship at center bottom
        self.rect.midbottom = self.screen_rect.midbottom
        self.tiy_rect.midtop = self.screen_rect.midtop

    def blitme(self):
        '''draw ship at current location'''
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.tiy, self.tiy_rect)