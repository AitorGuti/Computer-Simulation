Aitor Gutierrez Valero s1945281

Inner Solar System Simulation Documentation

Class name: Body

    A class used to represent a Celestial Body
    ...
    
    Attributes
    ----------
    c : str
        Colour of the Planet as a String
    patch_size : integer
        The Radius of the Planet's Patch in meters
    m : float
        Mass of the planet in kg
    r : ndarray
        Position in meters as a 1 x 2 array
    v : ndarray
        Velocity in meters/second as a 1 x 2 array
    an : ndarray
        New timestep acceleration in meters/second^2 as a 1 x 2 array
    ac : ndarray
        Current timestep acceleration in meters/second^2 as a 1 x 2 array
    ap : ndarray
        Previous timestep acceleration in meters/second^2 as a 1 x 2 array
    KE : float
        Kinetic Energy of the body relative to stationary cartesian plane in Joules
    PE : float
        Potential Energy of the body relative to other bodies in Joules

    Methods
    -------
    Body(mass, position, velocity, colour, patch_size)
        Creates a body object. All arguments mandatory.

    self.Update(bods, ts)
        Updates all Bodies in bods list for 1 timestep of length ts in seconds
    
    self.KE_up()
        Updates the Kinetic Energy of a body.
    --------
	
    Body(mass, position, velocity, colour, patch_size):
    	Parameters
    	----------
    	mass : str
        	    Mass of the body in kg
            
        	position : 1x2 list of integers or floats
            	    Position of the body on cartesian plane in meters
        
        	velocity : 1x2 list of integers or floats
            	    Velocity of the body in meters/second
        
        	colour : str
            	    Colour of the planet
        
        	patch_size : integer
            	    Size of the patch on the cartesian plane
	----------

    self.Update(self, bods, ts):
        	Parameters
        	----------
        	bods : list
            	    List of Body objects
        
        	ts : integer
            	    Timestep length in seconds
        	----------





Class name: Simulate

    A class used to simulate Body positions in space
    ...
    
    Attributes
    ----------
    b : 1 x n list
        List of Bodies to be simulated
    tl : integer
        Length of timesteps for each update in seconds

    Utilised Methods
    -------
    Simulate(bods, timestep)
        Creates a Simulate object. Both arguments necessary

    self.Display()
        Continually animates Body movement at timestep length chosen until user termination
    
    self.Energy_Array(N)
        Uses simulate object and N number of timesteps to make a n x 5 array of floats with columns Time, Total E, Potential E, Kinetic E, Mars-Satellite Distance
    
    self.Plot_Time_Total(Energy_Array)
        Uses Energy_Array output to plot Time versus Total energy in the system
    -------

    Simulate(bods, timestep)
        	Parameters
        	----------
        	bods : list
            	    List of Body objects
        
        	timestep : integer
            	    Timestep length of each update in seconds
        	----------

    self.Energy_Array(N)
	Parameters
	----------
	N : Integer
	    Number of timesteps to collect data for
	----------

    self.Plot__Time_Total (Energy_Array)
	Parameters
	----------
	Energy_Array : Array
	    This parameter is the n x 5 array from the Energy_Array(N) method
