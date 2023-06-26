import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import trapz

import os

# function

def diffPV(obs):
    PV=(obs[:,5]*epsilon/sigma**3)*(7.4889*sigma)**3
    nrT= nb/(6.02*10**(23)) * 8.314 *obs[:,4] * 119.8

    return PV-nrT
def MB(obs,Veldist,T):
    a=(nb/(2*np.pi*obs[T,4]))**(3/2) * (Veldist)**2 
    b=np.exp(-0.5*(nb*(Veldist)**2/obs[T,4]))
    return 4*np.pi*a*b
def P(x,a,b):
    return a*x+b*x**2
def D(x,a,b):
    return a*x+b

# get all the path of the data
path1=os.path.join(os.path.dirname(__file__),'msd.dat') 
path2=os.path.join(os.path.dirname(__file__),'vacf.dat') 
path3=os.path.join(os.path.dirname(__file__),'observables.dat') 
path4=os.path.join(os.path.dirname(__file__),'VelDist.dat')
path5=os.path.join(os.path.dirname(__file__),'rdf.dat') 

# unpack the data in array 
msd=np.loadtxt(path1)
vacf=np.loadtxt(path2)
obs=np.loadtxt(path3)
Veldist=np.loadtxt(path4)
rdf=np.loadtxt(path5)

# constant
epsilon=119.8*1.38015*10**(-23) # in J
kb=1.38015*10**(-23) # in J.k-1
sigma=0.3405*10**(-9) # in m 
nb=1 # number of particules == m*
R=8.314 # in J.K-1.mol-1



plt.plot(obs[:,0],diffPV(obs))
plt.ylabel("PV-nRT")
plt.xlabel("Nstep")
plt.title("PV-nRT over Nstep")
plt.show()



plt.plot(Veldist[:,0],Veldist[:,1],label="f(v) mesured")
veldistth=np.linspace(0,5,10000)
for i in range(0,2000,500):
    plt.plot(veldistth,MB(obs,veldistth,i),label=f"MB for T={obs[i,4]:.2f}")

plt.xlabel("v")
plt.ylabel("f(v)")
plt.legend()
plt.show()


# Create figure and axes
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3)
n=3000
fig.tight_layout()
# Plot data on each subplot
# Plot data on each subplot
ax1.plot(obs[:, 0], obs[:, 1],c='black')
ax1.axhline(np.mean(obs[:, 1]), c='dodgerblue')
ax1.axhline(np.mean(obs[n:, 1]), c='dodgerblue', ls='--')
ax2.plot(obs[:, 0], obs[:, 2],c='black')
ax2.axhline(np.mean(obs[:, 2]), c='gray')
ax2.axhline(np.mean(obs[n:, 2]), c='gray', ls='--')
ax3.plot(obs[:, 0], obs[:, 3],c='black')
ax3.axhline(np.mean(obs[:, 3]), c='tomato')
ax3.axhline(np.mean(obs[n:, 3]), c='tomato', ls='--')
ax4.plot(obs[:, 0], obs[:, 4],c='black')
ax4.axhline(np.mean(obs[:, 4]), c='limegreen')
ax4.axhline(np.mean(obs[n:, 4]), c='limegreen', ls='--')
ax5.plot(obs[:, 0], obs[:, 5],c='black')
ax5.axhline(np.mean(obs[:, 5]), c='orange')
ax5.axhline(np.mean(obs[n:, 5]), c='orange', ls='--')
# Calculate and plot average of all plots


ax6.set_facecolor('white')
ax6.text(0.5, 1, "Average for random configuration", horizontalalignment='center', verticalalignment='center', transform=ax6.transAxes)
ax6.text(0.3, 0.8, "Full", horizontalalignment='center', verticalalignment='center', transform=ax6.transAxes)
ax6.text(0.4, 0.7, f" Total        :   { np.mean(obs[:,1]):.4f}                        { np.mean(obs[n:,1]):.4f}", horizontalalignment='center', verticalalignment='center', transform=ax6.transAxes,c='dodgerblue')
ax6.text(0.4, 0.6, f" Potential    :   { np.mean(obs[:,2]):.4f}                        { np.mean(obs[n:,2]):.4f}", horizontalalignment='center', verticalalignment='center', transform=ax6.transAxes,c='gray')
ax6.text(0.4, 0.5, f" Kinetic      :   { np.mean(obs[:,3]):.4f}                        { np.mean(obs[n:,3]):.4f}", horizontalalignment='center', verticalalignment='center', transform=ax6.transAxes,c='tomato')
ax6.text(0.4, 0.4, f" Temperature  :   { np.mean(obs[:,4]):.4f}                        { np.mean(obs[n:,4]):.4f}", horizontalalignment='center', verticalalignment='center', transform=ax6.transAxes,c='limegreen')
ax6.text(0.4, 0.3, f" Pressure     :   { np.mean(obs[:,5]):.4f}                        { np.mean(obs[n:,5]):.4f}", horizontalalignment='center', verticalalignment='center', transform=ax6.transAxes,c='orange')

ax6.text(0.7, 0.85, f"with 0:{n} discard \n dashed lines", horizontalalignment='center', verticalalignment='center', transform=ax6.transAxes)

ax1.set_xlabel('Nstep')
ax1.set_ylabel('Total')
ax2.set_xlabel('Nstep')
ax2.set_ylabel('Potential')
ax3.set_xlabel('Nstep')
ax3.set_ylabel('Kinetic')
ax4.set_xlabel('Nstep')
ax4.set_ylabel('Temperature')
ax5.set_xlabel('Nstep')
ax5.set_ylabel('Pressure')
ax6.set_axis_off()


plt.suptitle("Quantities in observables.dat over Nsteps")
plt.show()

path6=os.path.join(os.path.dirname(__file__),'task5/rdf_rand.dat') 
rdf=np.loadtxt(path6)
path7=os.path.join(os.path.dirname(__file__),'task5/rdf_cs.dat') 
rdf_cs=np.loadtxt(path7)
plt.plot(rdf[:,0],rdf[:,1],label="random configuration")
plt.plot(rdf_cs[:,0],rdf_cs[:,1],label="simple cubic configuration")
plt.xlabel("r")
plt.ylabel("g(r)")
plt.legend()
plt.show()

path8=os.path.join(os.path.dirname(__file__),'Q9/observables_bussi.dat') 
obs_bussi=np.loadtxt(path8)
path9=os.path.join(os.path.dirname(__file__),'Q9/observables.dat') 
obs=np.loadtxt(path9)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

fig.tight_layout()


ax1.plot(obs[:,0],obs[:,1],label="Velocities rescale applied")
ax1.plot(obs_bussi[:,0],obs_bussi[:,1],label="Bussi thermostat applied")
ax2.plot(obs[:,0],obs[:,4],label="Velocities rescale applied")
ax2.plot(obs_bussi[:,0],obs_bussi[:,4],label="Bussi thermostat applied")
ax1.set_ylabel('Total')
ax1.set_xlabel('Nstep')
ax2.set_ylabel('Temperature')
ax2.set_xlabel('Nstep')
ax1.legend()
ax2.legend()
ax1.title.set_text("Total energy")
ax2.title.set_text("Temperature")
plt.show()
print("variance/av_T^2 = " ,np.var(obs_bussi[:,4])/np.mean(obs_bussi[:,4])**2)
print("2/3N = ",2/(3*336))

plt.hist(obs_bussi[3000:,1],bins=250,fill=False,histtype='step')
plt.xlabel("Total energy")
plt.ylabel("f(E)")
plt.title("probability distribution f(E) of the total energy in the NVT set")
plt.show()


Pressure=[0.01438,0.027309,0.041,0.04851,0.05579,0.0585535,0.06209,0.06675]
density=[0.01,0.03,0.05,0.06,0.07,0.08,0.09,0.1]


fit_coef, pcov = curve_fit(P,density,Pressure,maxfev=500000)

x=np.linspace(0,0.1,100)

plt.scatter(density,Pressure,label="data")
plt.plot(x,P(x,*fit_coef),c="cyan",label=" fit with a = %5.3f, b= %5.3f"%tuple(fit_coef))
plt.ylabel("Pressure")
plt.xlabel("density")
plt.title(r"P($\rho$)")
plt.legend()
plt.show()

fit_coef, pcov = curve_fit(D,msd[:,0],msd[:,1],maxfev=500000)
n=1500


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

area = trapz(vacf[n:,1], dx=0.01)

fig.tight_layout()

ax1.plot(vacf[:,0],vacf[:,1],label=f"vacf with area ={area:.4f} and D={area/3:.4f}")
ax2.plot(msd[:,0],D(msd[:,0],*fit_coef),label="msd fit with 6D = %5.3f, l= %5.3f"%tuple(fit_coef))
ax2.loglog(msd[:,0],msd[:,1],label="msd ")
ax1.set_ylabel('Total')
ax1.set_xlabel('Vacf')
ax2.set_ylabel('msd')
ax2.set_xlabel('Time')
ax1.legend()
ax2.legend()
ax1.title.set_text("vacf along time")
ax2.title.set_text("msd in loglog scale along time ")
plt.show()
