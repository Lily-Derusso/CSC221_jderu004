import sys
import pygame
from random import randint
#from pygame.sprite import Sprite
from rain import Rain
from time import sleep

class Raindrop:

    def __init__(self):
        '''init raindrop class'''
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("TIY12-4")

        self.game_active = True
        self.bg_color = (230,230,230)
        self.rain =pygame.sprite.Group()
        self._create_rain()

    def run_game(self):
        '''Has the rain fall forever'''
        while True:
            self._check_events()
            if self.game_active:
                self._update_rain()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        '''updates next screen'''
        self.screen.fill(self.bg_color)
        self.rain.draw(self.screen)
        pygame.display.flip()

    def _check_events(self):
        '''checks keydown and quit events'''
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit
            if event.type == pygame.KEYDOWN:
                self.end(event)

    def end(self,event):
            '''keydown quit event'''
            if event.key == pygame.K_q:
                sys.exit()

    def _create_rain(self):
        '''makes field of rain at the start of the program'''
        rain = Rain(self)
        rain_width, rain_height =rain.rect.size
        current_x, current_y = rain_width, rain_height
        while current_y < (self.screen_height - 1.5 * rain_height):
            while current_x < (self.screen_width - 2 * rain_width):
                self._create_raindrop(current_x, current_y)
                current_x += 1.5 * rain_width
            current_x = rain_width
            current_y += 2 * rain_height

    def _create_raindrop(self, x_position, y_position):
        '''makes a single raindrop'''
        new_rain = Rain(self)
        new_rain.x = x_position
        new_rain.y = y_position
        new_rain.rect.x = x_position
        new_rain.rect.y = y_position
        self.rain.add(new_rain)
    
    def _update_rain(self):
        '''checks if raindrop leaves the screen, if yes removes it and makes a new one 
        at the same x position at the top of page'''
        new_rain = Rain(self)
        self.rain.update()
        for drop in self.rain.copy():
            if drop.rect.top >= self.screen_height:
                new_drop_x = drop.x
                self.rain.remove(drop)
                self._create_raindrop(new_drop_x, new_rain.y )

if __name__ == '__main__':
    rain = Raindrop()
    rain.run_game()