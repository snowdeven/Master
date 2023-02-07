import numpy as np
import matplotlib.pyplot as plt
import os


path1=os.path.join(os.path.dirname(__file__),'data.dat')
data=np.loadtxt(path1)

plt.hist(data,bins=50,density=True)
plt.show()
