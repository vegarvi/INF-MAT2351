from numpy import *
import matplotlib.pylab as plt


def schemes(T,N,show_plot=True):
	dt = float(T)/N
	y = zeros(N+1)
	z = zeros(N+1)
	t = linspace(0,T,N+1)
        print t[1]-t[0]
	for n in range(N):
		y[n+1] = y[n] + dt*(1+4*y[n])
		z[n+1] = (z[n] + dt)/(1.0-4*dt)

	
	r = 0.25*(exp(4*t)-1)
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



