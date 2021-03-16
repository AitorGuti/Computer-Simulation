# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:55:52 2021

@author: aitor
"""

""" Project - Orbit of the inner planets: Sun, Mercury, Venus, Earth, Mars """


#Code should ask for
    #Number of timesteps, length of time step
    #mass of mars and phobos, and initial orbital radius

""" ALLOW US TO BEEEEEGIIIIIIIN """

import numpy as np
from numpy.linalg import norm
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.constants import G
from copy import deepcopy as dpcopy
import pandas as pd



class Body(object):
    
    #Initialise and define mass, position, and velocity.
    def __init__(self, mass, position, velocity, colour, patch_size):
        
        self.c = colour
        self.patch_size = patch_size
        self.m = mass
        self.r = np.array(position)
        self.v = np.array(velocity)
        self.an = np.array([0.,0.])
        self.ac = np.array([0.,0.])
        self.ap = np.array([0.,0.])
        self.KE = 0
        self.PE = 0
        
    
    #Update positions accelerations and velocities
    def Update(self, bods, ts):
        a = bods
        
        for i in a: #Update positions of objects
            i.r = i.r + i.v*ts + (1/6)*(4*i.ac-i.ap)*(ts**2)
        
        for i in range(len(a)): #Update new accelerations of objects
            c = a[0:i]+a[i+1:]
            Sum = np.array([0.,0.])
            for x in c:
                Sum += x.m/((norm(a[i].r-x.r)**3))*(a[i].r-x.r)
            a[i].an = -G*Sum
        
        for i in a: #Update velocities of all objects
            i.v = i.v + (1/6)*(2*i.an + 5*i.ac - i.ap)*ts
        
        for i in a: #Update all accelerations of objects
            i.ap = dpcopy(i.ac)
            i.ac = dpcopy(i.an)
            i.an = np.array([0,0])
        return a
    
    #Update KE of the planet
    def KE_up(self):
        self.KE = 0.5*self.m*(norm(self.v)**2)
    
    #Check orbital period
        
        
class Simulate(object):
    
    def __init__(self, bods, Frames, timelength):
        
        # Setup simulation parameters
        self.b = bods
        self.f = Frames
        self.tl = timelength
    
    #First instance of the animate object
    def init(self):
        return self.patches[0],
        
    #Update the bodies themselves
    def Opdate(self):
        self.b = self.b[0].Update(self.b, self.tl)

    #Update the positions of the circles on the plot
    def animate(self, i):
        self.Opdate()
        for i in range(len(self.patches)):
            self.patches[i].center = (self.b[i].r[0], self.b[i].r[1])

        return self.patches[0], self.patches[1], self.patches[2], self.patches[3], self.patches[4],

    #Creates patch list, makes the plot, and finally animates the plot
    def Display(self):
        # create list for patches
        self.patches = []
         
        # create patches to be animated and add to list
        for i in self.b:
            circ = plt.Circle((i.r[0], i.r[1]), i.patch_size,color=i.c, animated=True)
            self.patches.append(circ)
            
        # Create plot elements
        fig = plt.figure()
        ax = plt.axes()
        
        #add circles to axes
        for i in self.patches:
            ax.add_patch(i)
        
        #Scale and set limits of plot
        ax.axis("scaled")
        ax.set_xlim(-2.4*10**11,2.4*10**11)
        ax.set_ylim(-2.4*10**11,2.4*10**11)
        

        # animate the plot
        self.anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=self.f, interval=1, blit=True)
        plt.show()
        
    def Tot_E(self, N): #Finds Tot, P, and K energies and lists them. N is Number of timesteps
        
        #Empty list to contain time, total, potential, and kinetic. In order and repeating
        TPK = []
        
        #Loop N number of timelengths 
        for i in range(N):
            self.b = self.b[0].Update(self.b, self.tl)
            
            for k in self.b: #Update Kinetic Energy of all bodies
                k.KE_up()
            
            for f in range(len(self.b)): #Update Potential Energy of all bodies
                c = self.b[0:f]+self.b[f+1:]
                Summ = 0
                for x in c:
                    Summ += -0.5*G*x.m*self.b[f].m/(norm(self.b[f].r-x.r))
                self.b[f].PE = Summ

            Kinetic=0
            Potential=0
            
            for j in self.b: # Add up all Kinetic Energies and Potential Energies
                Kinetic += j.KE
                Potential += j.PE
            
            Total = Kinetic + Potential #Total Energy
            Time = float(i*self.tl/60/60/24) #Define Time passed up till this point
            
            TPK.append(Time)
            TPK.append(Total)
            TPK.append(Potential)
            TPK.append(Kinetic)
            
        TPK = np.array(TPK)
        TPK = np.reshape(TPK, (-1, 4))
        return TPK
    
    def Plot_E(self, listt):
        x = listt[1:,0]
        y1 = listt[1:,1]
        y2 = listt[1:,2]
        y3 = listt[1:,3]
    
        plt.scatter(x, y1, color = "blue", label = "Total E")
        #plt.scatter(x, y2, color = "brown", label = "Potential E")
        #plt.scatter(x, y3, color = "green", label = "Kinetic E")
    
        plt.title("Sum of the Potential and Kinetic Energies of Bodies in the Simulation of the Inner Solar System")
        plt.xlabel("Time / Days")
        plt.ylabel("Energy / Joules")
        plt.legend()
        
        plt.show()

def main():
    Sun     = Body(1.989*(10**30), [0.,0.], [0.,0.], "orange", 2*10**10)
    Mercury = Body(3.285*(10**23), [57909227000.,0.], [0.,47360], "grey", 10**9)
    Venus   = Body(4.8675*(10**24), [108209475000.,0.], [0.,35000.], "brown", 3*10**9)
    Earth   = Body(5.9724*(10**24), [149598262000.,0.], [0.,29780.], "Green", 3*10**9)
    Mars    = Body(6.4185*(10**23), [227943824000.,0.], [0.,24100.], "red", 2*10**9)
    
    Objs = [Sun, Mercury, Venus, Earth, Mars]
    
    Simulation = Simulate(Objs,300,3600)    #Create Simulation Object
    
    # Simulation.Display()
    
    TPK = Simulation.Tot_E(8766)    #To create n by 4 array where columns represent Time, Tot energy, Pot energy, Kin energy in order.
    Simulation.Plot_E(TPK)  #To plot Total energy against time in days
    
    # df = pd.DataFrame(TPK)     #To create dataframe from Time, tot, pot, kin
    #df.to_csv("THE_ARRAY.csv", index=False)    # To write dataframe as csv
    

main()


