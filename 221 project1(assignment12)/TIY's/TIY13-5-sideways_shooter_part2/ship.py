import pygame

class Ship:
    '''class to manage the player ship'''

    def __init__(self, ai_game):
        '''init ship and sets start position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #loading image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start ship at center bottom
        self.rect.midleft = self.screen_rect.midleft

        #float for x axis
        self.y = float(self.rect.y)

        #movement flag, starts not moving
        self.moving_down = False
        self.moving_up = False


    def update(self):
        '''updates position based on move flag'''
        if self.moving_down and self.rect.top < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        #update rect obj from self.x
        self.rect.y = self.y

    def blitme(self):
        '''draw ship at current location'''
        self.screen.blit(self.image, self.rect)