from random import randrange, randint, random
from World.cell import Cell
from Fauna.SocialGroups.socialGroup import SocialGroup

class Creature:
    """
    ### Creature
    base class for the implementation of creatures.
    """
    
    def __init__(self, neighborhood: int, maxEnergy: int, maxLife: int, aging: int, position: list[int,int], startEnergy: int=10):
        """
        ### Creature.constructor()
        generates a new creature object
        
        #### Parameters:
        - neighborhood: the destance over which neighbouring cells will be searched (diagonals count as one)
        - maxEnergy: the maximum amount of energy the creature is able to store
        - maxLife: the amount of days after which the creature will die of old age
        - aging: the amount of maxEnergy lost every 10 days
        - position: list [x,y] with the coordinates of the animal
        - startEnergy: the starting energy of the creature
        """
        self.neighborhood=neighborhood
        self.maxEnergy=maxEnergy
        self.maxLife=maxLife
        self.aging=aging
        
        
        self.age=0
        self.energy=startEnergy
        self.socialAttitude=randrange(0,100)
        self.position=position #list and not tuple because lists are mutable objects
        
        self.socialGroup: SocialGroup= None
        
    def joinSocialGroup(self, const: dict, group: SocialGroup):
        """ 
        ### Creature.joinSocialGroup()
        Makes a creature join a social group
        
        #### Parameters:
        - const: the constants dictionary
        - group: the group to join
        """
        if len(group.members)+1<=const["CREATURES"]["MAX_SOCIAL_GROUP"]:
            self.socialGroup=group
            group.addMember(self)
        
    def followGroup(self, const: dict, groupSize: int) -> bool:
        """
        ### Creature.followGroup()
        Decides if the creature will follow its social group (true) or leave it (false)
        
        #### Parameters:
        - const: the constants dictionary
        - groupSize: the current size of the social group
        """
        
        return random()<((-1*0.8*groupSize/const["CREATURES"]["MAX_SOCIAL_GROUP"]+0.9)(0.8*self.socialAttitude+0.1)) #check docs for formula explainations
       
    def scoreCell(self, cell: Cell, distance: int, groupchoice: tuple[int,int]=False):
        """
        ### Creature.scoreCell()
        Given a cell it produces a score for it, check documentation for scoring function
        
        #### Parameters:
        - cell: the cell to score
        - distance: the distance from the current position
        - groupChoice: in case the creature has decided to not follow its group, the coordinates where the group will go
        """
        if groupchoice:
            if cell.coordinates==groupchoice:
                return -10
        
        return 0 #no actual formula for general creatures, it should be rewritten inside the creature class
    
    def pickMovement(self, currentCell: Cell, cellsSeen: list[Cell]):
        """
        ### Creature.pickMovement()
        Given the cells that the creature can see it will pick one to move to.
        
        #### Parameters:
        - currentCell: the current cell where the creature is
        - cellsSeen: the cells that can be seen or remembered by the creature
        """
    
        highScore=self.scoreCell(currentCell, 0)
        bestCell=currentCell
        for c in cellsSeen:
            cScore = self.scoreCell(c, max(abs(currentCell.coordinates[0]-c.coordinates[0]), abs(currentCell.coordinates[1]-c.coordinates[1])))
            if cScore>highScore:
                highScore=cScore
                bestCell=c
        
        return bestCell
    
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
        
        
        
        
    