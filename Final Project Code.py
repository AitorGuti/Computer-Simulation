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



class Planet(object):
    
    #Initialise and define mass, position, and velocity.
    def __init__(self, mass, position, velocity, colour):
        
        self.c = colour
        self.m = mass
        self.r = np.array(position)
        self.v = np.array(velocity)
        self.an = np.array([0.,0.])
        self.ac = np.array([0.,0.])
        self.ap = np.array([0.,0.])
        self.KE = 0.5*self.m*(norm(self.v)**2)
        
    
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
    def KE(self):
        self.KE = 0.5*self.m*(norm(self.v)**2)
    
    #Check orbital period
        
        
class Simulate(object):
    
    def __init__(self, bods, Frames, timelength):
        
        # Setup simulation parameters
        self.b = bods
        self.f = Frames
        self.tl = timelength
        
    def init(self):
        return self.patches[4],
        
    #Update the bodies themselves
    def Opdate(self):
        self.b = self.b[0].Update(self.b, self.tl)

    #Update the positions of the circles on the plot
    def animate(self, i):
        self.Opdate()
        for i in range(len(self.patches)):
            self.patches[i].center = (self.b[i].r[0], self.b[i].r[1])

        return self.patches[0], self.patches[1], self.patches[2], self.patches[3], self.patches[4],

    def Display(self):
        # create list for circles
        self.patches = []
         
        # create circles to be animated and add to list
        for i in self.b:
            circ = plt.Circle((i.r[0], i.r[1]), 40000, color=i.c, animated=True)
            self.patches.append(circ)
            
        # Create plot elements
        fig = plt.figure()
        ax = plt.axes()
        
        #add circles to axes
        for i in self.patches:
            ax.add_patch(i)
        
        ax.axis("scaled")
        ax.set_xlim(-3**11,3**11)
        ax.set_ylim(-3**11,3**11)
        

        # animate the plot
        self.anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=self.f, interval=10, blit=True)
        plt.show()

def main():
    Sun     = Planet(1.989*(10**30), [0.,0.], [0.,0.], "orange")
    Mercury = Planet(3.285*(10**23), [57909227000.,0.], [0.,47360], "grey")
    Venus   = Planet(4.8675*(10**24), [0.,108209475000.], [-35000,0.], "yellow")
    Earth   = Planet(5.9724*(10**24), [-149598262000.,0.], [0.,-29780], "Green")
    Mars    = Planet(6.4185*(10**23), [0.,-227943824000.], [24100,0.], "red")
    
    Objs = [Sun, Mercury, Venus, Earth, Mars]
    
    Simulation = Simulate(Objs, 300, 1000)
    Simulation.Display()

main()