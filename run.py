import numpy as np
from random import randint

import matplotlib.pyplot as plt
from matplotlib.figure import SubFigure
from matplotlib.widgets import Button
from matplotlib.axes import Axes

from world import World
from Creatures.creature import Creature
from Creatures.erbast import Erbast

from planisuss_constants import NUMDAYS

def update():
    world.growVegetob()    
    
    for i in range(len(world.erbasts)-1,0,-1):
        if np.array_equal(world.erbasts[i].position, np.array([-1,-1])):
            del world.erbasts[i]
    
    for erbast in world.erbasts:
        movement=erbast.pickMovement(world.vegetob)
        if np.array_equal(movement, np.zeros(2)):
            erbast.eat(world.vegetob)
        else:
            erbast.movement(movement)
            
        erbast.older()
            
                            
def updateVis():
    #computation of rendering matrix
    renderMatrix=world.geography
    
    if show["vegetob"]:
        renderMatrix=renderMatrix+world.vegetob
    
    if show["erbast"]:
        erbastMatrix=np.zeros(world.geography.shape)
        for e in world.erbasts:
            erbastMatrix[e.position[0],e.position[1]]=15
        renderMatrix+=erbastMatrix
        
    im = sbplt1.imshow(renderMatrix)
    im.set_data(renderMatrix) 
    
    tags = ["Erbast", "Carviz"]
    numbers = [len(world.erbasts),0]    
    sbplt2.bar(tags, numbers)
    

if __name__ == "__main__":
    world = World()
    
    #variable keeping track of what to show
    show={
        "vegetob": True,
        "erbast": True
    }
    
    #initialization of window
    plt.ion()
    fig = plt.figure(figsize=(17, 10), facecolor="black")
    fig.canvas.manager.set_window_title('Planisuss')
    fig0,fig1=fig.subfigures(1,2,width_ratios=[2/3,1/3]);   fig0:SubFigure; fig1:SubFigure
    
    fig0.set_facecolor("turquoise")
    fig0.suptitle("Map",fontsize="xx-large")
    
    sbplt1=fig0.add_axes((0.05,0.05,0.90,0.85))
    sbplt1.tick_params(colors=(0, 0, 0, 0 ))
    sbplt1.set_autoscale_on(True)

    fig1.suptitle("Graphs",fontsize="xx-large",color=(1,1,1,1))

    sbplt2,sbplt3=fig1.subplots(2,1);   sbplt2:Axes; sbplt3: Axes
    sbplt2.set_facecolor((0.09,0.09,0.09,1))
    sbplt2.tick_params(colors="white")
    sbplt2.title.set_color("white")
    sbplt2.set_xlabel("Creatures")
    sbplt2.set_ylabel("")
    sbplt2.set_title("Population of Species")
    sbplt3.set_facecolor((0.09,0.09,0.09,1))
    sbplt3.tick_params(colors="white")
    sbplt3.title.set_color("white")
    
    pauseAx = fig0.add_axes([0.3, 0.005, 0.10, 0.04])
    vegetobAx = fig0.add_axes([0.4, 0.005, 0.10, 0.04])
    erbastAx = fig0.add_axes([0.5, 0.005, 0.10, 0.04])
    carvizAx = fig0.add_axes([0.6, 0.005, 0.10, 0.04])
    
    pauseButton = Button(pauseAx, "Pause", hovercolor="0.975")
    vegetobButton = Button(vegetobAx, "Vegetob", hovercolor="0.975")
    erbastButton = Button(erbastAx, "Erbast", hovercolor="0.975")
    carvizButton = Button(carvizAx, "Carviz", hovercolor="0.975")
    
    plt.show()
    
    day=0
    while day<NUMDAYS:
        print("day:",day)
        update()
        updateVis()
        day+=1
        plt.pause(0.1)
        
