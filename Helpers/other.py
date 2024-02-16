from math import sqrt

def mean(values: list[float]):
    return sum(values)/len(values)

def stdDev(values: list[float], mean: float):
    stdDev=0
    for e in values:
        stdDev+=e-mean
    stdDev=sqrt((stdDev**2)/len(values))
    
    return stdDev


