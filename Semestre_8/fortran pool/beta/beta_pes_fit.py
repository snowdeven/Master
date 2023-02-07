import numpy as np
import matplotlib.pyplot as plt
import os

# set a better plot style
plt.style.use("ggplot")

# unpack the data for 3D and color graph
path1=os.path.join(os.path.dirname(__file__),'pot.txt')
data=np.loadtxt(path1)
#forget the 2 first rows because this is not potential
potential=data[:,2:]  
# the first rows is the values of axis
axis=data[:,0]
# the second is the same value of z
z_value=data[0,1]

# start the subplot
fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1)

# plot the colorgraph
plt.pcolormesh(axis ,axis,potential , cmap="gist_heat", shading='auto')
plt.colorbar(label="Potential in eV", shrink=0.5)
plt.xlabel("x in "+ r"$\AA$")
plt.ylabel("y in "+ r"$\AA$")
plt.axis("equal")
plt.title(f"Color graph of the potential surface for z= {z_value}  "+ r"$\AA$")

ax = fig.add_subplot(1, 2, 2, projection='3d')


# make the 3D graph
X, Y = np.meshgrid(axis, axis)
surf = ax.plot_surface(X, Y, potential, cmap="gist_heat", linewidth=0, antialiased=False)
fig.colorbar(surf, label='potential in eV', orientation='horizontal', shrink=0.5)
ax.set_xlabel("x in " + r"$\AA$")
ax.set_ylabel("y in " + r"$\AA$")
plt.title(f"3D graph for the potential surface for z= {z_value} "+r"$\AA$")
plt.show()


# unpack the data for the fit
path1=os.path.join(os.path.dirname(__file__),'1Dcuts.txt')
fit=np.loadtxt(path1)

i=0 #set the iterator
# start subplot 
fig, axs = plt.subplots(2, 3)
# adjust the label
for ax in axs.flat:
    ax.label_outer() 
# loop over the files CRP
for filename in os.scandir("CRP"):
    if filename.is_file():
        # set the localisation
        loc=str(23) + str(i+1)
        plt.subplot(int(loc))
        # set the values
        z_pes=fit[:,6]
        v_pes=fit[:,i]
        # unpack the data CRP
        data=np.loadtxt(filename)
        # set the values
        z=data[:,0]
        v=list(data[:,1])
        # compute the mean error
        m=[]
        for j in range(v.index(min(v))-100,v.index(min(v))+100):
            m.append(abs(v_pes[j]/v[j]))
        
        print(f"mean error {np.mean(m)}")
        
        # plot the PES curves
        plt.plot(z_pes,v_pes, 'g',label='pes')
        # plot the CRP curves
        plt.plot(z,v,label='data')
        
        plt.title(os.path.basename(filename))
        plt.ylim(-10,10)
        plt.xlim(-2,5)
        plt.ylabel("potential in  eV")
        plt.xlabel("z in "+r"$\AA$")
        plt.legend()
        
        i +=1 #increment the iterator
plt.suptitle("the 1D-cuts for the six sites (top, bridge, hollow) and (top-bridge, top-hollow, bridge-hollow)")

plt.show()

