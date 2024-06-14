import numpy as np
from random import random
from Creatures.creature import Creature
from planisuss_constants import MAX_LIFE_E,SPEED_E

class Erbast(Creature):
    population=[]
    
    def __init__(self, position:np.ndarray[int,int], startEnergy: int=10, maxLife: int=MAX_LIFE_E, speed: int=SPEED_E):
        super().__init__(position,startEnergy,maxLife,speed)       
        
    def pickMovement(self, vegetobs: np.ndarray[float])->np.ndarray:
        """
        ### Erbast.pickMovement
        given a matrix of cells it picks the best suited for movement and returns the movement vector to reach it
        
        #### Parameters:
        - vegetobs: the vegetob grid
        """
        if vegetobs[self.position[0],self.position[1]]>1 and random()>0.3:
            return np.zeros(2)
        
        rangeM=min(self.speed, self.energy)
        
        ranking: tuple[float, np.ndarray[int, int]]=()
        for i in range(max(0,self.position[0]-rangeM), min(vegetobs.shape[0],self.position[0]+rangeM+1)):
            for j in range(max(0, self.position[1]-rangeM), min(vegetobs.shape[1],self.position[1]+rangeM+1)):
                if ranking==():
                    ranking=(vegetobs[i][j],np.array([i,j]))
                else:
                    if vegetobs[i][j]>=ranking[0]:
                        ranking=(vegetobs[i][j],np.array([i,j]))

        ranking=(ranking[0],ranking[1]-self.position)
        
        return ranking[1]   
    
    def eat(self, vegetobs):
        vegetobs[self.position[0],self.position[1]]-=1
        self.energy+=1
        
    def reproduce(self):
        pass #TODO
    