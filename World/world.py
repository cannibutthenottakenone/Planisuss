from Helpers import random_walk
from World.cell import Cell


import numpy as np
import matplotlib.pyplot as plt

class World:
    """
    ### World
    encapsulates the whole simulated world.   
    
    """

    def __init__(self, X: int =50, Y: int =50, minFertility: float =0.5, maxFertility: float =1.5):
        """
        ### World
        generates a new world as a X,Y sized matrix of cells
        
        parameters:
        X,Y: integers, represent the dimensions of the world

        """
        self.dimensions = (X, Y)
                
        self.world = [[-1 for _ in range(Y)] for _ in range(X)]
        cellSeeds = [[-1 for _ in range(Y)] for _ in range(X)]
        
        #creation of all cells according to weighted random walk
        randomType = random_walk.WeightedRandomWalk(100, p=0.5)
        randomFert = random_walk.WeightedRandomWalk(maxFertility, minFertility)
        
        for j in range(X):
            for i in range(Y):
                if i==0 or i==X-1 or j==0 or j==Y-1:
                    cellSeeds[j][i]={"value": 49, "fertility": 0}
                    self.world[j][i]=Cell()
                else:
                    roundvalue=[cellSeeds[j-1][i-1]["value"], cellSeeds[j-1][i]["value"], cellSeeds[j-1][i+1]["value"], cellSeeds[j][i-1]["value"]]
                    roundfert=[cellSeeds[j-1][i-1]["fertility"], cellSeeds[j-1][i]["fertility"], cellSeeds[j-1][i+1]["fertility"], cellSeeds[j][i-1]["fertility"]]
                    
                    centerDistanceMod=0
                    
                    value=randomType.evaluate(roundvalue, centerDistanceMod)
                    fert=randomFert.evaluate(roundfert)
                    # file = open("./log.txt", "x")
                    # self.file.write(str(value)+"\n")
                    
                    cellSeeds[j][i]={"value": value, "fertility": fert}
                    if value>49:
                        self.world[j][i]=Cell("soil", fert)
                    else:
                        self.world[j][i]=Cell("water", fert)
            
                
        
        #test of visualization
        for i in range(X):
            for j in range(Y):
                cellSeeds[j][i]=cellSeeds[j][i]["value"]                
        
        # A=np.asarray(cellSeeds)
        # plt.imshow(A)
        # plt.savefig('Figure_1a.png', bbox_inches='tight')
                
        
        del cellSeeds
        
        


    def growVegetob():
        pass

    def getCell(self, x, y)-> Cell:
            """returns a cell"""
            return self.world[y][x]
        
    def getDimensions(self) -> tuple[int, int]:
        return self.dimensions