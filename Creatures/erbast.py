import numpy as np
from random import random
from Creatures.creature import Creature
from planisuss_constants import MAX_LIFE_E, SPEED_E, MAX_ENERGY_E

class Erbast(Creature):
    population=[]
    maxEnergy=MAX_ENERGY_E
    
    def __init__(self, position:np.ndarray[int,int], startEnergy: int=80, maxLife: int=MAX_LIFE_E, speed: int=SPEED_E):
        """
        ### Erbast.constructor
        Initiates a new creature object
        #### Parameters
        - position: the creature's position in x,y coordinates
        - startEnergy: the starting energy
        - maxLife: the base maxLife, it will be remoduled through a normal function
        - speed: how far can the creature travel each turn
        """
        super().__init__(position,startEnergy,maxLife,speed)       
        
    def pickMovement(self, vegetobs: np.ndarray[float])->np.ndarray:
        """
        ### Erbast.pickMovement
        given a matrix of cells it picks the best suited for movement (within range) and returns the movement vector to reach it
        
        #### Parameters:
        - vegetobs: the vegetob grid
        """
        if vegetobs[self.position[0],self.position[1]]>1.5 and random()>0.3: #when there is enough food the erbast will not move 70% of the time
            return np.zeros(2)
        
        rangeM=min(self.speed, int(self.energy))
        
        bestCell: tuple[float, np.ndarray[int, int]]=()       
        for i in range(max(0,self.position[0]-rangeM), min(vegetobs.shape[0],self.position[0]+rangeM+1)):
            for j in range(max(0, self.position[1]-rangeM), min(vegetobs.shape[1],self.position[1]+rangeM+1)):
                if bestCell==():
                    bestCell=(vegetobs[i][j],np.array([i,j]))
                else:
                    if vegetobs[i][j]>=bestCell[0]:
                        bestCell=(vegetobs[i][j],np.array([i,j]))

        bestCell=(bestCell[0],bestCell[1]-self.position)
        
        return bestCell[1]   
    
    def eat(self, vegetobs):
        """
        ### Erbast.eat
        Reduces the vegetobs at the erbast's position and increases its energy
        #### Parameters:
        -vegetobs: the vegetob grid
        """
        if vegetobs[self.position[0],self.position[1]]>1.5:
            vegetobs[self.position[0],self.position[1]]-=1.5
            self.energy=min(self.energy+1, self.maxEnergy)
    