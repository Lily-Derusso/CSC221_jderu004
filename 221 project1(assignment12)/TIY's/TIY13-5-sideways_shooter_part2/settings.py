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

        #bullet settings
        self.bullet_speed = 4.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 13

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #direction 1 = down, -1 = up
        self.fleet_direction = 1