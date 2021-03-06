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

print dt/dx**2    # must be less than or equal to 0.5

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


print (a*x + b*t[-1] + c) - u[:,-1]


# example of surface plot
X,T = meshgrid(x,t)
u = transpose(u)	# check shape of X,T and u. (Must be the same)

from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = fig.add_subplot(111,projection='3d')
surf = ax.plot_surface(X,T,u)
show()




