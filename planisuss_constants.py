# planisuss_constants.py
"""
Collection of the main constants defined for the "Planisuss" project.
"""

### World

NUMDAYS = 100000     # Length of the simulation in days
NUMERBAST=200
NUMCARVIZ=10
SIZE = 200      # size of the (square) grid (NUMCELLS x NUMCELLS)
GROWING = 0.3          # Vegetob density that grows per day.

#Creatures
MAX_ENERGY = 100     # maximum value of Energy
MAX_ENERGY_E = 50   # maximum value of Energy for Erbast
MAX_ENERGY_C = 100   # maximum value of Energy for Carviz

MAX_LIFE = 300     # maximum value of Lifetime                  |
MAX_LIFE_E = 200   # maximum value of Lifetime for Erbast       |-> will all be remodulated around a gaussian s.t. not everybody will have the same lifespan
MAX_LIFE_C = 150   # maximum value of Lifetime for Carviz       |

SPEED = 1            # speed of default creature
SPEED_E = 2          # speed of Erbasts
SPEED_C = 4          # speed of Carvizes
