from matplotlib.pylab import *


n = 11
m = 201

u = zeros((n,m))

T = 1.0
L = 1.0
t = linspace(0,T,m)
x = linspace(0,L,n)

dt = t[1]-t[0]
dx = x[1]-x[0]

print dt/dx**2

a = 5.0
b = 4.0
c = 3.0

u0 = a*x + b*t[0] + c
u[:,0] = u0

for l in range(m-1):
	for i in range(1,n-1):
		u[i,l+1] = u[i,l] + (dt/(dx**2))*(u[i+1,l]-2*u[i,l]+u[i-1,l]) + dt*b
	
	u[0,l+1] = b*t[l+1] + c
	u[n-1,l+1] = a*L + c + b*t[l+1]

plot(x,u[:,m-1],x,(a*x + b*t[m-1] + c))
show()



