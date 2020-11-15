# Plotting the correlation function

We are now going to use what you have just learned to plot the degree of correlation between spins as a function of r.  To complete the exercise on the left you need to add the code that you have just written to the function called `correlation_function`. As in the previous exercise, this function takes two arguments:

1. `spins` - a list of spin variables that gives the coordinates for a particular microstate.
2. `r` - the distance between the spins that you would like to calculate the correlation between.

You will then notice that I have given you a list called `microstate`.  This list contains the values of the spin variables for a system of 10 spins.  Your task is to use your function, `correlation_function`, to calculate the degree of correlation for different values of `r`.  These values for the correlation function should be stored in a list called `correlation` so that the values for the correlation can be used in the commands that draw the graph of the correlation function at the end of the program.  

Notice that to draw this graph you also need to set the elements of a list called `rvalues`.  This list should contain the various values of r for which you calculated the value of the correlation function.  The smallest value of r you should use is 0.  Furthermore, the value of the correlation for r=0 should be 1 for obvious reasons.  You should then take all integer values of r up to and including the largest possible separation of spins that you can have in this system.  Remember that the spins are on a ring as this has an effect on how far apart the spins can be.   
