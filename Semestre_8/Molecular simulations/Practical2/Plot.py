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

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(data1[:,0],data1[:,1],label="T= 1.1  ")
ax1.plot(data2[:,0],data2[:,1],label="T= 2.1  ")
ax1.plot(data3[:,0],data3[:,1],label="T= 3.1  ")
ax1.set(xlabel="MC cycles", ylabel="Energy")
ax1.legend()

ax2.plot(data1[:,0],data1[:,2],label="T= 1.1  ")
ax2.plot(data2[:,0],data2[:,2],label="T= 2.1  ")
ax2.plot(data3[:,0],data3[:,2],label="T= 3.1  ")
ax2.set(xlabel="MC cycles", ylabel="Magnetization")
ax2.legend()

plt.suptitle(f"Q7 : energy and magnetization af a function of MC cycles for T = 1.1, 2.1, 3.1  ")
plt.show()



path=os.path.join(os.path.dirname(__file__), f'data2.1_10K.dat') 

data=np.loadtxt(path)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(data[:,0],data[:,1],label="T= 2.1  ")
ax1.set(xlabel="MC cycles", ylabel="Energy")
ax1.legend()

ax2.plot(data[:,0],data[:,2],label="T= 2.1  ")
ax2.set(xlabel="MC cycles", ylabel="Magnetization")
ax2.legend()

plt.suptitle(f"Q8 : energy and magnetization af a function of MC cycles for T = 2.1   and Nsteps = 10 000")
plt.show()



path=os.path.join(os.path.dirname(__file__), f'data2.1_100K.dat') 

data=np.loadtxt(path)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(data[:,0],data[:,1],label="T= 2.1  ")
ax1.set(xlabel="MC cycles", ylabel="Energy")
ax1.legend()

ax2.plot(data[:,0],data[:,2],label="T= 2.1  ")
ax2.set(xlabel="MC cycles", ylabel="Magnetization")
ax2.legend()

plt.suptitle(f"Q8 : energy and magnetization af a function of MC cycles for T = 2.1   and Nsteps = 100 000")
plt.show()


path=os.path.join(os.path.dirname(__file__), f'data1.75_100K.dat') 

data=np.loadtxt(path)



fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(data[:,0],data[:,1],label="T= 1.75  ")
ax1.set(xlabel="MC cycles", ylabel="Energy")
ax1.legend()

ax2.plot(data[:,0],data[:,2],label="T= 1.75  ")
ax2.set(xlabel="MC cycles", ylabel="Magnetization")
ax2.legend()

plt.suptitle(f"Q9 : energy and magnetization af a function of MC cycles for T = 1.75  ")
plt.show()

path=os.path.join(os.path.dirname(__file__), f'data2.1_100K_l40.dat') 

data=np.loadtxt(path)



fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(data[:,0],data[:,1],label="T= 2.1  ")
ax1.set(xlabel="MC cycles", ylabel="Energy")
ax1.legend()

ax2.plot(data[:,0],data[:,2],label="T= 2.1  ")
ax2.set(xlabel="MC cycles", ylabel="Magnetization")
ax2.legend()

plt.suptitle(f"Q9 : energy and magnetization af a function of MC cycles for T = 2.1  ")
plt.show()


path=os.path.join(os.path.dirname(__file__), f'data1.9_3K.dat') 

data=np.loadtxt(path)


fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(data[:,0],data[:,1],label="T= 1.9  ")
ax1.set(xlabel="MC cycles", ylabel="Energy")
ax1.legend()

ax2.plot(data1[:,0],data1[:,2],label="T= 1.9  ")
ax2.set(xlabel="MC cycles", ylabel="Magnetization")
ax2.legend()

plt.suptitle(f"Q10 : energy and magnetization af a function of MC cycles for T = 1.9  ")
plt.show()


path1=os.path.join(os.path.dirname(__file__), f'M_05.dat') 
path2=os.path.join(os.path.dirname(__file__), f'M_15.dat')
path3=os.path.join(os.path.dirname(__file__), f'M_30.dat')
path4=os.path.join(os.path.dirname(__file__), f'M_45.dat')
path5=os.path.join(os.path.dirname(__file__), f'M_60.dat')

data1=np.loadtxt(path1)
data2=np.loadtxt(path2)
data3=np.loadtxt(path3)
data4=np.loadtxt(path4)
data5=np.loadtxt(path5)
x=np.linspace(1.5,3,100000)


def yang(x):
    return (1-(np.sinh(2/x))**(-4))**(1/8)


plt.plot(data1[:,0],data1[:,2],label="l= 5",alpha=0.5)
plt.plot(data2[:,0],data2[:,2],label="l= 15",alpha=0.5)
plt.plot(data3[:,0],data3[:,2],label="l= 30",alpha=0.5)
plt.plot(data4[:,0],data4[:,2],label="l= 45",alpha=0.5)
plt.plot(data5[:,0],data5[:,2],label="l= 60",alpha=0.5)
plt.plot(x,yang(x),label="Yang function",color="b",linestyle="--")
plt.xlabel("Temperature")
plt.ylabel("Average magnetization per spin")
plt.legend()
plt.suptitle(f"Q11 & Q 12 :  magnetization as a function of temperature for several lattice size")
plt.show()


path1=os.path.join(os.path.dirname(__file__), f'M_100.dat')

data1=np.loadtxt(path1)


plt.plot(data1[:,0],data1[:,3],label="Cv")
plt.xlabel("Temperature")
plt.ylabel("specific heat capacity")
plt.legend()
plt.suptitle(f"Q13 :  specific heat capacity as a function of temperature for l = 100")
plt.show()




