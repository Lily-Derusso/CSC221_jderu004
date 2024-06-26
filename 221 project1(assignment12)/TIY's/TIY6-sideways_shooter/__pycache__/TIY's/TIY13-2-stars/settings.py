class Settings:
    '''A class to store all game settings'''
    
    def __init__(self):
        '''game settings'''
        #screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2

        #bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 0
        self.fleet_drop_speed = 0
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1