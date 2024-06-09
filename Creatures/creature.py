import numpy as np
import random
from planisuss_constants import MAX_LIFE, SPEED

class Creature():
    def __init__(self, position:np.ndarray[int,int], startEnergy: int=10, maxLife: int=MAX_LIFE, speed: int=SPEED):
        self.position=position
        self.energy=startEnergy
        self.maxLife=maxLife
        self.speed=speed
        self.age=0
        
    
    def movement(movement: np.ndarray[int,int]):
        """
        ### Creature.movement
        Makes the creature move.
        
        #### Parameters:
        - movement: movement array [dx,dy]. Allowed values for cells {-1*self.speed,0,1*self.speed}
        """
        position+=movement
        energy-=max(movement) #diagonal movement still counts as 1
        
    def pickMovement(self, seenCells: np.ndarray[int,int]):
        """each creature will implement this method in their own way"""
        return np.array([random.randint(-1,1),random.randint(-1,1)])
    
    def age(self):
        """
        ### Creature.age
        Makes the creature age.
        """
        self.age+=1
        if self.age>self.maxLife:
            self.die()
    
    def die(self):
        self.position=np.array([-1,-1]) #relies on upper levels to collect and delete