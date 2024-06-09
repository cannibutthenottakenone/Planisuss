import numpy as np
import random
from Creatures.creature import Creature
from planisuss_constants import MAX_LIFE_E, SPEED_E

class Erbast(Creature):
    def __init__(self, position:np.ndarray[int,int], startEnergy: int=10, maxLife: int=MAX_LIFE_E, speed: int=SPEED_E):
        super().__init__(position,startEnergy,maxLife,speed)
    
    def pickMovement(self, seenCells: np.ndarray[float]):
        """
        ### Erbast.pickMovement
        given a matrix of cells it picks the best suited for movement and returns the movement vector to reach it
        
        #### Parameters:
        - seenCells: the cells that the erbast is able to see, size: (self.speed*2)+1 with the center cell being the current occupied cell, value: vegetob density
        """
        # creating of an ordered list from best to worst of seen positions, based on vegetob amount
        ranking: list[(float, np.ndarray[int, int])]=[]
        for i in range(seenCells.shape[0]):
            for j in range(seenCells.shape[1]):
                if len(ranking)==0:
                    ranking.append((seenCells[i][j],np.array([i,j])))
                else:
                    for k in range(len(ranking)):
                        if seenCells[i][j]>=ranking[k][0]:
                            ranking.insert(k,(seenCells[i][j],np.array([i,j])))
        
        #mapping from imput matrix to movement vectors
        ranking=[(x[0], x[1]-self.speed) for x in ranking]
        
        #removal of unreachable vectors starting from the top and going down, if the first element is reachable, then the execution skips the rest
        if self.energy<=self.speed:
            for i in range(len(ranking)):
                if max(ranking[0][1][0], ranking[0][1][1])>self.energy:
                    ranking.pop(0)
                else:
                    break
        
        #removal of vegetob values from ranking | unnecessary cause we just return the movement from the first item
        #ranking=[x[1] for x in ranking]
        
        return ranking[0][1]
        
        
        
        