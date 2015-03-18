from matplotlib.pylab import *
from Newton import Newton

f = lambda x: x**2 - 4
df = lambda x: 2*x

g = lambda x: x**2
dg = lambda x: 2*x

x0 = 3.0
x4_f = Newton(f,df,x0,4,tol=0)
x4_g = Newton(g,dg,x0,4,tol=0)

print 'f(x4_f) = %g' %f(x4_f)
print 'g(x4_g) = %g' %g(x4_g)

x = linspace(-1,4,501)
plot(x,f(x),x,g(x),[-1,4],[0,0])
legend(['f','g'])
show()

h = lambda x: x**6
dh = lambda x: 6*x**5


x0 = 1.0
x4_h = Newton(h,dh,x0,4,tol=0)
print 'h(x4_h) = %g' % h(x4_h)
