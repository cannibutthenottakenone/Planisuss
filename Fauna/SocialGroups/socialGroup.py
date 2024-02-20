from Fauna.Creatures.creature import Creature

class SocialGroup:
    """
    ### SocialGroup
    base class for the implementation of social groups
    """
    
    def __init__(self, maxSize: int):
        self.members: list[Creature]=[]
        self.leaders: list[Creature]=[]  
        
    def addMember(self, dude: Creature):
        """
        ### SocialGroup.addMember()
        Adds a creature to the group
        
        #### Parameters:
        - dude: thre creature to add
        """
        self.members.append(dude)