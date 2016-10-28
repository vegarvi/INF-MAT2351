from diffusion import *
import scipy.interpolate as Spline

tIC,ICP = loadtxt('/home/vegard/CSF/code/gemesh/Pressure_tests/Eide_no_shift.txt')

tL,LP = loadtxt('/home/vegard/CSF/code/gemesh/Pressure_tests/Lumbar_P.txt')


LP_shift = 3.7
LP += LP_shift

idx = where(ICP == amax(ICP))[0][0]
idx2 = where(LP == amax(LP))[0][0]

idxm = where(LP < -0.2+LP_shift)[0][0]

time_start = tL[2]
time_peak = (tL[idx2]+tL[idx2-1])*0.5 - tIC[idx]

L = 0.45

v_start = L/time_start
v_peak = L/time_peak

shift_start = v_start*0.06
shift_peak = v_peak*0.06

pct = 0.06/L

print shift_start, shift_peak


ICP = append(ICP,ICP[1])
tIC = append(tIC,tIC[-1]+tIC[1])
LP = append(LP,LP[1])
tL = append(tL,tL[-1]+tL[1])

P_IC = Spline.PchipInterpolator(tIC,ICP)
P_L = Spline.PchipInterpolator(tL,LP)

T = 0.24*pct
dt = 0.005
dx = 0.05

def D0(t):
	return ICP[0] - pct*(ICP[0]-LP[2])*t/T
def D1(t):
	return ICP[-2]- pct*(ICP[-2]-LP[-2])*t/T


u = diffusion7_13(I=P_IC,D0=D0,D1=D1,k=0.1,f=lambda u,t:0,L=tIC[-2],T=T,dx=dx,dt=dt,show_plot=False)
#plot(tL-pct*tL[2],LP,tIC,ICP,)

idx3 = where(u==amax(u))
utime = linspace(0,tIC[-2],int(float(tIC[-2])/dx+1))
t = copy(utime)
utime += tL[2]*pct
print utime[idx3]-tIC[idx], shift_peak, shift_start
clf()
plot(utime,P_IC(t)-u,tL,LP,tIC,ICP)
draw()
figure()

U = Spline.PchipInterpolator(utime,u)
def applied_pres(t):
	return P_IC(t-tL[2]*pct)-U(t)
t_pres = linspace(0,tIC[-1],101)



