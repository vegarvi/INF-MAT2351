from numpy import *

def schemes(T,N,show_plot=True):
	dt = float(T)/N
	y = zeros(N+1)
	z = zeros(N+1)
	t = linspace(0,T,N+1)
        y[0], z[0] = 1,1
        
	for n in range(N):
		y[n+1] = y[n] + dt*(y[n]+2*t[n] - t[n]**2)
		z[n+1] = (z[n] + dt*(2*t[n+1] - t[n+1]**2))/(1.0-dt)
	

	r = exp(t)+t**2
	if show_plot:
		plt.plot(t,y,t,z,t,r)
		plt.legend(['y','z','r'])
		plt.show()
	
	# return error at T=1
	return abs(r[-1]-y[-1]), abs(r[-1]-z[-1])


for i in range(3,12):
	N = 2**i
	e_y,e_z = schemes(1,N,False)
	print e_y*N, e_z*N

