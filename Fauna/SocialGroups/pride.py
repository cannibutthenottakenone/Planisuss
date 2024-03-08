from Fauna.SocialGroups.socialGroup import SocialGroup
from Fauna.Creatures.creature import Creature
from Fauna.Creatures.carviz import Carviz
from Fauna.Creatures.erbast import Erbast

class Pride(SocialGroup):
    def __init__(self, maxSize: int):
        super().__init__(maxSize)
        
    def electLeader(self, const: dict):
        for e in self.members:
            self.updateLeader(e)
    
    def updateLeader(self, const: dict, element: Creature):
        if element.energy>self.leaders[0].energy:
            self.leaders[0]=element