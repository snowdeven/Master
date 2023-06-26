#%%
import numpy as np
import matplotlib.pyplot as plt

from function import *

plt.style.use("ggplot")


#%%
"""
||=================================================================||
||-----------------------------------------------------------------||
||                                                                 ||
||                       Simple error graph                        ||
||                                                                 ||
||-----------------------------------------------------------------||
||=================================================================||
"""

# Simple_error_plot(3,10000,100,"Nz")
# Simple_error_plot(100,10000,100,"Npts")
# Simple_error_plot(1,10,1,"Zsol")
# Simple_error_plot(1,10,1,"N")
#%%
"""
||=================================================================||
||-----------------------------------------------------------------||
||                                                                 ||
||                       Double error graph                        ||
||                                                                 ||
||-----------------------------------------------------------------||
||=================================================================||
"""

# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
# for i in range(2500,15000,2500):
#     err,err2, x = error(1,10,1,sub ="N",Nz=i)
#     ax1.plot(x,err,label=f'Nz = {i}')
#     ax1.set_xlabel('N')
#     ax1.set_title("Intensity error")
#     ax1.set_ylabel('Error in percent')
#     ax1.legend()
#     ax2.plot(x,err2,label=f'Nz = {i}')
#     ax2.legend()
#     ax2.set_xlabel('N')
#     ax2.set_ylabel('Error in percent')
#     ax2.set_title("Spectral Intensity error")
# plt.suptitle(r"Absolute error $\frac{||A(z=0) - A(z)||}{||A(z=0)||}$ along N  different values of Nz",size=18)
# plt.show()



fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
for i in range(1,100,5):
    
    err,err2, x = error(1,10,1,sub="N",nb=i)
    ax1.plot(x,err,label=f'Npts= {i}')
    ax1.set_xlabel('N')
    ax1.set_ylabel('Error in percent')
    ax1.set_title("Intensity error")
    ax1.legend()
    ax2.plot(x,err2,label=f'Npts= {i}')
    ax2.legend()
    ax2.set_xlabel('N')
    ax2.set_ylabel('Error in percent')
    ax2.set_title("Spectral Intensity error")
plt.suptitle(r"Absolute error $\frac{||A(z=0) - A(z)||}{||A(z=0)||}$ along N for different values of Npts",size=18)
plt.show()



#%%
"""
||===================================================================||
||-------------------------------------------------------------------||
||                                                                   ||
||    See the difference bewteen the begining and the end of A(z)    ||
||                                                                   ||
||-------------------------------------------------------------------||
||===================================================================||
"""

# N=4

# Npts=2000
# nb=1
# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
# Nz_values = [100000,500,200]
# for Nz in Nz_values:
#     Ip, Ip_TF, FF, TT, ZZ = propagator(N, Npts, Nz,nb)

#     Ip, Ip_TF, TT, FF = rescale(Ip, Ip_TF, TT, FF,Npts,threshold=0.01,threshold_TF=0.1)
    
    
    
    
#     ax1.plot(TT*10e12,Ip[-1,:],label=f"Nz = {Nz}")
#     ax1.set_xlabel('Time in ps')
#     ax1.set_ylabel('Intensity')
    
    

#     ax2.plot(FF*10e-12,Ip_TF[-1,:],label=f"Nz = {Nz}")
#     ax2.set_xlabel('Frequency in THz')
#     ax2.set_ylabel('Spectral intensity')
    

# ax1.plot(TT*10e12,Ip[0,:],label="Ip at ZZ=0",linestyle="--")
# ax2.plot(FF*10e-12,Ip_TF[0,:],label="Ip_TF at ZZ=0",linestyle="--")
# ax1.legend()
# ax2.legend()
# # fig.suptitle('Profiles for Different Propagators', fontsize=14)
# plt.tight_layout(h_pad=2, w_pad=0.5)
# plt.show()


#%%
"""
||===================================================================||
||-------------------------------------------------------------------||
||                                                                   ||
||               Appendix A: How to Compute the Error                ||
||                                                                   ||
||-------------------------------------------------------------------||
||===================================================================||
"""

# Npts = 2000  # Number of points
# nb = 1  # Number of zsol
# N=6
# Nz_values = [15000,5000, 2000, 500]  # List of Nz values to iterate over

# fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2, figsize=(17, 9))
# # Create subplots to visualize the results

# for Nz in Nz_values:
#     Ip, Ip_TF, FF, TT, ZZ = propagator(N, Npts, Nz, nb)

#     # Calculate the errors for different metrics
#     ListNorm = abs([max(Ip[i, :]) for i in range(Nz)] - max(Ip[0, :])) / max(Ip[0, :]) * 100
#     ListNorm2 = abs([max(Ip_TF[i, :]) for i in range(Nz)] - max(Ip_TF[0, :])) / max(Ip_TF[0, :]) * 100
#     ListNorm3 = abs([Norm(Ip[i, :]) for i in range(Nz)] - Norm(Ip[0, :])) / Norm(Ip[0, :]) * 100
#     ListNorm4 = abs([Norm(Ip_TF[i, :]) for i in range(Nz)] - Norm(Ip_TF[0, :])) / Norm(Ip_TF[0, :]) * 100
#     ListNorm5 = abs([np.mean(Ip[i, :]) for i in range(Nz)] - np.mean(Ip[0, :])) / np.mean(Ip[0, :]) * 100
#     ListNorm6 = abs([np.mean(Ip_TF[i, :]) for i in range(Nz)] - np.mean(Ip_TF[0, :])) / np.mean(Ip_TF[0, :]) * 100


#     # Plot the errors for each Nz value
#     ax1.plot(ZZ, ListNorm, label=f"{Nz}")
#     ax2.plot(ZZ, ListNorm2, label=f"{Nz}")
#     ax3.plot(ZZ, ListNorm3, label=f"{Nz}")
#     ax4.plot(ZZ, ListNorm4, label=f"{Nz}")
#     ax5.plot(ZZ, ListNorm5, label=f"{Nz}")
#     ax6.plot(ZZ, ListNorm6, label=f"{Nz}")
    

# # Add legends to the subplots
# ax1.legend()
# ax2.legend()
# ax3.legend()
# ax4.legend()
# ax5.legend()
# ax6.legend()

# # Set y-axis labels for each subplot
# ax1.set_ylabel('Percentage')
# ax2.set_ylabel('Percentage')
# ax3.set_ylabel('Percentage')
# ax4.set_ylabel('Percentage')
# ax5.set_ylabel('Percentage')
# ax6.set_ylabel('Percentage')

# # Set x-axis labels for each subplot
# ax1.set_xlabel('Propagation distance z')
# ax2.set_xlabel('Propagation distance z')
# ax3.set_xlabel('Propagation distance z')
# ax4.set_xlabel('Propagation distance z')
# ax5.set_xlabel('Propagation distance z')
# ax6.set_xlabel('Propagation distance z')

# # Set titles for each subplot
# ax1.set_title(r"Intensity error with $max(A(z=0))$")
# ax2.set_title(r"Spectral intensity error with $max(A(z=0))$")
# ax3.set_title(r"Intensity error with $||A(z=0)||$")
# ax4.set_title(r"Spectral intensity error with $||A(z=0)||$")
# ax5.set_title(r"Intensity error with $\frac{1}{N}\sum_{i=1}^{N} A(z=0)$")
# ax6.set_title(r"Spectral intensity error with $\frac{1}{N}\sum_{i=1}^{N} A(z=0)$")

# # Adjust the spacing between subplots
# fig.tight_layout()

# # Display the plot
# plt.show()

