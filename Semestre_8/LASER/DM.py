import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")


def zr(w0,wavelength):
    return (np.pi * w0**2/wavelength)
    
def Spotsize(z,w0,wavelength):
    return(w0*np.sqrt(1+(z/zr(w0,wavelength))**2))

# w_list2 = [w0 * np.sqrt(1 + (z / zR)**2) for zR in zR_list]
z=np.linspace(-5e-3,5e-3,1000)

# Define parameters for first plot
w0_list = [100e-6, 20e-6, 5e-6]  # initial waist sizes in meters
lambda0 = 780e-9  # wavelength in meters
z_max = 5e-3  # maximum distance to plot in meters


# Create array of distances to plot
z = np.linspace(-z_max, z_max, 1000)

# Calculate beam waist at each distance for each initial waist size
w_list = [Spotsize(z,w0,780e-9) for w0 in w0_list]

# Define parameters for second plot
w0 = 5e-6  # initial waist size in meters
lambda_list = [700e-9, 800e-9, 900e-9]  # wavelengths in meters



# Calculate beam waist at each distance for each wavelength
w_list2 = [Spotsize(z,5e-6,wavelength) for wavelength in lambda_list]

# Create figure with two subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4))

# Plot results in first subplot
ax1.fill_between(z*1e3, -w_list[0]*1e6, w_list[0]*1e6, alpha=0.2, color='blue')
ax2.fill_between(z*1e3, -w_list[1]*1e6, w_list[1]*1e6, alpha=0.2, color='orange')
ax3.fill_between(z*1e3, -w_list[2]*1e6, w_list[2]*1e6, alpha=0.2, color='green')
ax1.plot(z*1e3, w_list[0]*1e6, label='100 µm', color='blue')
ax2.plot(z*1e3, w_list[1]*1e6, label='20 µm', color='orange')
ax3.plot(z*1e3, w_list[2]*1e6, label='5 µm', color='green')
ax1.plot(z*1e3, w_list[0]*-1e6, label='100 µm', color='blue')
ax2.plot(z*1e3, w_list[1]*-1e6, label='20 µm', color='orange')
ax3.plot(z*1e3, w_list[2]*-1e6, label='5 µm', color='green')
ax1.set_xlabel('Distance (mm)')
ax1.set_ylabel('Beam waist (µm)')
ax2.set_xlabel('Distance (mm)')
ax2.set_ylabel('Beam waist (µm)')
ax3.set_xlabel('Distance (mm)')
ax3.set_ylabel('Beam waist (µm)')
ax1.set_title(f'waist = {w0_list[0]*1e6} µm')
ax2.set_title(f'waist = {w0_list[1]*1e6} µm')
ax3.set_title(f'waist = {w0_list[2]*1e6} µm')
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')
ax2.axhline(y=0, color='k')
ax2.axvline(x=0, color='k')
ax3.axhline(y=0, color='k')
ax3.axvline(x=0, color='k')
plt.suptitle(f"Evolution of Gaussian beam for several waist and lambda = {lambda0*1e9} nm")

plt.show()
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4))

# Plot results in second subplot
ax1.fill_between(z*1e3, -w_list2[0]*1e6, w_list2[0]*1e6, alpha=0.2, color='blue')
ax2.fill_between(z*1e3, -w_list2[1]*1e6, w_list2[1]*1e6, alpha=0.2, color='orange')
ax3.fill_between(z*1e3, -w_list2[2]*1e6, w_list2[2]*1e6, alpha=0.2, color='green')
ax1.plot(z*1e3, w_list2[0]*1e6, color='blue')
ax2.plot(z*1e3, w_list2[1]*1e6, color='orange')
ax3.plot(z*1e3, w_list2[2]*1e6, color='green')
ax1.plot(z*1e3, w_list2[0]*-1e6, color='blue')
ax2.plot(z*1e3, w_list2[1]*-1e6, color='orange')
ax3.plot(z*1e3, w_list2[2]*-1e6, color='green')
ax1.set_xlabel('Distance (mm)')
ax1.set_ylabel('Beam waist (µm)')
ax2.set_xlabel('Distance (mm)')
ax2.set_ylabel('Beam waist (µm)')
ax3.set_xlabel('Distance (mm)')
ax3.set_ylabel('Beam waist (µm)')
ax1.set_title(f'lambda = {lambda_list[0]*1e9} nm')
ax2.set_title(f'lambda = {lambda_list[1]*1e9} nm')
ax3.set_title(f'lambda = {lambda_list[2]*1e9} nm')
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')
ax2.axhline(y=0, color='k')
ax2.axvline(x=0, color='k')
ax3.axhline(y=0, color='k')
ax3.axvline(x=0, color='k')
plt.suptitle(f"Evolution of Gaussian beam for several lambda and waist  = {w0*1e6} µm")
plt.show()

fig, ax = plt.subplots()

# Plot results in last subplot
ax.fill_between(z*1e3, -w_list2[0]*1e6, w_list2[0]*1e6, alpha=0.2, color='blue')
ax.fill_between(z*1e3, -w_list2[1]*1e6, w_list2[1]*1e6, alpha=0.2, color='orange')
ax.fill_between(z*1e3, -w_list2[2]*1e6, w_list2[2]*1e6, alpha=0.2, color='green')
ax.plot(z*1e3, w_list2[0]*1e6, color='blue',label=f'lambda = {lambda_list[0]*1e9} nm')
ax.plot(z*1e3, w_list2[1]*1e6, color='orange',label=f'lambda = {lambda_list[1]*1e9} nm')
ax.plot(z*1e3, w_list2[2]*1e6, color='green',label=f'lambda = {lambda_list[2]*1e9} nm')
ax.plot(z*1e3, w_list2[0]*-1e6, color='blue')
ax.plot(z*1e3, w_list2[1]*-1e6, color='orange')
ax.plot(z*1e3, w_list2[2]*-1e6, color='green')
ax.set_xlabel('Distance (mm)')
ax.set_ylabel('Beam waist (µm)')
ax.legend()
# ax1.set_title(f'lambda = {lambda_list[0]*1e9} nm')
# ax2.set_title(f'lambda = {lambda_list[1]*1e9} nm')
# ax3.set_title(f'lambda = {lambda_list[2]*1e9} nm')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.title(f"Evolution of Gaussian beam for several lambda and waist  = {w0*1e6} µm")
plt.show()
