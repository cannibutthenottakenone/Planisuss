from math import sqrt

def mean(values: list[float]):
    """
    ### mean() 
    Returns the mean from a list of floats
    
    #### Parameters:
    - values: the list of floats of which the mean is needed
    """
    return sum(values)/len(values)

def stdDev(values: list[float], mean: float):
    """
    ### stdDev()
    Returns the standard deviation from a list of floats and the mean
    
    #### Parameters:
    - values: the list of floats of which the mean is needed
    - mean: the mean
    """
    stdDev=0
    for e in values:
        stdDev+=e-mean
    stdDev=sqrt((stdDev**2)/len(values))
    
    return stdDev


