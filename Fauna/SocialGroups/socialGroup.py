from Fauna.Creatures.creature import Creature

class SocialGroup:
    """
    ### SocialGroup
    base class for the implementation of social groups
    """
    
    def __init__(self, maxSize: int):
        self.members: list[Creature]=[]
        self.leaders: list[Creature]=[]
        self.energy=0
        
    def addMember(self, dude: Creature):
        """
        ### SocialGroup.addMember()
        Adds a creature to the group
        !! To add a creature to a social group use Creature.joinSocialGroup(). That method will call this one.
        
        #### Parameters:
        - dude: the creature to add
        """
        self.members.append(dude)
        
    def electLeader():
        
        
        pass