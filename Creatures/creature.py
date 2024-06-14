import numpy as np
from random import randint, random, randrange
from planisuss_constants import MAX_LIFE, SPEED
from math import log, sqrt

class Creature():
    population=[]
    
    @classmethod
    def populateCreature(cls, creature: type, world, amount: int=100):
        for i in range(amount):
            accPos=False
            while not accPos:
                position=np.array([randint(0, world.geography.shape[0]-1),randint(0, world.geography.shape[1]-1)])
                accPos=world.geography[position[0],position[1]]!=-1            
            cls.population.append(creature(position))
    
    def __init__(self, position:np.ndarray[int,int], startEnergy: float=10, maxLife: int=MAX_LIFE, speed: int=SPEED):
        self.position=position
        self.energy=startEnergy
        self.maxLife= maxLife+ randrange(-1,2,2) * min(50,sqrt(-72.24*log(random())))  # maxlife + random amount from a gaussian, check documentation for more info
        print(self.maxLife)
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
        return np.array([randint(-1,1),randint(-1,1)]) #random direction with distance one
    
    def older(self):
        """
        ### Creature.older
        Makes the creature age.
        """
        self.age+=1
        if self.age>self.maxLife:
            self.breed()
            self.die()
        if self.energy<0:
            self.die
    
    def die(self):
        self.dead=True #relies on upper levels to collect and delete
        
    def breed(self):
        pass