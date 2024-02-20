from random import randint

class Cell:
    """
    ### Cell
    Atomic unit of the simulated world
    """   
    
    
    def __init__(self, coordinates: tuple[int, int], cellType = "water", fertility: float = 0):
        """
        ### Cell.constructor()
        Creates a new cell
        
        #### Parameters:
        - coordinates: the coordinates of the cell
        - cellType: value used to decide cell type, <'water'|'soil'>
        - fertility: multiplier for plant growth
        """
        
        self.coordinates=coordinates
        self.cellType=cellType
        if self.cellType=="water":
            self.fertility=0
        else:
            self.fertility=fertility
            self.vegetobDensity=randint(0,100)
            
        self.socialGroups=[] #to store the social groups located on the cell
            
        self.traces=False #to allow predators to track preys
        self.tracesAge=0            
        
        
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
            
    def tracesSet(self):
        """
        ### Cell.tacesSet()
        Marks the cell as containing traces
        """
        self.traces=True
        self.tracesAge=0
        
    def tracesAging(self, const: dict):
        """
        ### Cell.tracesAging
        Ages the traces on the cell and deletes them if they're too old
        
        #### Parameters
        - const: the constants dictionary
        """
        if self.traces:
            if self.tracesAge==const["CREATURES"]["ERBAST"]["TRACES_LIFE"]:
                self.traces=False
                return
            self.tracesAge+=1