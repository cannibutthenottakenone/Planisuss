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

## The creatures

### MaxLife

In the constants file for each type of creature a MAX_LIFE value is specified, but this value is not a rigid wall at that kills creatures once their lifespan reaches it. When each new creature is created it acquires a maximum lifespan that is a calculated around MAX_LIFE using a gaussian function.
Specifically, to find the specific lifetime of the creature the following code is used:
```
self.maxLife= maxLife + randrange(-1,2,2) * min(50,sqrt(-72.24*log(random())))
```
where:
- `maxLife` is a parameter passed to the constructor which defaults to the creature's MAXLIFE constant
- `randrange(-1,2,2)` returns a number from the set $\{-1,1\}$ 
- `sqrt(-72.24*log(random()))` is the inverse function of the left wing of a Gaussian function with $a=1, b=0, c=6.01$ 
$$\text{Gaussian}: f(x)=\exp(-\frac{x^2}{72.24}); \text{ Inverse:} f^{-1}(x)=\sqrt{-72.24\ln(x)} x\in[0,1]$$
for the function $f^{-1}(x)$ we have that an input equal to 1 will return 0, which will assign the base parameter to the creature's life time, an input of 0.25 will have an effect of $\pm10$ on the lifetime while an $x\le0.0000000000000009$  will always have an effect of $\pm50$ days.

<p align="center">
  <img src="https://github.com/cannibutthenottakenone/Planisuss/assets/48643174/10f5c04e-3d55-4d88-85d2-9fd380943aea" alt="graph of f-1(x) created at https://www.desmos.com/calculator" />
</p>
