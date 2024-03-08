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
        
    def electLeader(self, const: dict):
        """
        ### SocialGroup.electLeader()
        Elects a number of group leaders to fill the leaders list untill it contains "LEADERS" (constant) elements
        
        #### Parameters: 
        - const: the constants dictionary
        """      
        pass #each species has their own type of "government" 
    
    def updateLeader(self, const: dict, element: Creature):
        """
        ### SocialGroup.updateLeader()
        Checks if an element that is new to the group has a right to oust a leader from the group
        
        #### Parameters: 
        - const: the constants dictionary
        """      
        pass #each species has their own type of "government" 