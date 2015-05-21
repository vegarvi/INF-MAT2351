from numpy import *
import matplotlib.pylab as plt
from quadLSQ import quadLSQ

#Linear function, derivation p. 162, equation 5.58 p. 163.

t = linspace(1,5,5)
y = array([55.2, 44.9, 37.9, 35.3, 30.1])


alpha,beta = quadLSQ(t,y)
print 'Linear approximation: y = %.2f %.2ft' %(alpha,beta)

def linear(t):
	return alpha + beta*t

# c)
z = log(y)

# d)
gamma,beta2 = quadLSQ(t,z)
alpha2 = exp(gamma)
print 'Exp approximation: y = %.2f exp(%.2ft)' %(alpha2,beta2)
def expLS(t):
	return alpha2*exp(beta2*t)

T = linspace(1,5,501)

plt.plot(t,y,'o',T,linear(T),T,expLS(T))
plt.legend(['data','app 1','app2'])
plt.show()

