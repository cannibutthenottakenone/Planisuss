from random import randint

class Cell:
    """
    ### Cell
    Atomic unit of the simulated world
    """   
    
    
    def __init__(self, cellType = "water", fertility: float = 0):
        """
        ### Cell.constructor()
        Creates a new cell
        
        #### Parameters:
        - cellType: value used to decide cell type, <water|soil>
        - fertility: multiplier for plant growth
        """
        
        self.cellType=cellType
        if self.cellType=="water":
            self.fertility=0
        else:
            self.fertility=fertility
            self.vegetobDensity=randint(0,100)
            
        
        
    def growVegetob(self, const: dict):
        """
        ### Cell.growVegetob()
        Will increase the vegetob density by GROWING*fertility
        
        #### Parameters
        - const: the constants dictionary
        """
        if self.cellType=="water":
            return
        
        self.vegetobDensity+=const["WORLD"]["GROWING"]*self.fertility
        if self.vegetobDensity>100:
            self.vegetobDensity=100