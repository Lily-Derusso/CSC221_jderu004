import pygame

class Ship:
    '''class to manage the player ship'''

    def __init__(self, ai_game):
        '''init ship and sets start position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #loading image
        self.image = pygame.image.load('images/tiy3.png')
        self.rect = self.image.get_rect()

        #start ship at center bottom
        self.rect.center = self.screen_rect.center

        #float for x axis
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movement flag, starts not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        '''updates position based on move flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.y += self.settings.ship_speed        
        #update rect obj from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        '''draw ship at current location'''
        self.screen.blit(self.image, self.rect)