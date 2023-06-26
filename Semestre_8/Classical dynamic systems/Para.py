import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time
import multiprocessing
from multiprocessing import Pool
from mayavi import mlab





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
    X_k[-1,-1] = np.random.uniform(-1,1)
    return X_k


def parallelisation(n):
    
    # if(n%int(N*0.1)==0):
    #     print("Controle_",n,"time = ",time.time()-start )
    X1=calcul_matrice(J1)
    X2=calcul_matrice(J2)
    X3=calcul_matrice(J3)
    
    xInt = X1[-1,-1]
    yInt = X2[-1,-1]
    zInt = X3[-1,-1]

    V1,V2,V3 = init_V(X1,X2,X3,h/2)

    
    

    for i in range(1,t):

    
        X1 = X1 + V1*h
        X2 = X2 + V2*h
        X3 = X3 + V3*h

        V1 = V1 + calc_V(X1, X1, X2, X3, h)
        V2 = V2 + calc_V(X2, X1, X2, X3, h)
        V3 = V3 + calc_V(X3, X1, X2, X3, h)
    
        
    
    
    return n,X1[-1,-1],X2[-1,-1],X3[-1,-1],xInt, yInt, zInt







# Constants

N = 1000


std=0.01

j  = 10 # important 
mj = int(2*j+1)
m  = [j - i for i in range(0,mj)]

n_length=int(2*j+2)

t  = 1000
t0 = 0
tf = 200

h=(tf-t0)/t

XT=[i*h for i in range(t)]

X1=init_X(n_length)
X2=init_X(n_length)
X3=init_X(n_length)

V1,V2,V3 = init_V(X1,X2,X3,h/2)

J1,J2,J3 = init_J()


pi_2 = 2*np.pi

ProbInt = np.zeros((3,N), dtype='complex_')
Prob = np.zeros((3,N), dtype='complex_')


if __name__ == '__main__':
    
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        for ind in pool.imap(parallelisation, range(N)): 
            print(ind[0])
            Prob[0,ind[0]] = ind[1]
            Prob[1,ind[0]] = ind[2]
            Prob[2,ind[0]] = ind[3]
            ProbInt[0,ind[0]] = ind[4]
            ProbInt[1,ind[0]] = ind[5]
            ProbInt[2,ind[0]] = ind[6]


            
    
    fig = mlab.figure(figure='3D', bgcolor=(1, 1, 1), fgcolor=(0, 0, 0))
    mlab.points3d(np.real(Prob[0,:]),np.real(Prob[1,:]),np.real(Prob[2,:]),color=(1.0,0.0,0.0),scale_factor=0.02,opacity=0.5,colormap="gist_heat",resolution =20)
    mlab.points3d(np.real(ProbInt[0,:]),np.real(ProbInt[1,:]),np.real(ProbInt[2,:]),color=(1.0,0.0,1.0),scale_factor=0.02,opacity=0.5,colormap="gist_heat",resolution =20)
    mlab.points3d(0,0,0,color=(1.0,1.0,0.0),scale_factor=0.05,opacity=0.9,resolution =20)
    phi, theta = np.mgrid[0:np.pi:1000j, 0:2*np.pi:1000j]



    # Calcul des coordonnées sphériques en fonction de phi et theta
    x = np.sqrt(j*(j+1))/j*np.sin(phi) * np.cos(theta)
    y = np.sqrt(j*(j+1))/j* np.sin(theta)*np.sin(phi)
    z = np.sqrt(j*(j+1))/j* np.cos(phi)
    
    

    # Affichage de la sphère
    mlab.mesh(x, y, z, color=(0, 0, 0), opacity=0.5)
    mlab.axes()

    mlab.show()
    

    # mlab.savefig(filename='test.png')
    
    # mlab.show()
    # X, Y = np.meshgrid(np.real(Prob[0,:]),np.real(Prob[1,:]))

    # X= np.linspace(0,1,N)

    # plt.pcolormesh(X,X,np.real(Prob[:1,:]), cmap="gist_heat", shading='auto')

    # x_in =np.real(ProbInt[0,:])
    # y_in = np.real(ProbInt[1,:])
    # z_in = np.real(ProbInt[2,:])

    # x_fin =np.real(Prob[0,:])
    # y_fin = np.real(Prob[1,:])
    # z_fin = np.real(Prob[2,:])

    # fig, ((ax1, ax2),(ax3, ax4),(ax5, ax6) ) = plt.subplots(nrows=3, ncols=2,figsize=(14.0,10.0),dpi=500)

    
    # colors=x_in+y_in

    # ax1.scatter(x_in, y_in, s=10,marker='s', c=colors,cmap="rainbow")
    # ax1.set_ylabel('y-axis') 
    # ax1.set_xlabel('x-axis')
    # ax1.title.set_text(f"Initial positions of {N} prob for J = {j} for Z=0")

    
    
    # ax2.scatter(x_fin, y_fin, s=10,marker='s',c=colors,cmap="rainbow")
    # ax2.set_ylabel('y-axis')
    # ax2.set_xlabel('x-axis')
    # ax2.title.set_text(f"Final positions of {N} prob for J = {j} for Z=0")
    
    
    # colors=y_in+z_in
    # ax3.scatter(y_in, z_in, s=10,marker='s', c=colors,cmap="rainbow")
    # ax3.set_ylabel('z-axis') 
    # ax3.set_xlabel('y-axis')
    # ax3.title.set_text(f"Initial positions of {N} prob for J = {j} for X=0")
    

    
    # ax4.scatter(y_fin, z_fin, s=10,marker='s',c=colors,cmap="rainbow")
    # ax4.set_ylabel('z-axis')
    # ax4.set_xlabel('y-axis')
    # ax4.title.set_text(f"Final positions of {N} prob for J = {j} for X=0")
    

    # colors=z_in+x_in
    # ax5.scatter(z_in, x_in, s=10,marker='s', c=colors,cmap="rainbow")
    # ax5.set_ylabel('x-axis') 
    # ax5.set_xlabel('z-axis')
    # ax5.title.set_text(f"Initial positions of {N} prob for J = {j} for Y =0")
    

    
    
    # ax6.scatter(z_fin, x_fin, s=10,marker='s',c=colors,cmap="rainbow")
    # ax6.set_ylabel('x-axis')
    # ax6.set_xlabel('z-axis')
    # ax6.title.set_text(f"Final positions of {N} prob for J = {j} for Y =0")
    

    # fig.tight_layout()

    # plt.savefig(f"Pictures/mixing-N={N}-j={j}-tf={tf}.png")
    # plt.show()



    





