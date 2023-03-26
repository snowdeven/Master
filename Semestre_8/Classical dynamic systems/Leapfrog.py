import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from time import sleep
from tqdm import tqdm
from mayavi import mlab

plt.style.use("ggplot")

# function

# def com(x, y):
#     # mat = np.einsum('ij,jk->ik', x, y) - np.einsum('ij,jk->ik', y, x)
#     mat = x @ y - y @ x
#     # n,m=np.shape(mat)
#     # for i in range(n):
#     #     for j in range(n):
#     #         if np.abs(np.imag(mat[i,j])) < 1e-10:
#     #             mat[i,j] = np.real(mat[i,j])
#     return mat

def A(x,a,b,c):
    com_X1_x = x @ a - a @ x
    com_X2_x = x @ b - b @ x
    com_X3_x = x @ c - c @ x
    
    mat = a @ com_X1_x - com_X1_x @ a + b @ com_X2_x - com_X2_x @ b + c @ com_X3_x - com_X3_x @ c
    return mat

def Er(line,column):
    mat = np.asarray( [[np.random.uniform(0,1) + 1j*np.random.uniform(0,1)  for i in range(column)] for j in range(line)])
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

def NormMat(a,b,c):
    return np.linalg.norm([np.linalg.norm(a),np.linalg.norm(b),np.linalg.norm(c)])



# Constants
j=10
std=0.01
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
X1[-1,-1]= 100

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

V1 = v + A(X1,X1,X2,X3)*h/2
V2 = v + A(X2,X1,X2,X3)*h/2
V3 = v + A(X3,X1,X2,X3)*h/2

Vacum= np.zeros((3,t), dtype='complex_')
Prob= np.zeros((3,t), dtype='complex_')
Norm= np.zeros(t, dtype='complex_')
d= np.zeros(t, dtype='complex_')
lyapunov= np.zeros(t, dtype='complex_')
d2= np.zeros(t, dtype='complex_')
lyapunov2= np.zeros(t, dtype='complex_')

# Dia= []
Vacum[0,0] = X1[:-1,-1] @ X1[-1,:-1]
Vacum[1,0] = X2[:-1,-1] @ X2[-1,:-1]
Vacum[2,0] = X3[:-1,-1] @ X3[-1,:-1]
#read the pos of prob
Prob[0,0] = X1[-1,-1]
Prob[1,0] = X2[-1,-1]
Prob[2,0] = X3[-1,-1]


Norm[0]=np.linalg.norm([X1[-1,-1],X2[-1,-1],X3[-1,-1]])

per1= Er(n,n)
per2= Er(n,n)
per3= Er(n,n)

d[0]=NormMat(per1,per2,per3)

d2[0]=np.linalg.norm([per1[-1,-1],per2[-1,-1],per3[-1,-1]])


X1tild=X1 + per1
X2tild=X2 + per2
X3tild=X3 + per3


X1tild2=X1 
X2tild2=X2 
X3tild2=X3 




for i in tqdm(range(1,t)):

    #compute V at time t+1/2
    V1 = V1 + A(X1,X1,X2,X3)*h
    V2 = V2 + A(X2,X1,X2,X3)*h
    V3 = V3 + A(X3,X1,X2,X3)*h
    #Compute X at time t+1
    X1 = X1 + V1*h
    X2 = X2 + V2*h
    X3 = X3 + V3*h

    #read the vacum
    Vacum[0,i] = X1[:-1,-1] @ X1[-1,:-1]
    Vacum[1,i] = X2[:-1,-1] @ X2[-1,:-1]
    Vacum[2,i] = X3[:-1,-1] @ X3[-1,:-1]
    #read the pos of prob
    Prob[0,i] = X1[-1,-1]
    Prob[1,i] = X2[-1,-1]
    Prob[2,i] = X3[-1,-1]
    #read norm of the probe
    Norm[i]=np.sqrt(np.linalg.norm([X1[-1,-1],X2[-1,-1],X3[-1,-1]]))


    V1tild = A(X1tild,X1tild,X2tild,X3tild)*h
    V2tild = A(X2tild,X1tild,X2tild,X3tild)*h
    V3tild = A(X3tild,X1tild,X2tild,X3tild)*h


    X1chapeau = X1tild + V1tild*h
    X2chapeau = X2tild + V2tild*h
    X3chapeau = X3tild + V3tild*h

    d[i]=NormMat(X1chapeau-X1,
                X2chapeau-X2,
                X3chapeau-X3)
    
    d2[i]=np.linalg.norm([X1chapeau[-1,-1]-X1[-1,-1],
                X2chapeau[-1,-1]-X2[-1,-1],
                X3chapeau[-1,-1]-X3[-1,-1]])
    X1tild=X1 + (d[0]/d[i])*(X1chapeau - X1)
    X2tild=X2 + (d[0]/d[i])*(X2chapeau - X2)
    X3tild=X3 + (d[0]/d[i])*(X3chapeau - X3)

    lyapunov[i]= sum(np.log(d[:i]/d[0]))/(i*h)

    lyapunov2[i]= sum(np.log(d2[:i]/d2[0]))/(i*h)


plt.plot(XT,np.real(Vacum[0]),label=r'$||\delta (x)_1>|$')
plt.plot(XT,np.real(Vacum[1]),label=r'$||\delta (x)_2>|$')
plt.plot(XT,np.real(Vacum[2]),label=r'$||\delta (x)_3>|$')
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"Vacum fluctuations for J= {j} and std= {std}")
plt.legend()
plt.show()
plt.plot(XT,np.real(lyapunov),label="Norme matricielle ")
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"Lyapunov exposant  for J= {j} and std= {std}")
plt.legend()
plt.show()
plt.plot(XT,np.real(lyapunov2),label="Norme matricielle ")
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"Lyapunov exposant  for J= {j} and std= {std}")
plt.legend()
plt.show()

plt.plot(XT,np.real(Norm),label=r'$ ||x|| $')
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"Evolution of prob for J= {j} and std= {std}")
plt.legend()
plt.show()



mlab.plot3d(np.real(Prob[0,:]),np.real(Prob[1,:]),np.real(Prob[2,:]), XT)
phi, theta = np.mgrid[0:np.pi:100j, 0:2*np.pi:100j]

# Calcul des coordonnées sphériques en fonction de phi et theta
x = np.sqrt(j*(j+1))/j*np.sin(phi) * np.cos(theta)
y = np.sqrt(j*(j+1))/j* np.sin(theta)*np.sin(phi)
z = np.sqrt(j*(j+1))/j* np.cos(phi)

# Affichage de la sphère
mlab.mesh(x, y, z, color=(0, 0, 0), opacity=0.5)

# Définition des valeurs min et max pour chaque axe
xmin, xmax = min(Prob[0,:]), max(Prob[0,:])
ymin, ymax = min(Prob[1,:]), max(Prob[1,:])
zmin, zmax = min(Prob[2,:]), max(Prob[2,:])

# Affichage des axes avec les valeurs min et max définies

mlab.quiver3d([0,0,0], [0,0,0], [0,0,0], [1,0,0], [0,1,0], [0,0,1], scale_factor=1)

# Affichage de la scène
mlab.show()
