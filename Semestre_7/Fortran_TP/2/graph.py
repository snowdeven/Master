import matplotlib.pyplot as plt
import numpy as np
import os
plt.style.use('ggplot')


path1=os.path.join(os.path.dirname(__file__),"mywavefunction.txt")
print(path1)
DATA=np.loadtxt(path1,delimiter=",")

plt.plot(DATA[:,0],DATA[:,1])
plt.title("Wavefunction")
plt.ylabel("Psi")
plt.xlabel("r")
plt.legend()
plt.show()



