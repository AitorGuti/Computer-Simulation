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



class Planet(object):
    
    #Initialise and define mass, position, and velocity.
    def __init__(self, mass, position, velocity):
        self.G = G
        
        self.m = mass
        self.r = np.array(position)
        self.v = np.array(velocity)
        self.a = [0,0]
        
        self.Ke = 0.5*self.m*(norm(self.v)**2)
    
    #Update 2 bodies for 1 timestep
    def Update(self, b2, timelength):
        G = 6.6743*(10**-11)
        
        self.a = -G*b2.m/((norm(self.r-b2.r))**3)*(self.r-b2.r)   #Update Acceleration of self
        b2.a = -G*self.m/((norm(b2.r-self.r))**3)*(b2.r-self.r)   #Update Acceleration of Body 2
        
        self.v = self.v + self.a*timelength   #Update Velocity of self
        b2.v = b2.v + b2.a*timelength         #Update Velocity of Body 2
        
        self.r = self.r + self.v*timelength   #Update Position of self
        b2.r = b2.r + b2.v*timelength         #Update Position of Body 2
        
        self.Ke = 0.5*self.m*(self.v**2)    #Update Kinetic Energy of self
        b2.Ke = 0.5*b2.m*(b2.v**2)          #Update Kinetic Energy of body 2
        
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

def main():
    Sun     = Planet(1.989*(10**30), [0,0], [0,0])
    Mercury = Planet(3.285*(10**23), [0,0], [0,0])
    Earth   = planet()
    Mars    = Planet(6.4185*(10**23), [0,0], [0,0])

#WHAT'S UP BITCHES
    

main()