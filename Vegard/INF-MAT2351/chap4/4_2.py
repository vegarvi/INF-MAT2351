from matplotlib.pylab import *
from Newton import Newton

g = lambda x: x - sin(x)
dg = lambda x: 1 - cos(x)

h = lambda x: 1 - cos(x)
dh = lambda x: sin(x)


# list of functions
# if more functions were needed this would be faster
# than calling Newton for all of them separately
pairs = [[g,dg],[h,dh]]

for pair in pairs:
	x0 = 1			# initial guess
	y = pair[0]
	dy = pair[1]
	x4 = Newton(y,dy,x0,4,tol=1E-18)
	print 'f(x4) = %g' %y(x4)

