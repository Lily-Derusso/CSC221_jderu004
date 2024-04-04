class Settings:
    '''A class to store all game settings'''
    
    def __init__(self):
        '''game settings'''
        #screen settings
        self.screen_width = 1000
        self.screen_hight = 600
        self.bg_color = (230,230,230)
        
        #ship settings
        self.ship_speed = 1.5