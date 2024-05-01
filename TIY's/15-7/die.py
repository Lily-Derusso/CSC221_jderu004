from random import randint

class Die:
    '''class representing a single die'''

    def __init__(self, num_sides=6):
        '''assuming a 6 sided die'''
        self.num_sides = num_sides

    def roll(self):
        '''return a random value between 1 and number of sides'''
        return randint(1, self.num_sides)