from numpy import *
import matplotlib.pylab as plt

# Want to minimize integral of (a-y(t))^2 dt
# Derivation p. 176, formula 5.109 gives

# a)

def y1(t):
	return 1 + 0.01*sin(t)
def Y1(a,b):
	return (b-0.01*cos(b)) - (a-0.01*cos(a))


# b)

def y2(t):	
	return exp(t)

def Y2(a,b):
	return exp(b)-exp(a)

# c)

def y3(t):
	return sqrt(t)
def Y3(a,b):
	return (2.0/3)*b**(3.0/2) - (2.0/3)*a**(3.0/2)

a1 = (1.0/pi)*Y1(0,pi)
a2 = exp(1)*Y2(0,exp(-1))
a3 = (1.0/pi)*Y3(0,pi)

print 'a1 = %.3f,  a2 = %.3f,  a3 = %.3f' %(a1,a2,a3)

t1 = linspace(0.01,pi,101)
t2 = linspace(0,exp(-1),101)

plt.subplot(1,3,1)
plt.plot(t1,y1(t1),[0,pi],[a1,a1])
plt.subplot(1,3,2)
plt.plot(t2,y2(t2),[0,exp(-1)],[a2,a2])
plt.subplot(1,3,3)
plt.plot(t1,y3(t1),[0,pi],[a3,a3])
plt.show()

