# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:01:23 2021

@author: aitor
"""
from Final_Project_Code import Body
from Final_Project_Code import Simulate

def main():
    
    inputdata = []
    with open("Body_Data.py", "r") as filein:
        for line in filein.readlines():
            if (not line.startswith("#")) and (not line.isspace()):
                inputdata.append(line.split())
    
    Body_list = []
    for i in inputdata:
        b = Body(float(i[1]), [float(i[2]), float(i[3])], [float(i[4]), float(i[5])], i[6], float(i[7]))
        Body_list.append(b)
        
    #Please add a body to the simulation here
    
    Simulation = Simulate(Body_list,10000)    #Create Simulation Object with timestep of 10000
    Simulation.Display()
    
    #TPK = Simulation.Array_Energies(700)    #To create n by 5 array where columns represent Time, Tot energy, Pot energy, Kin energy, and Mars-Sat in order.
    #Simulation.Plot_Time_Total(TPK)  #To plot Total energy against time in days
    #df = pd.DataFrame(TPK)     #To create dataframe from the n by 5 array
    #df.to_csv("Total Energy vs Time.csv", index=False)    # To write dataframe as csv

main()
