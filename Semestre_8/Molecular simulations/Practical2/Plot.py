import numpy as np
import matplotlib.pyplot as plt
import os
plt.style.use("ggplot")

path1=os.path.join(os.path.dirname(__file__), 'data1.1_2K.dat') 
path2=os.path.join(os.path.dirname(__file__), 'data2.1_2K.dat') 
path3=os.path.join(os.path.dirname(__file__), 'data3.1_2K.dat') 

data1=np.loadtxt(path1)
data2=np.loadtxt(path2)
data3=np.loadtxt(path3)


plt.plot(data1[:,0],data1[:,1],label="T= 1.1 K")
plt.plot(data2[:,0],data2[:,1],label="T= 2.1 K")
plt.plot(data3[:,0],data3[:,1],label="T= 3.1 K")
plt.xlabel("Cycle")
plt.ylabel("Energy")
plt.title("Q7-Energy")
plt.legend()
plt.show()
plt.plot(data1[:,0],data1[:,2],label="T= 1.1 K")
plt.plot(data2[:,0],data2[:,2],label="T= 2.1 K")
plt.plot(data3[:,0],data3[:,2],label="T= 3.1 K")
plt.xlabel("Cycle")
plt.ylabel("Magnetisation")
plt.title("Q7-Magnetisation")
plt.legend()
plt.show()



path=os.path.join(os.path.dirname(__file__), f'data2.1_10K.dat') 

data=np.loadtxt(path)



plt.plot(data[:,0],data[:,1],label="T= 2.1 K")
plt.xlabel("Cycle")
plt.ylabel("Energy")
plt.legend()
plt.title("Q8-energy")
plt.show()
plt.plot(data[:,0],data[:,2],label="T= 2.1 K")
plt.xlabel("Cycle")
plt.ylabel("Magnetisation")
plt.title("Q8-magnetisation")
plt.legend()
plt.show()


path=os.path.join(os.path.dirname(__file__), f'data1.75_2K.dat') 

data=np.loadtxt(path)



plt.plot(data[:,0],data[:,1],label="T= 2.1 K")
plt.xlabel("Cycle")
plt.ylabel("Energy")
plt.legend()
plt.title("Q9-energy")
plt.show()
plt.plot(data[:,0],data[:,2],label="T= 2.1 K")
plt.xlabel("Cycle")
plt.ylabel("Magnetisation")
plt.title("Q9-magnetisation")
plt.legend()
plt.show()


path=os.path.join(os.path.dirname(__file__), f'data1.9_3K.dat') 

data=np.loadtxt(path)



plt.plot(data[:,0],data[:,1],label="T= 1.9 K")
plt.xlabel("Cycle")
plt.ylabel("Energy")
plt.legend()
plt.title("Q9-energy")
plt.show()
plt.plot(data[:,0],data[:,2],label="T= 1.9 K")
plt.xlabel("Cycle")
plt.ylabel("Magnetisation")
plt.title("Q9-magnetisation")
plt.legend()
plt.show()





