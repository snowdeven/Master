import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time
import multiprocessing
from multiprocessing import Pool




plt.style.use("ggplot")

def A(x,a,b,c):
    
    com_X1_x = x @ a - a @ x
    com_X2_x = x @ b - b @ x
    com_X3_x = x @ c - c @ x

    return a @ com_X1_x - com_X1_x @ a + b @ com_X2_x - com_X2_x @ b + c @ com_X3_x - com_X3_x @ c



def J(sgn):
    J=np.zeros((mj,mj),dtype="complex")
    for i in range(0,mj):
        for k in range(0,mj):
            
            if sgn == "+":
                if m[k]+1 == m[i] :
                    J[i,k] = np.sqrt(j*(j+1) - m[k]*(m[k]+1))
            elif sgn == "z":
                if m[i] == m[k] :
                    J[i,k] = float(m[k])
            else:
                if m[k]-1 == m[i] :
                    J[i,k] = np.sqrt(j*(j+1) - m[k]*(m[k]-1))
    return J


def init_X(n):
    return np.zeros((n,n),dtype="complex")

def init_V(X1,X2,X3,h):
    return calc_V(X1,X1,X2,X3,h) ,calc_V(X2,X1,X2,X3,h), calc_V(X3,X1,X2,X3,h) 

def calc_V(X1,X2,X3,X4,h):
    return (A(X1,X2,X3,X4)*h)

def init_J():
    return (J("-")+J("+"))/2, (J("+")-J("-"))/(2*1j), J("z")

def calcul_matrice(J): 
    
    X_k=init_X(n_length)
    X_k[:-1,:-1]=J/j
    X_k[:-1,-1] = np.random.normal(0,std,mj)*np.exp(1j*np.random.uniform(0,pi_2,mj))
    X_k[-1,:-1] = np.conjugate(X_k[:-1,-1])
    X_k[-1,-1]= 1000+ np.random.normal(0,std)
    return X_k


def parallelisation(n):
    
    # if(n%10==0):
    #     print("Controle_",n)
    X1_k=calcul_matrice(J1)
    
    X2_k=calcul_matrice(J2)
    X3_k=calcul_matrice(J3)

    V1_k,V2_k,V3_k = init_V(X1_k,X2_k,X3_k,h/2)


    for i in range(1,t):

        V1_i = V1_k + calc_V(X1_k, X1_k, X2_k, X3_k, h)
        V2_i = V2_k + calc_V(X2_k, X1_k, X2_k, X3_k, h)
        V3_i = V3_k + calc_V(X3_k, X1_k, X2_k, X3_k, h)

        X1 = X1_k + V1_i*h
        X2 = X2_k + V2_i*h
        X3 = X3_k + V3_i*h
    
    
    return n,X1[-1,-1],X2[-1,-1],X3[-1,-1]





start = time.time()

# Constants

N = 1000

std=0.01

j  = 10 # important 
mj = int(2*j+1)
m  = [j - i for i in range(0,mj)]

n_length=int(2*j+2)

t  = 1000
t0 = 0
tf = 400

h=(tf-t0)/t

XT=[i*h for i in range(t)]

X1=init_X(n_length)
X2=init_X(n_length)
X3=init_X(n_length)

V1,V2,V3 = init_V(X1,X2,X3,h/2)

J1,J2,J3 = init_J()



pi_2 = 2*np.pi

Prob = np.zeros((3,N), dtype='complex_')


if __name__ == '__main__':
    
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        for ind in pool.imap(parallelisation, tqdm(range(N))): 
            Prob[0,ind[0]] = ind[1]
            Prob[1,ind[0]] = ind[2]
            Prob[2,ind[0]] = ind[3]
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter3D(np.real(Prob[0,:]),np.real(Prob[1,:]),np.real(Prob[2,:]), color = "green")

    plt.title(f"Vacum fluctuations for J= {j} and std= {std}")
    plt.legend()
    plt.show()
    
    

print(time.time()-start )



