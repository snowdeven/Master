import numpy as np
import matplotlib.pyplot as plt




def F(x):
    return x



def RK2(t0,tf,y0,N):
        
        y=[y0]
        x=[t0]
        t_n=0
        h=(tf-t0)/N
        for i in range(0,N-1):
            y.append(y[i] + F(y[i]+F(y[i])*h/2)*h)   
            t_n += h
            x.append(t_n)
        return x , y
    
        
    
t0=0
tf=5
y0=1
N=100




plt.plot(RK2(t0,tf,y0,N)[0],RK2(t0,tf,y0,N)[1])




plt.show()