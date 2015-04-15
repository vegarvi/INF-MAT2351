from matplotlib.pylab import *

def diffusion7_12(I,D0,D1,k,f,L,T,dx,dt,show_plot=False):
	alpha = float(dt)/dx**2
	print 'alpha*k = ', alpha*k
	n = int(float(L)/dx + 1)
	m = int(float(T)/dt + 1)
	x = linspace(0,L,n)
	t = 0
	u0 = I(x)
	u_new = zeros(n)

	if show_plot:
		ion()
		figure()
		plot(u0)
		draw()

	for l in range(m):
		print 't = ', t
		t += dt
		for i in range(1,n-1):
			u_new[i] = u0[i] + alpha*k*(u0[i-1]-2*u0[i]+u0[i+1]) + dt*f(x[i],t)

		u_new[0] = D0(t)
		u_new[n-1] = D1(t)
		u0 = u_new
		if show_plot:
			clf()
			plot(x,u_new)
			axis([0, L, 0, 1])
			draw()
	raw_input('press enter')
	return u_new
	
def diffusion7_13(I,N0,N1,k,f,L,T,dx,dt,show_plot=False):
	alpha = float(dt)/dx**2
	print 'alpha*k = ', alpha*k
	n = int(float(L)/dx + 1)
	m = int(float(T)/dt + 1)
	x = linspace(0,L,n)
	t = 0
	u0 = I(x)
	u_new = zeros(n)

	if show_plot:
		ion()
		figure()
		plot(u0)
		draw()
	
	for l in range(m):
		print 't = ', t
		t += dt
		for i in range(1,n-1):
			u_new[i] = u0[i] + alpha*k*(u0[i-1]-2*u0[i]+u0[i+1]) + dt*f(x[i],t)

		u_new[n-1] = u0[n-1] + 2*alpha*k*(u0[n-2]-u0[n-1]+N1(t)*dx) + dt*f(x[n-1],t)
		u_new[0] = u0[0] + 2*alpha*k*(-N0(t)*dx-u0[0]+u0[1]) + dt*f(x[0],t)
		u0 = u_new
		if show_plot:
			clf()
			plot(x,u_new)
			axis([0, L, 0, 2])
			draw()
	raw_input('press enter')
	return u_new
