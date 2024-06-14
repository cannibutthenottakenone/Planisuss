import numpy as np
from random import random

import matplotlib.pyplot as plt

from world import World
from render import Render
from Creatures.creature import Creature
from Creatures.erbast import Erbast
from Creatures.carviz import Carviz

from planisuss_constants import NUMDAYS, NUMERBAST, NUMCARVIZ

def deleteDeads(array: list[Creature]):
    for i in range(len(array)-1,0,-1):
        if array[i].dead:
            array.pop(i)           

def update():
    world.growVegetob()    
    
    deleteDeads(Erbast.population); deleteDeads(Carviz.population)
    
    for erbast in Erbast.population: #could be moved in the erbast class
        movement=erbast.pickMovement(world.vegetob)
        if np.array_equal(movement, np.zeros(2)):
            erbast.eat(world.vegetob)
        else:
            erbast.movement(movement)
            
        if erbast.energy>20 and random()>0.5:
            erbast.reproduce()            
            
        erbast.older()
        
    for carviz in Carviz.population: #could be moved in the carviz class
        if not carviz.target:
            carviz.pickTarget(Erbast.population)
        if carviz.energy<carviz.speed*2:
            carviz.hunt(world.geography)
        elif max(abs(carviz.target.position-carviz.position))>carviz.energy*2/3:
            carviz.stalk(world.geography)
        else:
            carviz.nap()
            
        carviz.older()      

    

if __name__ == "__main__":
    world = World()
    render = Render()
    Erbast.populateCreature(Erbast, world, NUMERBAST)
    Carviz.populateCreature(Carviz, world, NUMCARVIZ)
    popHistory: np.ndarray=np.array([[len(Erbast.population)],[len(Carviz.population)]])
    # energyAverage=[np.array([x.energy for x in Carviz.population]).mean()]

    day=0
    while day<NUMDAYS:
        if not render.paused:
            update()
            popHistory=np.append(popHistory, [[len(Erbast.population)],[len(Carviz.population)]], axis=1)
            # energyAverage.append(np.array([x.energy for x in Carviz.population]).mean())
            render.updateVis("day "+str(day), world, popHistory)
            print("day ",day)
            day+=1
        else:
            render.updateVis("paused", world, popHistory)
            
        if  not plt.get_fignums():
            exit()
        plt.pause(0.1)
    plt.pause(500)
        
