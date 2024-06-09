import numpy as np
from perlin_noise import PerlinNoise
from planisuss_constants import SIZE as n  #size of the side of the square world.

def generateIsland(scale:int =25,r:int =25, shape: tuple[int,int] =(n,n) ):
    """
    ### generateIsland
    Generates an island on a [shape] shaped grid.
    
    #### Parameters:
    - scale: scale to be applied to the perlin noise
    - r: radius reduction of the gradient mask. if =0 the radius will be the same as the interested direction//2.
    - shape: the shape of the grid
    """
    grid=np.zeros(shape) # 0: water, 1: land
    
    #generation of a noise map
    noise = PerlinNoise(0.5)   
    for i in range(shape[0]):
        for j in range(shape[1]):
            grid[i][j] = noise([i/scale,j/scale])
    perlinNormalizationV = np.vectorize(perlinNormalization)
    grid = perlinNormalizationV(grid)
    
    #generation of a gradient mask
    gradient, centerX, centerY=np.zeros(shape), shape[0]//2, shape[1]//2
    distanceToCorner=np.sqrt((centerX-r)**2+(centerY-r)**2)
    for i in range(shape[0]):
        for j in range(shape[1]):
            distance = np.sqrt((centerX - i)**2 + (centerY - j)**2)
            gradient[i][j] = distance / distanceToCorner /2
    
    geography=grid * (1-gradient) # application of noise and gradient mask
    
    islandFilterV = np.vectorize(islandFilter)
    
    geography = islandFilterV(geography, geography.mean())
    
    return geography

def perlinNormalization(x):
    """moves the values returned from perlinNoise from [-1,1] to [0,1]"""
    return (x+1)/2

def islandFilter(x,tresh):
    if x>tresh:
        return 1
    else:
        return 0

class World():    
    geography=generateIsland()
    
    
    