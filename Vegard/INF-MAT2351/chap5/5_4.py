from numpy import *

from quadLSQ import quadLSQ

n = array([65536*i for i in [1,2,4,8,16]])

Tn = array([0.048755, 0.097074, 0.194003, 0.386721, 0.771487])

a,b = quadLSQ(n,Tn)

print 'Linear approximation: T(n) = %g + %gn'%(a,b)

def T(n):
	return a+b*n


#b) Sending a vector of length 0 still takes time

#c) 

double = 64

print (double/b)*10**(-9)
