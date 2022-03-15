import random

class Wandering:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
    
    def posicion(self):
        return  (self.x, self.y)
    
    def distance_origin(self):
        return (self.x**2 + self.y**2)**0.5
        
class Comunwandering(Wandering):
    def __init__(self,name):
        super().__init__(name)
        
    def walk(self):
        dx, dy = random.choice([(0,4), (0,-4),(4,0),(-4,0)])
        self.x += dx
        self.y += dy
        return [dx, dy]

class Rightwandering(Wandering):
    
    def __init__(self,name):
        super().__init__(name)
    
    def walk(self):
        dx, dy = random.choice([(0,2), (1,-3),(5,0),(-1,3)])
        self.x += dx
        self.y += dy
        return [dx, dy]
    

class Leftwandering(Wandering):
    
    def __init__(self,name):
        super().__init__(name)
    
    def walk(self):
        dx, dy = random.choice([(3,2), (2,3), (5,1), (1,3)])
        self.x += dx
        self.y += dy
        return [dx, dy]
        
    
    