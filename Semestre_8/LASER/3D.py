import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Paramètres de la gaussienne
sigma = 1
k = 2*np.pi
x0 = 0
y0 = 0
z0 = 5

# Création de la grille de coordonnées
r = np.linspace(0, 5, 51)
phi = np.linspace(0, 2*np.pi, 51)
z = np.linspace(0, 10, 51)
R, Phi, Z = np.meshgrid(r, phi, z)

# Conversion en coordonnées cartésiennes
X = R*np.cos(Phi)
Y = R*np.sin(Phi)

# Calcul du champ électrique
R0 = np.sqrt((X-x0)**2 + (Y-y0)**2 + (Z-z0)**2)
E = np.exp(-(R0**2)/(2*sigma**2)) * np.exp(1j*k*R0)

# Tracé de la gaussienne
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, np.abs(E), cmap='viridis', alpha=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_zlim([0, 10])
plt.show()
