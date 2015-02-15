from matplotlib.pylab import *

# b)
t = linspace(0,5,101)

def s(t,x):
    return x*(x+exp(-t)*(1-x))**-1


for i in range(11):
    x = 0.2*i
    plot(t,s(t,x))
    hold('on')
title('b)')
xlabel('t')
ylabel('s(t)')
show()

# c/d)
figure()
x = linspace(0,5,101)
t = 1
ds = 1/(exp(1)*(exp(-1)*x-x-exp(-1))**2)
plot(x,s(t,x),x,ds)
title('c)-d)')
xlabel('x')
ylabel('S(x), t=1')
show()

# h)
def u(t,x):
    return x*(x+exp(t)*(1-x))**-1

t = linspace(0,5,101)
for i in range(11):
    x = 0.2*i
    plot(t,u(t,x))
    hold('on')
title('h)')
xlabel('t')
ylabel('u(t)')
show()

x = 1
eps = 4.54E-5
# we should know the behavior of these
# solutions from g):
print 'U(1) = %.4f      U(1.0000454) = %.4f' %(u(10,x),u(10,x+eps))

print 'Critical point for U(1.0000454): %.6f' %log((x+eps)/(x+eps-1))
