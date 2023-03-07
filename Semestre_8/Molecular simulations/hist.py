import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
plt.style.use("ggplot")
def func(x):
    if 0 <= x  and x <= 5 :
        return 1/7.86049 * (np.sin(x*np.pi)/(5*np.exp(-np.pi*x/3)+1) +1.5)
    else:
        return 0
    
def f(x,tau):
    return np.exp(-(x/tau))

path1=os.path.join(os.path.dirname(__file__),'data.dat')
data=np.loadtxt(path1)
x=np.linspace(0,5,1000)
y=[]

for i in x:
    y .append(func(i))
plt.plot(x,y)
plt.hist(data,bins=200,density=True)
plt.show()


x=data
N=len(x)
m=np.mean(x)
C=np.dot(x-m,x-m)/N
a=range(100)
CorrelFct= [1 if l==0 else np.dot(x[:-l] - m , x[l:] - m)/(N-l)/C for l in range(100)]

plt.plot(CorrelFct,label="CorrelFct")
fit_coef, pcov = curve_fit(f,a,CorrelFct) # use of curve.fit
plt.plot(a,f(a, *fit_coef),c='b',label="fit: tau=%5.3f "% tuple(fit_coef))
print("uncertainty = ", np.sqrt(C)/np.sqrt(N/(2*fit_coef)))
plt.legend()
plt.xlim(0,10)
plt.show()

binSizes=[2,4,50,100,200,500,1000,5000,10000,20000]
l=[]
for i in binSizes :
    inf=0
    sup=int(N/i)
    for j in range(0,N,int(N/i)):
        l.append(np.mean(x[inf:sup]))
        inf += int(N/i)
        sup += int(N/i)
        print(l)
    











