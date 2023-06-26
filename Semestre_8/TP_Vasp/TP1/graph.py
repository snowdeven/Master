import matplotlib.pyplot as plt
import numpy as np



val=np.loadtxt("TP1/energy.txt")
x_values = val[:,0]
y_values = val[:,1]

plt.plot(x_values, y_values, 'bo-')
plt.xlabel('ENCUT')
plt.ylabel('Energy')
plt.title('Energy vs. ENCUT')
plt.show()