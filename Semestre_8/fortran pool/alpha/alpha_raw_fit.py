import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import warnings
warnings.filterwarnings('ignore')
# use a better style for plot
plt.style.use("ggplot")

# define the fonction potential
def pot(z,D,alpha,req):
        return D*(np.exp(-2*alpha*(z-req))-2*np.exp(-alpha*(z-req)))


i=0 # set iterator
coef=np.zeros((3,3)) # empty array to store coefficients

# start the subplot
fig, axs = plt.subplots(1, 3)

# loop over the file Clean_data to plot the different graph
for filename in os.scandir("Clean_data"):
    if filename.is_file():
        #set the localisation
        loc=str(13) + str(i+1)
        plt.subplot(int(loc))
        #unpack the data
        data=np.loadtxt(filename.path)
        z=data[:,0]
        v=data[:,1]
        # use of curve.fit
        fit_coef, pcov = curve_fit(pot,z,v) # use of curve.fit
        # plot the data
        plt.scatter(z,v,label="Scatter plot",s=5,marker="+")
        # plot the fit
        plt.plot(z, pot(z, *fit_coef),c='b',label="scipy")
        plt.xlabel("z in "+r"$\AA$")
        plt.ylabel("potential in eV")
        plt.title(os.path.basename(filename.path))
        plt.ylim(-10,10)
        plt.xlim(-2,5)
        
        plt.legend()
        # put the fit_coef in the array coef
        coef[i,:] = fit_coef
        i +=1 #increment the tierateur

plt.suptitle("the fit with scipy for the sites (top, bridge, hollow)")
plt.show()

# save the coeffients in a txt file
np.savetxt('coeff.txt', coef, delimiter = ' ')


