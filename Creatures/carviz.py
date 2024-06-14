import numpy as np
from random import random
from Creatures.creature import Creature
from Creatures.erbast import Erbast
from planisuss_constants import MAX_LIFE_C,SPEED_C

class Carviz(Creature):
    population=[]
    
    def __init__(self, position:np.ndarray[int,int], startEnergy: int=10, maxLife: int=MAX_LIFE_C, speed: int=SPEED_C):
        super().__init__(position,startEnergy,maxLife,speed)       
        self.target: Erbast=None
            
    def pickTarget(self, erbasts: list[Erbast]):
        """
        ### Carviz.pickTarget
        Will compute and compare the distances of the Erbasts in the list and set the closest one as target
        """
        if len(erbasts)==0: return
        distance=max(abs(erbasts[0].position-self.position)) #since diagonals also count as distance 1
        self.target=erbasts[0]
        for i in range(1, len(erbasts)):
            iDistance=max(abs(erbasts[i].position-self.position))
            if iDistance<distance:
                distance=iDistance
                self.target=erbasts[i]
    
    def stalk(self, geography)-> None:
        """
        ### Carviz.stalk
        The carviz will move towards the target
        """
        
        self.movement(self.getDirection(geography))      
        
    
    def hunt(self, geography)-> None:
        """
        ### Carviz.hunt
        If the prey is within reach the carviz will kill and eat it otherwise it will move towards it
        """
        if max(abs(self.target.position-self.position))>self.speed:
            self.stalk(geography)
        else:
            self.position=self.target.position
            self.energy+=self.target.energy*5/6
            self.target.die()
            self.target=None
        
    def nap(self) -> None:
        self.energy-=0.5 
    
    def getDirection(self, geography) -> np.ndarray:
        #here a breadth search first algorithm could be used
        #TODO avoid sea
        completeD = self.target.position-self.position
        limitedD= np.array([min(self.speed, completeD[0]),min(self.speed, completeD[1])])
        return limitedD