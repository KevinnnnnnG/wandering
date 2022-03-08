from wandering import Comunwandering
from turtle import title
from track import Track
from location import Location
from bokeh.plotting import figure, output_file, show

def walking (location, wandering, steps):
    begining = location.get_location(wandering)
    
    for _ in range (steps):
        location.move_wandering(wandering)
    return begining.distancia(location.get_location(wandering))

    for _ in range (steps):
        location.move_wandering(wandering)
    
    return begining.distancia(location.get_location(wandering))

    def simulate_walk (steps, number_attempt, type_warning ):
        wandering = type_warning (name='Kevin')
        origen = Track(0,0)
        distancia = []
        
        for _ in range (number_attempt):
            location = Location()
            location.add_wandering(wandering, origen)
            simulation_walk = walking (location, wandering, steps)
            distancia.append(round(simulation_walk, 1))
        return distancia
    
    def graph(x,y):
        graphics = figure(title='Camino errante', x_axis_label='paos', y_axis_label='Distancia')
        graphics.line(x,y, legend='Distancia')
        show(graphics)
        
    def main(distancia_walk, number_attempt, type_warning):
        aerrage_walk_distancia = []
        
        for steps in distancia_walk:
            distancia = simulation_walk(steps, number_attempt, type_warning)
            middle_distancia = round(sum(distancia) / len(distancia), 4)
            max_distancia = nax(distancia)
            min_distancia = min(distancia)
            aerrage_walk_distancia.append(middle_distancia)
            print(f'{type_warning._name_} Caminata aletoria de {steps} pasos')
            print (f'Media = {middle_distancia}')
            print(f'Max = {max_distancia}')
            print (f'Min = {min_distancia}')
        graph(distancia_walk, aerrage_walk_distancia)
    
    if _name_ == '_nain_':
        distancia_walk = [10, 100, 1000, 10000]
        number_attempt =100
        main(distancia_walk, number_attempt, Comunwandering)
    

