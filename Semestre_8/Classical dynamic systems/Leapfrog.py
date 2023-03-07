import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from time import sleep
from tqdm import tqdm


plt.style.use("ggplot")

# function

def com(x,y):
    return (x@y - (y@x))

def V(x):
    
    return (com(X1,x)+com(X2,x)+com(X3,x))
    
def A(x):
    return (com(X1,com(x,X1))+com(X2,com(x,X2))+com(X3,com(x,X3)))

def J(sgn):
    J=np.zeros((mj,mj),dtype="complex")
    for i in range(0,mj):
        for k in range(0,mj):
            
            if sgn == "+":
                if m[k]+1 == m[i] :
                    J[i,k] = np.sqrt(j*(j+1) - m[k]*(m[k]+1))
            elif sgn == "z":
                if m[i] == m[k] :
                    J[i,k] = m[k]
            else:
                if m[k]-1 == m[i] :
                    J[i,k] = np.sqrt(j*(j+1) - m[k]*(m[k]-1))
    return J

def dague(x):
    return(np.transpose(np.conjugate(x)))


# Constante
j=1
std=0.01
mj=int(2*j+1)
m=[j - (1*i) for i in range(0,mj)]
n=int(2*j+2)
t=1000
t0=0
tf=200
h=(tf-t0)/t
XT=[i*h for i in range(t)]
X1=np.zeros((n,n),dtype="complex")
X2=np.zeros((n,n),dtype="complex")
X3=np.zeros((n,n),dtype="complex")

J1=(J("-")+J("+"))/2
J2=(J("+")-J("-"))/(2*1j)
J3=J("z")


# print(com(J1,J2) == 1j*J3)
# print(com(J1,J2))
# print(1j*J3)





X1[:-1,:-1]=J1/j
X1[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
X1[-1,:-1] = np.conjugate(X1[:-1,-1])
X1[-1,-1]= 5


X2[:-1,:-1]=J2/j
X2[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
X2[-1,:-1] = np.conjugate(X2[:-1,-1])
X2[-1,-1]= 0

X3[:-1,:-1]=J3/j
X3[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
X3[-1,:-1] = np.conjugate(X3[:-1,-1])
X3[-1,-1]= 0

v=np.zeros((n,n),dtype="complex")
v[-1,-1]= 0
V1 = v + A(X1)*h/2
V2 = v + A(X2)*h/2
V3 = v + A(X3)*h/2

Vacum= np.zeros((3,t), dtype='complex_')
Prob= np.zeros((3,t), dtype='complex_')
Det= np.zeros((3,t), dtype='complex_')
Vacum[0,0] = np.sqrt(np.dot(X1[:-1,-1], X1[-1,:-1]))
Vacum[1,0] = np.sqrt(np.dot(X2[:-1,-1], X2[-1,:-1]))
Vacum[2,0] = np.sqrt(np.dot(X3[:-1,-1], X3[-1,:-1]))
#read the pos of prob
Prob[0,0] = X1[-1,-1]
Prob[1,0] = X2[-1,-1]
Prob[2,0] = X3[-1,-1]

dia=np.sqrt(np.trace(dague(X1)*X1) + np.trace(dague(X2)*X2) + np.trace(dague(X2)*X2))

# Det[0,0] = np.linalg.det(X1)
# Det[1,0] = np.linalg.det(X2)
# Det[2,0] = np.linalg.det(X3)

Norm=[np.sqrt(X1[-1,-1]**2 +X2[-1,-1]**2 +X3[-1,-1]**2)]



for i in tqdm(range(1,t)):
    #compute V at time t+1/2
    V1 = V1 + A(X1)*h
    V2 = V2 + A(X2)*h
    V3 = V3 + A(X3)*h
    #Compute X at time t+1
    X1 = X1 + V1*h
    X2 = X2 + V2*h
    X3 = X3 + V3*h

    
    #read norm of the probe
    Norm.append(np.sqrt(X1[-1,-1]**2 +X2[-1,-1]**2 +X3[-1,-1]**2))

    #read the vacum
    Vacum[0,i] = np.sqrt(np.dot(X1[:-1,-1], X1[-1,:-1]))
    Vacum[1,i] = np.sqrt(np.dot(X2[:-1,-1], X2[-1,:-1]))
    Vacum[2,i] = np.sqrt(np.dot(X3[:-1,-1], X3[-1,:-1]))
    #read the pos of prob
    Prob[0,i] = X1[-1,-1]
    Prob[1,i] = X2[-1,-1]
    Prob[2,i] = X3[-1,-1]
    sleep(0.0002)

    #read the det
    # Det[0,i] = np.linalg.det(X1)
    # Det[1,i] = np.linalg.det(X2)
    # Det[2,i] = np.linalg.det(X3)






plt.plot(XT,np.real(Vacum[0]),label=r'$||\delta (x)_1>|$')
plt.plot(XT,np.real(Vacum[1]),label=r'$||\delta (x)_2>|$')
plt.plot(XT,np.real(Vacum[2]),label=r'$||\delta (x)_3>|$')
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"Vacum fluctuations for J= {j} and std= {std}")
plt.legend()
plt.show()

plt.plot(XT,np.real(Norm),label=r'$ ||x|| $')
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"Evolution of prob for J= {j} and std= {std}")
plt.legend()
plt.show()

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = np.sqrt(j*(j+1)) * np.outer(np.cos(u), np.sin(v))
y = np.sqrt(j*(j+1)) * np.outer(np.sin(u), np.sin(v))
z = np.sqrt(j*(j+1)) * np.outer(np.ones(np.size(u)), np.cos(v))
#for i in range(2):
#    ax.plot_surface(x+random.randint(-5,5), y+random.randint(-5,5), z+random.randint(-5,5),  rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)




fig = plt.figure()
ax = plt.axes(projection='3d')
plot=ax.scatter(np.real(Prob[0,:]),np.real(Prob[1,:]),np.real(Prob[2,:]),c =  plt.cm.jet(np.linspace(0,1,t)),label='Courbe')  # Tracé de la courbe 3D
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='black', linewidth=0, alpha=0.5)
plt.title("Courbe 3D")
fig.colorbar(plot)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')
plt.show()