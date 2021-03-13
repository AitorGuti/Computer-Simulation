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
        
        self.m = mass
        self.r = np.array(position)
        self.v = np.array(velocity)
        self.an = np.array([0.,0.])
        self.ac = np.array([0.,0.])
        self.ap = np.array([0.,0.])
        
    
    #Update positions
    def Update(self, objs, ts):
        a = objs
        
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


def main():
    Sun     = Planet(1.989*(10**30), [0.,0.], [0.,0.], "orange")
    Mercury = Planet(3.285*(10**23), [57909227000.,0.], [0.,47360], "grey")
    Venus   = Planet(4.8675*(10**24), [0.,108209475000.], [-35000,0.], "yellow")
    Earth   = Planet(5.9724*(10**24), [-149598262000.,0.], [0.,-29780], "Green")
    Mars    = Planet(6.4185*(10**23), [0.,-227943824000.], [24100,0.], "red")
    
    Objs = [Sun, Mercury, Venus, Earth, Mars]
    
    Moved = Sun.Update(Objs, 10000000.)
    Movedd = Sun.Update(Moved, 1000.)
    Moveddd = Sun.Update(Movedd, 1000.)
    print(Moveddd[3].r)


main()
            
    #Update Velocities
    
    #Calculate Kinetic energy
    
    #Check orbital period
        
        
# class Simulate(object):
    
#     def __init__(self, b1, b2, Frames, timelength): #set b1 to b2 at end. *args for i in args
#         self.b1 = b1
#         self.b2 = b2
#         # setup simulation parameters
#         self.Frames = Frames
#         self.tl = timelength
        
#     def init(self):
#         return self.patches[1],
        
#     #Update the bodies themselves
#     def opdate(self):
#         self.b1.Update(self.b2, self.tl)
#         self.b2.Update(self.b1, self.tl)

#     #Update the positions of the circles on the plot
#     def animate(self, i):
#         self.opdate()
#         self.patches[0].center = (self.b1.r[0], self.b1.r[1])
#         self.patches[1].center = (self.b2.r[0],self.b2.r[1])
#         print(self.b1.Ke+self.b2.Ke)
#         return self.patches[0], self.patches[1],

#     def display(self):
#         # create list for circles
#         self.patches = []
         
#         # create circles to be animated and add to list
#         self.patch1 = plt.Circle((self.b1.r[0], self.b1.r[1]), 4000000, color="red", animated=True)
#         self.patch2 = plt.Circle((self.b2.r[0], self.b2.r[1]), 500000, color="blue", animated=True)
#         self.patches.append(self.patch1)
#         self.patches.append(self.patch2)
            
#         # Create plot elements
#         fig = plt.figure()
#         ax = plt.axes()
        
#         #add circles to axes
#         for i in range(0, len(self.patches)):
#             ax.add_patch(self.patches[i])
        
#         ax.axis("scaled")
#         ax.set_xlim(-10**7,10**7)
#         ax.set_ylim(-10**7,10**7)
        

#         # animate the plot
#         self.anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=self.Frames, interval=10, blit=True)
#         plt.show()
