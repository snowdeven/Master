
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from time import sleep
from tqdm import tqdm
import scipy 

import multiprocessing 
from multiprocessing import Pool


plt.style.use("ggplot")

# function

def com(x,y):

    mat=(np.dot(x,y) - (np.dot(y,x)))
    # n,m=np.shape(mat)
    # for i in range(n):
    #     for j in range(n):
            
    #         if np.abs(np.imag(mat[i,j])) < 1e-10:
    #             mat[i,j] = np.real(mat[i,j])
    
    return mat

def A(x):
    print("e")
    return (com(X1,com(x,X1))+com(X2,com(x,X2))+com(X3,com(x,X3)))


def Er(line,column):
    mat = np.asarray( [[np.random.uniform(0,1)*0.1 + 1j*np.random.uniform(0,1)*0.1  for i in range(column)] for j in range(line)])
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
    return np.sqrt(np.linalg.norm(a) + np.linalg.norm(b) + np.linalg.norm(c))



# Constants
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


print(com(J1,J2) == 1j*J3)
print(com(J1,J2))
print(1j*J3)

# print(com(J2,J3) == 1j*J1)
# print(com(J2,J3))
# print(1j*J1)

# print(com(J3,J1) == 1j*J2)
# print(com(J3,J1))
# print(1j*J2)





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
Dia= []
Vacum[0,0] = np.sqrt(np.dot(X1[:-1,-1], X1[-1,:-1]))
Vacum[1,0] = np.sqrt(np.dot(X2[:-1,-1], X2[-1,:-1]))
Vacum[2,0] = np.sqrt(np.dot(X3[:-1,-1], X3[-1,:-1]))
#read the pos of prob
Prob[0,0] = X1[-1,-1]
Prob[1,0] = X2[-1,-1]
Prob[2,0] = X3[-1,-1]

Dia.append(NormMat(X1,X2,X3))

# Det[0,0] = np.linalg.det(X1)
# Det[1,0] = np.linalg.det(X2)
# Det[2,0] = np.linalg.det(X3)

Norm=[np.sqrt(X1[-1,-1]**2 +X2[-1,-1]**2 +X3[-1,-1]**2)]

per1= Er(n,n)
per2= Er(n,n)
per3= Er(n,n)

X1o=X1
X2o=X2
X3o=X3
X1tild=X1 + per1
X2tild=X2 + per2
X3tild=X3 + per3

for i in tqdm(range(1,t)):
    #compute V at time t+1/2
    V1 = V1 + A(X1)*h
    #V2 = V2 + A(X2)*h
    #V3 = V3 + A(X3)*h

    #print("multiprocessing.cpu_count() = ", multiprocessing.cpu_count())
    #(Pool(process=multiprocessing.cpu_count()).imap(A, X1))
    #for i in pool.imap(A, X1)
    if __name__ == '__main__':

        nbr = int(multiprocessing.cpu_count())

        with Pool(nbr) as pool : 
            res1 = (pool.map_async(A, X1))
            #res2 = (pool.map_async(A, X2))
            #res3 = (pool.map_async(A, X3))
    #test(X1,X2,X3,h)
    res1.wait()
    #res2.wait()
    #res3.wait()

    V1 = V1 + res1*h

    V2 = V2 + res2*h

    #for i in pool.imap(A, X1)
    V3 = V3 + res3*h


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

    Dia.append(NormMat(X1,X2,X3))
    
    sleep(0.0002)

    #read the det
    # Det[0,i] = np.linalg.det(X1)
    # Det[1,i] = np.linalg.det(X2)
    # Det[2,i] = np.linalg.det(X3)



X1chapeau = h*X1tild
X2chapeau = h*X2tild
X3chapeau = h*X3tild
D=[NormMat(per1,per2,per3),
NormMat(X1chapeau-h*X1o,
        X2chapeau-h*X2o,
        X3chapeau-h*X3o)]

print(D)

X1tild=h*X1o + (D[0]/D[1])*(X1chapeau - h*X1o)
X2tild=h*X2o + (D[0]/D[1])*(X2chapeau - h*X2o)
X3tild=h*X3o + (D[0]/D[1])*(X3chapeau - h*X3o)



for i in range(2,t):


    X1chapeau = h*X1tild
    X2chapeau = h*X2tild
    X3chapeau = h*X3tild
    
    # L1 = h*((i-1)*h*X1o+(D[0]/D[i-1])*(L1-(i-1)*h*X1o))
    # L2 = h*((i-1)*h*X2o+(D[0]/D[i-1])*(L2-(i-1)*h*X2o))
    # L3 = h*((i-1)*h*X3o+(D[0]/D[i-1])*(L3-(i-1)*h*X3o))
    
    D.append(NormMat(X1chapeau-i*h*X1o,
                    X2chapeau-i*h*X2o,
                    X3chapeau-i*h*X3o))


    X1tild=i*h*X1o + (D[0]/D[i])*(X1chapeau - i*h*X1o)
    X2tild=i*h*X2o + (D[0]/D[i])*(X2chapeau - i*h*X2o)
    X3tild=i*h*X3o + (D[0]/D[i])*(X3chapeau - i*h*X3o)




plt.plot(XT,np.real(Vacum[0]),label=r'$||\delta (x)_1>|$')
plt.plot(XT,np.real(Vacum[1]),label=r'$||\delta (x)_2>|$')
plt.plot(XT,np.real(Vacum[2]),label=r'$||\delta (x)_3>|$')
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"Vacum fluctuations for J= {j} and std= {std}")
plt.legend()
plt.show()
sum=0
lyapunov=[]
for i in range(1,t):
    sum +=np.log(D[i]/D[0])
    
    lyapunov.append(sum/(i*h))
    
    

plt.plot(XT[1:],np.real(lyapunov),label="Norme matricielle ")
plt.xlabel("time in u.a")
plt.ylabel("Norm in u.a")
plt.title(f"Norme matricielle  for J= {j} and std= {std}")
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

x = np.real(Dia[0]) * np.outer(np.cos(u), np.sin(v))
y = np.real(Dia[0]) * np.outer(np.sin(u), np.sin(v))
z = np.real(Dia[0]) * np.outer(np.ones(np.size(u)), np.cos(v))




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