from numpy import *
from quadLSQ import quadLSQ

n = linspace(100,400,4)    #NOTE: n measured in thousands
CPU = array([0.05,0.09,0.13,0.18])

a,b = quadLSQ(n,CPU)

print 'Linear approximation: c(n) = %g + %g n '%(a,b)

def CPUtime(n):
	return a+b*n

print 'n = 10^6 --> estimated CPU time: %.2f '%CPUtime(10**6)
print 'n = 10^7 --> estimated CPU time: %.2f '%CPUtime(10**7)
