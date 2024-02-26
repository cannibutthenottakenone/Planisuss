from Fauna.Creatures.creature import Creature
from Fauna.SocialGroups.herd import Herd
from World.cell import Cell
from math import sinh, pi

class Carviz(Creature):
    
    def __init__(self, neighborhood: int, maxEnergy: int, maxLife: int, aging: int, position: tuple[int, int], startEnergy: int = 10):
        super().__init__(neighborhood, maxEnergy, maxLife, aging, position, startEnergy)
        
    def scoreCell(self, cell: Cell, distance: int):
        herdEnergy=0
        for sg in cell.socialGroups:
            if sg is Herd:
                herdEnergy=sg.energy
        if self.socialGroup:
            return (sinh(pi*herdEnergy/len(self.socialGroup)))-distance+(cell.traces/(cell.tracesAge+1))
        else: 
            return (sinh(pi*herdEnergy))-distance+(cell.traces/(cell.tracesAge+1))