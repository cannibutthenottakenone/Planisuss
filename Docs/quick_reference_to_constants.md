# Quick reference to constants
The program contains multiple parameters that can e modified to modify the behaviour of the simulation. Below is a comprehensive list of them.

## World

- NUMDAYS: Length of the simulation in days (default:100000)
- NUMCELLS_x: Number of columns of the (potentially non-square) grid (default:400)
- NUMCELLS_Y: Number of rows of the (potentially non-square) grid (default:400)
- GROWING: Vegetob density that grows per day. (default:1)
- MAX_FERTILITY: Maximum multiplier for vegetob growth (default:1.5)
- MIN_FERTILITY: Minimum multiplier for vegetob growth (default:0.5)

## Creatures
- NEIGHBORHOOD: Radius of the region that a social group can evaluate to decide the movement 1
- MAX_ENERGY: Maximum value of Energy (default:100)
- MAX_LIFE: Maximum value of Lifetime (default:10000)
- AGING: Energy lost each month (default:1)
### Erbast
- NEIGHBORHOOD_E: Radius of the region that a herd can evaluate to decide the movement 1 
- MAX_ENERGY_E: Maximum value of Energy for Erbast (default:100)
- MAX_LIFE_E: Maximum value of Lifetime for Erbast (default:10000)
- AGING_E: Energy lost each month for Erbast (default:1)
- MAX_HERD: Maximum numerosity of a herd (default:1000)
### Carviz
- NEIGHBORHOOD_C: Radius of the region that a pride can evaluate to decide the movement 1 
- MAX_ENERGY_C: Maximum value of Energy for Carviz (default:100)
- MAX_LIFE_C: Maximum value of Lifetime for Carviz (default:10000)
- AGING_C: Energy lost each month for Carviz (default:1)
- MAX_PRIDE: Maximum numerosity of a pride (default:100)