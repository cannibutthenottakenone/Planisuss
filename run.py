from Helpers.planisuss_constants import import_constants
from World import world as worldm
from Rendering.show import show
import matplotlib.pyplot as plt

const=import_constants()
print(const)

world=worldm.World(const["WORLD"]["NUMCELLS_X"],const["WORLD"]["NUMCELLS_Y"],const["WORLD"]["MIN_FERTILITY"],const["WORLD"]["MAX_FERTILITY"])

worldVisual=show(world)
print(worldVisual)
plt.figure(2)
plt.imshow(worldVisual)
plt.savefig('Figure_1b.png', bbox_inches='tight')
plt.show()

world.growVegetob(const)