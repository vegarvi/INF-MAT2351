from diffusion import *

k = 4

L = 1
T = 1
dx = 0.05
dt = 0.01
I = lambda x: sin(4*pi*x)
wave(I,lambda x: 0,lambda x: 0,k,lambda x, t: 0,L,T,dx,dt,True)
