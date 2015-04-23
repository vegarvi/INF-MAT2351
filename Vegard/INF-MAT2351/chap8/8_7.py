from matplotlib.pylab import *

def f(x):
	return exp(-x**2)

def g(x):
	return sin(exp(cos(x)))

# also added possibility to change interval and function f
def TrapRuleFourier(a,b,n,k,f): 
	I = 0.5*(f(0)*sin(k*pi*0)+f(1)*sin(k*pi*1))
	h = (b-a)/float(n)
	for i in range(1,n):
		I += f(a+i*h)*sin(k*pi*i*h)    # i*h = x_i
	I *= h
	
	return 2*I

def SimRuleFourier(a,b,n,k,f):
	I = f(0)*sin(k*pi*0)+f(1)*sin(k*pi*1)
	h = (b-a)/float(n)
	for i in range(1,n/2):
		x2j_1 = a+(2*i-1)*h
		I += 4*f(x2j_1)*sin(k*pi*x2j_1)
	for i in range(1,n/2-1):
		x2j = a+2*i*h
		I+= 2*f(x2j)*sin(k*pi*x2j)
	I *= h/3
	
	return 2*I

N = 400
K = 30	
u0 = zeros(N+1)
x = linspace(0,1,N+1)
for k in range(1,K):
	Ck = TrapRuleFourier(0,1,N+1,k,f)
	u0 += Ck*sin(k*pi*x)

t = 0.1
u = zeros(N+1)

for k in range(1,K):
	Ck = TrapRuleFourier(0,1,N+1,k,f)
	u += Ck*exp(-(k*pi)**2*t)*sin(k*pi*x)



plot(x,exp(-x**2),x,u0,x,u)
legend(['f(x)','u0','u(%.2f)'%t])
show()


