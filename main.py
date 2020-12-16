import matplotlib.pyplot as plt

def correlation_function( spins, r ) :
  # Your code to calculate the average correlation between two spins separated by r
  # lattice sites go here.  The code in this function is going to be the same as the 
  # code that you wrote in the previous exercise.
  av2, var, average = 0, 0, sum(spins) / len(spins)
  for i in range(len(spins)) :
    av2 = av2 + (spins[i] - average)*(spins[(i+r)%len(spins)] - average )
    var = var + (spins[i] - average)*(spins[i] - average) 
  return av2 / var 

# This is the microstate for which I would like you to compute 
# the correlation.
microstate = [1,1,-1,-1,-1,1,-1,1,1,-1]

# I have defined empty lists called correlation and rvalues here.
# You have to set these equal to lists as described in the intstructions on 
# the right
rvalues, correlation = [], []

# Your code to calculate the values inside rvalues and correlation goes here
for r in range(6) : 
   rvalues.append(r)
   correlation.append( correlation_function( microstate, r ) )


# This plots the correlation function 
plt.plot( rvalues, correlation, 'ko')
plt.plot( rvalues, correlation, 'k-')
plt.savefig("correlation_function.png")
