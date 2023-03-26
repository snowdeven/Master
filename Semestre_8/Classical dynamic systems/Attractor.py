import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

plt.style.use("ggplot")

def A(x,a,b,c):
    com_X1_x = x @ a - a @ x
    com_X2_x = x @ b - b @ x
    com_X3_x = x @ c - c @ x
    
    mat = a @ com_X1_x - com_X1_x @ a + b @ com_X2_x - com_X2_x @ b + c @ com_X3_x - com_X3_x @ c
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



# Constants
N=1000
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
Prob= np.zeros((3,N), dtype='complex_')

J1=(J("-")+J("+"))/2
J2=(J("+")-J("-"))/(2*1j)
J3=J("z")


# print(np.sqrt(j*(j+1))/j)
# file = open(os.path.join(os.path.dirname(__file__),f"data.dat"),"w")
# #"w" to open a file and erase the previous data if he is already exsit
# file = open(os.path.join(os.path.dirname(__file__),f"data.dat"),"a")

for k in tqdm(range(1,N)):

    X1[:-1,:-1]=J1/j
    X1[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
    X1[-1,:-1] = np.conjugate(X1[:-1,-1])
    X1[-1,-1]=1 + np.random.normal(0,std)

    X2[:-1,:-1]=J2/j
    X2[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
    X2[-1,:-1] = np.conjugate(X2[:-1,-1])
    X2[-1,-1]=1 + np.random.normal(0,std)

    X3[:-1,:-1]=J3/j
    X3[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
    X3[-1,:-1] = np.conjugate(X3[:-1,-1])
    X3[-1,-1]=1 + np.random.normal(0,std)


    V1 = A(X1,X1,X2,X3)*h/2
    V2 = A(X2,X1,X2,X3)*h/2
    V3 = A(X3,X1,X2,X3)*h/2

    
    for i in range(1,t):
        #compute V at time t+1/2
        V1 = V1 + A(X1,X1,X2,X3)*h
        V2 = V2 + A(X2,X1,X2,X3)*h
        V3 = V3 + A(X3,X1,X2,X3)*h
        #Compute X at time t+1
        X1 = X1 + V1*h
        X2 = X2 + V2*h
        X3 = X3 + V3*h

    #read the pos of prob
    Prob[0,k] = X1[-1,-1]
    Prob[1,k] = X2[-1,-1]
    Prob[2,k] = X3[-1,-1]
    # file.write(Prob[:,k])

#"a" to open a file and add the data after the previous one

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# ax.scatter3D(np.real(Prob[0,:]),np.real(Prob[1,:]),np.real(Prob[2,:]), color = "green")

# plt.title(f"Vacum fluctuations for J= {j} and std= {std}")
# plt.legend()
# plt.show()













