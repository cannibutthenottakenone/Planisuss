import numpy as np
from random import randint
from Creatures.creature import Creature
from Creatures.erbast import Erbast
from planisuss_constants import MAX_LIFE_C,SPEED_C, MAX_ENERGY_C

class Carviz(Creature):
    population=[]
    maxEnergy=MAX_ENERGY_C
    
    def __init__(self, position:np.ndarray[int,int], startEnergy: int=10, maxLife: int=MAX_LIFE_C, speed: int=SPEED_C):
        """
        ### Carviz.constructor
        Initiates a new creature object
        #### Parameters
        - position: the creature's position in x,y coordinates
        - startEnergy: the starting energy
        - maxLife: the base maxLife, it will be remoduled through a normal function
        - speed: how far can the creature travel each turn
        """
        super().__init__(position,startEnergy,maxLife,speed)       
        self.target: Erbast=None
            
    def pickTarget(self, erbasts: list[Erbast]):
        """
        ### Carviz.pickTarget
        Will compute and compare the distances of the Erbasts in the list and set the closest one as target
        #### Parameters:
        - erbasts: the population list of the erbasts
        """
        if len(erbasts)==0: return
        distance=max(abs(erbasts[0].position-self.position)) #since diagonals also count as distance 1
        self.target=erbasts[0]
        if len(erbasts)==0:
            return
        for i in range(1, len(erbasts)):
            iDistance=max(abs(erbasts[i].position-self.position))
            if iDistance<distance:
                distance=iDistance
                self.target=erbasts[i]
    
    def stalk(self, geography):
        """
        ### Carviz.stalk
        The carviz will move towards the target
        #### Parameters:
        - geography: the world's geography grid
        """
        
        self.movement(self.getDirection(geography))      
        
    
    def hunt(self, geography):
        """
        ### Carviz.hunt
        If the prey is within reach the carviz will kill and eat it otherwise it will move towards it
        #### Parameters:
        - geography: the world's geography grid
        """
        if max(abs(self.target.position-self.position))>self.speed:
            self.stalk(geography)
        else:
            self.position=self.target.position
            self.energy= min(self.energy+self.target.energy*5/6, self.maxEnergy)
            self.target.die()
            self.target=None
        
    def nap(self):
        """
        ### Carviz.nap
        The carviz has nothing to do and will nap
        """
        self.energy-=0.5 
    
    def getDirection(self, geography) -> np.ndarray:
        """
        ### Carviz.getDirection
        Will return a movement vector towards the target
        """
        #here a breadth search first algorithm could be used       
        completeD = self.target.position-self.position
        limitedD= np.array([min(self.speed, completeD[0]),min(self.speed, completeD[1])])
        isSea=geography[self.position[0]+limitedD[0], self.position[1]+limitedD[1]]==-1
        if isSea: #if the place we want to go is water
            self.target=None #recompute target
            while isSea:
                limitedD=np.array([randint(0, self.speed),randint(0, self.speed)]) #and try a random directions
                temporaryPos: np.ndarray=self.position+limitedD
                if temporaryPos[0]<0 or temporaryPos[0]>geography.shape[0] or temporaryPos[1]<0 or temporaryPos[1]>geography.shape[1]:
                    continue
                isSea=geography[temporaryPos[0],temporaryPos[1]]==-1
        return limitedD