from re import X
from typing import final
from unicodedata import name
from wandering import Comunwandering
from wandering import Rightwandering
from wandering import Leftwandering
from turtle import title
from track import Track
from location import Location
from bokeh.plotting import figure, output_file, show

def know_type_wandering(type_warning):
    if type_warning.__name__ == "Comunwandering":
        return "Herrante comun"
    elif type_warning.__name__ == "Rightwandering":
        return "Herrante derechista "
    else:
        return "Herrante izquierdista"

def walking (wandering, steps, type_warning):
    begining = [wandering.posicion()]
    
    x_graph = [0]
    y_graph = [0]
    
    for _ in range (steps-1):
        wandering.walk()
        x, y = wandering.posicion()
        x_graph.append(x)
        y_graph.append(y)
        
    know_type = know_type_wandering(type_warning)
    graph_steps(x_graph, y_graph, know_type, steps)
    return wandering.distance_origin()



def simulate_walk (steps, number_attempt, type_warning ):
    
    wandering = []
    distancia = []
    
    for i in range (number_attempt):
        wandering.append(type_warning(name=f'Kike {i}'))
        simulation_walk = walking (wandering[i], steps, type_warning)
        distancia.append(round(simulation_walk, 1))
        
    return distancia

def graph_steps(x_graph, y_graph, type_warning, steps):
    
    graphics = figure(title=type_warning, x_axis_label='pasos', y_axis_label='Distancia')
    graphics.line(x_graph, y_graph, legend_label=str(steps)+'pasos')
    final_x = x_graph [-1]
    final_y = y_graph [-1]
    
    graphics.diamond_cross(0, 0, fill_color="green", line_color="green", size=18)
    graphics.diamond_cross(final_x, final_y, fill_color="red", line_color="green", size=18 )
    straight_final_x = [0, final_x]
    straight_final_y = [0, final_y]
    
    graphics.line(straight_final_x, straight_final_y, line_width=2, color="red")
    show(graphics)

    
def main(distancia_walk, number_attempt, type_warning):

    for steps in distancia_walk:
        distancia = simulate_walk(steps, number_attempt, type_warning)
        middle_distancia = round(sum(distancia) / len(distancia), 4)
        max_distancia = max(distancia)
        min_distancia = min(distancia)
        
        print(f'{type_warning.__name__} Caminata aletoria de {steps} pasos')
        print (f'Media = {middle_distancia}')
        print(f'Max = {max_distancia}')
        print (f'Min = {min_distancia}')

    
if __name__ == '__main__':
    
    distancia_walk = [10000]
    number_attempt =1
    main(distancia_walk, number_attempt, Comunwandering)
