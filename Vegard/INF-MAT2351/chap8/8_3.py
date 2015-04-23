from matplotlib.pylab import *


# Do integration by parts many times or use sympy
# /wolframalpha to find the Fourier coefficients
'''
import sympy as sp
x = sp.Symbol('x')
k = sp.Symbol('k',positive=True, integer=True)
C = 2*sp.integrate((x**2-x**3)*sp.sin(k*sp.pi*x),(x,0,1))
print C
C = sp.lambdify(k,C,'numpy')
'''
# With this code C is a python function as defined below

def C(k):
	return -4*(2*(-1)**k+1)/(pi*k)**3


N = 20
K = 50
u0 = zeros(N+1)
x = linspace(0,1,N+1)

T = 0.5    # Or change to T = 2

dx = 1./N
M = int(T/(0.5*dx**2)+10)     # ensures alhpa < 0.5
dt = float(T)/M
t = linspace(0,T,M+1)

dt = float(T)/M
dx = 1./N
print 'alpha = ', dt/dx**2


u = zeros((N+1,M+1))
u[:,0] = x**2-x**3

for l in range(M):
	for i in range(1,N):
		u[i,l+1] = u[i,l] + (dt/dx**2)*(u[i-1,l] - 2*u[i,l] + u[i+1,l]) 

	# boundary conditions (strictly not needed here because u is a matrix of zeros already)
	u[0,l+1] = u[N,l+1] = 0
	
		
	

def u_f(t,x,N):
	u = zeros(len(x))
	for k in range(1,K):
		u+= C(k)*exp(-(k*pi)**2*t)*sin(k*pi*x)
	
	return u

x_e = linspace(0,1,401)

plot(x_e,u_f(T,x_e,401),x,u[:,-1])
legend(['Fourier','Explicit'])
show()
