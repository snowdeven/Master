import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
from scipy.optimize import curve_fit
import os
from matplotlib.colors import ColorConverter 


def BirchM(a,E0,a0,B0,B0p):
    part1=(((a0/a)**(2) - 1 )**3)*B0p 
    part2= (((a0/a)**(2) - 1 )**2) 
    part3=(6 - 4*(a0/a)**(2))
    return E0 + (9*a0**3 *B0)/16 * (part1 +part2*part3)

def P(a,a0,B0,B0p):
    part4= ((a0/a)**(7) - (a0/a)**(5))
    part5= ( 1+ 3/4 *(B0p - 4)*((a0/a)**(2) - 1))

    return ((3*B0)/2 * (part4 * part5))  * 160.2

def proper_round(x):

    if x == float(int(x)):
        return int(x)
    else:
        return int(x) + 1


P_list  = [0,0.1,0.2,0.3,0.80,1]

it=0

n=len([entry for entry in os.listdir("data-volume/sI") if os.path.isfile(os.path.join("data-volume/sI", entry))])
clust_data1=np.empty((n,4), dtype=object)
data_convex1=np.zeros((n,12))

ev=160.2176634
rlabels1=[]

rowColours1=[]

digit=2

# fig, ((ax1, ax2), (ax3,ax4), (ax5,ax6)) = plt.subplots(nrows=3, ncols=2,figsize=(16,12))
fig, ((ax1, ax2))= plt.subplots(nrows=1, ncols=2,figsize=(16,10))
fig, ((ax3,ax4)) = plt.subplots(nrows=1, ncols=2,figsize=(16,10))
fig, ((ax5,ax6)) = plt.subplots(nrows=1, ncols=2,figsize=(16,10))
# loop over the file data-volume/sI to plot the different graph
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)

plt.rc('legend', fontsize=8)
ax1.title.set_text('sI')
for filename in os.scandir("data-volume/sI"):
    if filename.is_file():
        #unpack the data
        name=os.path.basename(filename)
        name=name[:name.rindex('.')]
        rlabels1.append(name)
        nb=proper_round(float(name[2:]) *6*2+ 154 )
        
        data=pd.read_table(filename,sep=" ",skiprows=0,header=None)
        data=data.to_numpy()
        v=list(data[:,0])
        a=list(data[:,0])
        E=list(data[:,3])
        v_th=np.linspace(min(v),max(v),100000)
        a_th=np.linspace(min(a),max(a),100000)
        
        # use of curve.fit
        fit_coef, pcov = curve_fit(BirchM,v,E,p0=[min(E),v[E.index(min(E))],5,0.1],maxfev=500000) 
        p_sigma = np.sqrt(np.diag(pcov))
        
        clust_data1[it,0] = str(round(fit_coef[0],digit+1))  +r" $\pm$ "+ str(round(p_sigma[0],digit+1))
        clust_data1[it,1] = str(round(fit_coef[1],digit+1))+r" $\pm$ "+ str(round(p_sigma[1],digit+1))
        clust_data1[it,2] = str(round(fit_coef[2]*160.2,4)) +r" $\pm$ "+ str(round(p_sigma[2]*160.2,digit))
        clust_data1[it,3] = str(round(fit_coef[3],digit)) +r" $\pm$ "+ str(round(p_sigma[3],digit))
        # plot the data
        ax1.scatter(a,abs(data[:,3]-fit_coef[0]),s=20,marker="X")
        # plot the fit
        line, = ax1.plot(a_th,abs(BirchM(v_th, *fit_coef)-fit_coef[0]),label=name +" fit")
        ax1.set_xlabel(r'unit cell parameter ($\AA$) ')
        ax1.set_ylabel("DFT potential energy difference" + r" $E-E_0$ (eV)")
        
        ax1.legend()
        Presure= P(a_th, *fit_coef[1:])
        
        ax3.plot(a_th,Presure,label=name +" fit")
        ax3.set_xlabel(r'unit cell parameter ($\AA$) ')
        ax3.set_ylabel("Pressure (GPa) ")
        
        ax3.legend()
        rowColours1.append(ColorConverter.to_rgb(line.get_color()))
        f=interpolate.interp1d(Presure,a_th)
        
        data_convex1[it, :] = (proper_round(float(name[2:])*6),fit_coef[0],fit_coef[1],
                            p_sigma[1],fit_coef[2]*ev,p_sigma[2]*ev,
                            *[f(val/ev) for val in P_list])

        it +=1


it=0

n=len([entry for entry in os.listdir("data-volume/sII") if os.path.isfile(os.path.join("data-volume/sII", entry))])
clust_data2=np.empty((n,4), dtype=object)
rlabels2=[]
rowColours2=[]

data_convex2=np.zeros((n,12))

# loop over the file data-volume/sII to plot the different graph
ax2.title.set_text('sII')

for filename in os.scandir("data-volume/sII"):
    if filename.is_file():
        name=os.path.basename(filename)
        name=name[:name.rindex('.')]
        rlabels2.append(name)
        nb=proper_round(float(name[2:]) *8  )
        
        data=pd.read_table(filename,sep=" ",skiprows=0,header=None)
        data=data.to_numpy()
        v=list(data[:,0])
        a=list(data[:,0])
        E=list(data[:,3])
        v_th=np.linspace(min(v),max(v),100000)
        a_th=np.linspace(min(a),max(a),100000)
        
        
        # use of curve.fit
        fit_coef, pcov = curve_fit(BirchM,v,E,p0=[min(E),v[E.index(min(E))],1,1],maxfev=500000) 
        p_sigma = np.sqrt(np.diag(pcov))
        digit=2
        clust_data2[it,0] = str(round(fit_coef[0],digit+1))  +r" $\pm$ "+ str(round(p_sigma[0],digit+1))
        clust_data2[it,1] = str(round(fit_coef[1],digit+1))+r" $\pm$ "+ str(round(p_sigma[1],digit+1))
        clust_data2[it,2] = str(round(fit_coef[2]*160.2,digit)) +r" $\pm$ "+ str(round(p_sigma[2]*160.2,digit))
        clust_data2[it,3] = str(round(fit_coef[3],digit)) +r" $\pm$ "+ str(round(p_sigma[3],digit))
        # plot the data
        ax2.scatter(data[:,0],abs(data[:,3]-fit_coef[0]),s=20,marker="X")
        # plot the fit
        line, = ax2.plot(a_th, abs(BirchM(v_th, *fit_coef)-fit_coef[0]),label=name +" fit")
        ax2.set_xlabel(r'unit cell parameter ($\AA$) ')
        ax2.set_ylabel("DFT potential energy difference" + r" $E-E_0$ (eV)")
        Presure= P(a_th, *fit_coef[1:])
        ax2.legend()
        ax4.plot(a_th, P(a_th, *fit_coef[1:]),label=name +" fit")
        ax4.set_xlabel(r'unit cell parameter ($\AA$) ')
        ax4.set_ylabel("Pressure (GPa)")
        f=interpolate.interp1d(Presure,a_th)
        f1=interpolate.interp1d(a_th,BirchM(v_th, *fit_coef))
        
        
        ax4.legend()
        rowColours2.append(ColorConverter.to_rgb(line.get_color()))
        print( name[2:],float(name[2:])*8,proper_round(float(name[2:])*8))
        data_convex2[it, :] = (proper_round(float(name[2:])*8),fit_coef[0],fit_coef[1],
                            p_sigma[1],fit_coef[2]*160.2,p_sigma[2]*160.2,
                            *[f(val/ev) for val in P_list])
        it +=1


collabel=(r"$\theta_{SC}$ / $\theta_{LC}$ ",r"$E_0$ (eV)",r" V0 ($\AA$) ","B0 (GPA)","B0p")

Table_data = np.empty((8, 5), dtype=object)
Table_data[1:, 1:] = clust_data1
Table_data[0, :] = collabel
Table_data[1:, 0] = rlabels1
Table_colors=np.empty((8, 5), dtype=object)

Table_colors[1:, 1:] = "w"
Table_colors[0, :] = "w"
Table_colors[1:, 0] = rowColours1
table = ax5.table(cellText=Table_data,cellColours=Table_colors,cellLoc="center",rowLoc="center",loc='best')

ax5.axis('tight')
ax5.axis('off')
table.scale(1,2)

Table_data = np.empty((9, 5), dtype=object)
Table_data[1:, 1:] = clust_data2
Table_data[0, :] = collabel
Table_data[1:, 0] = rlabels2
Table_colors=np.empty((9, 5), dtype=object)

Table_colors[1:, 1:] = "w"
Table_colors[0, :] = "w"
Table_colors[1:, 0] = rowColours2
table = ax6.table(cellText=Table_data,cellColours=Table_colors,cellLoc="center",rowLoc="center",loc='best')

ax6.axis('tight')
ax6.axis('off')
table.scale(1,2)

plt.tight_layout()
plt.show()
plt.show()
plt.show()

np.savetxt("dataConvex/data_convex1.txt", data_convex1)
np.savetxt("dataConvex/data_convex2.txt", data_convex2)
P_data= [val/160.2 for val in P_list]
np.savetxt("dataConvex/P.txt", P_data)


