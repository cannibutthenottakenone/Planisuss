import numpy as np
from world import World
import matplotlib.pyplot as plt
from matplotlib.figure import SubFigure
from matplotlib.widgets import Button

if __name__ == "__main__":
    world = World()
    
    fig = plt.figure(figsize=(17, 10), facecolor="black")
    fig.canvas.manager.set_window_title('Planisuss')
    fig0,fig1=fig.subfigures(1,2,width_ratios=[2/3,1/3]);   fig0:SubFigure; fig1:SubFigure
    
    fig0.set_facecolor("turquoise")
    fig0.suptitle("Map",fontsize="xx-large")
    
    sbplt1=fig0.add_axes((0.05,0.05,0.90,0.85))
    sbplt1.tick_params(colors=(0, 0, 0, 0 ))
    sbplt1.set_autoscale_on(True)

    fig1.suptitle("Graphs",fontsize="xx-large",color=(1,1,1,1))
    sbplt2,sbplt3=fig1.subplots(2,1)
    sbplt2.set_facecolor((0.09,0.09,0.09,1))
    sbplt2.tick_params(colors="white")
    sbplt2.title.set_color("white")
    sbplt3.set_facecolor((0.09,0.09,0.09,1))
    sbplt3.tick_params(colors="white")
    sbplt3.title.set_color("white")
    
    im = sbplt1.imshow(world.geography)
    im.set_data(world.geography)
    
    pauseAx = fig0.add_axes([0.3, 0.005, 0.10, 0.04])
    vegetobAx = fig0.add_axes([0.4, 0.005, 0.10, 0.04])
    erbastAx = fig0.add_axes([0.5, 0.005, 0.10, 0.04])
    carvizAx = fig0.add_axes([0.6, 0.005, 0.10, 0.04])
    
    pauseButton = Button(pauseAx, "Pause", hovercolor="0.975")
    vegetobButton = Button(vegetobAx, "Vegetob", hovercolor="0.975")
    erbastButton = Button(erbastAx, "Erbast", hovercolor="0.975")
    carvizButton = Button(carvizAx, "Carviz", hovercolor="0.975")
    
    plt.show()