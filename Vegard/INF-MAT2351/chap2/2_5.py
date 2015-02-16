from matplotlib.pylab import * 

data = loadtxt('population_data.txt',skiprows=1) 
year = data[:,0]
pop = data[:,1]

t = linspace(1800,1900,101)

r0 = 5.3
a = 0.03
r = lambda t: r0*exp(a*(t-1800))

subplot(1,2,1)
plot(t,r(t),year,pop,'o')

t = linspace(1800,1980,181)
year = append(year,1980)
pop = append(pop,226.5)

#t = linspace(1800,2015,216)
#year = append(year,2015)
#pop = append(pop,320.2)    #2015 included


subplot(1,2,2)
plot(t,r(t),year,pop,'o')
show()

# let's say we have an initial guess of parameters
R = 300
r0 = 5.3
a = 0.03
x0 = [a,r0,R]

'''
can we change the parameters to get a better fit?
strategy 1: try and fail
strategy 2: use fmin from scipy
'''

r_log = lambda x,t: x[1]/(x[1]+exp(-x[0]*(t-1800))*(x[2]-x[1]))*x[2]

# we now want to minimize the squared
# distance between the data points and the function
def minimizer(x0):
    return sum((pop-r_log(x0,year))**2) 


import scipy.optimize as sc
'''
scipy.optimize.fmin returns parameters that minimizes
the function in the input argument, here: minimizer
(everyone might not have this module installed)
'''
xopt = sc.fmin(func=minimizer,x0=x0)

print 'Optimal parameters:'
print 'a = %.4f   r0 = %.4f   R = %.4f' %(xopt[0],xopt[1],xopt[2])

plot(t,r_log(xopt,t),t,r_log(x0,t),'-',year,pop,'o')
legend(['optimized','initial guess','data'],loc='upper left')
show()
# with 2015: a = 0.0215   r0 = 9.2306   R = 473.2189
# without 2015: a = 0.0288   r0 = 5.8294   R = 287.7501

