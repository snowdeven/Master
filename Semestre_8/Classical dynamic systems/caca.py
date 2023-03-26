
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import time 
from tqdm import tqdm
import sys 

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

def Propag(a,b,c,X1,X2,X3):
    

    X1[:-1,:-1]=J1/j
    X1[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
    X1[-1,:-1] = np.conjugate(X1[:-1,-1])
    X1[-1,-1]=a

    X2[:-1,:-1]=J2/j
    X2[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
    X2[-1,:-1] = np.conjugate(X2[:-1,-1])
    X2[-1,-1]=b

    X3[:-1,:-1]=J3/j
    X3[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,2*np.pi,mj))
    X3[-1,:-1] = np.conjugate(X3[:-1,-1])
    X3[-1,-1]=c


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

    return X1[-1,-1],X2[-1,-1],X3[-1,-1]
    

# Constants
N=100
j=10
std=0.02
mj=int(2*j+1)
m=[j - i for i in range(0,mj)]
n=int(2*j+2)
t=1000
t0=0
tf=200

h=(tf-t0)/t
XT=[i*h for i in range(t)]



# Prob= np.zeros((3,N), dtype='complex_')

J1=(J("-")+J("+"))/2
J2=(J("+")-J("-"))/(2*1j)
J3=J("z")
# Prob= np.zeros((3,t), dtype='complex_')



if __name__ == '__main__':
    
    pool = mp.Pool()
    X1=np.zeros((n,n),dtype="complex")
    X2=np.zeros((n,n),dtype="complex")
    X3=np.zeros((n,n),dtype="complex")
    
    a= np.random.normal(0,std,N)
    b= np.random.normal(0,std,N)
    c= np.random.normal(0,std,N)
    it =0
    Prob= np.zeros((3,N), dtype='complex_')
    for i,j,k in zip(a,b,c):
        sys.stdout.write(f"\r Calculating for {it=}")
        sys.stdout.flush()
        result = pool.apply_async(Propag, args=(i,j,k,X1,X2,X3))
        Prob[:,it] = result.get()
        it+=1
        
    pool.close()
    pool.join()
    print(Prob)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter3D(np.real(Prob[0,:]),np.real(Prob[1,:]),np.real(Prob[2,:]), color = "green")

    plt.title(f"Vacum fluctuations for J= {j} and std= {std}")
    plt.legend()
    plt.show()