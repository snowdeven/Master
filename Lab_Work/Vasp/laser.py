import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
# Define constants
R = 20E-2 # radius of curvature of mirrors in m
Wlength = 800E-9 # wavelength in m

# Define array of cavity lengths
L = np.linspace(0, R, 10000) # range of cavity lengths to plot

# Define function for spot size of beam in cavity
def spotsize(R, L, Wlength):
    return (Wlength/np.pi)*np.sqrt(L*(R-L))

w0_max = np.max(spotsize(R, L, Wlength))
L_max = L[np.argmax(spotsize(R, L, Wlength))]

# Plot spot size as a function of cavity length
plt.plot(L*1e2, spotsize(R, L, Wlength)*1E9,color="orange",label=r"evolution of $\omega_0$ ")
plt.plot([L_max*1e2, L_max*1e2], [0, w0_max*1E9], 'b--',alpha=0.5,label=fr"$\omega_0 \ max $ = {w0_max*1E9:.2f} nm for L = {L_max*1E2:.2f} cm")
plt.plot([0, L_max*1e2], [w0_max*1E9, w0_max*1E9], 'b--',alpha=0.5)

plt.xlabel('Cavity length L (cm)')
plt.ylabel(r'Beam waist radius $\omega$ (nm)')
plt.title('Beam waist radius as a function of cavity length')
plt.legend()
plt.show()

