
import numpy as np
import matplotlib.pyplot as plt




def F(x):
    return x



def RK4(t0,tf,y0,N):
        
        y=[y0]
        x=[t0]
        t_n=0
        h=(tf-t0)/N
        for i in range(0,N-1):
            K1=F(y[i])
            K2=F(y[i]+K1*h/2)
            K3=F(y[i]+K2*h/2)
            K4=F(y[i]+K3*h)
            y.append(y[i] +( K1 + 2*K2 + 2*K3 +K4 )*h/6)   
            t_n += h
            x.append(t_n)
        return x , y
    
        
    
t0=0
tf=5
y0=1 
N=100









plt.plot(RK4(t0,tf,y0,N)[0],RK4(t0,tf,y0,N)[1])




plt.show()