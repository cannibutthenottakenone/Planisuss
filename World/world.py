from Helpers import random_walk
from World.cell import Cell
import numpy as np
import matplotlib.pyplot as plt

class World:
    """
    ### World
    Encapsulates the whole simulated world.    
    """

    def __init__(self, X: int =50, Y: int =50, minFertility: float =0.5, maxFertility: float =1.5):
        """
        ### World.constructor()
        Generates a new world as a X,Y sized matrix of cells
        
        #### Parameters:
        X,Y: integers, represent the dimensions of the world.
        """
        self.dimensions = (X, Y)
                
        self.world :list[Cell]= [[-1 for _ in range(Y)] for _ in range(X)]
        cellSeeds = [[-1 for _ in range(Y)] for _ in range(X)]
        
        #creation of all cells according to weighted random walk
        randomType = random_walk.WeightedRandomWalk(100, p=0.5)
        randomFert = random_walk.WeightedRandomWalk(maxFertility, minFertility)
        
        for j in range(X):
            for i in range(Y):
                if i==0 or i==X-1 or j==0 or j==Y-1:
                    cellSeeds[j][i]={"value": 49, "fertility": 0}
                    self.world[j][i]=Cell((i,j))
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
                        self.world[j][i]=Cell((i,j), "soil", fert)
                    else:
                        self.world[j][i]=Cell((i,j), "water", fert)
            
                
        
        #test of visualization
        for i in range(X):
            for j in range(Y):
                cellSeeds[j][i]=cellSeeds[j][i]["value"]                
        
        # A=np.asarray(cellSeeds)
        # plt.imshow(A)
        # plt.savefig('Figure_1a.png', bbox_inches='tight')
                
        
        del cellSeeds
        
        


    def growVegetob(self, const: dict):
        """
        ### World.growVegetob()
        Grows the vegetob across the map.
        
        #### Parameters:
        - const: the constants dictionary
        """
        for i in range(self.dimensions[1]):
            for j in range(self.dimensions[0]):
                self.world[i][j].growVegetob(const)
            

    def getCell(self, x, y)-> Cell:
            """
            ### World.getCell()
            Returns a cell.
            
            #### Parameters:
            - x: the x coordinate;
            - y: the y coordinate.            
            """
            return self.world[y][x]