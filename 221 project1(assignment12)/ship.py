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
        self.rect.midbottom = self.screen_rect.midbottom

        #float for x axis
        self.x = float(self.rect.x)

        #movement flag, starts not moving
        self.moving_right = False
        self.moving_left = False


    def update(self):
        '''updates position based on move flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect obj from self.x
        self.rect.x = self.x

    def blitme(self):
        '''draw ship at current location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''center ship in screen'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)