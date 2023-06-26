from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

plt.style.use("ggplot")

def DeltaH(E_DFT, l, E_REF_H20, E_REF_CO, P, vol, type):
    """
    Calculate Delta H for a given set of parameters.

    Args:
        E_DFT (float): DFT energy.
        l (float): Lambda parameter.
        E_REF_H20 (float): Reference energy of H2O.
        E_REF_CO (float): Reference energy of CO.
        P (float): Pressure.
        vol (float): Volume.
        type (str): Type of material.

    Returns:
        float: Delta H value.
    """
    if type == "sI":
        nb_H20 = 46
        nb_SC = 2
    else:
        nb_H20 = 136
        nb_SC = 16
    return (E_DFT - (nb_H20 * E_REF_H20) - (l + nb_SC) * E_REF_CO) / (l + nb_SC + nb_H20) + (P * vol**3) / (l + nb_SC + nb_H20)


def scale(l, type):
    """
    Scale the parameters based on the type of material.

    Args:
        l (float): Lambda parameter.
        type (str): Type of material.

    Returns:
        float: Scaled value.
    """
    if type == "sI":
        nb_H20 = 46
        nb_SC = 2
    else:
        nb_H20 = 136
        nb_SC = 16
    return nb_H20 / (nb_H20 + nb_SC + l)

# unpack data about the phase of C0 at different pressure at 0 K
P_CO_ice = np.loadtxt("dataIce/dataalpha_vdWDF2-PAW.dat",usecols=(2,))
E_C0_ice = np.loadtxt("dataIce/dataalpha_vdWDF2-PAW.dat",usecols=(4,))
# unpack pressure form the fit of BM
P_list =np.asarray(np.loadtxt("dataConvex/P.txt"))

# unpack data about the phase of water at different pressure at 0 K
P_ice_XI = np.loadtxt("dataIce/dataXI_vdWDF2-PAW.dat",usecols=(2,))
E_ice_XI = np.loadtxt("dataIce/dataXI_vdWDF2-PAW.dat",usecols=(4,))

P_ice_II = np.loadtxt("dataIce/dataII_vdWDF2-PAW.dat",usecols=(2,))
E_ice_II = np.loadtxt("dataIce/dataII_vdWDF2-PAW.dat",usecols=(4,))

P_ice_XV = np.loadtxt("dataIce/dataXV_vdWDF2-PAW.dat",usecols=(2,))
E_ice_XV = np.loadtxt("dataIce/dataXV_vdWDF2-PAW.dat",usecols=(4,))

P_ice_VIII = np.loadtxt("dataIce/dataVIII_vdWDF2-PAW.dat",usecols=(2,))
E_ice_VIII = np.loadtxt("dataIce/dataVIII_vdWDF2-PAW.dat",usecols=(4,))

E_REF_H20_list=[]
E_REF_CO_list=[]
# interpolation to get the E_ref_H2O value all the pressure depending on the stable phase of water ice
for p in P_list:
    p=p*160.2
    f1=interpolate.interp1d(P_ice_XI,E_ice_XI,kind='nearest',fill_value="extrapolate")
    f2=interpolate.interp1d(P_ice_II,E_ice_II,kind='nearest',fill_value="extrapolate")
    f3=interpolate.interp1d(P_ice_XV,E_ice_XV,kind='nearest',fill_value="extrapolate")
    f4=interpolate.interp1d(P_ice_VIII,E_ice_VIII,kind='nearest',fill_value="extrapolate")
    fCO=interpolate.interp1d(P_CO_ice,E_C0_ice,kind='nearest',fill_value="extrapolate")
    l=[f1(p),f2(p),f3(p),f4(p)]
    
    E_REF_H20_list.append(min(l))
    E_REF_CO_list.append(fCO(p))

# unpack data of sI and sII from the fit of BM
data_convex1=np.loadtxt("dataConvex/data_convex1.txt")
data_convex2=np.loadtxt("dataConvex/data_convex2.txt")
Vol_sI = data_convex1[:,6:]
Vol_sII = data_convex2[:,6:]
raw_points1 = data_convex1[:,:2]
raw_points2 = data_convex2[:,:2]


real_points = np.zeros((np.shape(raw_points1)[0]+np.shape(raw_points2)[0]+2,2))
fig, axs = plt.subplots(len(P_list), 2, figsize=(17, 9)) 
# range over the pressure to plot convex hull
for p in range(len(P_list)):
    # range over the larges cages occupancy for sI
    for j in range(np.shape(raw_points1)[0]):

        x_sI=scale(raw_points1[j,:][0],"sI")
        y_sI=DeltaH(raw_points1[j,:][1],raw_points1[j,:][0],E_REF_H20_list[p],E_REF_CO_list[p],P_list[p],Vol_sI[j,p],"sI")


        if j ==0 :
            axs[p,0].scatter(x_sI,y_sI,c="orangered",label="sI")
            axs[p,1].scatter(x_sI,y_sI,c="orangered",label="sI")
        
        axs[p,0].scatter(x_sI,y_sI,c="orangered")
        axs[p,1].scatter(x_sI,y_sI,c="orangered")
        
        axs[p,1].annotate(round(raw_points1[j,:][0]/6,2), (x_sI,y_sI),fontsize=6, textcoords="offset points", xytext=(0, 5), ha='center')
        real_points[j,:] = x_sI,y_sI
    # range over the larges cages occupancy for sII
    for i in range(1,np.shape(raw_points2)[0]+1):
        x_sII=scale(raw_points2[i-1,0],"sII")
        
        y_sII=DeltaH(raw_points2[i-1,1],raw_points2[i-1,:][0],E_REF_H20_list[p],E_REF_CO_list[p],P_list[p],Vol_sII[j,p],"sII")
        
        if i ==1 :
            axs[p,0].scatter(x_sII,y_sII,c="dodgerblue",label="sII")
            axs[p,1].scatter(x_sII,y_sII,c="dodgerblue",label="sII")
        
        axs[p,0].scatter(x_sII,y_sII,c="dodgerblue")
        axs[p,1].scatter(x_sII,y_sII,c="dodgerblue")

        axs[p,1].annotate(round(raw_points2[i-1,:][0]/8,2), (x_sII,y_sII),fontsize=6, textcoords="offset points", xytext=(0, 5), ha='center')
        real_points[i+j,:] = x_sII,y_sII

    axs[p,0].legend()
    axs[p,1].legend()
    real_points[-1,:] = 1,0
    real_points[-2,:] = 0,0
    
    # inset axes....
    
    # subregion of the original image
    x1, x2 = min(real_points[:-2,0])-0.01,max(real_points[:-2,0])+0.01
    y1, y2 = min(real_points[:-2,1]) - abs(0.05*min(real_points[:-2,1])) , max(real_points[:-2,1]) + abs(0.05*max(real_points[:-2,1]))
    
    axs[p,1].set_xlim(x1, x2)
    axs[p,1].set_ylim(y1, y2)
    

    axs[p,0].indicate_inset_zoom(axs[p,1], edgecolor="black")

    
    real_points[:,1]=np.clip(real_points[:,1], a_min=None, a_max=0)
    

    if min(real_points[:,1]) >= 0:
        ##print("yes")
        axs[p,0].plot([0,1],[0,0],c="cyan")
        axs[p,1].plot([0,1],[0,0],c="cyan")
        
    else:
        ##print()
        hull = ConvexHull(real_points,incremental=True)
        hull.simplices[0,:]=0,0
    
        for simplex in hull.simplices:
            if not np.array_equal(simplex,np.asarray([16,15])):
                
                axs[p,0].plot(real_points[simplex, 0], real_points[simplex, 1],c="cyan")
                axs[p,1].plot(real_points[simplex, 0], real_points[simplex, 1] ,c="cyan")
    if p == 0:
        axs[p,0].set_title(f'Convex hull')
        axs[p,1].set_title(f'Zoom of the Convex hull for the ROI')
    
    axs[p,0].set_ylabel(f"P={P_list[p]*160.2}")
    
    

axs[p,0].set_xlabel(r"Composition, $\frac{H_2O}{(H_2O+CO)}$")
axs[p,1].set_xlabel(r"Composition, $\frac{H_2O}{(H_2O+CO)}$")
fig.supylabel(r"$\Delta$ H for different values of P (ev/molecules)")
plt.tight_layout()
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.1, 
                    hspace=0)

plt.show()