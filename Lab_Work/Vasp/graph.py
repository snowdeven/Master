import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import os
plt.style.use("ggplot")

path1=os.path.join(os.path.dirname(__file__), 'ENCUT.dat') 
data1=np.loadtxt(path1,delimiter=";")

print(data1[:,1])
plt.plot(data1[:,0],data1[:,2],'x-b')
plt.show()

path1=os.path.join(os.path.dirname(__file__), 'VOLUME.dat') 

data1=np.loadtxt(path1,delimiter=";")
print(np.min(data1[:,1]),"min")
print([11.10+0.15*i for i in range(13)])

print(data1[:,1])
plt.plot(data1[:,0],data1[:,2],'x-b')
plt.xlabel(r'unit cell parameter in $\AA$')
plt.ylabel("Energy Vasp")
plt.title('Energy of CO-clathrate against unit cell parameter for the sI')
plt.show()

path1=os.path.join(os.path.dirname(__file__), 'ENCUT2.dat') 


data1=np.loadtxt(path1,delimiter=";")
print(data1[:,1])
plt.plot(data1[:,0],data1[:,3],'x-b')
plt.show()