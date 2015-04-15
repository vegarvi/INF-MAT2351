from diffusion import *

def I(x):
	return ones(len(x))

def D0(t):
	return 0

def D1(t):
	return 1

def N0(t):
	return 0

def N1(t):
	return sin(20*pi*t)

k = 10

L = 1
T = 4

dx = 0.1
dt = 0.0005

def f(x,t):
	return x

u = diffusion7_12(I,D0,D1,k,f,L,T,dx,dt,show_plot=False)
print u[len(u)/2]
plot(u)
show()

T = 0.2
u2 = diffusion7_13(I,N0,N1,k,f,L,T,dx,dt,show_plot=True)
