from Fauna.Creatures.creature import Creature
from Fauna.SocialGroups import socialGroup
from World.cell import Cell

class Erbast(Creature):
    
    def __init__(self, neighborhood: int, maxEnergy: int, maxLife: int, aging: int, position: tuple[int, int], startEnergy: int = 10):
        super().__init__(neighborhood, maxEnergy, maxLife, aging, position, startEnergy)
        
    def scoreCell(self, cell: Cell, distance: int):
        if self.socialGroup:
            return (cell.vegetobDensity/len(self.socialGroup.members))-distance
        else: 
            return cell.vegetobDensity-(distance**self.laziness)
        
    def graze(self, cell: Cell):
        """
        ### Erbast.graze()
        The erbast will feed on the vegtob present on the cell it is in.
        
        #### Parameters:
        - cell: the cell on which the erbast is located
        """
        
        cell.vegetobDensity-=1
        self.energy+=1