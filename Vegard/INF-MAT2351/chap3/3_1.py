from matplotlib.pylab import *
def F_S(S0, F0, dt):
	T = 10.0
	N = int(T/dt)
	F = zeros(N+1)
	S = zeros(N+1)
	F[0],S[0] = F0,S0
	
	for n in range(N):
		F[n+1] = F[n] + dt*(2-S[n])*F[n]
		S[n+1] = S[n] + dt*(F[n]-1)*S[n]
	
	plot(F,S)
	xlabel('F')
	ylabel('S')
	show()

F0 = 1.9
S0 = 0.1
dt = 0.0001
F_S(F0,S0,dt)

# F0 = 2.0, S0 = 1.0 gives F' = S' = 0 for eqn (3.69)
# and S[n+1] = S[n], F[n+1] = F[n] for scheme (3.70)

