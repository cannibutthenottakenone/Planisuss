from Creatures.creature import Creature

class Carviz(Creature):
    
    def __init__(self, neighborhood: int, maxEnergy: int, maxLife: int, aging: int, position: tuple[int, int], startEnergy: int = 10):
        super().__init__(neighborhood, maxEnergy, maxLife, aging, position, startEnergy)