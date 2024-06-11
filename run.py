import numpy as np
from random import random

import matplotlib.pyplot as plt
from matplotlib.figure import SubFigure
from matplotlib.widgets import Button
from matplotlib.axes import Axes


from world import World
from render import Render
from Creatures.creature import Creature
from Creatures.erbast import Erbast

from planisuss_constants import NUMDAYS

def deleteDeads(array: list[Creature]):
    for i in range(len(array)-1,0,-1):
        if array[i].dead:
            array.pop(i)           

def update():
    world.growVegetob()    
    
    deleteDeads(world.erbasts); deleteDeads(world.carvizes)
    
    for erbast in world.erbasts:
        movement=erbast.pickMovement(world.vegetob)
        if np.array_equal(movement, np.zeros(2)):
            erbast.eat(world.vegetob)
        else:
            erbast.movement(movement)
            
        if erbast.energy>20 and random()>0.5:
            erbast.reproduce()            
            
        erbast.older()
        
    for carviz in world.carvizes:
        if not carviz.target:
            carviz.pickTarget(world.erbasts)
        if carviz.energy<carviz.speed*2:
            carviz.hunt()
        elif max(abs(carviz.target.position-carviz.position))>carviz.energy*2/3:
            carviz.stalk()
        else:
            carviz.nap() #dummy method (pass)
            
        carviz.older()      

    

if __name__ == "__main__":
    world = World()
    render = Render()
    popHistory: np.ndarray=np.array([[len(world.erbasts)],[len(world.carvizes)]])

    day=0
    while day<NUMDAYS:
        if not render.paused:
            update()
            popHistory=np.append(popHistory, [[len(world.erbasts)],[len(world.carvizes)]], axis=1)
            render.updateVis("day "+str(day), world, popHistory)
            day+=1
        else:
            render.updateVis("paused", world, popHistory)
        
        if  not plt.get_fignums():
            exit()
        plt.pause(0.1)
    plt.pause(500)
        
