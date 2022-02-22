from wandering import Comunwandering

from track import Track
from location import Location
from bokeh.plotting import figure, output_file, show

def walking (location, wandering, steps):
    begining = location.get_location
    
    for _ in range (steps):
        location.move_wandering(wandering)
        
    return begining.distancia(location.get_location(wandering))

