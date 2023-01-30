import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

import warnings
warnings.filterwarnings('ignore')

plt.style.use("ggplot")


def pot(z,D,alpha,req):
        return D*(np.exp(-2*alpha*(z-req))-2*np.exp(-alpha*(z-req)))


i=0
coef=np.zeros((3,3))
for filename in os.scandir("Clean_thata"):
    if filename.is_file():
        loc=str(13) + str(i+1)
        plt.subplot(int(loc))
        data=np.loadtxt(filename.path)
        z=data[:,0]
        v=data[:,1]
        
        fit_coef, pcov = curve_fit(pot,z,v) # use of curve.fit
        plt.scatter(z,v,label="Scatter plot",s=5,marker="+")
        
        plt.plot(z, pot(z, *fit_coef),c='b',label="scipy")
        plt.xlabel("z in "+r"$\AA$")
        plt.ylabel("potential in eV")
        plt.title(os.path.basename(filename.path))
        plt.ylim(-10,10)
        plt.xlim(-2,5)
        
        plt.legend()
        
        coef[i,:] = fit_coef
        i +=1

plt.show()


np.savetxt('coeff.txt', coef, delimiter = ' ')


path1=os.path.join(os.path.dirname(__file__),'pot.txt')