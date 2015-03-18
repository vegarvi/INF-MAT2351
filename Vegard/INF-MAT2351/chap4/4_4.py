from matplotlib.pylab import *
# 4_4 done by hand, extra task: implement Newton for 2D systems

def Newton2D(F,J,x0,iterations,tol):
	k = 0
	eps = sum(abs(F(x0)))
	print 'x0 = ',x0
	while k < iterations and abs(eps) > tol:
		J_ = inv(J(x0))
		F1 = F(x0)
		dx = -J_*F(x0)
		x1 = x0 + dx
		eps = sum(abs(F(x1)))
		k+=1
		print 'x%d = ' %k, x1
		x0 = x1
	return x1
	

def f(x,y):
	return exp(y) - x - 1
def dfx(x,y):
	return -1
def dfy(x,y):
	return exp(y)

def g(x,y):
	return x**2 - y
def dgx(x,y):
	return 2*x
def dgy(x,y):
	return -1


def F(x):
	y = x[1,0]
	x = x[0,0]
	return matrix([[f(x,y)],[g(x,y)]])

def J(x):
	y = x[1,0]
	x = x[0,0]
	return matrix([[dfx(x,y),dfy(x,y)],[dgx(x,y),dgy(x,y)]])

x0 = matrix([[0.5],[0.5]])
x4 = Newton2D(F,J,x0,4,0)

print 'F(x4) = ', F(x4)

