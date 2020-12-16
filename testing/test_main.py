import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_correlation(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        average = sum(microstate) / len(microstate)
        nr = int( len(microstate)/2+1 )
        for i in range(nr) : 
            var, cor = 0, 0
            for j in range(len(microstate)) :
                var = var + ( microstate[j] - average )*( microstate[j] - average )
                cor = cor + ( microstate[j] - average )*( microstate[(j+i)%len(microstate)] - average )
            self.assertTrue( np.abs(this_y[i]-cor/var )<1e-8, "The values that you have computed for the correlation function are wrong" )
            
    def test_rvalues(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        nr = int( len(microstate)/2+1 )
        for i in range(nr) : self.assertTrue( np.abs(this_x[i]-i)<1e-8, "The r values at which you have computed the correlation function are wrong." )
        
    def test_npoints(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( (len(microstate)/2+1)==len(this_x), "You have calculated the correlation function for the wrong number of points." )
