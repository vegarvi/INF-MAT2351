from matplotlib.pylab import *

def u_v(u0,v0,N,T):
	dt = float(T)/N
	
	t = linspace(0,T,N+1)
	u = zeros(N+1)
	v = zeros(N+1)
	u[0],v[0] = u0,v0
	for n in range(N):
		u[n+1] = u[n] - dt*v[n]**3
		v[n+1] = v[n] + dt*u[n]**3

	subplot(1,3,1)
	plot(u,v)
	xlabel('u')
	ylabel('v')
	subplot(1,3,2)
	plot(t,u,t,v)
	legend(['u','v'])
	subplot(1,3,3)
	plot(t,u**4+v**4)
	axis([0,T,5,6])
	legend(['r'])
	show()

T = 10
N = int(1E5)
u0,v0 = 0.3,1.5
u_v(u0,v0,N,T)
