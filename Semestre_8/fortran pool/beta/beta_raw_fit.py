import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import warnings
warnings.filterwarnings('ignore')
# use a better style for plot
plt.style.use("ggplot")


# define the fonction potential
def pot(z,D,req,ar0,ar1,at0,at1,a,b):
    f=0.5 *(1+np.tanh(a*z+b))
    alpha=(1-f)*(ar0+ar1*z)+f*(at0+at1*z)
    return (D*(np.exp(-2*alpha*(z-req))-2*np.exp(-alpha*(z-req))))

# guest values for a et b in the order of the file Clean_data
la=[1,1,1,1,1,1]
lb=[-1.12,-0.807,-0.6312,-1.80,-1.59,-1.39]


i=0 # set iterator 
coef=np.zeros((6,8)) # empty array to store coefficients

# start the subplot
fig, axs = plt.subplots(2, 3)
# adjuste the label
for ax in axs.flat:
    ax.label_outer() 

# loop over the file Clean_data to plot the different graph
for filename in os.scandir("Clean_data"):
    if filename.is_file():
        #set the localisation
        loc=str(23) + str(i+1) 
        plt.subplot(int(loc))
        #unpack the data
        data=np.loadtxt(filename.path) 
        z=data[:,0]
        v=list(data[:,1])
        # use of curve.fit
        fit_coef, pcov = curve_fit(pot,z,v
        ,p0=[6.06,1.28,0.40,-0.33,-0.77,1.4,la[i],lb[i]],maxfev=500000) 
        # plot the data
        plt.scatter(z,v,label="Scatter plot",s=5,marker="+")
        # plot the fit
        plt.plot(z, pot(z, *fit_coef),label="scipy",c='b')
        plt.xlabel("z in" + r"$\AA$")
        plt.ylabel("potential in eV")
        plt.ylim(-10,5)
        plt.xlim(-2,5)
        plt.title(os.path.basename(filename))
        plt.legend()
        # put the fit_coef in the array coef
        coef[i,:] = fit_coef 
        i +=1 #increment the tierateur
plt.suptitle("the fit with scipy for the six sites (top, bridge, hollow) and (top-bridge, top-hollow, bridge-hollow)")
plt.show()

# compute the average on the parameter to have the guess value
for i in range(8):
    print(np.mean(coef[:,i]))

# save the coeffients in a txt file
np.savetxt('coef.txt', coef, delimiter = ' ')