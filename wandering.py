import random

class Wandering:
    def __init__(self,name):
        self.name = name
        
class Comunwandering(Wandering):
    def __init__(self,name):
        super().__init__(name)
        
    def walk(self):
        return random.choice([(0,4), (0,-4),(4,0),(-4,0)])
    
 