from Helpers.planisuss_constants import constants, import_constants
from World import world as worldm
from Rendering.show import show
import matplotlib.pyplot as plt

import_constants()

world=worldm.World(5000,5000)

worldVisual=show(world)
print(worldVisual)
plt.figure(2)
plt.imshow(worldVisual)
plt.savefig('Figure_1b.png', bbox_inches='tight')
plt.show()