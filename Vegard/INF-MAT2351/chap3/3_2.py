from matplotlib.pylab import *
def F_S(S0, F0, dt):
	T = 10.0
	N = int(T/dt)
	t = linspace(0,T,N+1)
	F = zeros(N+1)
	S = zeros(N+1)
	F[0],S[0] = F0,S0
	for n in range(N):
		F[n+1] = F[n] + dt*(2-S[n])*F[n]
		S[n+1] = S[n] + dt*(F[n]-1)*S[n]
	
	K = exp(F)*exp(S)/(F*S**2)	
	

	plot(t,K)
	axis([0,T,K[0],23])
	hold('on')
	return (K[N]-K[0])/(K[0]*dt)
F0 = 1.9
S0 = 0.1
for N in (100,200,300,400,500,1000,10000,20000):
	dt = 10./N
	c = F_S(F0,S0,dt)
	print c
title('K_n for various dt')
show()

# c is not independent of dt, but converges
# towards a constant as dt --> 0
