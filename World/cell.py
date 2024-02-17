from Helpers.planisuss_constants import constants
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
            
        
        
    def growVegetob(self):
        """
        ### Cell.growVegetob()
        Will increase the vegetob density by GROWING*fertility
        """
        if self.cellType=="water":
            return
        
        self.vegetobDensity+=constants["WPRLD"]["GROWING"]*self.fertility
        if self.vegtobDensity>100:
            self.vegtobDensity=100