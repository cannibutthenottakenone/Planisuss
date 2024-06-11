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
        self.dead=False
        
    
    def movement(self, movement: np.ndarray[int,int]):
        """
        ### Creature.movement
        Makes the creature move.
        
        #### Parameters:
        - movement: movement array [dx,dy]. Allowed values for cells {-1*self.speed,0,1*self.speed}
        """
        self.position+=movement
        self.energy-=max(movement) #diagonal movement still counts as 1
        if self.energy<0:
            self.die()
        
    def pickMovement(self, seenCells: np.ndarray[int,int]):
        """each creature will implement this method in their own way"""
        return np.array([random.randint(-1,1),random.randint(-1,1)])
    
    def older(self):
        """
        ### Creature.older
        Makes the creature age.
        """
        self.age+=1
        if self.age>self.maxLife:
            self.die()
    
    def die(self):
        self.dead=True #relies on upper levels to collect and delete
        
    def eat(self):
        pass