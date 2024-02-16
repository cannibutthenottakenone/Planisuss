class Cell:
    """
    ### Cell
    atomic unit of the simulated world
    """
    
    def __init__(self, cellType = "water", fertility: float = 0):
        """
        ### Cell
        creates a new cell
        
        parameters:
        - cellType: value used to decide cell type, <water|soil>
        - fertility: multiplier for plant growth
        """
        
        self.cellType=cellType
        if self.cellType=="water":
            self.fertility=0
        else:
            self.fertility=fertility