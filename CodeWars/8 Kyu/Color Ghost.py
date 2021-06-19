import random

class Ghost(object):
    def __init__(self):
        self.colors = ['white', 'yellow', 'red', 'purple']
        self.color = random.choice(self.colors)