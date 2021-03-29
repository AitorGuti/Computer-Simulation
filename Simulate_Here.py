# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:01:23 2021

@author: aitor
"""
#Import the Body class to make Celestial Bodies!
from Final_Project_Code import Body
#Import the Simulate class to run the Simulation!!!!!
from Final_Project_Code import Simulate

def main():
    
    #Gathers data from Body_Data folder. Check it out.
    inputdata = []
    with open("Body_Data.py", "r") as filein:
        for line in filein.readlines():
            if (not line.startswith("#")) and (not line.isspace()):
                inputdata.append(line.split())
    
    #Creates bodies from data given in Body_data. Try adding over there or make a body in this file!
    Body_list = []
    for i in inputdata:
        b = Body(float(i[1]), [float(i[2]), float(i[3])], [float(i[4]), float(i[5])], i[6], float(i[7]))
        Body_list.append(b)
        
    """
    Please add a body to the simulation here
    Step 1: Create a Body
        My_Body = Body(Mass in kg,
                       position as list [0, 0] x then y,
                       velocity as list [0, 0] x then y,)
                       Colour as string "Red",
                       Patch_size as integer 2e9 is a good starting point!)
    
    #Step 2: Add your body to the Body_list
        #Body_list.append(My_Body)
        
    #Step 3: Run the simulation!!!!!
    """
    
    Simulation = Simulate(Body_list,10000)    #Create Simulation Object with timestep length of 10000 seconds. Smaller length is more accurate but slower.
    Simulation.Display() #Runs the simulation
    
    #TPK = Simulation.Array_Energies(700)    #To create n by 5 array where columns represent Time, Tot energy, Pot energy, Kin energy, and Mars-Satellite distance in order. Also 700 is number of timesteps.
    #Simulation.Plot_Time_Total(TPK)  #To plot Total energy against time in days using TPK

    #df = pd.DataFrame(TPK)     #To create dataframe from the n by 5 array
    #df.to_csv("Total Energy vs Time.csv", index=False)    #To write dataframe as csv

main()
