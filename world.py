import numpy as np
from random import random
from perlin_noise import PerlinNoise

from planisuss_constants import SIZE as n  #size of the side of the square world.
from planisuss_constants import GROWING

def noiseMap(shape:tuple[int,int], scale:int):
    """
    ### noiseMap
    Uses perlin noise to generate a noise map
    
    #### Parameters:
    - shape: the shape of the grid
    - scale: scale to be applied to the perlin noise   
    """
    grid=np.zeros(shape)
    
    noise = PerlinNoise(0.5)   
    for i in range(shape[0]):
        for j in range(shape[1]):
            grid[i][j] = noise([i/scale,j/scale])
            
    return grid
    

def generateIsland(scale:int =25, r:int =25, shape: tuple[int,int] =(n,n) )->np.ndarray:
    """
    ### generateIsland
    Generates an island on a [shape] shaped grid.
    
    #### Parameters:
    - scale: scale to be applied to the perlin noise
    - r: radius reduction of the gradient mask. if =0 the radius will be the same as the interested direction//2.
    - shape: the shape of the grid
    """   
    
    #generation of a noise map
    grid=noiseMap(shape, scale)
    #perlinNormalizationV = np.vectorize(perlinNormalization)
    grid = perlinNormalizationV(grid)
    
    #generation of a gradient mask
    gradient, centerX, centerY=np.zeros(shape), shape[0]//2, shape[1]//2
    distanceToCorner=np.sqrt((centerX-r)**2+(centerY-r)**2)
    for i in range(shape[0]):
        for j in range(shape[1]):
            distance = np.sqrt((centerX - i)**2 + (centerY - j)**2)
            gradient[i][j] = distance / distanceToCorner /2
    
    geography=grid * (1-gradient) # application of noise and gradient mask
    
    islandFilterV = np.vectorize(lambda x, tresh: 0 if x>tresh else -1)
    
    geography = islandFilterV(geography, geography.mean())
    
    #no ground on borders
    geography[0,0:n]=-1
    geography[n-1,0:n]=-1
    geography[0:n,0]=-1
    geography[0:n,n-1]=-1
    
    return geography # -1: water, 0: land

def perlinNormalization(x):
    """moves the values returned from perlinNoise from [-1,1] to [0,1]"""
    return (x+1)/2

perlinNormalizationV=np.vectorize(perlinNormalization)  

class World():
    """
    ### World
    Class representing the world
    """
    def __init__(self):   
        self.geography=generateIsland()
        self.fertility=np.multiply(perlinNormalizationV(noiseMap((n,n),50)),self.geography+1) #elementwise multiplication of the two matrices to apply geography as a mask of our random walk
        self.vegetob=np.copy(self.fertility)*(random()*3)
        
        self.limitVegetobV=np.vectorize(lambda x: 10 if x>10 else x)
        
    def growVegetob(self):
        newVegetob=self.vegetob+self.fertility*GROWING
        self.vegetob=self.limitVegetobV(newVegetob)