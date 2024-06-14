import numpy as np

import matplotlib.pyplot as plt
from matplotlib.figure import SubFigure
from matplotlib.widgets import Button
from matplotlib.axes import Axes

from Creatures.erbast import Erbast
from Creatures.carviz import Carviz

class Render():
    
    def __init__(self):
        self.show={ #variable keeping track of what to show
        "vegetob": True,
        "erbast": True,
        "carviz": True
        }
        self.paused=False
        
        #initialization of window
        plt.ion()
        self.fig = plt.figure(figsize=(17, 10), facecolor="black")
        self.fig.canvas.manager.set_window_title('Planisuss')
        self.fig0,self.fig1=self.fig.subfigures(1,2,width_ratios=[2/3,1/3]);   self.fig0:SubFigure; self.fig1:SubFigure
        
        self.fig0.set_facecolor("turquoise")
        self.fig0.suptitle("Map",fontsize="xx-large")
        
        self.sbplt1=self.fig0.add_axes((0.05,0.05,0.90,0.85))
        self.sbplt1.tick_params(colors=(0, 0, 0, 0 ))
        self.sbplt1.set_autoscale_on(True)
           

        self.fig1.suptitle("Graphs",fontsize="xx-large",color=(1,1,1,1))

        self.sbplt2,self.sbplt3=self.fig1.subplots(2,1);   self.sbplt2:Axes; self.sbplt3: Axes
        self.sbplt2.set_facecolor((0.09,0.09,0.09,1))
        self.sbplt2.tick_params(colors="white")
        self.sbplt2.title.set_color("white")
        self.sbplt2.set_xlabel("Creatures")
        self.sbplt2.set_ylabel("")
        self.sbplt2.set_title("Population of Species")
        
        self.sbplt3.set_facecolor((0.09,0.09,0.09,1))
        self.sbplt3.tick_params(colors="white")
        self.sbplt3.title.set_color("white")
        
        self.pauseAx = self.fig0.add_axes([0.3, 0.005, 0.10, 0.04])
        self.vegetobAx = self.fig0.add_axes([0.4, 0.005, 0.10, 0.04])
        self.erbastAx = self.fig0.add_axes([0.5, 0.005, 0.10, 0.04])
        self.carvizAx = self.fig0.add_axes([0.6, 0.005, 0.10, 0.04])
        
        self.pauseButton = Button(self.pauseAx, "Pause")
        self.pauseButton.on_clicked(self.togglePause)
        self.vegetobButton = Button(self.vegetobAx, "Vegetob")
        self.vegetobButton.on_clicked( lambda e: self.toggleShow(e,"vegetob") )
        self.erbastButton = Button(self.erbastAx, "Erbast")
        self.erbastButton.on_clicked( lambda e: self.toggleShow(e,"erbast") )
        self.carvizButton = Button(self.carvizAx, "Carviz")
        self.carvizButton.on_clicked( lambda e: self.toggleShow(e,"carviz") )

        plt.show()
        
    def togglePause(self,event): 
        self.paused = not self.paused
        
    def toggleShow(self,event, element):
        self.show[element]=not self.show[element]
        
    def linearVegetobColor(self, x:float):
        """
        A function of the vegetob density of one cell to the corresponding rgb value
        """    
        return np.array([0.009*x+0.39,0.077*x+0.21,0])
    
    def updateVis(self,text: str, world, popHistory):
        #computation of rendering matrix
        renderMatrix=np.zeros((world.geography.shape[0], world.geography.shape[1], 3))
        
        #rendering of geography and vegetob
        for i in range(world.geography.shape[0]):
            for j in range(world.geography.shape[1]):
                if world.geography[i][j] == -1:
                    renderMatrix[i][j]=np.array([0.25,0.87,0.81])
                elif self.show["vegetob"]:
                    renderMatrix[i][j]= self.linearVegetobColor(world.vegetob[i][j])
                else:
                    renderMatrix[i][j]=np.array([0.39,0.21,0])              
            
        if self.show["erbast"]:
            for e in Erbast.population:
                renderMatrix[e.position[0],e.position[1]]=[1,1,1]
            
        
        if self.show["carviz"]:
            for e in Carviz.population:
                renderMatrix[e.position[0],e.position[1]]=[1,0,0]
        
        self.sbplt1.clear() 
        im = self.sbplt1.imshow(renderMatrix)
        self.sbplt1.set_title(text, loc="center")

        #bar chart        
        self.sbplt2.clear()
        numbers = [len(Erbast.population),len(Carviz.population)]    
        self.sbplt2.bar(["Erbast", "Carviz"], numbers, color=["white", "red"])
        
        #line chart
        self.sbplt3.clear()
        self.sbplt3.plot( popHistory[0], color="white")
        self.sbplt3.plot(popHistory[1], color="red")
        