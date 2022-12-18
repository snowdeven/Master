import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes

plt.style.use('ggplot')


for i in range(1,6):
    
    file="./Result/result_"+str(i)+".txt"
    DATA=np.loadtxt(file,delimiter=",")
    plt.title(f"spectre_{i}")
    plt.scatter(DATA[:,2],DATA[:,0],s=35,
                facecolors="None",edgecolors='b',
                label="data")
    plt.plot(DATA[:,2],DATA[:,1],label="fit")
    plt.plot(DATA[:,2],DATA[:,3],label="fit weighted")
    plt.ylabel("intensity")
    plt.xlabel("wavenumber in cm-1")
    plt.legend()
    plt.show()



DATA=np.loadtxt("./Result/regr_gamma.txt",delimiter=",")

plt.scatter(DATA[:,0],DATA[:,1],s=35,
                facecolors="None",edgecolors='b',label="Data")
x=np.linspace(-1,16,100)
plt.plot(x,DATA[1,2]*x +DATA[1,3],label=f"regr_lin with y={round(DATA[1,2],3)}*x + {round(DATA[1,3],3)}")
plt.title("linear regression of gamma")
plt.ylabel("gamma")
plt.xlabel("pressure in atm")
plt.legend()
plt.show()



DATA=np.loadtxt("./Result/regr_omega.txt",delimiter=",")

plt.scatter(DATA[:,0],DATA[:,1],s=35,
                facecolors="None",edgecolors='b',label="Data")
x=np.linspace(-1,16,100)
plt.plot(x,DATA[1,2]*x +DATA[1,3],label=f"regr_lin with y={round(DATA[1,2],3)}*x + {round(DATA[1,3],3)}")
plt.title("linear regression of omega_m")
plt.ylabel("omega_m in cm-1")
plt.xlabel("pressure in atm")
plt.legend()
plt.show()
