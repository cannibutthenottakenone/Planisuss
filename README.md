# Planisuss

> "Vegetob, Erbast, Carviz. Long ago, the three species lived together in harmony. Then, everything changed when the Carvizes attacked."

Welcome on planet planisuss, where three species live:
- Vegetob: the plants
- Erbast: the erbivores
- Carviz: the carnivores

The goal of this project is to simulate a simple ecosystem on an island where these three species live

## The world
### The geographical map
The map is a square (though it could easily be adapted to be rectangular) grid of SIZExSIZE pixels represented by a matrix.
It is procedurally generated using a combination of Perlin noise and a circular gradient. the obtained floating point result is split and remapped to -1 (the sea) and 0 (the island) using as separator the average value of the matrix.
### Fertility
A feature that i decided to implement is ground fertility; this feature has the effect of a different growth speed for the vegetobs in different locations on the island.
Vegetob $v$ growth for cell $(m,n)$,fertility map $m_f$ and global constant GROWING:
$$v[m,n]=v[m,n]+m_f[m,n]*\text{GROWING}$$
The fertility map $m_f$ is implemented through the pairwise multiplication of a new perlin noise map $p_f$ and the geographic map $m_g+1$
$$m_f[m,n]=p_f[m,n]*(m_g[m,n]+1)$$
This makes so that sea tiles always have 0 fertility.
### Vegetob (The plant)
Stored in a separate grid matrix $m_v$, they are initialized through a combination of the soil fertility and a random value $r\in[0,3)$.
$$m_v=mf*r$$
### Storing the creatures
The creatures objects are stored in the World class as well in classic python lists
