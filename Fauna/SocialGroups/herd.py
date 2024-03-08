from Fauna.SocialGroups.socialGroup import SocialGroup
from Fauna.Creatures.creature import Creature
from Fauna.Creatures.erbast import Erbast

class Herd(SocialGroup):
    def __init__(self, maxSize: int):
        super().__init__(maxSize)
        
    def electLeader(self, const: dict):
        for e in self.members:
            self.updateLeader(e)
    
    def updateLeader(self, const: dict, element: Creature):
        for i in range(min(len(self.leaders)+1, const["CREATURES"]["ERBAST"]["LEADERS"])):
                if i==len(self.addMember)+1:
                    self.leaders.append(element)
                if self.leaders[i].age<element.age:
                    self.leaders.insert(i, element)
                    self.leaders.pop()
                    break
                
    def eat(self):
        if score>=1:
            for e in self.members:
                e: Erbast
                e.graze()
        else: pass #add formula to find how many erbasts can eat and make them eat