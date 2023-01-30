import numpy as np
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')
plt.style.use("ggplot")


# path1=os.path.join(os.path.dirname(__file__),'pot.txt')

# data=np.loadtxt(path1)
# potential=data[:,2:]
# axis=data[:,0]
# z_value=data[0,1]


# plt.pcolormesh(axis ,axis,potential , cmap="gist_heat", shading='auto')
# contours = plt.contour(axis, axis, potential, 2, colors='black')
# plt.clabel(contours, inline=True, fontsize=8)


# plt.colorbar(label="Potential", shrink=0.5)
# plt.xlabel("x in "+r"$\AA$")
# plt.ylabel("y in "+r"$\AA$")
# plt.title(f"Color graph of the potential surface for z= {z_value}  "+ r"$\AA$")
# plt.legend()
# plt.show()


# # make the 3D graph
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# X, Y = np.meshgrid(axis, axis)
# surf = ax.plot_surface(X, Y, potential, cmap="gist_stern", linewidth=2, antialiased=False)

# # Add a color bar which maps values to colors and label
# fig.colorbar(surf, label='potential in eV', orientation='horizontal', shrink=0.5)
# plt.xlabel("x in "+r"$\AA$")
# plt.ylabel("y in "+r"$\AA$")
# plt.title(f"3D graph for the potential surface for z= {z_value}"+r"$\AA$")
# plt.show()

path1=os.path.join(os.path.dirname(__file__),'1Dcuts.txt')
fit=np.loadtxt(path1)
i=0
fig, axs = plt.subplots(2, 3)
for ax in axs.flat:
    ax.label_outer() 
for filename in os.scandir("CRP"):
    if filename.is_file():
        loc=str(23) + str(i+1)
        plt.subplot(int(loc))
        z_pes=fit[:,6]
        v_pes=fit[:,i]
        
        data=np.loadtxt(filename)
        z=data[:,0]
        v=data[:,1]
        m =0
        for j in range(len(z_pes)):
            m += abs(v[j]-v_pes[j])/v[j]

        print(f"mean error {np.mean(m)}")
        
        
        plt.plot(z_pes,v_pes, 'g',label='pes')
        plt.plot(z,v,label='data')
        
        plt.title(os.path.basename(filename))
        plt.ylim(-10,10)
        plt.xlim(-2,5)
        plt.ylabel("potential in  eV")
        plt.xlabel("z in "+r"$\AA$")
        plt.legend()
        
        i +=1

plt.show()

