from random import randrange, randint

class Creature:
    """
    ### Creature
    base class for the implementation of creatures.
    """
    
    def __init__(self, neighborhood: int, maxEnergy: int, maxLife: int, aging: int, position: tuple[int,int], startEnergy: int=10):
        """
        ### Creature.constructor()
        generates a new creature object
        
        #### Parameters:
        - neighborhood: the destance over which neighbouring cells will be searched (diagonals count as one)
        - maxEnergy: the maximum amount of energy the creature is able to store
        - maxLife: the amount of days after which the creature will die of old age
        - aging: the amount of maxEnergy lost every 10 days
        - position: tuple (x,y) with the coordinates of the animal
        - startEnergy: the starting energy of the creature
        """
        self.neighborhood=neighborhood
        self.maxEnergy=maxEnergy
        self.maxLife=maxLife
        self.aging=aging
        
        
        self.age=0
        self.energy=startEnergy
        self.socialAttitude=randrange(0,100)
        self.position=position
    
    def move(self, newposition: tuple[int,int]):
        """
        ### Creature.move()
        Moves the creature to a new cell and decreases the energy accordingly.
        If energy<distance an exception will be raised
        
        #### Parameters:
        - newposition: tuple (x,y) with the new location's coordinates
        """
        distance=max(newposition[0], newposition[1]) #because the movement over a diagonal is still considered 1
        
        if distance>self.energy:
            self.position=newposition
            self.energy-=distance
        else:
            raise Exception("too little energy for movement")
        
    def eat(self, energy: int):
        """
        ### Creature.eat()
        increases the creature energy
        
        #### Parameters:
        - energy: the amount of energy eaten
        """
        self.energy+=energy
    
    def reproduce(self, const: dict, babiesNumber: int=2):
        """
        ### Creature.reproduce()
        Generates and returns a list of babies and kills the creature
        
        #### Parameters:
        - babiesNumber: the number of babies generated
        """
        
        if self.energy<babiesNumber:
            babiesNumber=energy # to avoid to create childen that can't have any energy
        
        usedEnergy=0
        offspring: list[Creature]=[]
        for i in range(babiesNumber):
            if i==babiesNumber-1:
                energy=self.energy-usedEnergy
            else:
                energy=randint(1, self.energy-usedEnergy-babiesNumber+i)
            
            offspring.append(Creature(const["CREATURES"]["NEIGHBORHOOD"],const["CREATURES"]["MAX_ENERGY"], const["CREATURES"]["MAX_LIFE"], const["CREATURES"]["AGING"], self.position, energy))
        
        return offspring
        
    def agingF(self):
        """
        ### Creature.agingF()
        Function called every 10 days that decreases the creature max energy by the aging variable
        """
        self.maxEnergy-=self.aging

    def die(self):
        """
        ### Creature.die()
        Kills the creature and deletes the object
        """
        del self
        
        
        
        
    