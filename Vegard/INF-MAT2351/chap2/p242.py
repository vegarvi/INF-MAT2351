from matplotlib.pylab import *

	# g) solve:
	# u' = u
	# u(0) = 1

def solver(f_ex, N, T,exercise):
	dt = float(T)/N

	x = zeros(N+1)    # FE
	y = zeros(N+1)    # BE
	z = zeros(N+1)    # CN
	u = zeros(N+1)    # Heun
	v = zeros(N+1)    # RK4

	t = linspace(0,T,N+1)
	if exercise == 'g':
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
		        
	else: #(exercise h)
		x[0],y[0],z[0],u[0],v[0] = 10,10,10,10,10
		for n in range(N):
			x[n+1] = x[n] + x[n]*dt*(1-x[n])
			y[n+1] = (dt - 1 + sqrt(1 - 2*dt + 4*dt*y[n] + dt*dt))/(2*dt)

			a = 0.5*dt; b = 1 - dt*0.5; c = -z[n] - dt*0.5*z[n]*(1-z[n])
			z[n+1] = (-b + sqrt(b**2 - 4*a*c))/(2*a)
			

		
	plot(t,f_ex(t),t,x,t,y,t,z)
	legend(['r','FE','BE','CN'])
	show()
	ex = abs(f_ex(T) - x[-1])		# absolute error at t = T
	ey = abs(f_ex(T) - y[-1])
	ez = abs(f_ex(T) - z[-1])
	eu = abs(f_ex(T) - u[-1])
	ev = abs(f_ex(T) - v[-1])
	if exercise == 'g':
		print '%5.2f %5.2f %5.2f %5.2f %5.2f' %(ex/dt,ey/dt,ez/(dt**2),eu/(dt**2),ev/(dt**4))
	else:
		print '%5.4f %5.4f %5.4f' %(ex/dt,ey/dt,ez/(dt**2))	

f_exg = lambda t: exp(t)		# exact solution
f_exh = lambda t: exp(t)*(exp(t)-0.9)**-1

for i in range(4):
	N = 10*2**i      # N = 10,20,40....
	solver(f_exh,N,1.0,'h')  
	
	
