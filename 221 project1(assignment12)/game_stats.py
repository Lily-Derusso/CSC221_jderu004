
class GameStats:
    '''tracks stats for game'''

    def __init__(self, ai_game):
        '''init stats'''
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        '''init stats that change over game'''
        self.ships_left = self.settings.ship_limit