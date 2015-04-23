from matplotlib.pylab import *


N = 400
x = linspace(0,1,N+1)
u = zeros(N+1)
K = 100
T = 0.25

for k in range(1,K):
	# Ck = 2.0*(1-(-1)**k)/(pi*k)	# f(x) = 1
	Ck = (-1)**(k+1)/(k*pi)			# f(x) = x	
	u += Ck*sin(pi*k*x)


def u_f(t,x,N):				# Fourier version of u 
	u = zeros(len(x))
	for k in range(1,K):
		# Ck = 2.0*(1-(-1)**k)/(pi*k)	# f(x) = 1
		Ck = (-1)**(k+1)/(k*pi)			# f(x) = x	
		u+= Ck*exp(-(k*pi)**2*t)*sin(k*pi*x)
	
	return u


plot(x,u_f(T,x,N)) 
show()
