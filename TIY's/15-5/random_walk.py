from random import choice

class RandomWalk:
    '''a class to gen random walks'''

    def __init__(self, num_points=5000):
        '''init atts for walk'''
        self.num_points = num_points
        #all walks start at origen
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''calc all the points on walk'''
        #walk till the desired length is reached
        while len(self.x_values) < self.num_points:
            #decide direction and distance
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            #calc new postion
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    
    def get_step(self):
        '''generates direction and distance randomly. Then returns step'''
        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step


