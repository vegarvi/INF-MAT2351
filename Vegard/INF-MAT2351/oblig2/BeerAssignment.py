from matplotlib.pylab import *


def beer(N,h_T,q,cond,lim):
        rho = 1000
        cv = 4200
        k = 0.58
        r_c = 0.032
        
        x = linspace(0,1,N)

        dx = 1.0/(N-1)
        dt = 0.4*dx**2
        alpha = dt/dx**2
        u0 = ones(N)
        u = zeros(N)

        l = 0
        while cond(u0,x) > lim:
                for i in range(1,N-1):
                        # variable coeff
                        #u[i] = u0[i] + (1/x[i])*alpha*(q(x[i]+0.5*dx)*(u0[i+1]-u0[i]) - q(x[i]-0.5*dx)*(u0[i]-u0[i-1]))
                        # product rule w/ centered diff
                        u[i] = u0[i] + dt/(2*dx*x[i])*(u0[i+1]-u0[i-1]) + alpha*(u0[i+1]-2*u0[i]+u0[i-1])

						# third variant 
                        #u[i] = u0[i] + 1.0/(i)*alpha*((i+0.5)*(u0[i+1]-u0[i]) - (i-0.5)*(u0[i]-u0[i-1]))

                u[0] = u[1]
                        
                if h_T < 0:
                        u[N-1] = 0
                else:	
						# Newton centered diff
                        uN = u[N-2] - 2*dx*u[N-1]*h_T*r_c/k
                        u[N-1] = u0[N-1] + 1.0/(N-1)*alpha*((N-1+0.5)*(uN-u[N-1]) - (N-1-0.5)*(u[N-1]-u[N-2]))
						# Newton backward diff
                        #u[N-1] = u[N-2]*(1.0/(1+dx*h_T*r_c/k))

                u0 = copy(u)
                l+= 1

        return dt*l


q = lambda x: x
N = 40
def avg(u,x):
        return 2.0*sum(u*x)/len(x)
def inner(u,x):
        return u[0]

H = [-1,5,10,18]
c = [inner,avg,inner,avg,avg]
lim = [0.1,0.1,0.1,0.2,0.1]
ex = ['m)','n)','o)','p)','q)','r)']

for i in range(5):
        print ex[i]
        for h in H[:2]:
                if h < 0:
                        print 'h_T = inf  -->  ',
                else: print 'h_T = %g  --> ' %h,
                if i > 1:
                        print 't = ', beer(N,h,q,c[i],lim[i])*7415.17
                else:
                        print 't_bar = ', beer(N,h,q,c[i],lim[i])
print '\n EXERCISE r) \n'
for i in range(2,5):
        print ex[i]
        for h in H[2:]:
                if h < 0:
                        print 'h_T = inf --> ',
                else: print ' h_T = %g --> ' %h,
                if i > 1:
                        print 't = ', beer(N,h,q,c[i],lim[i])*7415
                else:
                        print 't_bar = ', beer(N,h,q,c[i],lim[i])
