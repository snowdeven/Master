import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import warnings
warnings.filterwarnings('ignore')
plt.style.use("ggplot")

def pot(z,D,req,ar0,ar1,at0,at1,a,b):
    f=0.5 *(1+np.tanh(a*z+b))
    alpha=(1-f)*(ar0+ar1*z)+f*(at0+at1*z)
    return (D*(np.exp(-2*alpha*(z-req))-2*np.exp(-alpha*(z-req))))

la=[-10,-10,-10,-10,-10,-10]
lb=[1.06,0.524,0.485,1.70,1.52,1.45]
i=0
coef=np.zeros((6,8))
fig, axs = plt.subplots(2, 3)
for ax in axs.flat:
    ax.label_outer() 
for filename in os.scandir("Clean_thata"):
    if filename.is_file():
        loc=str(23) + str(i+1)
        plt.subplot(int(loc))
        print(filename)
        data=np.loadtxt(filename.path)
        z=data[:,0]
        v=data[:,1]
        fit_coef, pcov = curve_fit(pot,z,v,p0=[1,1,1,1,1,1,la[i],lb[i]],maxfev=10000) # use of curve.fit
        fit_coef[-2] = la[i]
        fit_coef[-1] = lb[i]
        plt.scatter(z,v,label="Scatter plot",s=10,marker="+",c='b')
        plt.plot(z, pot(z, *fit_coef),label="scipy")
        plt.xlabel("z in" +r"$\AA$")
        plt.ylabel("potential in eV")
        plt.ylim(-10,5)
        plt.xlim(-2,5)
        plt.title(os.path.basename(filename))
        plt.legend()
        coef[i,:] = fit_coef
        i +=1
plt.suptitle("the fit with scipy for the six sites (top, bridge, hollow) and (top-bridge, top-hollow, bridge-hollow)")
plt.show()

np.savetxt('coef.txt', coef, delimiter = ' ')