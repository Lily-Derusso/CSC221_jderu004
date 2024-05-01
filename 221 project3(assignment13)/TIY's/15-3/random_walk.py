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
            x_direction = choice([1,-1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance 
            #reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            #calc new postion
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)