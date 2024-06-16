# Planisuss

> "Vegetob, Erbast, Carviz. Long ago, the three species lived together in harmony. Then, everything changed when the Carvizes attacked."

Welcome on planet planisuss, where three species live:
- Vegetob: the plants
- Erbast: the erbivores
- Carviz: the carnivores

The goal of this project is the simulation and the visualization of a simple ecosystem on an randomly generated island where these three species live.
## Behaviors
While the vegetob can only grow of a different amount based on the ground fertility, the other two species have a more complex behaviour.
### The day of an Erbast
- decide the movement: based on the available food at the creature's location and on the surrounding cells the erbast will decide if it wants to stay in its position or if it wants to move towards a better one.
- graze: if it didn't move the erbast will graze the vegetobs at its location reducing their density by 1.5 and gaining 1 energy
- age: the erbast will increase its age value by one
- breed: the erbasts that reached their maximum age will die splitting into two new erbasts. The sum of the energies of these new erbasts will be equal to the parent's.

### The day of a Carviz
- pick a target: if the carviz doesn't have a target erbast to hunt the closest one will be selected
- pick an action:
	- hunt: if the carviz's energy is lower than double its speed, it will hunt its target to acquire five sixths of its energy
	- stalk: if the target has moved too far follow it
	- nap: if the carviz is not hungry and the target is close enough the carviz will nap
- age and breed in an equal way to erbasts

## Visualization
To allow for a simple and understandable visualization of the simulation the library Matplotlib was used. Through its application the program generates a window which is split in two figures: the map visualization on the left and the graph visualization on the right.
The map visualization shows the simulated world and the creatures roaming it as if in a video game with pixel colors representing the sea, the land and the species on it.
The graph view shows two plots on which the population size and the population size history are shown, though they could be adapted to illustrate any other data from the simulation.

## Implementation
### The world
#### The geographical map
The map is a square (though it could easily be adapted to be rectangular) grid of SIZExSIZE pixels represented by a matrix.
It is procedurally generated using a combination of Perlin noise and a circular gradient. The obtained floating point result is split around the mean of all values and remapped to -1 (the sea) and 0 (the island).
#### Fertility
A feature that I decided to implement is ground fertility; this has the effect of a different growth speed for the vegetobs in different locations of the island.
Vegetob $v$ growth for cell $(m,n)$,fertility map $m_f$ and global constant GROWING:
$$v[m,n]=v[m,n]+m_f[m,n]*\text{GROWING}$$
The fertility map $m_f$ is implemented through the pairwise multiplication of a new Perlin noise map $p_f$ and the geographic map $m_g+1$

$$m_f[m,n]=p_f[m,n]*(m_g[m,n]+1)$$
This makes so that sea tiles always have 0 fertility.
#### Vegetob (The plant)
Stored in a separate grid matrix $m_v$, they are initialized through a combination of the soil fertility and a random value $r\in[0,3)$.
$$m_v[m,n]=mf[m,n]*r$$

### The creatures
#### General
Each species is implemented through its own class, child of  the Creature class.
Each creature implements the attributes:
- position: a numpy one dimensional array of size 2 containing the coordinates of the creature
- energy: the amount of energy the creature possesses;
- maxLife: the creature max life in days, once this age is reached the creature spawns its progeny and dies. It will be better described in the next paragraph;
- speed: the maximum amount of cells the creature can reach in one turn (diagonal motion is considered to be as long as orthogonal motion);
- age: the creature's age;
- dead: a boolean attribute specifying if the creature is dead;
and the methods:
- movement: moves the creature by a movement vector $(\Delta x,\Delta y)$ and reduces the creature energy by the distance traveled;
- pickMovement: overridden by each subclass, locates the next cell to which the creature will move;
- older: increases the creature age and call for breed and die when it's the time
- die: sets the creature to be dead;
- breed: creates the creature's progeny and adds it to the population list. The first child will have a percentage p of the parent's energy while the second will have a percentage 1-p.
Other than the above attributes and methods a class variable 'population' and a class method 'populateCreature' are implemented. The former is a list containing all living members of the species, the latter is called in the beginning of the simulation to spawn the requested entities.
##### MaxLife

In the constants file for each type of creature a MAX_LIFE value is specified, but this value is not a rigid wall that kills creatures once their lifespan reaches it. When each new creature is created it acquires a maximum lifespan that is a calculated around MAX_LIFE using a gaussian function.
Specifically, to find the specific lifetime of the creature the following code is used:
```
self.maxLife= maxLife + randrange(-1,2,2) * min(50,sqrt(-72.24*log(random())))
```
where:
- `maxLife` is a parameter passed to the constructor which defaults to the creature's MAXLIFE constant
- `randrange(-1,2,2)` returns a number from the set $\{-1,1\}$ 
- `sqrt(-72.24*log(random()))` is the inverse function of the left wing of a Gaussian function with $a=1, b=0, c=6.01$ 
$$\text{Gaussian}: f(x)=\exp(-\frac{x^2}{72.24}); \text{ Inverse:} f^{-1}(x)=\sqrt{-72.24\ln(x)} x\in[0,1]$$
for the function $f^{-1}(x)$ we have that an input equal to 1 will return 0, which will assign the base parameter to the creature's life time, an input of 0.25 will have an effect of $\pm10$ on the lifetime while an $x\le0.9*10^{-15}$ will always have an effect of $\pm50$ days.

<p align="center">
  <img src="https://github.com/cannibutthenottakenone/Planisuss/assets/48643174/10f5c04e-3d55-4d88-85d2-9fd380943aea" alt="graph of f-1(x) created at https://www.desmos.com/calculator" />
</p>

#### Erbasts
The only methods that tell the Erbast apart from the Creature class are eat and pickMovement.
- eat: this method will reduce the vegetobs density corresponding with the erbast position by 1.5 and increase the erbast energy by 1 or, if it is necessary to avoid exceding the MAX_ENERGY_E constant, by less
- pickMovement: based on the current occupied cell and a random probability, the erbast will decide to move or stay still. If it decided to move the best cell within range will be selected and a movement vector towards it will be returned.

#### Carviz
Carvized have a slightly more complex behaviour which translates in a slightly more complex implementation of their class. For each of their possible actions a different method is implemented together with a method to choose a new target and a method to calculate the vector movement to reach said target.
- pickTarget: iterates through the erbast population vector and picks the closest one as target
- stalk: moves the carviz towards its prey
- hunt: if the target is within reach (distance<carviz.speed) it will be killed and the carviz will gain the five sixth of its energy.
- nap: the erbast will nap in this turn losing only 0.5 energy
- getDirection: will compute the movement to reach the target, if this movement vector would place the carviz in a water cell a new random movement vector that wouldn't is returned

### The Render class
The Render class has the purpose of handling the visualization of the simulation through the library Matplotlib.
To accomplish this it divides a figure into two subfigures, the first will handle the map visualization on the left and the second the graph visualization on the right.
The map visualization uses the imshow function to display a renderMatrix of dimensions nxnx3 where the third dimension is used to store the rgb values that compose the pixels of the image.
The graph subfigure is divided in two subplots, each displaying a different graph.

## Results
The final simulation works and follows all the rules specified in the program. The main problems seem to be related to the balance between the vegetob quantity, the erbasts and the carviz strength.
This leads often either to an extinction of the erbasts or to an explosion in their population and rarely to an equilibrum.

Another problem is the creation of multiple islands due to the random nature of Perlin noise.

## Possible future features 
Among the multitude of possible features that could be implemented in the future there is the ability of the carvizes to track down their prey instead of just knowing where it is. The tracking system could be implemented through the creation of a new object (the track itself) or through the recognition of a direction in the eaten erbasts. 
Another possible feature could be the ability of the erbasts to run away from the carvizes, this could happen either in general, i.e. when a carviz is near, or when a erbast is actively being hunted.

## References  
**Libraries used**
- [numpy](https://numpy.org/): for array and matrix storing and calculations, it is also a dependency of matplotlib
- [matplotlib](https://matplotlib.org/): for the visualization
- [perlin_noise](https://github.com/salaxieb/perlin_noise): for the random world generation

**Theoretical help**
- [Wikipedia](https://en.wikipedia.org/):
	- [perlin noise](https://en.wikipedia.org/wiki/Perlin_noise)
	- [gaussian function](https://en.wikipedia.org/wiki/Gaussian_function)
	- [Wa-Tor](https://en.wikipedia.org/wiki/Wa-Tor)
 
**Tools used**
- [Desmos graphical representation](https://www.desmos.com/calculator): to better understand graphs such as the gaussian
- [Wolfram Alpha](https://www.wolframalpha.com/): to check my calculations and matrix operations
- [ChatGPT](https://chat.openai.com/): to ask for explanations about some concepts used in the project

**Documentations**  
other than the specific documentations for the libraries listed above  
- [W3Schools](https://www.w3schools.com/python)
- [official python documentation](https://docs.python.org/3/)

**Special thanks** go to [Stack Overflow](https://stackoverflow.com/) for being any coder greatest ally since 2008
