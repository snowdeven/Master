import matplotlib.pyplot as plt
import numpy as np
from function import *




N = 6  # Number of soliton orders to iterate over
Nz = 10000  # Number of points on the propagation Z-axis
Npts = 2000  # Number of points on the time and frequency axis
nb = 1  # Number of zsol, the spatial period the soliton should propagate exactly

fig, axs = plt.subplots(2, N, figsize=(17, 9))  # Create subplots for visualizing the results

# Iterate over different soliton orders
for i in range(N):
    # Perform soliton propagation
    Ip, Ip_TF, FF, TT, ZZ = propagator(i + 1, Npts, Nz, nb)

    # Rescale the obtained results
    Ip, Ip_TF, TT, FF = rescale(Ip, Ip_TF, TT, FF, Npts)

    # Calculate and print the errors in intensity and spectral intensity
    intensity_error = abs((Norm(Ip[0, :]) - Norm(Ip[-1, :])) / Norm(Ip[0, :])) * 100
    spectral_error = abs((Norm(Ip_TF[0, :]) - Norm(Ip_TF[-1, :])) / Norm(Ip_TF[0, :])) * 100
    
    axs[0, 0].set_ylabel('Propagation Distance')
    axs[1, 0].set_ylabel('Propagation Distance')

    # Plot the intensity heatmap
    im = axs[0, i].pcolormesh(TT * 10e12, ZZ, Ip, cmap="gist_ncar")
    axs[0, i].set_xlabel('Time in ps')
    axs[0, i].set_title(f"{i}")

    # Plot the spectral intensity heatmap
    im2 = axs[1, i].pcolormesh(FF * 10e-12, ZZ, Ip_TF, cmap="gist_ncar")
    axs[1, i].set_xlabel('Frequency in THz')
    axs[1, i].set_title(f"{i}")

# Add colorbars to the subplots
fig.colorbar(im, ax=axs[0, i], label='Intensity (a.u.)')
fig.colorbar(im2, ax=axs[1, i], label='Spectral Intensity (a.u.)')

plt.tight_layout(h_pad=2, w_pad=0.5)
plt.show()



