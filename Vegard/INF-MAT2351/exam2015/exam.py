import matplotlib.pylab as plt
from numpy import *

def e1():
	print 'Ex 1 \n'
	a = 1.0
	b = 1.2

	print '1a) Trapezoid approx:', (b-a)*0.5*(1.0/b+1.0/a)
	print 'log(1.2) = ', log(1.2)

	dt = 0.1

	y0 = 1

	y1 = y0*(1+dt/2.0)/(1-dt/2.0)
	print '\n1c) y1 = ',y1
	print '\n \n'	
	
#2)
def e2():
	print 'Ex 2 \n'
	y = array([2.556, 3.039, 3.706])


	dy50 = (y[1]-y[0])/10.0
	dy60 = (y[2]-y[0])/20.0
	dy70 = (y[2]-y[1])/10.0

	n = 3
	t = array([0,10,20])
	dy = array([dy50,dy60,dy70])

	# minimize: F(alpha) = sum((alpha*y - dy)**2)

	alpha = sum(dy)/sum(y)
	print 'Exp, growth: alpha = ',alpha
	f = lambda t: y[0]*exp(alpha*t)
	ti = linspace(0,20,201)

	plt.plot(t,y,'o',ti,f(ti))


	# Set: dy/y = alpha*(1-y/beta)
	# gamma = -alpha/beta
	# dy/y = gamma*y + alpha
	# minimize: F(alpha,beta) = sum((gamma*y + alpha - dy/y)**2)

	A = matrix([[n,sum(y)],[sum(y),sum(y*y)]])
	b = matrix([[sum(dy/y)],[sum(dy)]])
	alpha,gamma = linalg.solve(A,b)
	gamma,alpha = float(gamma),float(alpha)
	beta = -alpha/gamma
	print 'Log growth:'
	print 'alpha = ',alpha
	print 'beta = ', beta
	g = lambda t: (y[0]*beta)/(y[0]+exp(-alpha*t)*(beta-y[0]))
	plt.plot(ti,g(ti))
	plt.legend(['data','expo','logistic'],'upper left')
	plt.show()


#3)
import sympy as sp
def e3():	
	print 'Ex 3 \n'
	k = sp.Symbol('k',positive=True,integer=True)
	x = sp.Symbol('x')
	c = (2/pi)*sp.integrate(sp.cos(k*x)*x*x,(x,0,sp.pi))
	t = linspace(-pi,pi,50)
	F = 1/pi*sp.integrate(x*x,(x,0,sp.pi)) # This is c0
	print 'c0 = ', F
	for n in range(1,4):
		F+= c.subs(k,n)*cos(n*t)
	plt.plot(t,F,t,t**2)
	plt.show()

#4)
def e4():
	print 'Ex 4 \n'
	v0 = 1
	dt = 0.01	
	n = 1
	# Ma velge +- slik at vi sikrer v positiv for alle t
	for i in range(n):
		v1 = -0.5*(dt**(-1) - sqrt(dt**(-2)+4*v0*dt**(-1)))
		v0 = v1
	print 'v1 = ',v1

if __name__=='__main__':
	e1()
	e2()
	e3()
	e4()
	


