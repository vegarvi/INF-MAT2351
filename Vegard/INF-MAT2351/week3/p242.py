from matplotlib.pylab import *

	# g) solve:
	# u' = u
	# u(0) = 1

def solver(f_ex, N, T):
	dt = float(T)/N

	x = zeros(N+1)    # FE
	y = zeros(N+1)    # BE
	z = zeros(N+1)    # CN
	u = zeros(N+1)    # Heun
	v = zeros(N+1)    # RK4

	t = linspace(0,T,N+1)
	
	x[0],y[0],z[0],u[0],v[0] = 1,1,1,1,1

	# These schemes need to be changed to solve exercise h): u' = u(1-u), u0 = 10
	# Exact solution in h) is u(t) = exp(t)*(exp(t)-0.9)**-1
	
	for n in range(N):
		x[n+1] = x[n] + dt*x[n]			# FE
		y[n+1] = y[n]/(1.0-dt)			# BE
		z[n+1] = z[n]*(1+dt/2.0)/(1-dt/2.0)	# CN
	        
	        U1 = u[n] + dt*u[n]
	        u[n+1] = u[n] + dt/2*(u[n]+U1)          # Heun

	        F1 = v[n]
	        F2 = v[n] + 0.5*F1*dt
	        F3 = v[n] + 0.5*F2*dt
	        F4 = v[n] + F3*dt
	        v[n+1] = v[n] + (dt/6.)*(F1+2*F2+2*F3+F4)   # RK4

	
	r = f_ex(t)
	#plot(t,r,t,x,t,y,t,z)
	#legend(['r','FE','BE','CN'])
	#show()
	ex = abs(r[-1] - x[-1])		# absolute error at t = T
	ey = abs(r[-1] - y[-1])
	ez = abs(r[-1] - z[-1])
	eu = abs(r[-1] - u[-1])
	ev = abs(r[-1] - v[-1])

	print '%5.4f %5.4f %5.4f %5.4f %5.4f' %(ex/dt,ey/dt,ez/(dt**2),eu/(dt**2),ev/(dt**4))

f_ex = lambda t: exp(t)		# exact solution

for i in range(8):
	N = 10*2**i      # N = 10,20,40....
	solver(f_ex,N,5.0)  
	
	
