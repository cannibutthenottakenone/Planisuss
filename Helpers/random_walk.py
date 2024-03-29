from Helpers.other import mean, stdDev
from random import choices
from math import exp, pi


class WeightedRandomWalk:
    """
    ### WeightedRandomWalk
    Used for the creation of the world it follows a random walk in which the number of steps varies in an inverse proportion with he distance from the center.
    """
    
    
    def __init__(self, maxValue: float = 10, minValue: float = 0, p: float = 0.5):
        """
        ### WeightedRandomWalk.contructor()
        Creates a new object.
        
        #### Parameters:
        - maxValue: the maximum value that can be reached;
        - minValue: the minimum value that can be reached;
        - p: the probability that the walk will muve in the positive direction. the probability for the negative direction id given by 1-p.
        """
        self.minValue=minValue
        self.maxValue=maxValue
        self.center=(minValue+maxValue)/2
        
        self.p, self.q=p, 1-p
        
    def weightFunction(self, x: float) -> float:
        """
        ### WeightedRandomWalk.weightFunction()
        Returns the weight needed for the random walk
        
        #### Parameters:
        - x: the value that needs weighting
        """
        return (((2.9921)*exp(-0.03125*((x-50)**2)))+1)

    def evaluate(self, values: list[float], pModifier: float =0) -> float:
        """
        ### WeightedRandomWalk.evaluate()
        Evaluates a new value starting from other values.
        
        #### Parameters:
        - values: the starting values as a list.        
        """
        
        meanV=mean(values)
        direction=choices([-1,1],[self.q-pModifier,self.p+pModifier])[0]
        weight=self.weightFunction(meanV)
        
        return (meanV+(direction*weight))