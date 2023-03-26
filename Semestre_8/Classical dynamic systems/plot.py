import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from time import sleep
from tqdm import tqdm
import scipy 



import os
plt.style.use("ggplot")

path1=os.path.join(os.path.dirname(__file__), 'data.dat') 
# path2=os.path.join(os.path.dirname(__file__), 'data.dat') 
# path3=os.path.join(os.path.dirname(__file__), 'data.dat') 

data1=np.loadtxt(path1)
# data2=np.loadtxt(path2)
# data3=np.loadtxt(path3)



print(data1)

plt.plot(data1[:,0],data1[:,1],label=r'$||\delta (x)_1>|$')
plt.plot(data1[:,0],data1[:,2],label=r'$||\delta (x)_2>|$')
plt.plot(data1[:,0],data1[:,3],label=r'$||\delta (x)_3>|$')
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
# plt.title(f"Vacum fluctuations for J= {j} and std= {std}")
plt.legend()
plt.show()