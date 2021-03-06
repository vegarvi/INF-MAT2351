from matplotlib.pylab import *
class solver:
	# Class to solve an ODE on the form
	# u' = f(u,t), works for the explicit schemes FE, Heun, RK4
	def __init__(self,f,u0,T,N):
		self.f = f
		self.T = T
		self.N = N
		self.u0 = u0
		self.u = zeros(N+1)
		self.t = linspace(0,T,N+1)
		self.dt = float(T)/N
	
	def solve(self):
		self.u[0] = self.u0	
		for n in range(self.N):
			self.u[n+1] = self.step(self.u[n],self.t[n])    # depends on method
	
		return self.u,self.t

	
	def error(self,u_ex):
		return abs(u_ex(self.T)-self.u[-1])
	

class FE(solver):
	def step(self,u_,t):
		u = u_ + self.dt*self.f(u_,t)
		return u
	
class Heun(solver):
	def step(self,u_,t):
		F1 = self.f(u_,t)
		F2 = self.f(u_ + self.dt*F1,t+self.dt)
	
		u = u_ + 0.5*self.dt*(F1+F2)
		return u
class RK4(solver):
	def step(self,u_,t):
		f = self.f
		F1 = f(u_,t)
		F2 = f(u_ + 0.5*self.dt*F1,t+0.5*self.dt)
		F3 = f(u_ + 0.5*self.dt*F2,t+0.5*self.dt)
		F4 = f(u_ + self.dt*F3,t+self.dt)
		u = u_ + (self.dt/6.0)*(F1+2*F2+2*F3+F4)
		return u

# ex n)

T = 1.1
eps = 0.25
f = lambda u,t: 2*(1-t)*u/eps**2

u0 = exp(-1/eps**2)
u_ex = lambda t: u0*exp((2-t)*t/eps**2)

import time
for method in range(3):
	i = 1
	err = 10
	while err > 1E-4:    # with FE, it takes a long time to reach 10**-5
		N = 100*2**i
		if method == 0:
			solver = FE(f,u0,T,N)
		elif method == 1:
			solver = Heun(f,u0,T,N)
		else: solve = RK4(f,u0,T,N)
		t1 = time.time()
		solver.solve()
		time_used = time.time()-t1
		err = solver.error(u_ex)

		i += 1
	print err, time_used,N

# conclusion for this problem: FE is simple, but slow. Heun is fast but not as accurate as RK4.
# RK4 is accurate but needs more time per iteration. (More operations at each step)

