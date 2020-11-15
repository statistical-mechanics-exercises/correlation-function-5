import matplotlib.pyplot as plt

def correlation_function( spins, r ) :
  # Your code to calculate the average correlation between two spins separated by r
  # lattice sites go here.  The code in this function is going to be the same as the 
  # code that you wrote in the previous exercise.
  
  return 

# This is the microstate for which I would like you to compute 
# the correlation.
microstate = [1,1,-1,-1,-1,1,-1,1,1,-1]

# I have defined empty lists called correlation and rvalues here.
# You have to set these equal to lists as described in the intstructions on 
# the right
rvalues, correlation = [], []

# Your code to calculate the values inside rvalues and correlation goes here


# This plots the correlation function 
plt.plot( rvalues, correlation, 'ko')
plt.plot( rvalues, correlation, 'k-')
plt.savefig("correlation_function.png")
