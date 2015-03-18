from matplotlib.pylab import *
from Newton import Newton

f = lambda x: exp(x) - 1
df = lambda x: exp(x)

x = linspace(-1,1,101)
plot(x,f(x))
show()
print f(0)

x0 = 1
x4 = Newton(f,df,x0,4,tol=0)
print 'f(x4) = %g' %f(x4)
