import numpy as np
import matplotlib.pyplot as plt
from World.world import World

def show(world: World):
    worldVisual=np.ndarray((world.dimensions[1], world.dimensions[0], 3))
    
    for i in range(worldVisual.shape[1]):
        for j in range(worldVisual.shape[0]):
            if world.getCell(j, i).cellType=="water":
                worldVisual[i,j,:]=[0,0,255]
            else:
                worldVisual[i,j,:]=[255,0,0]   

    return worldVisual