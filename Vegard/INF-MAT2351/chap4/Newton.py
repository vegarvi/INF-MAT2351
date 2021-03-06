from matplotlib.pylab import *

def Newton(f,df,x0,iterations,tol=1E-12):
	k = 0
	error = f(x0)
	print 'x0 = %g' %x0
	x1 = x0
	while k < iterations and abs(error) > tol:
		x1 = x0 - f(x0)/float(df(x0))
		x0 = x1
		k+=1
		error = f(x1)
		print 'x%d = %g  f(x%d) = %g' %(k,x1,k,f(x1))
	return x1
