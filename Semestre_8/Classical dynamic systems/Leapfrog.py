import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from time import sleep
from tqdm import tqdm
from mayavi import mlab
import os
import copy
from numba import jit

plt.style.use("ggplot")

# function

@jit(nopython=True)
def A(x,a,b,c):
    com_X1_x = x @ a - a @ x
    com_X2_x = x @ b - b @ x
    com_X3_x = x @ c - c @ x
    
    mat = (a @ com_X1_x - com_X1_x @ a) + (b @ com_X2_x - com_X2_x @ b) + (c @ com_X3_x - com_X3_x @ c)
    return mat

def Er(line,column):
    mat = np.asarray([[np.random.uniform(0,std2) * 1j*np.random.uniform(0,std2)  for i in range(column)] for j in range(line)])
    mat = (mat + dague(mat))/2
    for i in range(n):
        mat[i,i] = np.real(mat[i,i])
    
    return mat
def J(sgn):
    J=np.zeros((mj,mj),dtype="complex")
    for i in range(0,mj):
        for k in range(0,mj):
            
            if sgn == "+":
                if m[k]+1 == m[i] :
                    J[i,k] = float(np.sqrt(j*(j+1) - m[k]*(m[k]+1)))
            elif sgn == "z":
                if m[i] == m[k] :
                    J[i,k] = float(m[k])
            else:
                if m[k]-1 == m[i] :
                    J[i,k] = float(np.sqrt(j*(j+1) - m[k]*(m[k]-1)))
    return J

def dague(x):
    return(np.transpose(np.conjugate(x)))


# def NormMat(a,b,c):
#     return np.sqrt(np.trace(dague(a)@a)+np.trace(dague(b)@b)+np.trace(dague(c)@c))

def NormMat(a,b,c):
    m1=np.linalg.norm(a,ord=2)
    m2=np.linalg.norm(b,ord=2)
    m3=np.linalg.norm(c,ord=2)

    return np.linalg.norm([m1,m2,m3])

# def lyapunov(time,)


# Constants
j=10
std=0
std2=0.01
mj=int(2*j+1)
m=[j - i for i in range(0,mj)]
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

X1[:-1,:-1]=J1/j
X1[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
X1[-1,:-1] = np.conjugate(X1[:-1,-1])
X1[-1,-1]= 0

X2[:-1,:-1]=J2/j
X2[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
X2[-1,:-1] = np.conjugate(X2[:-1,-1])
X2[-1,-1]= 0

X3[:-1,:-1]=J3/j
X3[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
X3[-1,:-1] = np.conjugate(X3[:-1,-1])
X3[-1,-1]= 0

v=np.zeros((n,n),dtype="complex")
v[-1,-1]=0

V1 = copy.deepcopy(v - A(X1,X1,X2,X3)*h/2)
V2 = copy.deepcopy(v - A(X2,X1,X2,X3)*h/2)
V3 = copy.deepcopy(v - A(X3,X1,X2,X3)*h/2)

Vacum= np.zeros((3,t), dtype='complex')
Prob= np.zeros((3,t), dtype='complex')
Norm= np.zeros(t, dtype='complex')
d= np.zeros(t, dtype='complex')
lyapunov=[]
d2= np.zeros(t, dtype='complex')
Norm2 = np.zeros((3,t), dtype='complex')
lyapunov2= []

# Dia= []
Vacum[0,0] = X1[:-1,-1] @ X1[-1,:-1]
Vacum[1,0] = X2[:-1,-1] @ X2[-1,:-1]
Vacum[2,0] = X3[:-1,-1] @ X3[-1,:-1]
#read the pos of prob
Prob[0,0] = X1[-1,-1]
Prob[1,0] = X2[-1,-1]
Prob[2,0] = X3[-1,-1]


Norm[0]=np.linalg.norm([X1[-1,-1],X2[-1,-1],X3[-1,-1]])


Norm2[0,0]=np.linalg.norm(X1,ord=2)
Norm2[1,0]=np.linalg.norm(X2,ord=2)
Norm2[2,0]=np.linalg.norm(X3,ord=2)



X1tild=copy.deepcopy(X1)
X1tild[:-1,-1] = np.random.normal(0,std2,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
X1tild[-1,:-1] = np.conjugate(X1tild[:-1,-1])
X1tild[-1,-1]= 0
X2tild=copy.deepcopy(X2)

X2tild[:-1,-1] = np.random.normal(0,std2,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
X2tild[-1,:-1] = np.conjugate(X2tild[:-1,-1])
X2tild[-1,-1]= 0
X3tild=copy.deepcopy(X3)
X3tild[:-1,-1] = np.random.normal(0,std2,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
X3tild[-1,:-1] = np.conjugate(X3tild[:-1,-1])
X3tild[-1,-1]= 0

# X1tild=copy.deepcopy(X1+Er(n,n))
# X2tild=copy.deepcopy(X2+Er(n,n))
# X3tild=copy.deepcopy(X3+Er(n,n))

d[0]=NormMat(X1tild-X1,X2tild-X2,X3tild-X3)



V1tild = copy.deepcopy(-A(X1tild,X1tild,X2tild,X3tild)*h/2)
V2tild = copy.deepcopy(-A(X2tild,X1tild,X2tild,X3tild)*h/2)
V3tild = copy.deepcopy(-A(X3tild,X1tild,X2tild,X3tild)*h/2)


per1=np.random.uniform(0,0.1)
per2=np.random.uniform(0,0.1)
per3=np.random.uniform(0,0.1)
X1tild2=copy.deepcopy(X1)
X1tild2[-1,-1] = X1tild2[-1,-1] + per1
X2tild2=copy.deepcopy(X2) 
X2tild2[-1,-1] = X2tild2[-1,-1] + per2
X3tild2=copy.deepcopy(X3)
X3tild2[-1,-1] = X3tild2[-1,-1] + per3

V1tild2 =copy.deepcopy(-A(X1tild2,X1tild2,X2tild2,X3tild2)*h)
V2tild2 =copy.deepcopy(-A(X2tild2,X1tild2,X2tild2,X3tild2)*h)
V3tild2 = copy.deepcopy(-A(X3tild2,X1tild2,X2tild2,X3tild2)*h)
d2[0]=np.linalg.norm([per1,per2,per3])
a=0
a2=0

for i in tqdm(range(1,t)):


    #Compute X at time t+1
    X1 += copy.deepcopy(V1*h)
    X2 += copy.deepcopy(V2*h)
    X3 += copy.deepcopy(V3*h)
    #compute V at time t+1/2
    V1 += copy.deepcopy(A(X1,X1,X2,X3)*h)
    V2 += copy.deepcopy(A(X2,X1,X2,X3)*h)
    V3 += copy.deepcopy(A(X3,X1,X2,X3)*h)
    
    # Norm2[0,i]=np.linalg.norm(X1,ord=2)
    # Norm2[1,i]=np.linalg.norm(X2,ord=2)
    # Norm2[2,i]=np.linalg.norm(X3,ord=2)

    #read the vacum
    Vacum[0,i] = X1[:-1,-1] @ X1[-1,:-1]
    Vacum[1,i] = X2[:-1,-1] @ X2[-1,:-1]
    Vacum[2,i] = X3[:-1,-1] @ X3[-1,:-1]
    #read the pos of prob
    Prob[0,i] = X1[-1,-1]
    Prob[1,i] = X2[-1,-1]
    Prob[2,i] = X3[-1,-1]
    #read norm of the probe
    Norm[i]=np.linalg.norm([X1[-1,-1],X2[-1,-1],X3[-1,-1]])


    
    X1chapeau =copy.deepcopy( X1tild + V1tild*h)
    X2chapeau =copy.deepcopy( X2tild + V2tild*h)
    X3chapeau =copy.deepcopy( X3tild + V3tild*h)

    d[i]=NormMat(X1chapeau-X1,X2chapeau-X2,X3chapeau-X3)
    
    a+=np.log(d[i]/d[0])
    lyapunov.append(a/(i*h))
    
    V1tild =copy.deepcopy(V1tild + A(X1tild,X1tild,X2tild,X3tild)*h)
    V2tild =copy.deepcopy(V2tild + A(X2tild,X1tild,X2tild,X3tild)*h)
    V3tild =copy.deepcopy(V3tild + A(X3tild,X1tild,X2tild,X3tild)*h)

    X1tild=copy.deepcopy(X1 + (d[0]/d[i])*(X1chapeau - X1))
    X2tild=copy.deepcopy(X2 + (d[0]/d[i])*(X2chapeau - X2))
    X3tild=copy.deepcopy(X3 + (d[0]/d[i])*(X3chapeau - X3))



    
    
    # #---------------------------------------------------


    # X1chapeau2 =copy.deepcopy( X1tild2 + V1tild2*h)
    # X2chapeau2 =copy.deepcopy( X2tild2 + V2tild2*h)
    # X3chapeau2 =copy.deepcopy( X3tild2 + V3tild2*h)

    # d2[i]=np.real(NormMat(X1chapeau2-X1,
    #             X2chapeau2-X2,
    #             X3chapeau2-X3))
    
    # a2+=np.log(d2[i]/d2[0])
    # lyapunov2.append(a2/(i*h))

    # V1tild2 =copy.deepcopy( V1tild2 + A(X1tild2,X1tild2,X2tild2,X3tild2)*h)
    # V2tild2 =copy.deepcopy( V2tild2 + A(X2tild2,X1tild2,X2tild2,X3tild2)*h)
    # V3tild2 =copy.deepcopy( V3tild2 + A(X3tild2,X1tild2,X2tild2,X3tild2)*h)

    # X1tild2=copy.deepcopy(X1 + (d2[0]/d2[i])*(X1chapeau2 - X1))
    # X2tild2=copy.deepcopy(X2 + (d2[0]/d2[i])*(X2chapeau2 - X2))
    # X3tild2=copy.deepcopy(X3 + (d2[0]/d2[i])*(X3chapeau2 - X3)) 


    
plt.figure()
plt.plot(XT,np.real(Vacum[0]),label=r'$|||\delta (x)_1||$')
plt.plot(XT,np.real(Vacum[1]),label=r'$|||\delta (x)_2||$')
plt.plot(XT,np.real(Vacum[2]),label=r'$|||\delta (x)_3||$')
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"Vacum fluctuations for J= {j} and std= {std}")
plt.legend()
plt.show()

plt.figure()
plt.plot(XT,np.real(Norm2[0]),label=r'$||X_1 (t)||$')
plt.plot(XT,np.real(Norm2[1]),label=r'$||X_2 (t)||$')
plt.plot(XT,np.real(Norm2[2]),label=r'$||X_3 (t)||$')
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"2-norm Evolution over the time for J= {j} and std= {std}")
plt.legend()
plt.show()


plt.figure()

plt.plot(XT[:-1],np.real(lyapunov))
plt.xlabel("time in u.a")
plt.ylabel("Lyapunov exponent in u.a")
plt.title(f"Lyapunov exponent of the fermionic string for J= {j}")
plt.show()
# plt.figure()
# plt.plot(XT,np.real(Norm),label=r'$ ||\delta x|| $')
# plt.xlabel("time in u.a")
# plt.ylabel("Norm in u.a")
# plt.title(f"Evolution of Norm of the prob for J= {j} and std= {std}")
# plt.legend()




# plt.figure()
# plt.plot(XT,np.real(Prob[0,:]),label=r'$ \delta x_1(t) $')
# plt.plot(XT,np.real(Prob[1,:]),label=r'$ \delta x_2(t) $')
# plt.plot(XT,np.real(Prob[2,:]),label=r'$ \delta x_3(t) $')
# plt.xlabel("time in u.a")
# plt.ylabel("position in u.a")
# plt.title(f"Evolution of the position of prob over the three axes for J= {j} and std= {std}")
# plt.legend()

# plt.show()



mlab.plot3d(np.real(Prob[0,:]),np.real(Prob[1,:]),np.real(Prob[2,:]), XT,line_width=10,tube_radius=0.01,tube_sides=10)





# Définition des valeurs min et max pour chaque axe
xmin, xmax = min(Prob[0,:]), max(Prob[0,:])
ymin, ymax = min(Prob[1,:]), max(Prob[1,:])
zmin, zmax = min(Prob[2,:]), max(Prob[2,:])

# Affichage des axes avec les valeurs min et max définies

# mlab.quiver3d([0,0,0], [0,0,0], [0,0,0], [1,0,0], [0,1,0], [0,0,1], scale_factor=1)
ax=mlab.axes()
ax.axes.font_factor=0.5



ax.title_text_property.font_size = 10


ax.label_text_property.font_size = 1
cb=mlab.colorbar(title="Time in a.u.")

cb.scalar_bar.unconstrained_font_size = True

cb.scalar_bar_representation.proportional_resize=True
cb.label_text_property.font_size=14
# Affichage de la scène
mlab.show()
