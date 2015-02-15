from matplotlib.pylab import *
import scipy.optimize as sc

infile = open('pop_data2.txt','r')

year = []
pop = []
for line in infile:
    if ',' in line:
        line = line.replace(',','')
        pop.append(float(line))
    elif line.startswith('1') or line.startswith('2'):
	year.append(float(line.strip('')))


infile.close()
plot(year,pop)
show()

year = array(year)
pop = array(pop)
pop = pop*1E-6
t = linspace(1776,2010,235)
r0 = 2.5
a = 0.03
R = 300
x0 = [a,r0,R]

r_log = lambda x,t: x[1]/(x[1]+exp(-x[0]*(t-1776))*(x[2]-x[1]))*x[2]

# we now want to minimize the squared
# distance between the data points and the function
def minimizer(x0):
    return sum((pop-r_log(x0,year))**2) 


import scipy.optimize as sc
'''
scipy.optimize.fmin returns parameters that minimizes
the function in the input argument, here: minimizer
'''
xopt = sc.fmin(func=minimizer,x0=x0)

print 'Optimal parameters:'
print 'a = %.4f   r0 = %.4f   R = %.4f' %(xopt[0],xopt[1],xopt[2])

plot(t,r_log(xopt,t),t,r_log(x0,t),'-',year,pop,'o')
legend(['optimized','initial guess','data'],loc='upper left')
show()



